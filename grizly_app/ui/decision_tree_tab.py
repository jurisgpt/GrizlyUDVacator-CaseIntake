import json

import streamlit as st
from graphviz import Digraph

from ..logic.decision_tree_logic import (create_decision_tree,
                                         highlight_decision_path)
from .decision_tree_header import render_decision_tree_header


def export_decision_data(tree, facts):
    """Export decision data in multiple formats.
    
    Args:
        tree: A Graphviz Digraph object representing the decision tree
        facts: Dictionary containing the facts used for the decision
    """
    # Get evaluation result from session state
    result = st.session_state.get("evaluation", {})
    
    # Export DOT format if tree is valid
    if tree and hasattr(tree, 'source'):
        try:
            dot_data = tree.source
            st.download_button(
                label="📥 Download Decision Tree (.dot)",
                data=dot_data,
                file_name="decision_tree.dot",
                mime="text/vnd.graphviz"
            )
        except Exception as e:
            st.warning(f"Could not export decision tree: {str(e)}")
    else:
        st.warning("Could not export decision tree: Invalid tree format")
    
    # Export JSON summary if we have valid data
    if not isinstance(facts, dict):
        facts = {}
        
    if not isinstance(result, dict):
        result = {}
    
    try:
        graph_facts = {
            "status": result.get("status", "unknown"),
            "reason": result.get("reason", "N/A"),
            "facts": facts,
            "rules_applied": result.get("rules_applied", [])
        }
        
        json_export = json.dumps(graph_facts, indent=2, default=str)
        st.download_button(
            label="📥 Download Decision Summary (.json)",
            data=json_export,
            file_name="decision_summary.json",
            mime="application/json"
        )
    except Exception as e:
        st.error(f"Error generating JSON export: {str(e)}")
        if st.checkbox("Show export error details"):
            st.exception(e)

def render_decision_tree_tab():
    """Render the decision tree tab with visualization and exports."""
    render_decision_tree_header()

    # Get data from session state
    result = st.session_state.get("evaluation", {})
    facts = st.session_state.get("facts", {})

    if not result or not facts:
        st.warning("Please complete the intake form to view your decision path.")
        return

    try:
        # Create and highlight decision tree
        tree = create_decision_tree(result, facts)
        if tree is None:
            st.error("Failed to create decision tree.")
            return
            
        highlight_decision_path(tree, result, facts)
        st.graphviz_chart(tree)

        # Export options - pass result and facts separately
        export_decision_data(tree, facts)
        
    except Exception as e:
        st.error(f"Error rendering decision tree: {str(e)}")
        if st.checkbox("Show error details"):
            st.exception(e)
