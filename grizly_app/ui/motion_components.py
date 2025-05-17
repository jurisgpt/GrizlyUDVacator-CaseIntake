import streamlit as st


def render_motion_status(status, reason):
    """Render the status and reason section"""
    st.info(f"""
**Status:** {status.replace('_', ' ').capitalize()}
**Reason:** {reason}
""")

def render_motion_display(motion_text, facts):
    """Render the motion display with formatting"""
    motion_lines = motion_text.strip().splitlines()
    numbered_motion = "\n".join([f"{i+1:02}. {line}" for i, line in enumerate(motion_lines)])
    
    # Centered container for the motion
    st.markdown("""
    <div style="display: flex; justify-content: center;">
        <div style="max-width: 850px; width: 100%;">
    """, unsafe_allow_html=True)

    # Motion display with card styling
    st.markdown("""
    <div class="card motion-preview">
        <div class="card-header">📝 Motion to Set Aside Default Judgment</div>
        <div class="card-content">
            <div style='overflow:auto; max-height:500px; white-space:pre-wrap; 
                    font-family:monospace; background:#f9f9f9; padding:1rem; 
                    border-radius:8px; border:1px solid #ddd; text-align: left !important;'>
                <div style='text-align: left !important;'>
    """, unsafe_allow_html=True)
    
    st.markdown(f"{numbered_motion}", unsafe_allow_html=True)
    
    st.markdown("""
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Close the centered container
    st.markdown("""
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_motion_download(motion_text):
    """Render the motion download button"""
    # Centered container for the download button
    st.markdown("""
    <div style="text-align: center; margin-top: 1rem;">
    """, unsafe_allow_html=True)

    # Download button with custom styling
    st.download_button(
        label="📥 Download Legal Evaluation Summary",
        data=motion_text.encode('utf-8'),
        file_name="legal_eval_summary.txt",
        mime="text/plain",
        use_container_width=True
    )

    # Close the centered container
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

def render_legal_reasoning(facts, status, reason):
    """Render the legal reasoning section"""
    st.subheader("📜 Legal Reasoning")
    st.markdown(f"""
1. Motion Timing: {facts.get('motion_date', 'unknown date')} (vs. Service: {facts.get('served_date', 'unknown date')})
2. Relief Eligibility: {reason}
3. Status: {status.replace('_', ' ').capitalize()}
""")

def render_supporting_authority():
    """Render the supporting legal authority section"""
    st.expander("🔎 Supporting Legal Authority").write(
        "• CCP § 473.5 allows for relief if motion is timely AND no actual notice.\n"
        "• Cited in *Anastos v. Lee* and *Rappleyea v. Campbell*."
    )

def render_decision_path():
    """Render the decision path visualization"""
    st.subheader("📊 Decision Path")
    st.graphviz_chart("""
    digraph LegalDecision {
        rankdir=LR;
        "Start" -> "Check Timeliness";
        "Check Timeliness" -> "Timely" [label="Yes"];
        "Check Timeliness" -> "Check Exceptions" [label="No"];
        "Check Exceptions" -> "Eligible" [label="Yes"];
        "Check Exceptions" -> "Ineligible" [label="No"];
        
        "Timely" [style=filled, color=lightgreen];
        "Eligible" [style=filled, color=lightgreen];
        "Ineligible" [style=filled, color=lightcoral];
    }
    """)
