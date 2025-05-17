import streamlit as st


def reduce_top_padding():
    """Reduce top padding"""
    st.markdown("""
        <style>
        .block-container {
            padding-top: 1rem !important;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_custom_styles():
    """Apply all custom styles"""
    reduce_top_padding()
    # Add other custom styles here if needed
