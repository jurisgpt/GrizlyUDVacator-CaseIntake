"""
Decision tree logic for tenant relief evaluation.

This module contains the core logic for generating and manipulating decision trees
used in the tenant relief evaluation process.
"""

import graphviz


def create_decision_tree(result, facts):
    """Create and configure the decision tree visualization.

    Args:
        result (dict): Evaluation result containing case status and reason
        facts (dict): Case facts including participation and notice status

    Returns:
        graphviz.Digraph: Configured decision tree graph
    """
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
    """Highlight the decision path based on case facts.

    Args:
        tree (graphviz.Digraph): The decision tree to modify
        result (dict): Evaluation result containing case status and reason
        facts (dict): Case facts including participation and notice status
    """
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