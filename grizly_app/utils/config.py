from typing import Any, Dict, List

import streamlit as st
import yaml
from openai import OpenAI

from grizly_app.utils.logger_manager import LoggerManager

# Initialize logger
logger = LoggerManager().get_logger()

# Initialize OpenAI client with caching
@st.cache_resource
def get_openai_client(api_key: str) -> OpenAI:
    """Initialize and cache the OpenAI client."""
    return OpenAI(api_key=api_key)

# Cache the legal evaluation function
@st.cache_data
def cached_evaluate_rules(facts: Dict[str, Any]) -> Dict[str, Any]:
    """Cache the legal evaluation results."""
    try:
        from grizly_app.legal_logic_aligned import evaluate_rules
        return evaluate_rules(facts)
    except Exception as e:
        logger.error(f"Error in cached_evaluate_rules: {str(e)}")
        raise

# Cache the GPT explanation generation
@st.cache_data
def cached_explain_output(result: Dict[str, Any]) -> str:
    """Cache the GPT explanation."""
    try:
        from grizly_app.response_logic import explain_output
        return explain_output(result)
    except Exception as e:
        logger.error(f"Error in cached_explain_output: {str(e)}")
        raise

# Load and cache intake questions
@st.cache_data
def load_questions() -> List[Dict[str, Any]]:
    """Load and cache intake questions."""
    try:
        with open("intake_questions.yaml", "r") as f:
            return yaml.safe_load(f)["questions"]
    except Exception as e:
        logger.error(f"Error loading questions: {str(e)}")
        raise
