import pytest
from datetime import datetime, timedelta
from grizly_app.legal_logic_aligned import evaluate_rules

# Helper to convert string to date
def to_date(dstr):
    return datetime.strptime(dstr, "%Y-%m-%d").date() if dstr else None

# Test cases with clear names and descriptions
test_cases = [
    # Basic relief cases
    {
        "name": "basic_relief_case",
        "served_date": "2025-01-01",
        "motion_date": "2025-04-01",
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
        "expected": {
            "status": "relief_possible",
            "reason": "Motion filed within 180 days of service (90 days) — timely under CCP § 473.5.",
            "rules_applied": ["CCP § 473.5"]
        }
    },
    # Motion before service
    {
        "name": "motion_before_service",
        "served_date": "2025-01-10",
        "motion_date": "2025-01-05",
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
        "expected": {
            "status": "needs_review",
            "reason": "Motion was filed before service — verify accuracy.",
            "rules_applied": []
        }
    },
    # Bad advice overrides timeliness
    {
        "name": "bad_advice_overrides_timeliness",
        "served_date": "2022-01-01",
        "motion_date": "2025-04-01",
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": True,
        "expected": {
            "status": "relief_possible",
            "reason": "Late motion excused due to reliance on bad legal advice — constructive diligence.",
            "rules_applied": ["CCP § 473.5"]
        }
    },
    # 180-day boundary cases
    {
        "name": "exactly_180_days",
        "served_date": "2024-11-18",
        "motion_date": "2025-05-17",
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
        "expected": {
            "status": "relief_possible",
            "reason": "Motion filed within 180 days of service (180 days) — timely under CCP § 473.5.",
            "rules_applied": ["CCP § 473.5"]
        }
    },
    {
        "name": "one_day_over_180",
        "served_date": "2024-11-17",
        "motion_date": "2025-05-17",
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
        "expected": {
            "status": "relief_barred",
            "reason": "Motion filed after 180 days without valid excuse.",
            "rules_applied": []
        }
    },
    # Future dates
    {
        "name": "future_dates",
        "served_date": "2026-01-01",
        "motion_date": "2026-01-02",
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
        "expected": {
            "status": "needs_review",
            "reason": "One or more dates are in the future. Please verify.",
            "rules_applied": []
        }
    },
    # Missing dates
    {
        "name": "missing_dates",
        "served_date": None,
        "motion_date": None,
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
        "expected": {
            "status": "incomplete",
            "reason": "Missing service or motion date.",
            "rules_applied": []
        }
    }
]

@pytest.mark.parametrize("test_case", test_cases, ids=[tc["name"] for tc in test_cases])
def test_legal_logic(test_case):
    """Test the legal relief determination logic"""
    # Convert dates to datetime objects
    inputs = {
        "served_date": test_case["served_date"],
        "motion_date": test_case["motion_date"],
        "participated": test_case["participated"],
        "actual_notice": test_case["actual_notice"],
        "relied_on_bad_advice": test_case["relied_on_bad_advice"]
    }
    
    result = evaluate_rules(inputs)
    
    # Check status
    assert result["status"] == test_case["expected"]["status"], (
        f"{test_case['name']}: Expected status={test_case['expected']['status']}, got {result['status']}"
    )
    
    # Check reason
    assert result["reason"] == test_case["expected"]["reason"], (
        f"{test_case['name']}: Expected reason='{test_case['expected']['reason']}', got '{result['reason']}'"
    )
    
    # Check rules applied
    assert result["rules_applied"] == test_case["expected"]["rules_applied"], (
        f"{test_case['name']}: Expected rules={test_case['expected']['rules_applied']}, got {result['rules_applied']}"
    )
