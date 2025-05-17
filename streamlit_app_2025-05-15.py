from typing import Dict, Any, List
import streamlit as st
from openai import OpenAI
import yaml
from legal_logic import evaluate_rules
from response_logic import explain_output
from summary_generator import generate_summary, save_summary

# Initialize OpenAI client with caching
@st.cache_resource
def get_openai_client(api_key: str) -> OpenAI:
    """Initialize and cache the OpenAI client."""
    return OpenAI(api_key=api_key)

# Cache the legal evaluation function
@st.cache_data
def cached_evaluate_rules(facts: Dict[str, Any]) -> Dict[str, Any]:
    """Cache the legal evaluation results."""
    return evaluate_rules(facts)

# Cache the GPT explanation generation
@st.cache_data
def cached_explain_output(result: Dict[str, Any]) -> str:
    """Cache the GPT explanation."""
    return explain_output(result)

# Load and cache intake questions
@st.cache_data
def load_questions() -> List[Dict[str, Any]]:
    """Load and cache intake questions."""
    with open("intake_questions.yaml", "r") as f:
        return yaml.safe_load(f)["questions"]

# Generate motion text and handle errors
def generate_motion(facts, result, explanation):
    """Generate motion text and handle errors"""
    try:
        from motion_drafter import render_motion_template
        motion_text = render_motion_template(
            facts,
            result,
            explanation
        )
        return motion_text
    except (TypeError, ValueError) as e:
        st.error(f"Error generating motion: {str(e)}")
        return None

