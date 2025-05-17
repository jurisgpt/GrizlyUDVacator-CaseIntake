import streamlit as st

from grizly_app.utils.logging import log_event


def render_external_form_tab():
    st.header("📨 Input Form")
    st.markdown("Use this form to provide additional context and details")

    try:
        # Check if we have an active session state
        if 'external_form_loaded' not in st.session_state:
            st.session_state['external_form_loaded'] = False
            st.session_state['external_form_error'] = None

        # Show loading state
        if not st.session_state['external_form_loaded']:
            with st.spinner('Loading form...'):
                try:
                    # Use Streamlit's components instead of iframe
                    st.components.v1.iframe(
                        "https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true",
                        width=640,
                        height=1544,
                        scrolling=True
                    )
                    st.session_state['external_form_loaded'] = True
                    st.session_state['external_form_error'] = None
                except Exception as e:
                    st.session_state['external_form_error'] = str(e)
                    st.session_state['external_form_loaded'] = True

        # Show error if present
        if st.session_state['external_form_error']:
            st.error(f"Error loading form: {st.session_state['external_form_error']}")
            st.info("Please try refreshing the page or contact support if the issue persists.")

        # Log successful render
        log_event("external_form_render", {
            "status": "success" if not st.session_state['external_form_error'] else "error",
            "error": st.session_state['external_form_error']
        })
    
    except Exception as e:
        # Log error
        log_event("external_form_error", {"status": "error", "message": str(e)})
        st.error(f"Error rendering external form: {str(e)}")
        st.info("Please try refreshing the page or contact support if the issue persists.")
        raise
