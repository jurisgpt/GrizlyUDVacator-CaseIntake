import pytest
import json
from datetime import datetime, timedelta
from legal_logic import evaluate_rules
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import pytest_html
from dataclasses import dataclass

# Helper to convert string to date
def to_date(dstr):
    return datetime.strptime(dstr, "%Y-%m-%d").date() if dstr else None

# Create a data class for test case organization and reporting
@dataclass
class CaseScenario:
    name: str
    served_date: str
    motion_date: str
    participated: bool
    actual_notice: bool
    relied_on_bad_advice: bool
    expected_relief: bool
    expected_rules: list
    expected_status: str = None
    description: str = ""
    
    def to_dict(self):
        return {
            "name": self.name,
            "served_date": self.served_date,
            "motion_date": self.motion_date,
            "participated": self.participated,
            "actual_notice": self.actual_notice,
            "relied_on_bad_advice": self.relied_on_bad_advice,
            "expected_relief": self.expected_relief,
            "expected_rules": self.expected_rules,
            "expected_status": self.expected_status,
            "description": self.description,
        }
    
    def form_inputs(self):
        """Convert to the input format for evaluate_rules"""
        return {
            "served_date": to_date(self.served_date),
            "motion_date": to_date(self.motion_date),
            "participated": self.participated,
            "actual_notice": self.actual_notice,
            "relied_on_bad_advice": self.relied_on_bad_advice,
        }

# Define test cases with clear names and descriptions
test_cases = [
    # Standard relief cases
    CaseScenario(
        name="basic_relief_case",
        served_date="2025-01-01", 
        motion_date="2025-04-01", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Basic timely motion with no complicating factors"
    ),
    CaseScenario(
        name="relief_with_notice",
        served_date="2025-01-01", 
        motion_date="2025-04-01", 
        participated=False, 
        actual_notice=True, 
        relied_on_bad_advice=False, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Relief possible despite actual notice due to no participation"
    ),
    CaseScenario(
        name="relief_with_participation",
        served_date="2025-01-01", 
        motion_date="2025-04-01", 
        participated=True, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Relief possible despite participation due to no actual notice"
    ),
    
    # Relief denied cases
    CaseScenario(
        name="no_relief_participation_and_notice",
        served_date="2025-01-01", 
        motion_date="2025-04-01", 
        participated=True, 
        actual_notice=True, 
        relied_on_bad_advice=False, 
        expected_relief=False, 
        expected_rules=[],
        expected_status="relief_barred",
        description="Relief barred due to both participation and actual notice"
    ),
    
    # Untimely motion cases
    CaseScenario(
        name="untimely_motion_years_late",
        served_date="2022-01-01", 
        motion_date="2025-04-01", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=False, 
        expected_rules=[],
        expected_status="relief_barred",
        description="Relief barred due to untimely motion (years after service)"
    ),
    CaseScenario(
        name="exactly_180_days",
        served_date="2024-11-18", 
        motion_date="2025-05-17", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Relief possible at exactly 180 days"
    ),
    CaseScenario(
        name="one_day_over_180",
        served_date="2024-11-17", 
        motion_date="2025-05-17", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=False, 
        expected_rules=[],
        expected_status="relief_barred",
        description="Relief barred at 181 days (just over time limit)"
    ),
    
    # Edge cases
    CaseScenario(
        name="same_day_filing",
        served_date="2025-01-01", 
        motion_date="2025-01-01", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Relief possible when motion filed same day as service"
    ),
    CaseScenario(
        name="null_dates",
        served_date=None, 
        motion_date=None, 
        participated=None, 
        actual_notice=None, 
        relied_on_bad_advice=False, 
        expected_relief=False, 
        expected_rules=[],
        expected_status="incomplete",
        description="Missing required information (null dates)"
    ),
    CaseScenario(
        name="future_dates",
        served_date="2026-01-01", 
        motion_date="2026-01-02", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=False, 
        expected_rules=[],
        expected_status="needs_review",
        description="Future dates should be flagged for review"
    ),
    CaseScenario(
        name="motion_before_service",
        served_date="2025-01-10", 
        motion_date="2025-01-05", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=False, 
        expected_relief=False, 
        expected_rules=[],
        expected_status="needs_review",
        description="Motion filed before service date"
    ),
    
    # Overriding factors
    CaseScenario(
        name="bad_advice_overrides_timeliness",
        served_date="2022-01-01", 
        motion_date="2025-04-01", 
        participated=False, 
        actual_notice=False, 
        relied_on_bad_advice=True, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Bad legal advice overrides untimely motion"
    ),
    CaseScenario(
        name="bad_advice_overrides_participation",
        served_date="2025-01-01", 
        motion_date="2025-04-01", 
        participated=True, 
        actual_notice=True, 
        relied_on_bad_advice=True, 
        expected_relief=True, 
        expected_rules=["CCP § 473.5"],
        expected_status="relief_possible",
        description="Bad legal advice overrides participation and notice"
    ),
]

