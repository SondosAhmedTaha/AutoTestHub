import os
import sys
import subprocess
import datetime
import json
import time
import difflib

# Ensure correct import paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.logger import log_info, log_success, log_error, log_title
from src.db_handler import save_result

def run_io_tests():
    code_path = os.path.join(PROJECT_ROOT, "code", "main.cpp")
    binary_path = os.path.join(PROJECT_ROOT, "program")
    input_dir = os.path.join(PROJECT_ROOT, "input")
    output_dir = os.path.join(PROJECT_ROOT, "output")
    expected_dir = os.path.join(PROJECT_ROOT, "expected")
    report_dir = os.path.join(PROJECT_ROOT, "reports")

    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    run_timestamp = datetime.datetime.now().replace(microsecond=0)  # Shared timestamp for all results

    json_report_path = os.path.join(report_dir, f"io_report_{now}.json")
    html_report_path = os.path.join(report_dir, f"io_report_{now}.html")

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(report_dir, exist_ok=True)

    log_title("Running I/O Tests")

    compile_result = subprocess.run(["g++", code_path, "-o", binary_path])
    if compile_result.returncode != 0:
        log_error("Compilation failed.")
        return

    results = []

    for file in os.listdir(input_dir):
        if file.startswith("input") and file.endswith(".in"):
            suffix = file[len("input"):-len(".in")]
            input_file = os.path.join(input_dir, file)
            output_file = os.path.join(output_dir, f"output{suffix}.out")
            expected_file = os.path.join(expected_dir, f"expected{suffix}.out")

            start = time.time()
            with open(input_file) as inp, open(output_file, "w") as out:
                subprocess.run([binary_path], stdin=inp, stdout=out)
            duration = round(time.time() - start, 6)

            result = "PASS"
            diff_html = ""
            if not os.path.exists(expected_file):
                result = "FAIL"
                diff_html = "<i>Expected file not found.</i>"
            else:
                with open(output_file) as o, open(expected_file) as e:
                    actual = o.read().splitlines()
                    expected = e.read().splitlines()
                    if actual != expected:
                        result = "FAIL"
                        diff = difflib.HtmlDiff().make_table(expected, actual, "Expected", "Actual", context=True, numlines=3)
                        diff_html = diff

            save_result(f"IO::{file}", result, duration, timestamp=run_timestamp)
            log_info(f"{file}: {result} ({duration}s)")

            results.append({
                "test_name": file,
                "status": result,
                "duration": duration,
                "diff_html": diff_html
            })

    with open(json_report_path, "w") as f:
        json.dump(results, f, indent=2)

    with open(html_report_path, "w") as f:
        f.write(f"""
        <html>
        <head>
            <title>I/O Test Report</title>
            <style>
                body {{ font-family: Arial; padding: 20px; }}
                table {{ border-collapse: collapse; width: 100%; }}
                th, td {{ border: 1px solid #ccc; padding: 8px; }}
                th {{ background: #eee; }}
                .pass {{ background-color: #d4edda; }}
                .fail {{ background-color: #f8d7da; }}
                details {{ margin-top: 1em; }}
            </style>
        </head>
        <body>
            <h1>I/O Test Report ({now})</h1>
            <table>
                <tr><th>Test Name</th><th>Status</th><th>Duration (s)</th></tr>
        """)

        for r in results:
            row_class = "pass" if r["status"] == "PASS" else "fail"
            f.write(f"<tr class='{row_class}'><td>{r['test_name']}</td><td>{r['status']}</td><td>{r['duration']}</td></tr>")

        f.write("</table>")

        for r in results:
            if r["status"] == "FAIL" and r["diff_html"]:
                f.write(f"<details><summary>Details for {r['test_name']}</summary>{r['diff_html']}</details>")

        f.write("</body></html>")

    log_success(f"HTML report written to {html_report_path}")
    log_success(f"JSON report written to {json_report_path}")

if __name__ == "__main__":
    run_io_tests()
