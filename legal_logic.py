from datetime import datetime

def evaluate_rules(facts):
    """
    Evaluate post-default UD relief eligibility under CCP § 473.5.
    """
    result = {
        'status': 'ineligible',
        'reason': '',
        'rules_applied': []
    }
    
    try:
        served = datetime.strptime(facts.get("served_date"), "%Y-%m-%d")
        motion = datetime.strptime(facts.get("motion_date"), "%Y-%m-%d")
    except (ValueError, TypeError):
        return {
            "status": "incomplete",
            "reason": "Missing or invalid date(s).",
            "rules_applied": []
        }

    late = (motion - served).days > 180
    participated = facts.get("participated", False)
    actual_notice = facts.get("actual_notice", True)
    relied_on_bad_advice = facts.get("relied_on_bad_advice", False)

    rules_applied = []
    if late: rules_applied.append("late_motion(P)")
    if not participated: rules_applied.append("not participated_before_default(P)")
    if not actual_notice: rules_applied.append("not actual_notice(P)")
    if relied_on_bad_advice: rules_applied.append("relied_on_bad_advice(P)")

    # Legal Logic
    if late and participated:
        return {
            "status": "relief_barred",
            "reason": "Late motion and tenant participated before default — barred under CCP § 473.5(c).",
            "rules_applied": rules_applied
        }

    if late and not participated and not actual_notice:
        return {
            "status": "relief_possible",
            "reason": "Late motion overridden by due process violation — no notice and no participation.",
            "rules_applied": rules_applied
        }

    if late and not participated and relied_on_bad_advice:
        return {
            "status": "relief_possible",
            "reason": "Late motion may be excused due to reliance on bad legal advice — constructive diligence.",
            "rules_applied": rules_applied
        }

    if not late:
        return {
            "status": "relief_possible",
            "reason": "Motion filed within 180 days — timely under CCP § 473.5.",
            "rules_applied": rules_applied
        }

    return {
        "status": "needs_review",
        "reason": "Unclear eligibility — recommend attorney review.",
        "rules_applied": rules_applied
    }
