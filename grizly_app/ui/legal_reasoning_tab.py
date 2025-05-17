import streamlit as st
from datetime import datetime
import logging

from .legal_reasoning_header import render_legal_reasoning_header
from grizly_app.utils.logging import log_info, log_error

# Define status icons
STATUS_ICONS = {
    "relief_possible": "✅",        # Green checkmark
    "relief_barred": "❌",          # Red X
    "needs_review": "⚠️",           # Yellow warning
    "unknown": "ℹ️"                # Blue info
}

def render_reasoning_tab():
    """Render the legal reasoning tab with case evaluation and motion generation."""

    result = st.session_state.get("evaluation")
    facts = st.session_state.get("facts")

    if not result or not facts:
        st.warning("Please complete the Intake Form to evaluate your legal situation.")
        return

    # Case Summary Header
    status = result['status']
    icon = STATUS_ICONS.get(status, "ℹ️")
    
    st.markdown(f"""
    <div style="padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid #e0e0e0;">
        <h3 style="margin: 0;">📄 Case Summary</h3>
        <div style="margin-top: 0.5rem;">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: bold; width: 120px; text-align: left;">Status:</span> 
                <span style="color: #333; flex: 1;">{icon} {status}</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: bold; width: 120px; text-align: left;">Motion Timing:</span> 
                <span style="color: #333; flex: 1;">{facts['motion_date']} (vs. Service: {facts['served_date']})</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="font-weight: bold; width: 120px; text-align: left;">Relief Eligibility:</span> 
                <span style="color: #333; flex: 1;">{result['reason']}</span>
            </div>
        </div>
    </div>
    """.replace("{icon}", icon), unsafe_allow_html=True)

    # Status Highlight Box
    icon = STATUS_ICONS.get(status, "ℹ️")  # Remove unused status variable
    
    status_text = {
        "relief_possible": "✅ Relief Likely – Motion is timely and meets required conditions.",
        "relief_barred": "❌ Relief Not Available – Motion filed too late without valid excuse.",
        "needs_review": "⚠️ Motion eligibility uncertain – Review facts with a legal advisor.",
        "unknown": "ℹ️ Status Unknown – Please check your inputs."
    }.get(status, "ℹ️ Status Unknown")

    # Skip status text display since it's redundant with interpretation
    # st.markdown(f"""
    #     <div style="padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid #e0e0e0;">
    #         <p style="margin: 0; font-size: 1.1rem; color: #333; text-align: left;">{status_text}</p>
    #     </div>
    #     """, unsafe_allow_html=True)

    # Downloadable Draft Motion (only show if relief is possible)
    if result["status"] == "relief_possible":
        motion_text = generate_motion_text(facts, result)
        
        st.markdown(f"""
        <div style="margin-bottom: 1rem; text-align: left;">
            <h3 style="margin: 0; margin-bottom: 0.5rem;">📝 Motion to Set Aside Default Judgment</h3>
            <div style="white-space: pre-wrap;">
                {motion_text}
            </div>
            <div style="margin-top: 1rem;">
                <button style="
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 4px;
                    cursor: pointer;
                    text-align: left;
                " onclick="downloadMotion()">
                    📥 Download Draft Motion (Text)
                </button>
            </div>
        </div>
        
        <script>
        function downloadMotion() {{
            const text = `{motion_text}`;
            const blob = new Blob([text], {{ type: 'text/plain' }});
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'motion_to_set_aside.txt';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            window.URL.revokeObjectURL(url);
        }}
        </script>
        """, unsafe_allow_html=True)
    else:
        st.info("ℹ️ No motion template available since relief is not possible.")

    # Legal Evaluation Summary
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <h3 style="margin: 0; margin-bottom: 0.5rem;">📜 Legal Evaluation Summary</h3>
        <div style="text-align: left;">
            <p style="margin: 0; margin-bottom: 0.5rem;">Status: <code>{result['status']}</code></p>
            <p style="margin: 0;">Reason: {result['reason']}</p>
        </div>
    </div>
    """.replace("{{icon}}", icon), unsafe_allow_html=True)

    # Applied rules
    rules = result.get("rules_applied", [])
    if rules:
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <h3 style="margin: 0; margin-bottom: 0.5rem;">⚖️ Rules Applied</h3>
            <div style="text-align: left;">
        """ + "\n".join([f"<p style='margin: 0; margin-bottom: 0.5rem;'>• {rule}</p>" for rule in rules]) + """
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <p style="color: #dc3545; margin: 0;">⚠️ No legal rules applied to this fact pattern.</p>
        </div>
        """, unsafe_allow_html=True)

    # Facts Considered - Table Layout
    st.markdown(f"""
    <div style="margin-bottom: 1rem;">
        <h3 style="margin: 0; margin-bottom: 0.5rem;">📌 Facts Considered</h3>
        <div style="text-align: left;">
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: bold; width: 120px;">Service Date:</span>
                <span>{facts['served_date']}</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: bold; width: 120px;">Motion Date:</span>
                <span>{facts['motion_date']}</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: bold; width: 120px;">Participated:</span>
                <span>{'Yes' if facts['participated'] else 'No'}</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                <span style="font-weight: bold; width: 120px;">Actual Notice:</span>
                <span>{'Yes' if facts['actual_notice'] else 'No'}</span>
            </div>
            <div style="display: flex; align-items: center;">
                <span style="font-weight: bold; width: 120px;">Bad Legal Advice:</span>
                <span>{'Yes' if facts['relied_on_bad_advice'] else 'No'}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Optional explanation
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <h3 style="margin: 0; margin-bottom: 0.5rem;">💡 Interpretation</h3>
        <div style="text-align: left;">
    """ + interpret_reasoning(result) + """
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(interpretation)

def generate_motion_text(facts, result):
    """Generate a formatted motion text based on facts and result."""
    motion_text = f"""<div style='text-align: left; font-family: Arial, sans-serif; white-space: pre-line;">
MOTION TO SET ASIDE DEFAULT JUDGMENT

CASE INFORMATION
- Service Date: {facts['served_date']}
- Motion Date: {facts['motion_date']}
- Status: {result['status']}
- Reason: {result['reason']}

LEGAL BASIS
- CCP § 473.5
- Motion Timing: {facts['motion_date']} (vs. Service: {facts['served_date']})
- Relief Eligibility: {result['reason']}

FACTS CONSIDERED
- Participated Before Default: {'Yes' if facts['participated'] else 'No'}
- Had Actual Notice: {'Yes' if facts['actual_notice'] else 'No'}
- Relied on Bad Advice: {'Yes' if facts['relied_on_bad_advice'] else 'No'}

RECOMMENDATION
{interpret_reasoning(result)}
</div>"""
    return motion_text

def interpret_reasoning(result):
    status = result.get("status")
    reason = result.get("reason", "").lower()
    facts = st.session_state.get("facts", {})

    if "timely" in reason:
        return f"✅ Motion Timely: The motion was filed within 180 days (filed on {facts.get('motion_date')} vs. service on {facts.get('served_date')}), satisfying CCP § 473.5."
    elif "due process" in reason:
        return f"🛡️ Due Process Violation: Relief is available because the defendant had no notice ({'no' if not facts.get('actual_notice') else 'yes'} notice) and did not participate ({'no' if not facts.get('participated') else 'yes'} participation)."
    elif "bad legal advice" in reason or "constructive diligence" in reason:
        return f"📘 Equitable Exception: The court may excuse the late motion due to reliance on poor legal advice ({'yes' if facts.get('relied_on_bad_advice') else 'no'} reliance) — an exception under CCP § 473.5."
    elif "barred" in reason:
        return f"🚫 Relief Barred: The court cannot provide relief because the defendant both participated ({'yes' if facts.get('participated') else 'no'} participation) and filed too late ({facts.get('motion_date')} vs. service on {facts.get('served_date')}), without any equitable exceptions."
    else:
        return "⚠️ No Rule Match: No rule matched these facts. The motion is late, and no due process or equitable exception was found. Consider consulting a legal professional for further guidance."
