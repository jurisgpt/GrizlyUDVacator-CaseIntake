from datetime import datetime

import streamlit as st

from .case_insights_header import render_case_insights_header
from .motion_components import (render_decision_path, render_legal_reasoning,
                                render_motion_display, render_motion_download,
                                render_motion_status,
                                render_supporting_authority)
from .motion_header import render_motion_header


def render_motion_tab():
    try:
        render_case_insights_header()

        # Check if we have evaluation data
        if "evaluation" not in st.session_state or "facts" not in st.session_state:
            st.info("👈 Please complete the Intake Form first to see your case insights.")
            if st.button("Go to Intake Form"):
                st.session_state["force_tab"] = "intake"
                st.rerun()
            return

        # Retrieve from session
        evaluation = st.session_state.evaluation
        facts = st.session_state.facts

        # Safely extract status and reason with better defaults
        status = evaluation.get("status", "not_evaluated")
        reason = evaluation.get("reason", "No evaluation has been performed yet.")
    except Exception as e:
        st.error(f"Error loading evaluation data: {str(e)}")
        return

    # Always show status and reason
    render_motion_status(status, reason)

    # Motion Display (only if relief is possible)
    if status == "relief_possible":
        try:
            # Generate motion text with fallbacks
            motion = f"""
DRAFT MOTION TO SET ASIDE DEFAULT JUDGMENT -ATTORNEY/LEGAL STAFF USE ONLY

Defendant moves this Court to set aside the default judgment under CCP § 473.5.

I. FACTUAL BACKGROUND

Defendant was served with court papers on {facts.get('served_date', 'unknown date')}.
Defendant filed this motion on {facts.get('motion_date', 'unknown date')}.

II. LEGAL ARGUMENT

A. Timeliness

The motion is timely under CCP § 473.5, which allows motions within 180 days.

B. Lack of Notice

Defendant did not have actual notice of the lawsuit before judgment.

III. CONCLUSION

WHEREFORE, Defendant respectfully requests that this Court set aside the default judgment and allow the case to proceed on its merits.
"""

            # Display motion and download options
            render_motion_display(motion, facts)
            render_motion_download(motion)
        except Exception as e:
            st.error(f"Error generating motion: {str(e)}")
            st.info("You may wish to consult an attorney to explore alternative remedies.")
    elif status == "relief_barred":
        st.warning("⚠️ No motion draft available due to ineligibility under CCP § 473.5.")
    else:
        st.warning("⚠️ No motion draft available due to incomplete information.")

    # Legal reasoning - always show
    render_legal_reasoning(facts, status, reason)

    # Supporting authority section
    render_supporting_authority()

    # Decision path visualization
    render_decision_path()

    # File uploader for exhibits
    st.markdown("### 📁 Attach Exhibits")
    uploaded_files = st.file_uploader(
        "Upload declaration and supporting documents",
        accept_multiple_files=True,
        type=['pdf', 'docx', 'txt']
    )
    if uploaded_files:
        st.success(f"Successfully uploaded {len(uploaded_files)} files")

    # Legal summary
    st.markdown("### 📌 Summary of Legal Relief")
    st.info(f"**Status:** {status.replace('_', ' ').capitalize()}\n**Reason:** {reason}")