def main():
    """Main application function"""
    
    # Initialize session state variables
    if "motion_generator" not in st.session_state:
        st.session_state.motion_generator = {
            "enabled": False,
            "show": False,
            "motion_text": ""
        }

    if "facts" not in st.session_state:
        st.session_state.facts = None

    if "result" not in st.session_state:
        st.session_state.result = None

    if "explanation" not in st.session_state:
        st.session_state.explanation = None

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if "pdf_download_count" not in st.session_state:
        st.session_state.pdf_download_count = 0

    # Show title and description
    st.markdown("""
    ## 🏠 GrizlyUDVacator – Tenant Relief Triage Chatbot

    Welcome to **GrizlyUDVacator**, a symbolic AI-powered assistant designed to help tenants—and the legal professionals who support them—analyze and challenge default judgments in **unlawful detainer (eviction)** cases under **California Code of Civil Procedure § 473.5**.

    This chatbot uses a combination of:
    - 🧠 **Formal legal logic** (statutory rules + case law reasoning)
    - 💬 **OpenAI's GPT model** (for clear explanations and summaries)
    - ⚖️ Designed for **legal aid clinics, pro bono teams, and tenants facing eviction**

    ### 🔐 Getting Started

    ---
    """)

    # Sidebar Resources
    with st.sidebar:
        st.warning("PDF block reached.")  # Debug: Confirm sidebar block is reached
        st.markdown("### 📂 Resources")

        # Debug panel
        if st.checkbox("🧪 Show debug state", key="debug_state_checkbox"):
            st.json(st.session_state, expanded=False)

        # Resources section
        st.markdown("### 📄 Manual Case Intake PDF")
        st.caption(
            "Download the official paper intake form used to evaluate post-default motions under CCP § 473.5 and related provisions. "
            "Useful for offline triage or legal aid clients."
        )

        # Metadata
        FORM_VERSION = "v1.0"
        FORM_LAST_UPDATED = "2025-05-05"

        # Session-state-safe counter
        if "pdf_download_count" not in st.session_state:
            st.session_state["pdf_download_count"] = 0

        # Load and serve PDF
        try:
            with open("case-intake.pdf", "rb", encoding="utf-8") as f:
                pdf_bytes = f.read()

            downloaded = st.download_button(
                label="📥 Download Intake Form",
                data=pdf_bytes,
                file_name="case-intake.pdf",
                mime="application/pdf",
                help="Click to download the official Legal Aid intake form",
                key="download_intake_form"
            )

            if downloaded:
                st.session_state["pdf_download_count"] += 1
                try:
                    st.toast(f"📄 Intake form downloaded ({st.session_state['pdf_download_count']}x)")
                except st.errors.StreamlitAPIError as e:
                    st.success(f"📄 Intake form downloaded ({st.session_state['pdf_download_count']}x)")
                    st.warning(f"Toast notification failed: {str(e)}")

        except FileNotFoundError:
            st.error("⚠️ Intake form PDF not found. Please ensure `case-intake.pdf` is in the app folder.")
        except Exception as e:
            st.error(f"⚠️ Error loading PDF: {str(e)}")

        # Footer: version and update
        st.markdown(f"🗓️ **Version:** `{FORM_VERSION}`  —  *Last Updated: {FORM_LAST_UPDATED}*")

    # Load questions
    questions = load_questions()

    # Intake Form
    with st.expander("📋 Intake Form", expanded=True):
        with st.form("ud_intake_form"):
            st.subheader("📝 Intake Form – Tell us what happened")
            
            form_inputs: Dict[str, Any] = {}
            
            for q in questions:
                if q["type"] == "date":
                    date_val = st.date_input(
                        q["text"],
                        key=f"date_{q['id']}"
                    )
                    form_inputs[q["id"]] = date_val  # Store date object directly
                elif q["type"] == "bool":
                    form_inputs[q["id"]] = st.checkbox(
                        q["text"],
                        key=f"checkbox_{q['id']}"
                    )

            submitted = st.form_submit_button("Evaluate Legal Relief")

    # Process form submission
    if submitted:
        facts = {
            "served_date": form_inputs["served_date"].isoformat() if form_inputs["served_date"] else None,
            "motion_date": str(form_inputs["motion_date"]),
            "participated": form_inputs["participated"],
            "actual_notice": form_inputs["actual_notice"],
            "relied_on_bad_advice": form_inputs["relied_on_bad_advice"]
        }

        result = cached_evaluate_rules(facts)
        explanation = cached_explain_output(result)

        # Store form submission state
        st.session_state.submitted = True
        st.session_state.facts = facts
        st.session_state.result = result
        st.session_state.explanation = explanation

    # Legal Evaluation
    with st.expander("⚖️ Legal Evaluation", expanded=True):
        if submitted and facts and result and explanation:
            st.markdown("### ✅ Evaluation Result")
            st.success(f"**Status:** {result['status'].replace('_', ' ').title()}")
            st.info(f"**Reason:** {result['reason']}")
            st.code(f"Rules Applied: {', '.join(result['rules_applied'])}")

            # Show GPT explanation
            st.markdown("### 🧠 GPT Explanation")
            st.write(explanation)

            # Generate and save case summary
            summary_text = generate_summary(facts, result, explanation)
            st.session_state.summary_text = summary_text

            # Download case summary
            if "summary_text" in st.session_state:
                st.download_button(
                    label="📥 Download Case Summary",
                    data=st.session_state["summary_text"],
                    file_name="case-summary.txt",
                    mime="text/plain",
                    key="download_case_summary"
                )

    # Motion Generator
    if st.session_state.get("submitted", False):
        with st.expander("📝 Generate Motion to Vacate", expanded=False):
            show_motion_generator = st.checkbox(
                "Generate motion draft",
                key="motion_generator_checkbox"
            )

            if show_motion_generator:
                st.info("🧪 Debug: Checkbox triggered — generating draft...")

                # Get values safely with .get()
                facts = st.session_state.get("facts")
                result = st.session_state.get("result")
                explanation = st.session_state.get("explanation")

                try:
                    motion_text = generate_motion(facts, result, explanation)
                    if motion_text:
                        st.text_area("Generated Motion (Editable)", value=motion_text, height=300, key="motion_text_area")

                        st.download_button(
                            label="📥 Download Draft Motion (.txt)",
                            data=motion_text,
                            file_name="motion_to_vacate.txt",
                            mime="text/plain",
                            key="download_motion_draft"
                        )
                except AssertionError as e:
                    st.error(f"⚠️ Missing required session key: {e}")
                except Exception as e:
                    st.exception(e)

                # Add developer debug panel
                with st.expander("🧪 Developer Debug Panel"):
                    st.markdown("### Session State:")
                    st.json(st.session_state)

