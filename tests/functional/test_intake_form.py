import os
import time
import subprocess
import json
import sys
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grizly_app.utils import logger as logging

# Helper function to submit form data using Selenium
def submit_form(data, port=8501):
    """Simulate form submission using Selenium."""
    try:
        # Setup Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        # Initialize driver
        driver = webdriver.Chrome(options=chrome_options)
        
        # Navigate to app
        driver.get(f"http://localhost:{port}")
        
        # Wait for form elements
        wait = WebDriverWait(driver, 10)
        
        # Fill form
        served_date = wait.until(EC.presence_of_element_located((By.NAME, "served_date")))
        motion_date = wait.until(EC.presence_of_element_located((By.NAME, "motion_date")))
        participated = wait.until(EC.presence_of_element_located((By.NAME, "participated")))
        actual_notice = wait.until(EC.presence_of_element_located((By.NAME, "actual_notice")))
        bad_advice = wait.until(EC.presence_of_element_located((By.NAME, "bad_advice")))
        submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
        
        # Set values
        served_date.clear()
        served_date.send_keys(data.get("served_date", datetime.now().strftime("%Y-%m-%d")))
        motion_date.clear()
        motion_date.send_keys(data.get("motion_date", datetime.now().strftime("%Y-%m-%d")))
        
        if data.get("participated", False):
            participated.click()
        if data.get("actual_notice", False):
            actual_notice.click()
        if data.get("bad_advice", False):
            bad_advice.click()
        
        # Submit form
        submit_button.click()
        
        # Wait for submission to complete
        time.sleep(2)  # Give time for submission to process
        
        driver.quit()
        return True
        
    except Exception as e:
        print(f"Error submitting form: {e}")
        return False

# Constants
APP_PORT = 8501
LOG_DIR = "logs"
APP_LOG = os.path.join(LOG_DIR, "app.log")
ERROR_LOG = os.path.join(LOG_DIR, "error.log")

# Configure logging
logging.log("INFO", "Test start", {"timestamp": datetime.now().isoformat()})

def test_intake_form():
    """Test the intake form with different scenarios."""
    print("\nTesting intake form...")
    
    # Test scenarios
    test_cases = [
        {
            "name": "Valid Case - Recent Service",
            "data": {
                "served_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                "motion_date": datetime.now().strftime("%Y-%m-%d"),
                "participated": True,
                "actual_notice": True,
                "bad_advice": True
            }
        },
        {
            "name": "Invalid Case - No Participation",
            "data": {
                "served_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                "motion_date": datetime.now().strftime("%Y-%m-%d"),
                "participated": False,
                "actual_notice": False,
                "bad_advice": False
            }
        },
        {
            "name": "Future Dates",
            "data": {
                "served_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
                "motion_date": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
                "participated": True,
                "actual_notice": True,
                "bad_advice": True
            }
        }
    ]
    
    # Verify logs for each test case
    for case in test_cases:
        print(f"\nTesting: {case['name']}")
        
        # Submit form
        if submit_form(case['data'], APP_PORT):
            print("Form submitted successfully")
        else:
            print("❌ Form submission failed")
            continue
        
        print("Waiting for logs to update...")
        time.sleep(2)  # Give time for logs to be written
        
        # Check app.log for form submission
        with open(APP_LOG, 'r') as f:
            logs = f.read()
            if f"form_submitted" in logs:
                print("✅ Found form submission log")
            else:
                print("❌ Form submission log not found")
        
        # Check for errors
        with open(ERROR_LOG, 'r') as f:
            errors = f.read()
            if errors:
                print("❌ Found errors in error.log:")
                print(errors)
            else:
                print("✅ No errors found")

def start_streamlit():
    """Start the Streamlit app in a subprocess."""
    print("Starting Streamlit app...")
    
    # Ensure logs directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Kill any existing Streamlit processes
    subprocess.run(["pkill", "-f", "streamlit run"], capture_output=True)
    
    # Set PYTHONPATH to include both project root and utils directory
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{project_root}:{os.path.join(project_root, 'utils')}:" + env.get("PYTHONPATH", "")
    
    # Start Streamlit in a subprocess
    process = subprocess.Popen([
        "streamlit", "run", "grizly_app/app.py",
        "--server.port", str(APP_PORT),
        "--server.address", "localhost",
        "--browser.gatherUsageStats", "false"
    ], env=env)
    
    # Wait for the app to start
    time.sleep(5)
    return process

def test_intake_form():
    """Test the intake form with different scenarios."""
    print("\nTesting intake form...")
    
    # Test scenarios
    test_cases = [
        {
            "name": "Valid Case - Recent Service",
            "data": {
                "served_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                "motion_date": datetime.now().strftime("%Y-%m-%d"),
                "participated": True,
                "actual_notice": True,
                "bad_advice": True
            }
        },
        {
            "name": "Invalid Case - No Participation",
            "data": {
                "served_date": (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
                "motion_date": datetime.now().strftime("%Y-%m-%d"),
                "participated": False,
                "actual_notice": False,
                "bad_advice": False
            }
        },
        {
            "name": "Future Dates",
            "data": {
                "served_date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
                "motion_date": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d"),
                "participated": True,
                "actual_notice": True,
                "bad_advice": True
            }
        }
    ]
    
    # Verify logs for each test case
    for case in test_cases:
        print(f"\nTesting: {case['name']}")
        print("Waiting for logs to update...")
        time.sleep(2)  # Give time for logs to be written
        
        # Check app.log for form submission
        with open(APP_LOG, 'r') as f:
            logs = f.read()
            if f"form_submitted" in logs:
                print("✅ Found form submission log")
            else:
                print("❌ Form submission log not found")
        
        # Check for errors
        with open(ERROR_LOG, 'r') as f:
            errors = f.read()
            if errors:
                print("❌ Found errors in error.log:")
                print(errors)
            else:
                print("✅ No errors found")

def verify_logs():
    """Verify that logs are being generated correctly."""
    print("\nVerifying logs...")
    
    # Check if log files exist
    if not os.path.exists(APP_LOG):
        print("❌ app.log not found")
        return False
    
    if not os.path.exists(ERROR_LOG):
        print("❌ error.log not found")
        return False
    
    # Check log content
    with open(APP_LOG, 'r') as f:
        logs = f.read()
        if "form_rendered" in logs:
            print("✅ Found form render logs")
        else:
            print("❌ Form render logs not found")
    
    with open(ERROR_LOG, 'r') as f:
        errors = f.read()
        if "evaluate_rules() takes 1 positional argument" in errors:
            print("❌ Found argument error in logs")
            return False
    
    return True

def cleanup():
    """Clean up after testing."""
    print("\nCleaning up...")
    
    # Kill any running Streamlit processes
    subprocess.run(["pkill", "-f", "streamlit run"], capture_output=True)
    
    # Clear logs
    if os.path.exists(APP_LOG):
        os.remove(APP_LOG)
    if os.path.exists(ERROR_LOG):
        os.remove(ERROR_LOG)

def main():
    try:
        # Cleanup any existing logs
        cleanup()
        
        # Start Streamlit
        process = start_streamlit()
        
        # Run tests
        test_intake_form()
        
        # Verify logs
        if verify_logs():
            print("\n✅ All tests passed!")
        else:
            print("\n❌ Some tests failed!")
            
    finally:
        # Cleanup
        cleanup()

if __name__ == "__main__":
    main()
