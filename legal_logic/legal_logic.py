from datetime import datetime
from typing import Dict, Any, List

# =============================================================================
# LEGAL LOGIC MODULE: CCP § 473.5 Eligibility Evaluation
# -----------------------------------------------------------------------------
# This module evaluates whether a tenant is eligible to set aside a default
# judgment under California Code of Civil Procedure § 473.5.
# =============================================================================

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
            "status": str,               # One of: "relief_possible", "relief_barred", "ineligible", "incomplete"
            "reason": str,               # Human-readable explanation of legal logic
            "rules_applied": List[str]   # Which legal rule(s) were applied
        }
    """

    # Default output if no conditions are met
    result = {
        "status": "ineligible",
        "reason": "No qualifying conditions met under CCP § 473.5.",
        "rules_applied": []
    }

    try:
        served_date = facts.get("served_date")
        motion_date = facts.get("motion_date")
        
        if not served_date or not motion_date:
            return {
                "status": "incomplete",
                "reason": "Missing date(s).",
                "rules_applied": []
            }
            
        served = datetime.strptime(served_date, "%Y-%m-%d")
        motion = datetime.strptime(motion_date, "%Y-%m-%d")
        
        # Check for motion before service first
        if motion < served:
            return {
                "status": "needs_review",
                "reason": "Motion filed before service date — recommend attorney review.",
                "rules_applied": []
            }

        # Check for future dates
        today = datetime.now().date()
        if served > today or motion > today:
            return {
                "status": "needs_review",
                "reason": "Future dates — recommend attorney review.",
                "rules_applied": []
            }

        # If dates are valid, proceed with the rest of the logic
        late = (motion - served).days > 180
        participated = facts.get("participated", False)
        actual_notice = facts.get("actual_notice", False)
        relied_on_bad_advice = facts.get("relied_on_bad_advice", False)

        rules_applied = []
        if late:
            rules_applied.append("CCP § 473.5")
        if not participated:
            rules_applied.append("CCP § 473.5")
        if not actual_notice:
            rules_applied.append("CCP § 473.5")
        if relied_on_bad_advice:
            rules_applied.append("CCP § 473.5")

        # Legal Logic
        if late:
            if participated:
                return {
                    "status": "relief_barred",
                    "reason": "Late motion and tenant participated before default — barred under CCP § 473.5(c).",
                    "rules_applied": []
                }
            elif not actual_notice:
                return {
                    "status": "relief_possible",
                    "reason": "Late motion overridden by due process violation — no notice and no participation.",
                    "rules_applied": ["CCP § 473.5"]
                }
            elif relied_on_bad_advice:
                return {
                    "status": "relief_possible",
                    "reason": "Late motion may be excused due to reliance on bad legal advice — constructive diligence.",
                    "rules_applied": ["CCP § 473.5"]
                }
            else:
                return {
                    "status": "relief_barred",
                    "reason": "Motion filed after 180 days without valid excuse.",
                    "rules_applied": []
                }
        elif not late and participated:
            if not actual_notice:
                return {
                    "status": "relief_possible",
                    "reason": "Motion within 180 days but no notice — due process violation.",
                    "rules_applied": ["CCP § 473.5"]
                }
            elif relied_on_bad_advice:
                return {
                    "status": "relief_possible",
                    "reason": "Motion within 180 days and reliance on bad legal advice.",
                    "rules_applied": ["CCP § 473.5"]
                }
            else:
                return {
                    "status": "relief_barred",
                    "reason": "Motion within 180 days but tenant participated before default.",
                    "rules_applied": []
                }
        else:
            return {
                "status": "relief_possible",
                "reason": "Motion within 180 days and no participation before default.",
                "rules_applied": ["CCP § 473.5"]
            }

    except (ValueError, TypeError):
        return {
            "status": "incomplete",
            "reason": "Invalid date format.",
            "rules_applied": []
        }


        }

    return result

    # -------------------------------------------------------------------------
    # 4. DEFAULT RETURN (IF NO CONDITIONS MET)
    # -------------------------------------------------------------------------
    return result
