from datetime import datetime
from typing import Dict, Any, List

# =============================================================================
# LEGAL LOGIC MODULE: CCP § 473.5 Eligibility Evaluation
# -----------------------------------------------------------------------------
# This module evaluates whether a tenant is eligible to set aside a default
# judgment under California Code of Civil Procedure § 473.5.
# =============================================================================

def _are_dates_valid(served_date_str: str, motion_date_str: str) -> Dict[str, Any]:
    """Validates and parses service and motion dates."""
    if not served_date_str or not motion_date_str:
        return {"valid": False, "reason": "Missing date(s).", "served": None, "motion": None}

    try:
        served = datetime.strptime(served_date_str, "%Y-%m-%d")
        motion = datetime.strptime(motion_date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        return {"valid": False, "reason": "Invalid date format.", "served": None, "motion": None}

    today_dt = datetime.now()
    # Compare only dates, not times, by converting datetime objects to date objects for comparison
    today = today_dt.date()
    served_date_obj = served.date()
    motion_date_obj = motion.date()

    if motion_date_obj < served_date_obj:
        return {"valid": False, "reason": "Motion filed before service date — recommend attorney review.", "served": served, "motion": motion}

    if served_date_obj > today or motion_date_obj > today:
        return {"valid": False, "reason": "Future dates — recommend attorney review.", "served": served, "motion": motion}

    return {"valid": True, "reason": "", "served": served, "motion": motion}


def _is_motion_timely(served_date: datetime, motion_date: datetime) -> bool:
    """Checks if the motion was filed within 180 days of service."""
    return (motion_date - served_date).days <= 180


def _evaluate_late_motion_conditions(facts: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluates conditions for a late motion."""
    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", False)
    relied_on_bad_advice = facts.get("relied_on_bad_advice", False)

    rules = ["CCP § 473.5: Late Motion"]

    if participated:
        return {
            "status": "relief_barred",
            "reason": "Late motion and tenant participated before default — barred under CCP § 473.5(c).",
            "rules_applied": rules + ["CCP § 473.5(c): Barred - Prior Participation"]
        }
    if not actual_notice:
        return {
            "status": "relief_possible",
            "reason": "Late motion overridden by due process violation — no notice and no participation.",
            "rules_applied": rules + ["CCP § 473.5: Due Process Violation (No Notice)"]
        }
    if relied_on_bad_advice:
        return {
            "status": "relief_possible",
            "reason": "Late motion may be excused due to reliance on bad legal advice — constructive diligence.",
            "rules_applied": rules + ["CCP § 473.5: Constructive Diligence (Bad Advice)"]
        }
    return {
        "status": "relief_barred",
        "reason": "Motion filed after 180 days without valid excuse.",
        "rules_applied": rules + ["CCP § 473.5: Barred - No Valid Excuse for Lateness"]
    }


def _evaluate_timely_motion_conditions(facts: Dict[str, Any]) -> Dict[str, Any]:
    """Evaluates conditions for a timely motion."""
    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", False)
    relied_on_bad_advice = facts.get("relied_on_bad_advice", False)

    rules = ["CCP § 473.5: Timely Motion"]

    if participated:
        if not actual_notice:
            return {
                "status": "relief_possible",
                "reason": "Motion within 180 days but no notice — due process violation.",
                "rules_applied": rules + ["CCP § 473.5: Due Process Violation (No Notice)"]
            }
        if relied_on_bad_advice: # This condition implies actual_notice might be true or false, but bad_advice is key
            return {
                "status": "relief_possible",
                "reason": "Motion within 180 days and reliance on bad legal advice.",
                "rules_applied": rules + ["CCP § 473.5: Constructive Diligence (Bad Advice)"]
            }
        return { # Participated and had actual notice (or no bad advice excuse)
            "status": "relief_barred",
            "reason": "Motion within 180 days but tenant participated before default with notice.",
            "rules_applied": rules + ["CCP § 473.5(c): Barred - Prior Participation with Notice"]
        }
    # Not participated
    return {
        "status": "relief_possible",
        "reason": "Motion within 180 days and no participation before default.",
        "rules_applied": rules + ["CCP § 473.5: No Prior Participation"]
    }


def evaluate_rules(facts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates post-default relief eligibility under CCP § 473.5 based on user input.

    Parameters
    ----------
    facts : dict
        Dictionary containing:
            - served_date: str in "YYYY-MM-DD"
            - motion_date: str in "YYYY-MM-DD"
            - participated: bool
            - actual_notice: bool
            - relied_on_bad_advice: bool

    Returns
    -------
    dict
        {
            "status": str,               # One of: "relief_possible", "relief_barred", "ineligible", "incomplete", "needs_review"
            "reason": str,               # Human-readable explanation of legal logic
            "rules_applied": List[str]   # Which legal rule(s) were applied
        }
    """
    served_date_str = facts.get("served_date")
    motion_date_str = facts.get("motion_date")

    date_validation_result = _are_dates_valid(served_date_str, motion_date_str)
    if not date_validation_result["valid"]:
        return {
            "status": "incomplete" if date_validation_result["reason"] in ["Missing date(s).", "Invalid date format."] else "needs_review",
            "reason": date_validation_result["reason"],
            "rules_applied": []
        }

    served_date = date_validation_result["served"]
    motion_date = date_validation_result["motion"]

    if not _is_motion_timely(served_date, motion_date):
        return _evaluate_late_motion_conditions(facts)
    
    return _evaluate_timely_motion_conditions(facts)

    # Default return, though ideally all paths are covered by helpers
    # This line should ideally not be reached if logic is exhaustive.
    # return {
    #     "status": "ineligible",
    #     "reason": "No qualifying conditions met under CCP § 473.5. (Default)",
    #     "rules_applied": ["CCP § 473.5: Default - No Conditions Met"]
    # }
# Note: Removed the final "return result" and the "DEFAULT RETURN" comment block as they are now unreachable
# due to the refactoring. The main function now directly returns results from helper functions.
