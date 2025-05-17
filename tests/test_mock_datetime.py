import unittest
from datetime import date
from grizly_app.legal_logic_aligned import evaluate_rules

class TestDateValidation(unittest.TestCase):
    def test_date_validation(self):
        """
        Test date validation with actual date objects
        """
        # Test case where motion is before service
        test_facts = {
            "served_date": date(2024, 1, 1),
            "motion_date": date(2023, 12, 1),
            "participated": False,
            "actual_notice": False,
            "relied_on_bad_advice": False
        }
        
        result = evaluate_rules(test_facts)
        self.assertEqual(result["status"], "error")
        self.assertIn("Motion date cannot be before service date", result["reason"])

    def test_timely_filing(self):
        """
        Test timely filing case with actual date objects
        """
        # Test case where motion is within 180 days
        test_facts = {
            "served_date": date(2024, 1, 1),
            "motion_date": date(2024, 6, 1),
            "participated": False,
            "actual_notice": False,
            "relied_on_bad_advice": False
        }
        
        result = evaluate_rules(test_facts)
        self.assertEqual(result["status"], "relief_possible")
        self.assertIn("timely_filing(P)", result["rules_applied"])

if __name__ == '__main__':
    unittest.main()
