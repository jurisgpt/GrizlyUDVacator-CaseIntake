import streamlit as st


def apply_claude_style():
    """Apply Claude-inspired styling to the Streamlit app"""
    st.markdown("""
    <style>
    /* Global font and background */
    html, body, [class*="css"] {
        font-family: "Georgia", serif;
        background-color: #FAF9F6;
        color: #2E2E2E;
        font-size: 17px;
        line-height: 1.6;
    }

    /* Section headers */
    h1, h2, h3 {
        font-family: "Georgia", serif;
        font-weight: 600;
        margin-bottom: 0.4em;
    }

    /* Container tweaks */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* Panels and expander boxes */
    .st-expander, .stAlert, .stMarkdown, .stTextArea, .stSelectbox {
        background-color: #FFFFFF !important;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        padding: 1rem;
    }

    /* Buttons */
    .stButton button {
        border-radius: 8px;
        background-color: #E5E5E5;
        color: #1F1F1F;
        border: none;
        padding: 0.5rem 1.2rem;
        font-weight: 500;
    }

    .stButton button:hover {
        background-color: #DCDCDC;
        cursor: pointer;
    }

    /* Disclaimer (footer) */
    footer {
        font-size: 0.8rem;
        color: #777777;
        text-align: center;
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)
