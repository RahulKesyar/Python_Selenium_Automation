Selenium-Pytest Framework

This repository contains a Selenium-based test automation framework built with Pytest. The framework is designed to separate concerns and improve maintainability by using a modular structure. It supports testing web applications with a focus on UI validations and functional testing.

Project Structure

selenium-pytest-framework/
├── tests/
│   ├── test_login.py               # Test cases for Login functionality
│   ├── test_ui_validations.py      # Test cases for UI validations
├── pages/
│   ├── base_page.py                # Base class for all pages
│   ├── login_page.py               # Page class for Login functionality
├── utils/
│   ├── helpers.py                  # General-purpose utilities
│   ├── logger.py                   # Centralized logging mechanism
├── test_data/
│   ├── test_data.json              # Test data in JSON format
│   ├── config.yaml                 # Configuration data (e.g., URLs, environment variables)
├── conftest.py                     # Pytest fixtures and driver setup
├── requirements.txt                # Required Python dependencies
├── pytest.ini                      # Pytest configurations
├── README.md                       # Project documentation

Features

Framework Highlights

Page Object Model (POM):
Encapsulates page-specific actions and elements into reusable classes.

Modular Design:
Separate concerns into tests, pages, utils, and test_data.

Data-Driven Testing:
Uses test_data.json and config.yaml for test inputs and configurations.

Logging:
Provides centralized logging for actions and results through logger.py.

Cross-Browser Testing:
Support for multiple browsers via Selenium WebDriver.

Reusable Utilities:
General-purpose utility functions in helpers.py.

Supported Test Categories

UI Validations: Tests for layout, labels, and visual elements.

Functional Testing: Tests for business logic and workflows.

Setup Instructions

Prerequisites

Python 3.7+

Pip (Python package manager)

ChromeDriver, GeckoDriver, or any browser driver installed and added to the system PATH.

Installation

Clone the repository:

git clone <repository_url>
cd selenium-pytest-framework

Install dependencies:

pip install -r requirements.txt

Update the config.yaml file with the base URL and browser settings:

base_url: "https://example.com"
browser: "chrome"

Usage

Running Tests

To execute all tests:

pytest

To execute a specific test file:

pytest tests/test_login.py

To generate a detailed HTML report:

pytest --html=report.html

Directory Details

tests/

Contains all test cases categorized by functionality.

test_login.py: Validates login functionality.

test_ui_validations.py: Checks UI elements and behaviors.

pages/

Implements the Page Object Model (POM):

base_page.py: A reusable base class for common Selenium actions (e.g., click, send_keys).

login_page.py: Encapsulates elements and actions for the Login page.

utils/

Provides helper files for auxiliary operations:

helpers.py: Contains utilities for generating test data, working with dates, and reading/writing files.

logger.py: A centralized logging mechanism to log test actions and results.

test_data/

Holds externalized data for tests:

test_data.json: Stores test inputs like usernames, passwords, etc.

config.yaml: Stores configurations like base URLs and environment variables.

conftest.py

Defines fixtures for driver setup, teardown, and reusable components.

Extending the Framework

Adding a New Test

Create a new test file in the tests/ folder (e.g., test_new_feature.py).

Use existing page objects or create new ones in the pages/ folder.

Add test data to test_data.json if needed.

Implement the test using Pytest syntax.

Adding a New Page Object

Create a new file in the pages/ folder (e.g., new_page.py).

Extend BasePage to inherit common functionality.

Add locators and methods specific to the new page.

Best Practices

Use meaningful names for test cases and methods.

Keep test data externalized for easy updates.

Use assertions to validate expected behavior.

Separate Selenium interactions (in page objects) from test logic (in test files).

Follow the DRY (Don't Repeat Yourself) principle to reuse code where possible.

Sample Test Execution Output

============================= test session starts =============================
collected 4 items

tests/test_login.py::test_valid_login PASSED                               [ 25%]
tests/test_login.py::test_invalid_login PASSED                            [ 50%]
tests/test_ui_validations.py::test_page_title PASSED                      [ 75%]
tests/test_ui_validations.py::test_button_labels PASSED                   [100%]

============================== 4 passed in 3.42s ==============================

Contributing

Feel free to submit issues or pull requests to enhance the framework. Follow the project's coding standards and maintain consistency in structure.

License

This project is licensed under the MIT License. See the LICENSE file for details.


