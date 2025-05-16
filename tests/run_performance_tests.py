import subprocess
import time
from statistics import mean, stdev
import json

def run_tests(num_runs: int = 5) -> dict:
    """Run performance tests multiple times and collect statistics."""
    all_results = []
    
    print(f"Running performance tests {num_runs} times...")
    
    for i in range(num_runs):
        print(f"\nRun #{i+1}:")
        
        # Run the tests
        result = subprocess.run(
            ["python", "-m", "pytest", "test_performance.py", "-v"],
            capture_output=True,
            text=True,
            shell=False
        )
        
        # Parse timing information
        timings = {}
        output = result.stdout
        
        # Extract timing information
        for line in output.split('\n'):
            if "loaded in" in line:
                timings["questions"] = float(line.split()[2])
            elif "evaluation completed in" in line:
                timings["legal_eval"] = float(line.split()[4])
            elif "explanation generated in" in line:
                timings["gpt_explain"] = float(line.split()[4])
            elif "client initialized in" in line:
                timings["openai_init"] = float(line.split()[4])
            elif "Complete flow completed in" in line:
                timings["total"] = float(line.split()[5])
        
        all_results.append(timings)
        time.sleep(1)  # Small delay between runs
    
    # Calculate statistics
    stats = {}
    for key in all_results[0].keys():
        values = [r[key] for r in all_results]
        stats[key] = {
            "mean": mean(values),
            "stddev": stdev(values),
            "min": min(values),
            "max": max(values)
        }
    
    return stats

def main():
    """Main function to run performance tests."""
    results = run_tests()
    
    # Print results
    print("\nPerformance Test Results:")
    print("-" * 50)
    for key, stats in results.items():
        print(f"\n{key.replace('_', ' ').title()}:")
        print(f"  Mean: {stats['mean']:.4f} s")
        print(f"  Std Dev: {stats['stddev']:.4f} s")
        print(f"  Min: {stats['min']:.4f} s")
        print(f"  Max: {stats['max']:.4f} s")
    
    # Save results to JSON
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    with open(f"performance_results_{timestamp}.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
