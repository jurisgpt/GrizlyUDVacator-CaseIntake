import unittest
from datetime import date
from grizly_app.legal_logic_aligned import evaluate_rules
from grizly_app.response_logic import explain_output
import yaml

class TestUDVacatorIntegration(unittest.TestCase):
    def setUp(self):
        # Load questions from YAML
        with open("intake_questions.yaml", "r") as f:
            self.questions = yaml.safe_load(f)["questions"]
        
        # Create test facts
        self.test_facts = {
            "served_date": date(2023, 1, 1),
            "motion_date": date(2023, 6, 1),  # Within 180 days
            "participated": False,
            "actual_notice": False,
            "relied_on_bad_advice": True
        }

    def test_legal_logic(self):
        """Test the legal logic evaluation"""
        result = evaluate_rules(self.test_facts)
        self.assertEqual(result["status"], "relief_possible")
        self.assertIn("Motion filed within 180 days", result["reason"])
        self.assertIn("not actual_notice(P)", result["rules_applied"])
        self.assertIn("relied_on_bad_advice(P)", result["rules_applied"])

    def test_response_generation(self):
        """Test the GPT explanation generation"""
        result = evaluate_rules(self.test_facts)
        explanation = explain_output(result)
        self.assertIsInstance(explanation, str)
        self.assertIn("Motion filed within 180 days", explanation)
        self.assertIn("California Code of Civil Procedure § 473.5", explanation)

    def test_yaml_structure(self):
        """Test the YAML questions structure"""
        self.assertEqual(len(self.questions), 5)
        question_types = set(q["type"] for q in self.questions)
        self.assertEqual(question_types, {"date", "bool"})
        
        # Verify each question has required fields
        for q in self.questions:
            self.assertIn("id", q)
            self.assertIn("text", q)
            self.assertIn("type", q)
            self.assertIn("predicate", q)

    def test_180_day_boundary(self):
        """
        Test filing exactly on 180th day boundary
        """
        # Set motion date exactly 180 days after service date
        self.test_facts["motion_date"] = date(2023, 6, 29)  # 180 days after 2023-01-01
        result = evaluate_rules(self.test_facts)
        self.assertEqual(result["status"], "relief_possible")
        self.assertIn("Motion filed within 180 days", result["reason"])
        self.assertIn("timely_filing(P)", result["rules_applied"])

    def test_181_day_filing(self):
        """
        Test filing one day after the 180-day period
        """
        # Set motion date to 181 days after service date
        self.test_facts["motion_date"] = date(2023, 6, 30)  # 181 days after 2023-01-01
        result = evaluate_rules(self.test_facts)
        self.assertEqual(result["status"], "relief_barred")
        self.assertIn("Motion filed after 180 days", result["reason"])

if __name__ == '__main__':
    unittest.main()
