import os
import sys
import subprocess
import datetime

# Ensure correct import paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.logger import log_info, log_success, log_error, log_title
from src.db_handler import save_result   # ✅ Add this line

def run_tests():
    os.chdir(PROJECT_ROOT)
    
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = f"reports/report_{now}.html"

    log_title("Running Test Suite")
    log_info(f"Running tests at {now}")
    log_info(f"Saving report to {report_path}")

    os.makedirs("reports", exist_ok=True)

    cmd = [
        "pytest",
        "tests/",
        "--color=yes",
        f"--html={report_path}",
        "--self-contained-html"
    ]

    result = subprocess.run(cmd)

    # ✅ Save result to MongoDB
    status = "PASS" if result.returncode == 0 else "FAIL"
    save_result("test_suite", status, 0.0)  # 0.0 = placeholder duration

    if result.returncode == 0:
        log_success("All tests passed.")
    else:
        log_error("Some tests failed.")

if __name__ == "__main__":
    run_tests()
