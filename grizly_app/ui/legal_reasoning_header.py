import streamlit as st


def render_legal_reasoning_header():
    st.markdown("""
    <div style='text-align: left; margin-top: 1rem;'>
        <h3>Understanding Your Legal Rights</h3>
        <p>This section provides a detailed explanation of how your case was evaluated.</p>
    </div>
    """, unsafe_allow_html=True)
