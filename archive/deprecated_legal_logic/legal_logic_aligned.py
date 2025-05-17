from datetime import datetime, timedelta
from typing import Dict, Any, List

# =============================================================================
# LEGAL LOGIC MODULE: CCP § 473.5 Relief Eligibility Evaluator (Aligned Version)
# -----------------------------------------------------------------------------
# This version aligns exactly with test expectations in terms of logic and
# message wording. Designed for consistent evaluation and test automation.
# =============================================================================

def evaluate_rules(facts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parameters
    ----------
    facts : dict
        {
            'served_date': 'YYYY-MM-DD',
            'motion_date': 'YYYY-MM-DD',
            'participated': bool,
            'actual_notice': bool,
            'relied_on_bad_advice': bool
        }

    Returns
    -------
    dict
        {
            'status': str,
            'reason': str,
            'rules_applied': List[str]
        }
    """

    # --- Default return structure ---
    result = {
        "status": "ineligible",
        "reason": "No qualifying conditions met under CCP § 473.5.",
        "rules_applied": []
    }

    # --- Date parsing and sanity checks ---
    try:
        served_str = facts.get("served_date")
        motion_str = facts.get("motion_date")

        if not served_str or not motion_str:
            return {
                "status": "incomplete",
                "reason": "Missing service or motion date.",
                "rules_applied": []
            }

        served = datetime.strptime(served_str, "%Y-%m-%d").date()
        motion = datetime.strptime(motion_str, "%Y-%m-%d").date()
        today = datetime.now().date()

        # Allow one day skew tolerance
        if (served - today).days > 1 or (motion - today).days > 1:
            return {
                "status": "needs_review",
                "reason": "One or more dates are in the future. Please verify.",
                "rules_applied": []
            }

        if motion < served:
            return {
                "status": "needs_review",
                "reason": "Motion was filed before service date — recommend verification.",
                "rules_applied": []
            }

    except Exception:
        return {
            "status": "incomplete",
            "reason": "Invalid date format. Expected YYYY-MM-DD.",
            "rules_applied": []
        }

    # --- Legal evaluation flags ---
    timely = motion <= served + timedelta(days=180)
    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", False)
    bad_advice = facts.get("relied_on_bad_advice", False)

    # --- Final decision tree ---
    if timely:
        return {
            "status": "relief_possible",
            "reason": "Motion was filed within 180 days of service — timely under CCP § 473.5.",
            "rules_applied": ["CCP § 473.5"]
        }

    if not timely and participated:
        return {
            "status": "relief_barred",
            "reason": "Late motion and prior participation — procedural bar under CCP § 473.5(c).",
            "rules_applied": []
        }

    if not timely and not actual_notice and not participated:
        return {
            "status": "relief_possible",
            "reason": "Relief allowed due to due process violation — tenant had no notice and did not participate.",
            "rules_applied": ["CCP § 473.5"]
        }

    if not timely and bad_advice and not participated:
        return {
            "status": "relief_possible",
            "reason": "Late motion excused due to reliance on bad legal advice and no participation — constructive diligence.",
            "rules_applied": ["CCP § 473.5"]
        }

    # --- No qualifying path ---
    return result
