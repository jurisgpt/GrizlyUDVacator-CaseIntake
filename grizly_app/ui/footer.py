import streamlit as st


def render_footer():
    st.markdown("""
    <style>
    .footer {
        text-align: center;
        padding: 1rem;
        margin-top: 2rem;
        border-top: 1px solid #eee;
    }
    .footer p {
        color: #666;
    }
    .footer .disclaimer {
        color: #d32f2f;  /* Slightly darker red for better readability */
        font-weight: normal;
        font-size: 0.9em;
        line-height: 1.4;
    }
    </style>
    
    <div class="footer">
        <p>© 2024 Tenant Relief Evaluation Tool. All rights reserved.</p>
        <p class="disclaimer">Disclaimer: This tool does not provide legal information and does not constitute legal advice. This is a research/education project</p>
    </div>
    """, unsafe_allow_html=True)
