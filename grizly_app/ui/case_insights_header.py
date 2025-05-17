import streamlit as st


def render_case_insights_header():
    st.header("🔍 Case Insights")
    st.markdown("""
    <style>
    .case-insights-header {
        text-align: left;
        margin-bottom: 1.5rem;
    }
    .case-insights-header h3 {
        margin-bottom: 0.5rem;
    }
    .case-insights-header p {
        margin: 0;
        color: #4a4a4a;
    }
    </style>
    
    <div class="case-insights-header">
        <h3>Legal Analysis & Recommendations</h3>
        <p>Based on your case details, we've analyzed your legal situation and provide insights into potential options.</p>
    </div>
    """, unsafe_allow_html=True)
