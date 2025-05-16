import streamlit as st
from openai import OpenAI
import yaml
from typing import Dict, Any, List
from legal_logic import evaluate_rules
from response_logic import explain_output
import sys
from summary_generator import generate_summary, save_summary
from motion_drafter import render_motion_template
from datetime import datetime

# Feature toggle for motion draft generation
ENABLE_MOTION_GENERATOR = True

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

# Show title and description.
st.markdown("""
## 🏠 GrizlyUDVacator – Tenant Relief Triage Chatbot

Welcome to **GrizlyUDVacator**, a symbolic AI-powered assistant designed to help tenants—and the legal professionals who support them—analyze and challenge default judgments in **unlawful detainer (eviction)** cases under **California Code of Civil Procedure § 473.5**.

This chatbot uses a combination of:
- 🧠 **Formal legal logic** (statutory rules + case law reasoning)
- 💬 **OpenAI’s GPT model** (for clear explanations and summaries)
- ⚖️ Designed for **legal aid clinics, pro bono teams, and tenants facing eviction**

### 🔐 Getting Started
To run the chatbot, please provide your **OpenAI API key** below. This is required to generate natural language explanations based on your intake.

---

### 📁 Project Repository
[![GitHub](https://img.shields.io/badge/View_on-GitHub-24292e?logo=github&logoColor=white)](https://github.com/jurisgpt/GrizlyUDVacator-CaseIntake)

**Version:** `v1.0.0-beta`
🔐 Mode: `Legal Aid Staff`

> Don’t worry — your data is not shared or stored, and everything runs locally in your browser.

---
""")

questions = load_questions()

form_inputs: Dict[str, Any] = {}

with st.form("ud_intake_form"):
    st.subheader("📝 Intake Form – Tell us what happened")
    
    for q in questions:
        if q["type"] == "date":
            date_val = st.date_input(q["text"])
            form_inputs[q["id"]] = str(date_val) if date_val else None
        elif q["type"] == "bool":
            form_inputs[q["id"]] = st.checkbox(q["text"])

    submitted = st.form_submit_button("Evaluate Legal Relief")

# Initialize session state for motion generator
if "motion_generator" not in st.session_state:
    st.session_state.motion_generator = {
        "enabled": False,
        "show": False,
        "motion_text": ""
    }

# Initialize variables to prevent NameError
facts = None
result = None
explanation = None

if submitted:
    # Create facts and result
    facts = {
        "served_date": str(form_inputs["served_date"]),
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

    # Only show motion generator if form was submitted and we have valid data
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
        st.session_state['summary_text'] = summary_text
        save_summary(summary_text)

# Show motion generator after successful submission
if ENABLE_MOTION_GENERATOR and st.session_state.get("submitted"):
    st.markdown("### 📝 Optional: Draft Motion to Vacate")

    show_motion_generator = st.checkbox(
        "Generate motion draft",
        key="checkbox_motion"
    )

    if show_motion_generator:
        st.info("🧪 Debug: Checkbox triggered — generating draft...")

        try:
            # Validate required keys exist
            assert "facts" in st.session_state, "Facts missing from session"
            assert "result" in st.session_state, "Result missing from session"
            assert "explanation" in st.session_state, "Explanation missing from session"

            from motion_drafter import render_motion_template

            motion_text = render_motion_template(
                st.session_state["facts"],
                st.session_state["result"],
                st.session_state["explanation"]
            )

            st.text_area("Generated Motion (Editable)", value=motion_text, height=300)

            st.download_button(
                label="📥 Download Draft Motion (.txt)",
                data=motion_text,
                file_name="motion_to_vacate.txt",
                mime="text/plain"
            )

        except AssertionError as e:
            st.error(f"⚠️ Missing required session key: {e}")
        except Exception as e:
            st.exception(e)

    # Add developer debug panel
    with st.expander("🧪 Developer Debug Panel"):
        st.markdown("### Session State:")
        st.json(st.session_state)

    # Add download button for case summary
    if "summary_text" in st.session_state:
        st.download_button(
            label="📥 Download Case Summary",
            data=st.session_state["summary_text"],
            file_name="case-summary.txt",
            mime="text/plain"
        )



try:
    # Get API key from secrets
    openai_api_key = st.secrets["openai"]["api_key"]
    if not openai_api_key:
        st.error("Please add your OpenAI API key in .streamlit/secrets.toml")
        st.stop()
    
    # Get cached OpenAI client
    client = get_openai_client(openai_api_key)
    
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
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
except KeyError:
    st.error("Please add your OpenAI API key in .streamlit/secrets.toml")
