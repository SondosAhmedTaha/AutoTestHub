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

```text
AutoTestHub/
├── code/           # Your code file (default: main.cpp)
├── input/          # input1.in, input2.in, ...
├── expected/       # expected1.out, expected2.out, ...
├── output/         # Output files written here after test runs
├── reports/        # HTML + JSON reports generated here
├── src/            # Core logic: runner, logger, DB, utils
├── scripts/        # Helper scripts (Docker and local execution)
├── tests/          # Unit tests for the framework
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```


## ⚙️ Usage Options

You can run AutoTestHub in two ways: locally or using Docker.

---

### ✅ Option 1: Run Locally (No Docker)

#### 1️⃣ Clone the repository:
```bash
git clone https://github.com/SondosAhmedTaha/AutoTestHub.git
cd AutoTestHub
```

#### 2️⃣ Add Your Code & Tests:
- Place your source code inside the `code/` directory (e.g., `main.cpp`).
- Place your input test files inside the `input/` directory (e.g., `input1.in`, `input2.in`, ...).
- Place your expected output files inside the `expected/` directory (e.g., `expected1.out`, `expected2.out`, ...).

> ⚠️ File names must match: `input1.in` → `expected1.out`, `input2.in` → `expected2.out`, etc.

#### 3️⃣ Set up a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 4️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

#### 5️⃣ Run tests:
```bash
./scripts/run_tests.sh
```

✅ This will:
- Compile your `main.cpp` (or other language file)
- Run your program on each input file
- Compare output with expected results
- Save an HTML and JSON report inside the `reports/` directory

---

### 🐳 Option 2: Run with Docker (Fully Isolated)

> Requires [Docker](https://docs.docker.com/get-docker/) installed.

#### 1️⃣ Run tests inside Docker:
```bash
./scripts/docker_run.sh
```

✅ This will:
- Build the Docker image
- Spin up a MongoDB container
- Execute all tests in a clean, isolated container
- Save reports to the `reports/` directory inside the container
- Persist results in the MongoDB database

---

### 💡 Supported Test Format

Your program **must**:
- Read from **standard input**
- Write to **standard output**

Each test consists of:
- `input/input1.in`
- `expected/expected1.out`

Your code will be compiled and executed for each input, and the actual output will be compared to the expected result.


# 🔧 What If My Code Is Not C++?

By default, `runner.py` compiles and runs `main.cpp`.  
To use another programming language, you need to update **two sections** in `src/runner.py`:

---

### 1. 🔨 Change the Compilation Command  
Edit this line in `runner.py`:

```python
compile_result = subprocess.run([...])
```

Examples for different languages:

**C++:**
```bash
g++ main.cpp -o program
```

**Java:**
```bash
javac Main.java
```

**Rust:**
```bash
rustc main.rs -o program
```

**Python:**  
No compilation step needed — just skip this part.

---

## 2. ▶️ Change the Execution Command  
Edit this line in `runner.py`:

```python
subprocess.run([...], stdin=..., stdout=...)
```

Examples:

**C++:**
```python
subprocess.run(["./program"], stdin=inp, stdout=out)
```

**Python:**
```python
subprocess.run(["python3", "main.py"], stdin=inp, stdout=out)
```

**Java:**
```python
subprocess.run(["java", "Main"], stdin=inp, stdout=out)
```

**Node.js:**
```python
subprocess.run(["node", "main.js"], stdin=inp, stdout=out)
```

---

🧠 **Note:** The folder structure remains the same — just adapt `runner.py` to your language's compilation and runtime.

Each test run is timestamped and logged to MongoDB (using Docker).
You can query results or use src/view_results.py to view previous runs:

```bash
python src/view_results.py
```

## 🧾 Dependencies
Python 3.8+

Docker (optional, for containerized testing)

MongoDB (runs via Docker)

pytest, pytest-html, pytest-json-report

pymongo, rich

Install all with:

```bash
pip install -r requirements.txt
```

## 🛣️ Roadmap
 C++ I/O testing

 MongoDB test result storage

 HTML + JSON reports

 Docker support

 Optional language selector for runner

## 👩‍💻 Author
Sondos Taha
GitHub: @SondosAhmedTaha

## 📄 License
This project is licensed under the MIT License.
