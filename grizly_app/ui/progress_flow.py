import streamlit as st


def render_progress_flow():
    """Render a dynamic visual progress flow using session_state"""
    # Initialize current step to 1 if not set
    if "current_step" not in st.session_state:
        st.session_state.current_step = 1

    steps = [
        {"name": "Intake", "number": 1},
        {"name": "Legal Reasoning", "number": 2},
        {"name": "Motion Generation", "number": 3},
        {"name": "Attach Exhibits", "number": 4}
    ]

    # Determine CSS class for each step
    step_classes = []
    for step in steps:
        if step["number"] < st.session_state.current_step:
            step_classes.append("step-done")
        elif step["number"] == st.session_state.current_step:
            step_classes.append("step-current")
        else:
            step_classes.append("step-pending")

    # --- CSS Styling ---
    css = """
    <style>
    .progress-flow {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.5rem 2rem;
        margin: 1rem 0 2.5rem 0;
        background: #ffffff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        position: relative;
        z-index: 1;
    }
    
    .step {
        flex: 1;
        text-align: center;
        padding: 0.75rem 0.5rem;
        position: relative;
        z-index: 2;
        transition: all 0.3s ease;
    }
    
    /* Connector lines between steps */
    .step:not(:last-child)::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 60%;
        right: -40%;
        height: 2px;
        background: #e9ecef;
        z-index: -1;
        transform: translateY(-50%);
    }
    
    /* Style for the step number circle */
    .step-number {
        width: 32px;
        height: 32px;
        line-height: 32px;
        border-radius: 50%;
        margin: 0 auto 0.5rem;
        font-size: 0.9rem;
        font-weight: 600;
        background: #e9ecef;
        color: #6c757d;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
    }
    
    .step-label {
        font-size: 0.85rem;
        color: #6c757d;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    /* Current step styling */
    .step-current .step-number {
        background: #007bff;
        color: white;
        transform: scale(1.1);
        box-shadow: 0 2px 8px rgba(0, 123, 255, 0.3);
    }
    
    .step-current .step-label {
        color: #007bff;
        font-weight: 600;
    }
    
    /* Completed step styling */
    .step-done .step-number {
        background: #28a745;
        color: white;
    }
    
    .step-done .step-label {
        color: #28a745;
    }
    
    /* Connector line for completed steps */
    .step-done:not(:last-child)::after,
    .step-current:not(:last-child)::after {
        background: #28a745;
    }
    
    /* Pending step styling */
    .step-pending .step-number {
        background: #e9ecef;
        color: #adb5bd;
    }
    
    .step-pending .step-label {
        color: #adb5bd;
    }
    </style>
    """

    # --- Render ---
    st.markdown(css, unsafe_allow_html=True)
    
    # Create progress flow HTML
    progress_html = ['<div class="progress-flow">']
    for i, (step, cls) in enumerate(zip(steps, step_classes)):
        progress_html.append(f'''
        <div class="step {cls}">
            <div class="step-number">Step {i + 1}</div>
            <div class="step-label">{step['name']}</div>
        </div>''')
    progress_html.append("</div>")
    
    # Render the progress flow
    st.markdown(''.join(progress_html), unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin: 1rem 0;">
        <p style="text-align: center; color: #6c757d; margin: 0.5rem 0;">
            Follow the steps to complete your case evaluation and motion generation.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.empty()