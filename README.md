# 🚀 Selenium Automation Framework

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Test Scenarios](#test-scenarios)
- [Environment Variables](#environment-variables)
- [Browser Support](#browser-support)
- [Key Files](#key-files)
- [Contributing](#contributing)
- [License](#license)

## 📘 About the Project
This **Selenium Automation Framework** is designed to automate end-to-end testing for web applications. It follows the **Page Object Model (POM)** design pattern, ensuring maintainable, reusable, and scalable test code.

The framework supports multi-browser execution (**Chrome, Firefox, Edge**) and offers flexibility for running tests locally or via CI/CD pipelines like **GitHub Actions, Jenkins, or Azure DevOps**.

## 🛠️ Technologies Used
- **Programming Language**: Python
- **Testing Framework**: Pytest
- **Browser Drivers**: ChromeDriver, EdgeDriver, GeckoDriver
- **Selenium WebDriver**: Browser automation
- **Reporting**: HTML report generation using pytest-html
- **Logging**: Custom logging for test execution tracking

## 📂 Project Structure
```plaintext
├── tests
│    └── test_login.py            # Test cases for login page
├── pages
│    ├── base_page.py             # Base Page with generic methods
│    └── login_page.py            # Login page-specific methods and locators
├── utils
│    ├── config.py                # Configuration file
│    └── logger.py                # Logger for tracking actions and errors
├── conftest.py                   # Pytest fixtures for driver setup/teardown
├── requirements.txt              # Python dependencies
├── README.md                     # Documentation
├── .gitignore                    # Git ignore file
```

## 📦 Installation
To get a local copy up and running, follow these steps:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/RahulKesyar/Python_Selenium_Automation.git
cd Python_Selenium_Automation
```

### 2️⃣ Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Download WebDriver
- Download **ChromeDriver** for your Chrome version [here](https://sites.google.com/chromium.org/driver/).
- Download **EdgeDriver** for Edge browser [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
- Download **GeckoDriver** for Firefox [here](https://github.com/mozilla/geckodriver/releases).

## 🚀 Running the Tests

Run tests using **pytest**. Example for login functionality:

### 1️⃣ Run All Tests
```bash
pytest --html=report.html --self-contained-html
```

### 2️⃣ Run a Specific Test
```bash
pytest tests/test_login.py::TestLogin::test_valid_login_without_remember_me
```

### 3️⃣ Generate HTML Report
```bash
pytest --html=report.html
```

## 🧪 Test Scenarios
| Test Case      | Description                         | Test Method                             |
|----------------|-------------------------------------|-----------------------------------------|
| Valid Login    | Test login with valid credentials   | `test_valid_login_with_remember_me()`   |
| Invalid Login  | Test login with invalid credentials | `test_invalid_login()`                  |
| Empty Username | Test login with empty username      | `test_login_with_empty_username()`      |
| Empty Password | Test login with empty password      | `test_login_with_empty_password()`      |
| SQL Injection  | Verify SQL Injection on login       | `test_sql_injection_login()`            |
| XSS Attack     | Verify XSS attack handling          | `test_xss_attack_login()`               |

## 📄 Environment Variables
| Variable   | Description                          | Default Value         |
|------------|--------------------------------------|----------------------|
| `BASE_URL` | Base URL of the application          | `https://example.com`|
| `BROWSER`  | Browser (chrome/firefox/edge)        | `chrome`             |

> **Note:** The `BROWSER` value can be changed in `utils/config.py`:
```python
BROWSER = "edge"  # Options: chrome, firefox, edge
```

## 🖥️ Browser Support
This framework supports:
- **Google Chrome**
- **Mozilla Firefox**
- **Microsoft Edge**

To switch the browser, change the `BROWSER` variable in **utils/config.py**.

## 📝 Key Files
| File           | Description                                 |
|----------------|---------------------------------------------|
| base_page.py   | Reusable methods for all pages              |
| login_page.py  | Locators and methods for login              |
| test_login.py  | Test cases for login features               |
| conftest.py    | Setup and teardown of the driver            |
| config.py      | Global settings and environment variables   |
| logger.py      | Custom logging implementation               |

## 🔥 Core Concepts

1️⃣ **Page Object Model (POM)**
- Pages as classes in `pages/`
- Each page contains locators and page-specific methods
- Example: `login_page.py` with methods like `login`, `open_login_page`, `get_error_message`

2️⃣ **Test Cases**
- Located in `tests/` folder
- Using page objects to perform actions
- Example: `TestLogin` calls `LoginPage.login(username, password)`

3️⃣ **Driver Setup**
- Driver setup is in `conftest.py` using `pytest.fixture`
- Multi-browser support
- Kills orphan chromedriver, msedgedriver, geckodriver processes

## 👨‍💻 Contributing
1. Fork the Repository
2. Clone your Fork
3. Create a New Branch
4. Make your Changes
5. Test the Changes
6. Push the Changes
7. Submit a Pull Request (PR)

Please follow the PEP-8 guidelines for Python coding.

## 📜 License
This project is licensed under the **MIT License**.

## 📢 Feedback & Support
Raise a GitHub issue or contact the maintainers.

## @RahulKesyar
