from datetime import datetime
from typing import Dict, Any

def render_motion_template(facts: Dict[str, Any], result: Dict[str, Any], explanation: str) -> str:
    """
    Generate a motion draft based on evaluated facts and legal analysis.
    
    Args:
        facts (Dict): Case facts from intake form
        result (Dict): Legal evaluation result
        explanation (str): GPT-generated explanation
        
    Returns:
        str: Draft motion text
    """
    
    # Get all potentially missing keys with defaults
    defendant_name = facts.get('defendant_name', '[DEFENDANT NAME]')
    case_number = facts.get('case_number', '[CASE NUMBER]')
    served_date = facts.get('served_date', '[DATE SERVED]')
    motion_date = facts.get('motion_date', '[DATE FILED]')
    
    # Format dates if they exist
    if served_date != '[DATE SERVED]':
        served_date = datetime.strptime(served_date, '%Y-%m-%d').strftime('%B %d, %Y')
    if motion_date != '[DATE FILED]':
        motion_date = datetime.strptime(motion_date, '%Y-%m-%d').strftime('%B %d, %Y')
    
    return f"""
    [This is a rough drat/demo. Attorney can replace this template. ]
    
    MOTION TO VACATE DEFAULT AND SET ASIDE DEFAULT JUDGMENT
    
    CASE NAME: [Case Name]
    CASE NUMBER: {case_number}
    
    I. INTRODUCTION
    
    1. This motion is brought pursuant to California Code of Civil Procedure § 473.5.
    2. The motion is based on this notice of motion, the attached points and authorities,
       and any oral argument that may be heard by the Court.
    
    II. FACTUAL BACKGROUND
    
    1. On {served_date}, Plaintiff served Defendant with the Summons and Complaint.
    2. Defendant did not appear or answer the Complaint due to:
       a. {"Actual notice of the lawsuit" if facts.get('actual_notice', False) else "No actual notice"}
       b. {"Reliance on bad legal advice" if facts.get('relied_on_bad_advice', False) else "No reliance on bad legal advice"}
    3. On {motion_date}, Defendant filed this motion to vacate default and set aside default judgment.
    
    III. LEGAL ARGUMENT
    
    1. Motion is timely under CCP § 473.5
    2. {result.get('reason', 'Legal reason not specified')}
    3. {explanation}
    
    IV. RELIEF REQUESTED
    
    Defendant respectfully requests that the Court:
    1. Vacate the default entered against Defendant
    2. Set aside the default judgment
    3. Allow Defendant to answer the Complaint
    4. Grant such other and further relief as the Court deems just and proper
    
    DATED: {datetime.now().strftime('%B %d, %Y')}
    
    ___________________________
    {defendant_name}
    
    [This is a draft template. This is for research purposes only. Please consult with an attorney before filing.]"""
