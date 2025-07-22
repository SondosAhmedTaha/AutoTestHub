 🚀 AutoTestHub

**AutoTestHub** is a Python-based QA automation framework built for scalable, maintainable testing.  
It provides a lightweight yet powerful structure for writing, running, and reporting automated tests — with support for HTML reports, Dockerized execution, and CI/CD integration.

---

## 📌 Features

- ✅ Write modular test cases using `pytest`
- 📊 Generate timestamped HTML reports
- 🐳 Run tests inside a Docker container
- 🧪 Supports integration with MongoDB or SQLite (planned)
- 🛠️ Ready for CI/CD pipelines (GitHub Actions, GitLab CI, etc.)
- 📂 Clean and extensible folder structure

---

## 🧱 Project Structure

AutoTestHub/
├── src/ # Core runner and logic
│ └── runner.py
├── tests/ # Pytest test cases
│ └── test_sample.py
├── reports/ # HTML test reports
├── Dockerfile # Docker container setup
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy
Edit

---

## 🚀 Getting Started

### 🔧 Local Setup

#### 1. Clone the repository

```bash
git clone https://github.com/SondosAhmedTaha/AutoTestHub.git
cd AutoTestHub
```
2. Create and activate a virtual environment
```bash

python3 -m venv .venv
source .venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the test suite
```bash
pytest tests
```
6. Generate an HTML report via runner
```bash
python src/runner.py
```
Reports will be saved in the reports/ folder with a timestamped name.

🐳 Running with Docker
🔨 Build the image
```bash
docker build -t autotesthub .
```
▶️ Run tests in the container
```bash
docker run --rm autotesthub
```
💾 (Optional) Save reports to your local machine
```bash
docker run --rm -v "$(pwd)/reports:/app/reports" autotesthub
```
This mounts your local reports/ folder so HTML reports generated inside the container are saved on your machine.

📦 Dependencies
Python 3.8+

pytest

pytest-html

rich (for CLI logging, planned)

Docker (for containerized testing)

Install with:

```bash
pip install -r requirements.txt
```
🛣️ Roadmap
 MongoDB integration for test results

 GitHub Actions / GitLab CI setup

 Test tagging and filtering

 Rich logging with color-coded CLI output

 Docker Compose support

 Parallel test execution (pytest-xdist)

👩‍💻 Author
Sondos Taha
GitHub: @SondosAhmedTaha
