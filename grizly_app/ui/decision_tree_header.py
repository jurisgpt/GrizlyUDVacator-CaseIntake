import streamlit as st


def render_decision_tree_header():
    st.header("🌳 Legal Decision Tree")
    st.markdown("""
    <style>
    .decision-tree-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    
    <div class="decision-tree-header">
        <h3>Visualizing Your Legal Options</h3>
        <p>This decision tree shows how your case was evaluated based on California law.</p>
    </div>
    """, unsafe_allow_html=True)
