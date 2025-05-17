from grizly_app.legal_logic_aligned import evaluate_rules

# Test case: Basic relief case
case1 = {
    "served_date": "2025-01-01",
    "motion_date": "2025-04-01",
    "participated": False,
    "actual_notice": False,
    "relied_on_bad_advice": False
}

# Test case: Motion before service
case2 = {
    "served_date": "2025-01-10",
    "motion_date": "2025-01-05",
    "participated": False,
    "actual_notice": False,
    "relied_on_bad_advice": False
}

# Test case: Bad advice overrides timeliness
case3 = {
    "served_date": "2022-01-01",
    "motion_date": "2025-04-01",
    "participated": False,
    "actual_notice": False,
    "relied_on_bad_advice": True
}

# Test cases: 180-day boundary
case4 = {
    "served_date": "2024-11-18",
    "motion_date": "2025-05-17",
    "participated": False,
    "actual_notice": False,
    "relied_on_bad_advice": False
}

case5 = {
    "served_date": "2024-11-17",
    "motion_date": "2025-05-17",
    "participated": False,
    "actual_notice": False,
    "relied_on_bad_advice": False
}

test_cases = [case1, case2, case3, case4, case5]

for i, case in enumerate(test_cases, 1):
    result = evaluate_rules(case)
    print(f"\nTest Case {i}:")
    print(f"Input: {case}")
    print(f"Result: {result}")
