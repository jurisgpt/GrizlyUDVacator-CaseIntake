import streamlit as st

from .global_styles import apply_global_styles
from .intake_form_tab import render_intake_tab
from .intake_header import render_intake_header

# Apply global styles
apply_global_styles()

# Render the intake header
render_intake_header()

# Render the intake form
def render_intake_form():
    """Render the intake form with all input fields."""
    st.title("📋 Intake Form")
    st.caption("Please fill out the following information to evaluate your legal situation.")

    # Create two columns for form layout
    col1, col2 = st.columns(2)

    with col1:
        # Case Information
        st.subheader("Case Information")
        case_number = st.text_input("Case Number", key="case_number")
        county = st.selectbox("County",
                            ["Alameda", "Contra Costa", "Marin", "Napa", "San Francisco",
                             "San Mateo", "Santa Clara", "Solano", "Sonoma"],
                            key="county")
        court = st.selectbox("Court",
                           ["Superior Court of California"],
                           key="court")

    with col2:
        # Party Information
        st.subheader("Party Information")
        plaintiff = st.text_input("Plaintiff (Landlord)", key="plaintiff")
        defendant = st.text_input("Defendant (Tenant)", key="defendant")
        address = st.text_input("Property Address", key="address")

    # Timeline Information
    st.subheader("Timeline Information")
    served_date = st.date_input("Date Served", key="served_date")
    motion_date = st.date_input("Date of Motion", key="motion_date")

    # Relief Information
    st.subheader("Relief Information")
    relief_type = st.selectbox("Type of Relief",
                             ["Relief from Default Judgment", "Relief from Default"],
                             key="relief_type")
    reason = st.text_area("Reason for Relief",
                        "Please explain why you believe you are entitled to relief.",
                        key="reason")

    # Submit button
    if st.button("Submit"):
        st.success("Intake form submitted successfully!")
        st.session_state.facts = {
            "case_number": case_number,
            "county": county,
            "court": court,
            "plaintiff": plaintiff,
            "defendant": defendant,
            "address": address,
            "served_date": served_date,
            "motion_date": motion_date,
            "relief_type": relief_type,
            "reason": reason
        }

if __name__ == "__main__":
    render_intake_form()
