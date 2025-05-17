import os

print("Starting test_legal_logic_param.py")
print("Current working directory:", os.getcwd())
print("PYTHONPATH:", os.environ.get('PYTHONPATH', 'Not set'))

import pytest
from datetime import date
from grizly_app.legal_logic_aligned import evaluate_rules

# Test cases for legal logic evaluation
# Each test case includes:
# - motion_date: Date motion was filed
# - served_date: Date service was received
# - expected_status: Expected status (relief_possible, relief_barred, error, incomplete)
# - expected_reason_part: Expected reason text
# - rules_applied: List of rules that should be applied

@pytest.mark.parametrize(
    "motion_date, served_date, expected_status, expected_reason_part, rules_applied",
    [
        # Test case: Timely filing within 180 days
        # Inputs: Motion filed 180 days before service date
        # Expected: Relief possible, motion is timely
        pytest.param(
            date(2023, 6, 1),
            date(2023, 1, 1),
            "relief_possible",
            "Motion filed within 180 days",
            ["CCP § 473.5", "timely_filing(P)", "not actual_notice(P)", "not participated(P)", "relied_on_bad_advice(P)"],
            id="timely_filing"
        ),

        # Test case: Filing on 179th day
        # Inputs: Motion filed on day 179 (within 180-day period)
        # Expected: Relief possible, motion is timely
        pytest.param(
            date(2023, 6, 29),
            date(2023, 1, 1),
            "relief_possible",
            "Motion filed within 180 days of service (179 days)",
            ["CCP § 473.5", "timely_filing(P)", "not actual_notice(P)", "not participated(P)", "relied_on_bad_advice(P)"],
            id="timely_filing_179_days"
        ),
        # Test case: Filing one day after 180-day period
        # Inputs: Motion filed one day after 180-day period
        # Expected: Relief barred, motion is untimely
        pytest.param(
            date(2023, 6, 30),
            date(2023, 1, 1),
            "relief_barred",
            "Motion filed after 180 days",
            [],
            id="untimely_filing"
        ),

        # Test case: Late filing with bad legal advice
        # Inputs: Motion filed two days late with bad legal advice
        # Expected: Relief possible due to reliance on bad advice
        pytest.param(
            date(2023, 7, 1),
            date(2023, 1, 1),
            "relief_possible",
            "Motion filed after 180 days excused due to reliance on bad legal advice",
            ["CCP § 473.5", "relied_on_bad_advice(P)"],
            id="late_filing_with_bad_advice"
        ),
        # Test case: Motion date before service date
        # Inputs: Motion date is before service date
        # Expected: Error, invalid filing order
        pytest.param(
            date(2022, 12, 31),
            date(2023, 1, 1),
            "error",
            "Motion date cannot be before service date",
            [],
            id="invalid_filing_order"
        ),

        # Test case: Missing motion date
        # Inputs: Motion date is None
        # Expected: Incomplete, missing required field
        pytest.param(
            None,
            date(2023, 1, 1),
            "incomplete",
            "Missing service or motion date",
            [],
            id="missing_required_field"
        ),

        # Test case: Invalid date type
        # Inputs: Motion date is string instead of date object
        # Expected: Error, invalid date type
        pytest.param(
            "2023-06-01",
            date(2023, 1, 1),
            "error",
            "Invalid date objects provided",
            [],
            id="invalid_date_format"
        )
    ]
)
def test_legal_logic_parametrized(motion_date, served_date, expected_status, expected_reason_part, rules_applied):
    """
    Test various legal logic scenarios using parametrization
    """
    # Set bad_advice based on the test case
    bad_advice = True if motion_date == date(2023, 7, 1) else False
        
    test_facts = {
        "served_date": served_date,
        "motion_date": motion_date,
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": bad_advice
    }  
    result = evaluate_rules(test_facts)
    assert result["status"] == expected_status
    assert expected_reason_part in result["reason"]
    assert result["rules_applied"] == rules_applied
