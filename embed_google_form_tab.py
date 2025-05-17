import streamlit as st

# Page config
st.set_page_config(page_title="Grizly UD Vacator", layout="wide", initial_sidebar_state="collapsed")

# Top-level Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📋 Intake Form", 
    "📑 Motion Summary", 
    "🧠 Legal Reasoning", 
    "🌳 Decision Tree", 
    "📂 Evidence & Attachments", 
    "📨 External Intake Form"
])

# Tab 6: Google Form Embed
with tab6:
    st.header("📨 Submit via Google Form")
    st.markdown("Use this form if you prefer a familiar web interface. Your response will be processed and analyzed.")

    st.components.v1.iframe(
        src="https://docs.google.com/forms/d/e/1FAIpQLSc3RrptlqZctHOVmGGyoRPL38DfgmwCKYtkHZrIxlQGVReYiw/viewform?embedded=true",
        height=900
    )
