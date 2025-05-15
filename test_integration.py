import unittest
from datetime import datetime
from legal_logic import evaluate_rules
from response_logic import explain_output
import yaml

class TestUDVacatorIntegration(unittest.TestCase):
    def setUp(self):
        # Load questions from YAML
        with open("intake_questions.yaml", "r") as f:
            self.questions = yaml.safe_load(f)["questions"]
        
        # Create test facts
        self.test_facts = {
            "served_date": "2025-01-01",
            "motion_date": "2025-06-01",  # Within 180 days
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

if __name__ == '__main__':
    unittest.main()
