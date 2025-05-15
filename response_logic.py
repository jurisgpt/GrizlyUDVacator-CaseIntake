from typing import Dict

def explain_output(result: Dict) -> str:
    """
    Generate a GPT-friendly explanation of the evaluation result.
    
    Args:
        result (Dict): Evaluation result from evaluate_rules
        
    Returns:
        str: Natural language explanation
    """
    explanation = f"""
    Based on the evaluation of your case under California Code of Civil Procedure § 473.5:

    Status: {result['status'].replace('_', ' ').title()}
    
    Reason: {result['reason']}
    
    The following rules were applied:
    {', '.join(result['rules_applied'])}
    
    This evaluation considers:
    - The 180-day filing requirement
    - Whether you participated in the lawsuit
    - Whether you had actual notice of the lawsuit
    - Whether you relied on bad legal advice
    
    If you have any questions about this evaluation, feel free to ask!
    """
    return explanation
