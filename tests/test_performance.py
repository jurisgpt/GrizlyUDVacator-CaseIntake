import pytest
import time
from datetime import datetime
import streamlit as st
from streamlit_app import load_questions, cached_evaluate_rules, cached_explain_output, get_openai_client
from legal_logic import evaluate_rules
from response_logic import explain_output

# Sample test data
test_facts = {
    "served_date": "2025-01-01",
    "motion_date": "2025-02-01",
    "participated": False,
    "actual_notice": False,
    "relied_on_bad_advice": False
}

def setup_module():
    """Setup function to initialize test environment."""
    # Initialize session state
    st.session_state.messages = []
    
    # Create a mock secrets object
    class MockSecrets:
        def __init__(self):
            self._openai = {"api_key": "test-api-key"}
        
        @property
        def openai(self):
            return self._openai
        
        def __getitem__(self, key):
            if key == 'openai':
                return self.openai
            raise KeyError(key)
    
    # Replace the secrets object
    st.secrets = MockSecrets()

class TestPerformance:
    def test_load_questions_performance(self):
        """Test performance of loading questions."""
        start_time = time.time()
        questions = load_questions()
        load_time = time.time() - start_time
        
        assert len(questions) > 0, "No questions loaded"
        print(f"Questions loaded in {load_time:.4f} seconds")
        assert load_time < 0.1, "Loading questions took too long"

    def test_legal_evaluation_performance(self):
        """Test performance of legal evaluation."""
        start_time = time.time()
        result = cached_evaluate_rules(test_facts)
        eval_time = time.time() - start_time
        
        assert result is not None, "Legal evaluation failed"
        print(f"Legal evaluation completed in {eval_time:.4f} seconds")
        assert eval_time < 0.05, "Legal evaluation took too long"

    def test_gpt_explanation_performance(self):
        """Test performance of GPT explanation generation."""
        result = cached_evaluate_rules(test_facts)
        
        start_time = time.time()
        explanation = cached_explain_output(result)
        explain_time = time.time() - start_time
        
        assert explanation is not None, "GPT explanation failed"
        print(f"GPT explanation generated in {explain_time:.4f} seconds")
        assert explain_time < 1.0, "GPT explanation took too long"

    def test_openai_client_init_performance(self):
        """Test performance of OpenAI client initialization."""
        start_time = time.time()
        client = get_openai_client(st.secrets["openai"]["api_key"])
        init_time = time.time() - start_time
        
        assert client is not None, "OpenAI client initialization failed"
        print(f"OpenAI client initialized in {init_time:.4f} seconds")
        assert init_time < 0.1, "OpenAI client initialization took too long"

    def test_complete_flow_performance(self):
        """Test performance of complete application flow."""
        start_time = time.time()
        
        # Load questions
        questions = load_questions()
        
        # Evaluate rules
        result = cached_evaluate_rules(test_facts)
        
        # Generate explanation
        explanation = cached_explain_output(result)
        
        # Total time
        total_time = time.time() - start_time
        
        print(f"Complete flow completed in {total_time:.4f} seconds")
        assert total_time < 2.0, "Complete flow took too long"

if __name__ == "__main__":
    pytest.main(["-v", "test_performance.py"])
