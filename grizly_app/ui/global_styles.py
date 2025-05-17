import streamlit as st


def apply_global_styles():
    """Apply all global styles to the Streamlit app"""
    # Load tab styles
    with open("grizly_app/ui/styles/colorful_tabs.css", "r") as f:
        tab_styles = f.read()
    
    # Create the complete CSS string
    css = f"""
    <style>
        /* Import professional fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Merriweather:wght@400;600;700&display=swap');

        /* Global font and background */
        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
            background-color: #FAF9F6;
            color: #2E2E2E;
            font-size: 17px;
            line-height: 1.6;
        }}

        /* Section headers with Merriweather for classical polish */
        h1, h2, h3 {{
            font-family: 'Merriweather', serif;
            font-weight: 600;
            margin-bottom: 0.4em;
            letter-spacing: -0.02em;
        }}

        /* Container tweaks */
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }}

        /* Panels and expander boxes */
        .st-expander, .stAlert, .stMarkdown, .stTextArea, .stSelectbox {{
            background-color: #FFFFFF !important;
            border-radius: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.05);
            padding: 1rem;
        }}

        /* Card styling for content blocks */
        .card {{
            background: #ffffff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }}

        /* Card header styling */
        .card-header {{
            font-weight: 600;
            margin-bottom: 1rem;
            color: #2E2E2E;
        }}

        /* Card content styling */
        .card-content {{
            color: #444444;
            line-height: 1.6;
        }}

        /* Card variants for different sections */
        .card.motion-preview {{
            border-left: 4px solid #007bff;
        }}

        .card.legal-reasoning {{
            border-left: 4px solid #28a745;
        }}

        .card.summary {{
            border-left: 4px solid #dc3545;
        }}

        /* Buttons */
        .stButton button {{
            border-radius: 8px;
            background-color: #E5E5E5;
            color: #1F1F1F;
            border: none;
            padding: 0.5rem 1.2rem;
            font-weight: 500;
        }}

        .stButton button:hover {{
            background-color: #DCDCDC;
            cursor: pointer;
        }}

        /* Download button styling */
        a.download-button {{
            background-color: #eaeaea;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            text-decoration: none;
            color: #333;
            font-weight: 500;
            display: inline-block;
        }}

        a.download-button:hover {{
            background-color: #dcdcdc;
            cursor: pointer;
        }}

        /* Disclaimer (footer) */
        footer {{
            font-size: 0.8rem;
            color: #777777;
            text-align: center;
            padding-top: 2rem;
        }}

        /* Tabs styling */
        .stTabs {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1rem;
            padding: 0.5rem;
            background: #f8f9fa;
            border-radius: 4px;
        }}
        
        .stTabs > div {{
            flex: 1;
            text-align: center;
        }}
        
        .stTabs button {{
            padding: 0.5rem 1rem;
            font-weight: 500;
            border-radius: 4px;
        }}
        
        .stTabs button:hover {{
            background-color: #e9ecef;
        }}
        
        /* Center only the title and subtitle */
        .stMarkdown h1, .stMarkdown h2 {{
            text-align: center;
            margin-top: 1rem;
        }}
        
        /* Keep other content full-width */
        .stMarkdown {{
            max-width: 100%;
            margin: 0;
        }}
        
        .stTabs [data-baseweb="tab-list"] {{
            display: flex;
            gap: 0.5rem;
            padding: 0.5rem;
            border-bottom: 2px solid #e9ecef;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px 4px 0 0;
            background: #fff;
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        
        .stTabs [data-baseweb="tab"]:hover {{
            background: #f8f9fa;
        }}
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {{
            background: #fff;
            border-bottom: 2px solid #007bff;
            color: #007bff;
            font-weight: 600;
        }}
        
        .stTabs [data-baseweb="tab"][aria-selected="false"] {{
            color: #6c757d;
        }}
        
        .stTabs [data-baseweb="tab-panel"] {{
            padding: 1rem;
            background: #fff;
            border-radius: 0 4px 4px 4px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        
        /* Additional styling */
        {tab_styles}
    </style>
    """
    
    # Apply the styles using Streamlit's markdown with unsafe HTML
    st.markdown(css, unsafe_allow_html=True)
