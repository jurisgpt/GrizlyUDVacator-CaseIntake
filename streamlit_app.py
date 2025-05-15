import streamlit as st
from openai import OpenAI

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

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
try:
    # Get API key from secrets
    openai_api_key = st.secrets["openai"]["api_key"]
    if not openai_api_key:
        st.error("Please add your OpenAI API key in .streamlit/secrets.toml")
    else:
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
