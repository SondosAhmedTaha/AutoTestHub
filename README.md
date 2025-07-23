# 🚀 AutoTestHub

**AutoTestHub** is a lightweight QA automation framework designed for testing C++ (or any CLI-based) programs using input/output files.  
It provides automated test execution, result comparison, HTML reporting, and MongoDB integration — all wrapped in a Docker-ready environment.

> 🔧 Designed for **developers who want to plug in their own code and tests**, and instantly get organized pass/fail results, saved and viewable.

---

## 📌 Features

- ✅ Test any CLI-based program (default: C++)
- 🧪 Input/output file testing
- 📊 Auto-generated HTML & JSON test reports
- 🐳 Docker and virtualenv support
- 💾 Results saved to MongoDB (for history, CI, dashboards, etc.)
- 🔄 Reusable structure — drop in your own code and tests
- 🧼 Built-in cleanup and test result viewer

---

## 🗂️ Project Structure

AutoTestHub/
├── code/             # Your code file (default: main.cpp)
├── input/            # input1.in, input2.in, ...
├── expected/         # expected1.out, expected2.out, ...
├── output/           # Output files written here after test runs
├── reports/          # HTML + JSON reports generated here
├── src/              # Core logic: runner, logger, DB, utils
├── scripts/          # Helper scripts (Docker and local execution)
├── tests/            # Unit tests for the framework
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md




## ⚙️ Usage Options

### ✅ Option 1: Run Locally (No Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/SondosAhmedTaha/AutoTestHub.git
   cd AutoTestHub
Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
Install dependencies: 

```bash
pip install -r requirements.txt
```
Run tests using the CLI script:
```bash
./scripts/run_tests.sh
```
✅ This will:

Compile your main.cpp (or other language file)

Run tests using files in input/ and expected/

Compare outputs

Generate an HTML report and JSON report inside the reports/ directory

🐳 Option 2: Run with Docker (Fully Isolated)
Requires Docker installed.

Build and run with:

```bash
./scripts/docker_run.sh
```
This will:

Build the Docker image

Spin up MongoDB

Execute all tests in a container

Save test results to reports/ (inside the container)

Persist MongoDB results

💡 Supported Test Format
Your program must:

Read from standard input

Write to standard output

Each test must have:

An input file: input/input1.in

An expected output file: expected/expected1.out

Your program will be compiled and run for each test, and actual output will be compared to the expected output.

🛠️ What If My Code Is Not C++?
By default, runner.py compiles and runs main.cpp.
To use other languages, modify two parts in src/runner.py:

1. Change the Compilation Command
Language	Edit code_path and compiler
C++	g++ main.cpp -o program
Python	No compile step needed
Java	javac Main.java
Rust	rustc main.rs -o program

2. Change the Execution Command
Language	Execution command inside runner.py
C++	subprocess.run(["./program"])
Python	subprocess.run(["python3", "main.py"])
Java	subprocess.run(["java", "Main"])
Node.js	subprocess.run(["node", "main.js"])

The structure is the same — just update runner.py to match your language’s compilation and runtime.

📋 MongoDB Integration
Each test run is timestamped and logged to MongoDB (using Docker).
You can query results or use src/view_results.py to view previous runs:

```bash
python src/view_results.py
```

🧾 Dependencies
Python 3.8+

Docker (optional, for containerized testing)

MongoDB (runs via Docker)

pytest, pytest-html, pytest-json-report

pymongo, rich

Install all with:

```bash
pip install -r requirements.txt
```

🛣️ Roadmap
 C++ I/O testing

 MongoDB test result storage

 HTML + JSON reports

 Docker support

 Optional language selector for runner

 Web dashboard with Flask (optional)

 Test coverage integration (pytest-cov)

👩‍💻 Author
Sondos Taha
GitHub: @SondosAhmedTaha

📄 License
This project is licensed under the MIT License.