if __name__ == "__main__":
    main()

    # Chat Interface
    try:
        # Get API key from secrets
        api_key = st.secrets.get("OPENAI_API_KEY") or st.text_input(
            "🔑 Enter your OpenAI API Key",
            type="password",
            help="Your API key is never stored or transmitted.",
            key="openai_api_key"
        )

        if not api_key:
            st.warning("🔑 Please enter your OpenAI API key to use the chatbot.")
            st.stop()
        
        # Get cached OpenAI client
        client = get_openai_client(api_key)
        
        # Create a session state variable to store the chat messages. This ensures that the
        # messages persist across reruns.
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display the existing chat messages via `st.chat_message`.
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Create a chat input field to allow the user to enter a message. This will display
        # automatically at the bottom of the page.

        if prompt := st.chat_input("What is up?"):

            # Store and display the current prompt.
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate a response using the OpenAI API.
            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )

            # Stream the response to the chat using `st.write_stream`, then store it in 

        # Generate and save case summary
        summary_text = generate_summary(facts, result, explanation)
        st.session_state.summary_text = summary_text

        # Download case summary
        if "summary_text" in st.session_state:
            st.download_button(
                label="📥 Download Case Summary",
                data=st.session_state["summary_text"],
                file_name="case-summary.txt",
                mime="text/plain",
                key="download_case_summary"
            )

# Motion Generator
if st.session_state.get("submitted", False):
    with st.expander("📝 Generate Motion to Vacate", expanded=False):
        show_motion_generator = st.checkbox(
            "Generate motion draft",
            key="motion_generator_checkbox"
        )

        if show_motion_generator:
            st.info("🧪 Debug: Checkbox triggered — generating draft...")

            # Get values safely with .get()
            facts = st.session_state.get("facts")
            result = st.session_state.get("result")
            explanation = st.session_state.get("explanation")

            try:
                motion_text = generate_motion(facts, result, explanation)
                if motion_text:
                    st.text_area("Generated Motion (Editable)", value=motion_text, height=300, key="motion_text_area")

                    st.download_button(
                        label="📥 Download Draft Motion (.txt)",
                        data=motion_text,
                        file_name="motion_to_vacate.txt",
                        mime="text/plain",
                        key="download_motion_draft"
                    )
            except AssertionError as e:
                st.error(f"⚠️ Missing required session key: {e}")
            except Exception as e:
                st.exception(e)

# Remove duplicate Motion Generator block
# ... (rest of the code remains the same)
            key="motion_generator_checkbox"
        )

        if show_motion_generator:
            st.info("🧪 Debug: Checkbox triggered — generating draft...")

            # Get values safely with .get()
            facts = st.session_state.get("facts")
            result = st.session_state.get("result")
            explanation = st.session_state.get("explanation")

            try:
                motion_text = generate_motion(facts, result, explanation)
                if motion_text:
                    st.text_area("Generated Motion (Editable)", value=motion_text, height=300, key="motion_text_area")

                    st.download_button(
                        label="📥 Download Draft Motion (.txt)",
                        data=motion_text,
                        file_name="motion_to_vacate.txt",
                        mime="text/plain",
                        key="download_motion_draft"
                    )
            except AssertionError as e:
                st.error(f"⚠️ Missing required session key: {e}")
            except Exception as e:
                st.exception(e)

            # Add developer debug panel
            with st.expander("🧪 Developer Debug Panel"):
                st.markdown("### Session State:")
                st.json(st.session_state)

if __name__ == "__main__":
    main()
