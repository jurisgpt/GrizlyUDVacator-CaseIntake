# summary_generator.py

"""
This module generates a professional, plain text case summary that includes:
✅ User inputs (facts)
✅ Legal rule result
✅ GPT-generated explanation
The summary is saved to a file: case-summary.txt
The user can also download it via Streamlit's download button.

📌 Disclaimer: This tool is for research and educational use only. It is not legal advice.
"""

import datetime

def generate_summary(facts: dict, result: dict, explanation: str, case_name: str = "Tenant vs. Landlord") -> str:
    """
    Create a formatted case summary string.

    Args:
        facts (dict): Input data from the form (served_date, motion_date, etc.)
        result (dict): Output from evaluate_rules()
        explanation (str): GPT explanation of legal result
        case_name (str): Optional case name or placeholder

    Returns:
        str: Formatted summary text
    """

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    summary = f"""\
============================================================
🏠 GrizlyUDVacator: Case Summary
============================================================

📅 Timestamp: {timestamp}
📁 Case: {case_name}

------------------------------------------------------------
🔍 User-Provided Facts
------------------------------------------------------------
- Date Served:         {facts.get("served_date")}
- Motion Filed:        {facts.get("motion_date")}
- Participated:        {"Yes" if facts.get("participated") else "No"}
- Actual Notice:       {"Yes" if facts.get("actual_notice") else "No"}
- Bad Legal Advice:    {"Yes" if facts.get("relied_on_bad_advice") else "No"}

------------------------------------------------------------
⚖️ Legal Rule Evaluation (CCP § 473.5)
------------------------------------------------------------
- Outcome:             {result.get("status").replace("_", " ").title()}
- Reason:              {result.get("reason")}
- Rules Applied:       {', '.join(result.get("rules_applied"))}

------------------------------------------------------------
🧠 GPT Explanation
------------------------------------------------------------
{explanation}

------------------------------------------------------------
📢 Disclaimer
------------------------------------------------------------
This tool is for research and educational use only.
It does not constitute legal advice or attorney-client relationship.

============================================================
"""

    return summary


def save_summary(summary: str, filename: str = "case-summary.txt") -> None:
    """
    Save the summary text to a local file for backend use.

    Args:
        summary (str): Case summary text
        filename (str): Output file name
    """
    with open(filename, "w") as f:
        f.write(summary)