# Dynamic test generation from test cases
@pytest.mark.parametrize("test_case", test_cases, ids=[tc.name for tc in test_cases])
def test_legal_relief(test_case):
    """Test the legal relief determination logic"""
    form_inputs = test_case.form_inputs()
    result = evaluate_rules(form_inputs)
    rules_applied = result.get('rules_applied', [])
    status = result.get('status', None)

    # Check if relief is possible
    relief_possible = bool(rules_applied)
    assert relief_possible == test_case.expected_relief, (
        f"{test_case.name}: Expected relief={test_case.expected_relief}, got {relief_possible}"
    )
    
    # Check rules applied
    assert set(rules_applied) == set(test_case.expected_rules), (
        f"{test_case.name}: Expected rules={test_case.expected_rules}, got {rules_applied}"
    )
    
    # Check status if specified
    if test_case.expected_status:
        assert status == test_case.expected_status, (
            f"{test_case.name}: Expected status={test_case.expected_status}, got {status}"
        )


# Test for input validation
def test_input_validation():
    """Test that the function properly handles invalid inputs"""
    # Empty dictionary
    assert evaluate_rules({}).get('status') == "incomplete"
    
    # String instead of date
    invalid_input = {
        "served_date": "not-a-date",
        "motion_date": to_date("2025-01-01"),
        "participated": False,
        "actual_notice": False,
        "relied_on_bad_advice": False,
    }
    assert evaluate_rules(invalid_input).get('status') == "incomplete"


# Generate comprehensive report with visualization
@pytest.fixture(scope="session")
def generate_test_report(request):
    """Generate a comprehensive test report with visualizations"""
    # Setup - runs before all tests
    yield
    # Teardown - runs after all tests
    
    # Create results directory
    results_dir = Path("test_results")
    results_dir.mkdir(exist_ok=True)
    
    # Convert test cases to dataframe for analysis
    df = pd.DataFrame([tc.to_dict() for tc in test_cases])
    
    # Generate timeline visualization for date-based tests
    plt.figure(figsize=(12, 8))
    
    # Filter out None dates
    df_dates = df[df['served_date'].notna() & df['motion_date'].notna()].copy()
    if not df_dates.empty:
        df_dates['served_date'] = pd.to_datetime(df_dates['served_date'])
        df_dates['motion_date'] = pd.to_datetime(df_dates['motion_date'])
        df_dates['days_between'] = (df_dates['motion_date'] - df_dates['served_date']).dt.days
        
        # Plot timeline
        plt.scatter(
            df_dates['days_between'], 
            range(len(df_dates)),
            c=df_dates['expected_relief'].map({True: 'green', False: 'red'}),
            s=100,
            alpha=0.7
        )
        
        # Add case names as labels
        for i, row in df_dates.iterrows():
            plt.text(
                row['days_between'] + 5, 
                df_dates.index.get_loc(i), 
                row['name'], 
                fontsize=9
            )
        
        plt.axvline(x=180, color='red', linestyle='--', label='180 Day Limit')
        plt.xlabel('Days Between Service and Motion')
        plt.ylabel('Test Cases')
        plt.title('Timeline of Test Cases')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(results_dir / "test_timeline.png")
    
    # Generate boolean factor matrix
    bool_factors = ['participated', 'actual_notice', 'relied_on_bad_advice', 'expected_relief']
    bool_df = df[bool_factors].copy()
    
    plt.figure(figsize=(10, 6))
    plt.imshow(bool_df.astype(int).T, cmap='RdYlGn', aspect='auto')
    plt.yticks(range(len(bool_factors)), bool_factors)
    plt.xticks(range(len(df)), df['name'], rotation=90)
    plt.colorbar(ticks=[0, 1], label='False/True')
    plt.title('Boolean Factors Matrix')
    plt.tight_layout()
    plt.savefig(results_dir / "boolean_factors.png")
    
    # Create summary JSON
    with open(results_dir / "test_cases.json", "w") as f:
        json.dump([tc.to_dict() for tc in test_cases], f, indent=4, default=str)
    
    # Create HTML report
    with open(results_dir / "test_report.html", "w") as f:
        f.write(f"""<!DOCTYPE html>
        <html>
        <head>
            <title>Legal Logic Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .case {{ border: 1px solid #ccc; padding: 10px; margin: 10px 0; border-radius: 5px; }}
                .pass {{ background-color: #e6ffe6; }}
                .fail {{ background-color: #ffe6e6; }}
                .images {{ margin: 20px 0; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
            </style>
        </head>
        <body>
            <h1>Legal Logic Test Report</h1>
            <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            
            <h2>Test Case Matrix</h2>
            <div class="images">
                <img src="boolean_factors.png" alt="Boolean Factors Matrix" style="max-width:100%">
            </div>
            
            <h2>Timeline Analysis</h2>
            <div class="images">
                <img src="test_timeline.png" alt="Test Timeline" style="max-width:100%">
            </div>
            
            <h2>Test Cases</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Served Date</th>
                    <th>Motion Date</th>
                    <th>Participated</th>
                    <th>Actual Notice</th>
                    <th>Bad Advice</th>
                    <th>Expected Relief</th>
                    <th>Status</th>
                    <th>Description</th>
                </tr>
                {"".join(f'''
                <tr class="{'pass' if tc.expected_relief else ''}">
                    <td>{tc.name}</td>
                    <td>{tc.served_date}</td>
                    <td>{tc.motion_date}</td>
                    <td>{tc.participated}</td>
                    <td>{tc.actual_notice}</td>
                    <td>{tc.relied_on_bad_advice}</td>
                    <td>{tc.expected_relief}</td>
                    <td>{tc.expected_status}</td>
                    <td>{tc.description}</td>
                </tr>''' for tc in test_cases)}
            </table>
        </body>
        </html>
        """)
    
    print(f"\nTest report generated in {results_dir}")


