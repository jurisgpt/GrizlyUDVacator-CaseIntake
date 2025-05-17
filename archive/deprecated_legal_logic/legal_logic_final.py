from datetime import datetime, timedelta
from typing import Dict, Any, List

# =============================================================================
# LEGAL LOGIC MODULE: CCP § 473.5 Relief Eligibility Evaluator
# -----------------------------------------------------------------------------
# Evaluates eligibility to set aside a default judgment under California Code
# of Civil Procedure § 473.5 based on service date, motion date, participation,
# notice, and reliance on legal advice.
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

    result = {
        "status": "ineligible",
        "reason": "No qualifying conditions met under CCP § 473.5.",
        "rules_applied": []
    }

    # -------------------------------------------------------------------------
    # 1. DATE PARSING AND VALIDATION
    # -------------------------------------------------------------------------
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

        # Allow 1-day clock skew tolerance
        if (served - today).days > 1 or (motion - today).days > 1:
            return {
                "status": "needs_review",
                "reason": "One or more dates appear to be in the future. Please verify.",
                "rules_applied": []
            }

        if motion < served:
            return {
                "status": "needs_review",
                "reason": "Motion filed before service date — recommend verification.",
                "rules_applied": []
            }

    except Exception:
        return {
            "status": "incomplete",
            "reason": "Invalid date format. Expected YYYY-MM-DD.",
            "rules_applied": []
        }

    # -------------------------------------------------------------------------
    # 2. INPUT FLAGS AND LEGAL TIMELINE
    # -------------------------------------------------------------------------
    timely = motion <= served + timedelta(days=180)
    late = not timely

    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", False)
    bad_advice = facts.get("relied_on_bad_advice", False)

    # -------------------------------------------------------------------------
    # 3. LEGAL EVALUATION LOGIC (ORDERED BY PRIORITY)
    # -------------------------------------------------------------------------

    # 3.1: Timely motion → Always eligible
    if timely:
        return {
            "status": "relief_possible",
            "reason": "Motion filed within 180 days of service — timely under CCP § 473.5.",
            "rules_applied": ["CCP § 473.5"]
        }

    # 3.2: Late + Participated → Relief barred by CCP § 473.5(c)
    if late and participated:
        return {
            "status": "relief_barred",
            "reason": "Late motion and prior participation — procedural bar under CCP § 473.5(c).",
            "rules_applied": []
        }

    # 3.3: Late + No notice + No participation → Due process override
    if late and not actual_notice and not participated:
        return {
            "status": "relief_possible",
            "reason": "Relief allowed due to due process violation — no notice and no participation.",
            "rules_applied": ["CCP § 473.5"]
        }

    # 3.4: Late + Bad legal advice + No participation → Constructive diligence
    if late and bad_advice and not participated:
        return {
            "status": "relief_possible",
            "reason": "Late motion excused due to reliance on bad legal advice and no participation — constructive diligence.",
            "rules_applied": ["CCP § 473.5"]
        }

    # -------------------------------------------------------------------------
    # 4. DEFAULT FALLBACK
    # -------------------------------------------------------------------------
    return result
