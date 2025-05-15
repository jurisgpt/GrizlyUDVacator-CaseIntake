import streamlit as st
from openai import OpenAI
import yaml
from legal_logic import evaluate_rules
from response_logic import explain_output
from summary_generator import generate_summary, save_summary

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

> Don’t worry — your data is not shared or stored, and everything runs locally in your browser.

---
""")

@st.cache_data
def load_questions():
    with open("intake_questions.yaml", "r") as f:
        return yaml.safe_load(f)["questions"]

questions = load_questions()

form_inputs = {}

with st.form("ud_intake_form"):
    st.subheader("📝 Intake Form – Tell us what happened")
    
    for q in questions:
        if q["type"] == "date":
            form_inputs[q["id"]] = st.date_input(q["text"])
        elif q["type"] == "bool":
            form_inputs[q["id"]] = st.checkbox(q["text"])

    submitted = st.form_submit_button("Evaluate Legal Relief")

if submitted:
    facts = {
        "served_date": form_inputs["served_date"].strftime("%Y-%m-%d"),
        "motion_date": form_inputs["motion_date"].strftime("%Y-%m-%d"),
        "participated": form_inputs["participated"],
        "actual_notice": form_inputs["actual_notice"],
        "relied_on_bad_advice": form_inputs["relied_on_bad_advice"]
    }

    result = evaluate_rules(facts)
    explanation = explain_output(result)

    st.markdown("### ✅ Evaluation Result")
    st.success(f"**Status:** {result['status'].replace('_', ' ').title()}")
    st.info(f"**Reason:** {result['reason']}")
    st.code(f"Rules Applied: {', '.join(result['rules_applied'])}")
    st.markdown("### 🧠 GPT Explanation")
    st.write(explanation)

    # Generate and save case summary
    summary_text = generate_summary(facts, result, explanation)
    save_summary(summary_text)

    # Add download button for case summary
    st.download_button(
        label="📥 Download Case Summary",
        data=summary_text,
        file_name="case-summary.txt",
        mime="text/plain"
    )

try:
    # Get API key from secrets
    openai_api_key = st.secrets["openai"]["api_key"]
    if not openai_api_key:
        st.error("Please add your OpenAI API key in .streamlit/secrets.toml")
        exit()
    
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)
    
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