# Add boundary date tests dynamically
def test_day_by_day_boundaries():
    """Test boundary cases for the 180-day limit day by day"""
    base_served_date = to_date("2025-01-01")
    results = []
    
    # Test around the 180-day boundary
    for day_offset in range(175, 186):
        motion_date = base_served_date + timedelta(days=day_offset)
        form_inputs = {
            "served_date": base_served_date,
            "motion_date": motion_date,
            "participated": False,
            "actual_notice": False,
            "relied_on_bad_advice": False,
        }
        result = evaluate_rules(form_inputs)
        relief_possible = bool(result.get('rules_applied', []))
        results.append({
            "days": day_offset,
            "relief_possible": relief_possible,
            "status": result.get('status', '')
        })
    
    # Verify the exact cutoff is at 180 days
    df = pd.DataFrame(results)
    
    # Find the day where relief changes from possible to not possible
    for i in range(len(df) - 1):
        if df.iloc[i]['relief_possible'] and not df.iloc[i+1]['relief_possible']:
            cutoff_day = df.iloc[i]['days']
            assert cutoff_day == 180, f"Expected relief cutoff at 180 days, but found {cutoff_day}"
            break
    
    # Ensure we found a transition point
    assert 'cutoff_day' in locals(), "No transition from relief_possible to not possible found"
    
    # Save a visualization of the boundary
    plt.figure(figsize=(10, 6))
    plt.plot(df['days'], df['relief_possible'].astype(int), 'o-', linewidth=2)
    plt.axvline(x=180, color='red', linestyle='--', label='Expected Cutoff (180 days)')
    plt.xlabel('Days after service')
    plt.ylabel('Relief Possible (1=Yes, 0=No)')
    plt.title('Day-by-Day Analysis of 180-Day Boundary')
    plt.grid(True, alpha=0.3)
    plt.xticks(df['days'])
    plt.legend()
    
    # Ensure directory exists
    results_dir = Path("test_results")
    results_dir.mkdir(exist_ok=True)
    plt.savefig(results_dir / "boundary_analysis.png")


# Ensure report generation runs after all tests
pytestmark = pytest.mark.usefixtures("generate_test_report")

if __name__ == "__main__":
    pytest.main(["-v"])
