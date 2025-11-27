from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "https://example.com/login"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember-me")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.ID, "error-msg")

    def open_login_page(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, username, password, remember_me=False):
        self.find_element(self.USERNAME_INPUT).send_keys(username)
        self.find_element(self.PASSWORD_INPUT).send_keys(password)
        if remember_me:
            self.find_element(self.REMEMBER_ME_CHECKBOX).click()
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        try:
            return self.find_element(self.ERROR_MESSAGE).text
        except Exception:
            return None

    def is_logged_in(self):
        # Dummy check, replace with actual logic
        return "dashboard" in self.driver.current_url
