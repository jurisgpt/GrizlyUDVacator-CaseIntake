# grizly_app/ui/header.py

import streamlit as st


def render_app_header():
    st.markdown("""
    <div style='text-align: center; margin-top: 1rem; margin-bottom: 1rem;'>
        <h1 style='font-size: 2.4rem;'>⚖️ Tenant Relief Evaluation Tool</h1>
        <p style='font-size: 1.1rem; color: gray;'>Analyze eligibility for relief from eviction default judgment</p>
    </div>
    """, unsafe_allow_html=True)

