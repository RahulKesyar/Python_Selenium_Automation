# Selenium-Pytest Framework

## Overview
This project is a modular Selenium-Pytest framework for web application testing. It is designed with scalability, maintainability, and ease of use in mind, making it ideal for both beginners and advanced users.

---

## Project Structure

```
selenium-pytest-framework/
├── tests/
│   ├── test_login.py               # Test cases for Login functionality
│   ├── test_ui_validations.py      # Test cases for UI validations
├── pages/
│   ├── base_page.py                # Base class for all pages
│   ├── login_page.py               # Page class for Login functionality
├── utils/
│   ├── helpers.py                  # General-purpose utilities (non-Selenium)
│   ├── logger.py                   # Centralized logging mechanism
├── test_data/
│   ├── test_data.json              # Test data for all test cases
│   ├── config.yaml                 # Configuration for environment settings
├── conftest.py                     # Pytest fixtures and driver setup
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configurations
├── README.md                       # Documentation for the project
```

---

## Features
- **Modular Design**: Separate folders for tests, pages, utilities, and test data.
- **Pytest Fixtures**: Reusable fixtures for WebDriver setup and teardown.
- **Configurable Environment**: Configurable test environment using `config.yaml`.
- **Centralized Logging**: Unified logging for debugging and tracking test execution.
- **Reusable Base Page**: Encapsulates common Selenium operations (click, send keys, waits, etc.).
- **Data-Driven Testing**: Uses `test_data.json` for parameterized tests.

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- Google Chrome and ChromeDriver (or another browser and corresponding WebDriver).

### Installation
1. Clone the repository:
   ```bash
   git clone https://your-repository-url.git
   cd selenium-pytest-framework
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Update the `test_data/config.yaml` with your application's base URL and other configurations.

---

## Running Tests

### Run All Tests
```bash
pytest
```

### Run Specific Tests
```bash
pytest tests/test_login.py
```

### Generate HTML Report
Install `pytest-html` if not already installed:
```bash
pip install pytest-html
```
Run tests with HTML report:
```bash
pytest --html=report.html
```

---

## Writing New Tests

### Steps to Add a New Test Case
1. **Create a New Page Class (if needed):**
   Add a new file in the `pages/` folder and extend `BasePage`.

   Example:
   ```python
   from pages.base_page import BasePage
   from selenium.webdriver.common.by import By

   class DashboardPage(BasePage):
       dashboard_title = (By.ID, "dashboard-title")

       def get_dashboard_title(self):
           return self.get_text(self.dashboard_title)
   ```

2. **Write the Test Case:**
   Add a new test in the `tests/` folder.

   Example:
   ```python
   def test_dashboard_title(setup):
       dashboard_page = DashboardPage(setup)
       dashboard_page.open("https://example.com/dashboard")
       assert dashboard_page.get_dashboard_title() == "Welcome, User!"
   ```

3. **Add Test Data:**
   Update `test_data.json` if the test requires specific data.

---

## Utilities

### Logger
Centralized logging for consistent test output:
```python
from utils.logger import logger
logger.info("Test started.")
logger.error("Element not found.")
```

### Helpers
Non-Selenium utility functions, e.g., string manipulation, API calls, or custom waits.

---

## Extending the Framework

1. **Add New Utilities:** Place reusable utility functions in the `utils/` folder.
2. **Parameterize Tests:** Use `pytest.mark.parametrize` for data-driven testing.
3. **Custom Fixtures:** Add custom fixtures in `conftest.py` for shared setup logic.
4. **Add New Configurations:** Update `config.yaml` and access values via the YAML parser in your tests.

---

## Example Configurations

### config.yaml
```yaml
base_url: "https://your-app-url.com"
browser: "chrome"
timeout: 10
```

### test_data.json
```json
{
    "valid_user": {
        "username": "testuser",
        "password": "password123"
    },
    "invalid_user": {
        "username": "invalid",
        "password": "wrongpass"
    }
}
```

---

## Troubleshooting

1. **Driver Not Found:**
   Ensure the WebDriver executable path is added to your system's PATH variable.

2. **Test Data Missing:**
   Verify `test_data.json` and `config.yaml` are correctly formatted and present in the `test_data/` folder.

3. **Timeout Errors:**
   Increase `timeout` in `config.yaml` for slower environments.

---

## Contributing
Please drop your comments and suggestions

## License
Copyright © 2024 @RahulKesyar
All rights reserved.

