"""
login_page: Encapsulates the login pages-specific elements and methods
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for the Login Page."""
    # Locator
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    remember_me_checkbox = (By.NAME, "rememberme")
    login_button = (By.CLASS_NAME, "MuiButton-label")
    password_error_msg = (By.ID, "username-helper-text")

    def open_login_page(self, url):
        """Navigate to the login Page."""
        self.open(url)

    def login(self, username, password, remember_me=True):
        """
        Perform the login action.
        :param username: Username for login
        :param password: Password for login
        :param remember_me: (default: True).
        :return:
        """
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        if remember_me:
            self.click(self.remember_me_checkbox)
        self.click(self.login_button)

    def login_without_remember_me(self, username, password):
        """
        Perform the login without selecting the 'Remember Me' Checkbox.
        This is an alternative to the login 'login' method for thr specific tests.
        :param username:
        :param password:
        :return:
        """
        self.login(username, password, remember_me=False)

    def get_password_error_message(self):
        """
        Get the error message displayed below the password input field.
        :return:
        """
        return self.get_text(self.password_error_msg)
    
