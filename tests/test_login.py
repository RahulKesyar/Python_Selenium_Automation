import pytest
from pages.login_page import LoginPage

class TestLogin:

    def test_valid_login_with_remember_me(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("valid_user", "valid_pass", remember_me=True)
        assert login_page.is_logged_in()

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open_login_page()
        login_page.login("invalid_user", "wrong_pass")
        assert login_page.get_error_message() == "Invalid credentials"