# Mobile Dev Toolkit

A Python CLI tool that analyzes Flutter projects and generates a JSON report containing:

* Total Dart lines of code
* Widget count
* Asset count
* Total asset size
* Dependency count
* Dependency list

## Features

* Scan Flutter projects recursively
* Count Dart source lines
* Detect StatelessWidget, StatefulWidget, and Widget classes
* Parse `pubspec.yaml`
* Analyze assets defined in Flutter configuration
* Output structured JSON
* Gracefully handle missing files and invalid paths

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Ak-s-hi/mobile-dev-toolkit.git
cd mobile-dev-toolkit
```

### Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -e .
```

---

## Usage

Analyze a Flutter project:

```bash
mobile-dev-toolkit path/to/flutter_project
```

Example:

```bash
mobile-dev-toolkit "F:/Projects/billing_app"
```

---

## Help

```bash
mobile-dev-toolkit --help
```

Example output:

```text
Usage: mobile-dev-toolkit [OPTIONS] PROJECT_PATH

Analyze a Flutter project.

Examples:

  mobile-dev-toolkit .
  mobile-dev-toolkit ./my_flutter_app
  mobile-dev-toolkit "C:/Projects/BillingApp"

Options:
  --help  Show this message and exit.
```

---

## Example Output

```json
{
  "lines": 15482,
  "widgets": 67,
  "assets": {
    "count": 124,
    "totalSizeMB": 12.45
  },
  "dependencies": {
    "count": 18,
    "list": [
      "flutter",
      "provider",
      "dio",
      "http",
      "shared_preferences"
    ]
  }
}
```

---

## Running Tests

```bash
python -m pytest
```

### Coverage

```bash
python -m pytest --cov=toolkit
```

---

## Static Analysis

### MyPy

```bash
mypy toolkit tests --strict
```

### Ruff

```bash
ruff check .
ruff format .
```

---

## Project Structure

```text
mobile-dev-toolkit/
├── toolkit/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── reporter.py
│   └── cli.py
│
├── tests/
│   ├── conftest.py
│   └── test_analyzer.py
│
├── pyproject.toml
└── README.md
```

---

## Future Improvements

* Cyclomatic complexity analysis
* Flutter package size analysis
* Unused asset detection
* Code quality metrics
* HTML and CSV report export
* CI/CD integration with GitHub Actions

```
```
