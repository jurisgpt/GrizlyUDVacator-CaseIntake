import streamlit as st

from grizly_app.utils.logging import log_event


def render_external_content():
    """Render external content with proper error handling"""
    try:
        # Add proper CORS headers for Google Forms
        st.markdown("""
        <style>
        .form-container {
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.1);
        }
        .form-container iframe {
            width: 100%;
            height: 1000px;
            border: none;
            border-radius: 8px;
        }
        </style>
        
        <div class="form-container">
            <iframe
                src="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true"
                id="external-iframe"
                title="Tenant Relief Evaluation Form"
                aria-label="Tenant Relief Evaluation Form"
                role="application"
                sandbox="allow-forms allow-same-origin allow-scripts allow-popups allow-popups-to-escape-sandbox"
                allow="autoplay; encrypted-media; fullscreen; microphone; camera"
                allowfullscreen="allowfullscreen"
                loading="lazy"
            ></iframe>
        </div>
        
        <script>
        // Get iframe element
        const iframe = document.getElementById('external-iframe');
        
        // Handle onload
        iframe.onload = function() {
            console.log('Form loaded successfully');
        };

        // Handle errors
        iframe.onerror = function() {
            console.error('Iframe failed to load:', iframe.src);
            alert('Failed to load the form. Please try refreshing the page.');
        };

        // Poll for iframe load
        const checkIframe = setInterval(() => {
            if (iframe.contentWindow && !iframe.contentWindow.document.body) {
                clearInterval(checkIframe);
                console.error('Iframe failed to load content');
            }
        }, 1000);

        // Cleanup
        setTimeout(() => clearInterval(checkIframe), 30000);
        </script>
        
        <noscript>
            <div class="noscript-warning">
                <h4>⚠️ JavaScript Required</h4>
                <p>This feature requires JavaScript to be enabled.</p>
                <p><a href="https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform" 
                      rel="noopener noreferrer" 
                      target="_blank">Open the form directly</a></p>
            </div>
        </noscript>
        """, unsafe_allow_html=True)
        
        # Log successful render
        log_event("iframe_render", {"status": "success", "src": "https://docs.google.com/forms/d/e/1FAIpQLSdQwUZBmye7cNuJnDK4H2JG8eTrj-Skz3n28pKRHydlawoBvw/viewform?embedded=true"})
    
    except Exception as e:
        # Log any errors
        log_event("iframe_error", {"status": "error", "message": str(e)})
        st.error(f"Error rendering iframe: {str(e)}")
        if st.session_state.get("debug_mode"):
            st.exception(e)

# Add CSS styles
st.markdown("""
<style>
.component-container {
    position: relative;
    width: 100%;
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 8px;
    background: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.loader {
    text-align: center;
    padding: 20px;
    font-weight: bold;
}

.error-message, .noscript-warning {
    padding: 20px;
    border-radius: 4px;
    background: #fef2f2;
    color: #991b1b;
    text-align: center;
}

.error-message h4, .noscript-warning h4 {
    margin: 0 0 10px 0;
    color: #991b1b;
}

.error-message a, .noscript-warning a {
    color: #16a34a;
    text-decoration: none;
}

.error-message a:hover, .noscript-warning a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)
