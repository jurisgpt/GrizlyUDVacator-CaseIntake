import requests
import json
from datetime import datetime

def submit_form(data, port=8501):
    """Simulate form submission to Streamlit app."""
    url = f"http://localhost:{port}/"
    
    # Format data for Streamlit
    form_data = {
        "served_date": data.get("served_date", datetime.now().strftime("%Y-%m-%d")),
        "motion_date": data.get("motion_date", datetime.now().strftime("%Y-%m-%d")),
        "participated": data.get("participated", False),
        "actual_notice": data.get("actual_notice", False),
        "bad_advice": data.get("bad_advice", False)
    }
    
    try:
        # Send POST request to simulate form submission
        response = requests.post(url, json=form_data)
        return response.status_code == 200
    except Exception as e:
        print(f"Error submitting form: {e}")
        return False
