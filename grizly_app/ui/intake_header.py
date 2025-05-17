import streamlit as st


def render_intake_header():
    st.markdown(
        """
        <div style='text-align: center; margin-top: 1rem;'>
            <h3 style='font-weight: 600;'>Let us know — what happened and when?</h3>
            <p style='font-size: 1rem; font-style: italic;'>
                Provide factual details about your case to check legal eligibility under CCP § 473.5.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
