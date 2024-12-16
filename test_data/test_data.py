# test_data.py: Contains reusable test data like usernames, passwords, and expected messages
from utils.config import Config


class TestData:
    """
    This class contains reusable test data for use in multiple test cases. It includes
    user credentials, expected messages, and URL information for the test suite.
    """
    # Valid credentials
    VALID_USERNAME = "infoadmin"
    VALID_PASSWORD = "infoadmin"

    # Invalid credentials
    INVALID_USERNAME = "invaliduser"
    INVALID_PASSWORD = "invalidpassword"
    LOGIN_ERROR_MESSAGE = "Invalid Credentials."

    # Test data for empty fields
    EMPTY_USERNAME = ""
    EMPTY_PASSWORD = ""

    # Test data for SQL injection attempt
    SQL_INJECTION_USERNAME = "'; DROP TABLE users; --"
    SQL_INJECTION_PASSWORD = "password"

    # Test data for XSS attack attempt
    XSS_ATTACK_USERNAME = "<script>alert('XSS');</script>"
    XSS_ATTACK_PASSWORD = "<script>alert('XSS');</script>"

    # Test data for various user roles (if applicable)
    ADMIN_USERNAME = "adminuser"
    ADMIN_PASSWORD = "adminpassword"

    REGULAR_USER_USERNAME = "regularuser"
    REGULAR_USER_PASSWORD = "userpassword"

    # Expected error messages
    LOGIN_ERROR_MESSAGE = "Invalid Credentials."
    EMPTY_FIELD_ERROR_MESSAGE = "This field is required."

    # Additional data for UI/functional test validations
    PAGE_TITLE = "FMS - Login Page"
    DASHBOARD_TITLE = "FMS - Dashboard"

    # URLs for navigation validations
    LOGIN_PAGE_URL = Config.BASE_URL
    DASHBOARD_URL = Config.URL + "/mcdashboard"

