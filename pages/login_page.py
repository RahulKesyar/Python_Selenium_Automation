from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page object for the login page."""

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    remember_me_checkbox = (By.NAME, "rememberme")
    login_button = (By.CLASS_NAME, "MuiButton-label")
    error_message_locator = (By.CLASS_NAME, 'error-message')

    def open_login_page(self, url, approach="clear_cookies", request=None):
        """Navigate to the login page."""
        try:
            print(f"🔗 Opening URL: {url} using approach: {approach}")
            self.driver.get(url)
        except Exception as e:
            print(f"❌ Failed to open URL: {url} - Error: {e}")
            raise e

    def login(self, username, password, remember_me=True):
        """Login with credentials and optionally select Remember Me."""
        try:
            self.send_keys(self.username_input, username)
            self.send_keys(self.password_input, password)

            if remember_me:
                self.click(self.remember_me_checkbox)

            self.click(self.login_button)
            print(f"✅ Logged in with username: {username}")
        except Exception as e:
            print(f"❌ Failed to login. Error: {e}")
            raise e

    def get_error_message(self):
        """Get the error message displayed below the password input field."""
        try:
            return self.find_element(self.error_message_locator).text
        except Exception as e:
            print(f"❌ Failed to get error message. Error: {e}")
            raise e
