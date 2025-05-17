import pytest
from datetime import datetime
from legal_logic import evaluate_rules

# Helper to convert string to date
def to_date(dstr):
    return datetime.strptime(dstr, "%Y-%m-%d").date() if dstr else None

@pytest.mark.parametrize("served_date, motion_date, participated, knew, bad_advice, expected_relief, expected_rules", [
    # Valid relief scenarios
    ("2025-01-01", "2025-04-01", False, False, False, True, ["CCP § 473.5"]),
    ("2025-01-01", "2025-04-01", False, True, False, True, ["CCP § 473.5"]),
    ("2025-01-01", "2025-04-01", True, False, False, True, ["CCP § 473.5"]),
    # No relief because of participation and notice
    ("2025-01-01", "2025-04-01", True, True, False, False, []),
    # No relief due to untimely motion
    ("2022-01-01", "2025-04-01", False, False, False, False, []),
    # Edge case: same day
    ("2025-01-01", "2025-01-01", False, False, False, True, ["CCP § 473.5"]),
    # Null inputs
    (None, None, None, None, False, False, []),
    # Future dates
    ("2026-01-01", "2026-01-02", False, False, False, False, []),
    # Motion before service
    ("2025-01-10", "2025-01-05", False, False, False, False, []),
    # Edge of 180 days - should fail
    ("2024-11-17", "2025-05-16", False, False, False, False, []),
])
def test_legal_relief(served_date, motion_date, participated, knew, bad_advice, expected_relief, expected_rules):
    form_inputs = {
        "served_date": to_date(served_date),
        "motion_date": to_date(motion_date),
        "participated": participated,
        "actual_notice": knew,
        "relied_on_bad_advice": bad_advice,
    }
    result = evaluate_rules(form_inputs)
    rules_applied = result.get('rules_applied', [])

    relief_possible = bool(rules_applied)
    assert relief_possible == expected_relief, f"Expected relief={expected_relief}, got {relief_possible}"
    assert set(rules_applied) == set(expected_rules), f"Expected rules={expected_rules}, got {rules_applied}"
