from datetime import datetime
from typing import Dict, Any, List

# =============================================================================
# LEGAL LOGIC MODULE: CCP § 473.5 Relief Eligibility Evaluator
# -----------------------------------------------------------------------------
# This module evaluates whether a tenant qualifies for post-default relief
# under California Code of Civil Procedure § 473.5.
#
# The logic implements statutory timelines, due process protections, and
# equitable doctrines recognized in California case law such as:
# - Manson v. Black (2009)
# - Peralta v. Heights Medical (1988)
# - Anastos v. Lee (2004)
# =============================================================================

# Message constants for consistent responses
REASON_TIMELY = "Motion was filed within 180 days of service — timely under CCP § 473.5."
REASON_BAD_ADVICE = "Late motion excused due to reliance on bad legal advice — constructive diligence."
REASON_NO_NOTICE = "Relief allowed due to due process violation — tenant had no notice and did not participate."
REASON_BARRED = "Late motion and prior participation — procedural bar under CCP § 473.5(c)."
REASON_FUTURE = "One or more dates are in the future. Please verify."
REASON_BEFORE_SERVICE = "Motion was filed before service — verify accuracy."

# Status constants
STATUS_RELIEF_POSSIBLE = "relief_possible"
STATUS_RELIEF_BARRED = "relief_barred"
STATUS_NEEDS_REVIEW = "needs_review"
STATUS_INCOMPLETE = "incomplete"

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

    # ---------------------------
    # 0. Setup and Default Output
    # ---------------------------
    result = {
        "status": "ineligible",
        "reason": "No qualifying conditions met under CCP § 473.5.",
        "rules_applied": []
    }

    # ---------------------------
    # 1. Date Parsing and Checks
    # ---------------------------
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

        if served > today or motion > today:
            return {
                "status": STATUS_NEEDS_REVIEW,
                "reason": REASON_FUTURE,
                "rules_applied": []
            }

        if motion < served:
            return {
                "status": STATUS_NEEDS_REVIEW,
                "reason": REASON_BEFORE_SERVICE,
                "rules_applied": []
            }

    except Exception:
        return {
            "status": "incomplete",
            "reason": "Invalid date format. Expected YYYY-MM-DD.",
            "rules_applied": []
        }

    # ---------------------------
    # 2. Input Flags and Timeliness
    # ---------------------------
    days_elapsed = (motion - served).days
    timely = days_elapsed <= 180
    late = not timely

    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", False)
    bad_advice = facts.get("relied_on_bad_advice", False)

    # ---------------------------
    # 3. Legal Logic Evaluation
    # ---------------------------

    # Rule: Timely motion = always eligible
    if days_elapsed <= 180:
        return {
            "status": STATUS_RELIEF_POSSIBLE,
            "reason": REASON_TIMELY,
            "rules_applied": ["CCP § 473.5"]
        }

    # Rule: Late + participated = relief barred (473.5(c))
    if days_elapsed > 180 and participated:
        return {
            "status": STATUS_RELIEF_BARRED,
            "reason": REASON_BARRED,
            "rules_applied": []
        }

    # Rule: Bad legal advice override
    if late and bad_advice:
        return {
            "status": STATUS_RELIEF_POSSIBLE,
            "reason": REASON_BAD_ADVICE,
            "rules_applied": ["CCP § 473.5"]
        }

    # Rule: Due process violation override (no notice + no participation)
    if late and not actual_notice and not participated:
        return {
            "status": "relief_possible",
            "reason": "Relief allowed due to due process violation — tenant had no actual notice and did not participate.",
            "reason": "Relief allowed due to due process violation — tenant had no notice and did not participate.",
            "rules_applied": ["CCP § 473.5"]
        }

    # Rule: Constructive diligence override (bad advice)
    if late and bad_advice:
        return {
            "status": "relief_possible",
            "reason": "Late motion excused due to reliance on bad legal advice — constructive diligence.",
            "rules_applied": ["CCP § 473.5"]
        }

    # ---------------------------
    # 4. Default Denial
    # ---------------------------
    return result
