import streamlit as st


def render_motion_header():
    st.header("📑 Case Summary")
    st.markdown("""
    <style>
    .motion-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    
    <div class="motion-header">
        <h3>Review Your Legal Evaluation</h3>
        <p>Below you'll find a summary of your legal evaluation and any available motion drafts.</p>
    </div>
    """, unsafe_allow_html=True)
