import streamlit as st
import graphviz
from ui.decision_tree_header import render_decision_tree_header

def create_decision_tree(result, facts):
    """Create and configure the decision tree visualization."""
    tree = graphviz.Digraph()
    tree.attr(rankdir='TB', size='6')

    # Define nodes
    tree.node("A", "Was motion filed within 180 days?")
    tree.node("B", "✅ Relief Granted (Timely)")
    tree.node("C", "Did tenant participate before default?")
    tree.node("D", "❌ Relief Barred (473.5c)")
    tree.node("E", "Was there no notice or bad legal advice?")
    tree.node("F", "✅ Relief Granted (Due Process or Equity)")
    tree.node("G", "❌ No Relief")

    # Define edges
    tree.edge("A", "B", label="Yes")
    tree.edge("A", "C", label="No")
    tree.edge("C", "D", label="Yes")
    tree.edge("C", "E", label="No")
    tree.edge("E", "F", label="Yes")
    tree.edge("E", "G", label="No")

    return tree

def highlight_decision_path(tree, result, facts):
    """Highlight the decision path based on case facts."""
    timely = "within 180" in result["reason"].lower()
    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", False)
    bad_advice = facts.get("relied_on_bad_advice", False)

    if timely:
        tree.node("B", "✅ Relief Granted (Timely)", style="filled", fillcolor="lightgreen")
    elif not timely and participated:
        tree.node("D", "❌ Relief Barred (473.5c)", style="filled", fillcolor="lightcoral")
    elif not timely and not actual_notice and not participated:
        tree.node("F", "✅ Relief Granted (Due Process)", style="filled", fillcolor="lightgreen")
    elif not timely and bad_advice and not participated:
        tree.node("F", "✅ Relief Granted (Bad Advice)", style="filled", fillcolor="lightgreen")
    else:
        tree.node("G", "❌ No Relief", style="filled", fillcolor="lightcoral")

def export_decision_data(result, facts):
    """Export decision data in multiple formats."""
    # Export DOT format
    dot_data = result.source
    st.download_button(
        label="📥 Download Decision Tree (.dot)",
        data=dot_data,
        file_name="decision_tree.dot",
        mime="text/vnd.graphviz"
    )

    # Export JSON summary
    graph_facts = {
        "status": result.get("status", "unknown"),
        "reason": result.get("reason", "N/A"),
        "facts": facts,
        "rules_applied": result.get("rules_applied", [])
    }
    json_export = json.dumps(graph_facts, indent=2)

    st.download_button(
        label="📥 Download Decision Summary (.json)",
        data=json_export,
        file_name="decision_summary.json",
        mime="application/json"
    )

def render_decision_tree_tab():
    """Render the decision tree tab with visualization and exports."""
    render_decision_tree_header()

    result = st.session_state.get("evaluation")
    facts = st.session_state.get("facts")

    if not result or not facts:
        st.warning("Please complete the intake form to view your decision path.")
        return

    # Create and highlight decision tree
    tree = create_decision_tree(result, facts)
    highlight_decision_path(tree, result, facts)
    st.graphviz_chart(tree)

    # Export options
    export_decision_data(tree, facts)
