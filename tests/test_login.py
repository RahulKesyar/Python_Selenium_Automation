import pytest
from pages.login_page import LoginPage
from utils.config import Config
from test_data.test_data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_valid_login_with_remember_me(self, request):
        login_page = LoginPage(self.driver)
        login_page.open_login_page(Config.BASE_URL, approach="clear_cookies", request=request)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD, remember_me=True)
        WebDriverWait(self.driver, 30).until(EC.url_to_be(Config.DASHBOARD_URL))
        assert self.driver.current_url == Config.DASHBOARD_URL

    def test_valid_login_without_remember_me(self, request):
        login_page = LoginPage(self.driver)
        login_page.open_login_page(Config.BASE_URL, approach="restart_browser", request=request)
        login_page.login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD, remember_me=False)
        WebDriverWait(self.driver, 30).until(EC.url_to_be(Config.DASHBOARD_URL))
        assert self.driver.current_url == Config.DASHBOARD_URL

    def test_invalid_login(self, request):
        login_page = LoginPage(self.driver)
        login_page.open_login_page(Config.BASE_URL, approach="refresh_page", request=request)
        login_page.login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)
        error_message = login_page.get_password_error_message()
        assert error_message == TestData.LOGIN_ERROR_MESSAGE

    def test_sql_injection_login(self, request):
        login_page = LoginPage(self.driver)
        login_page.open_login_page(Config.BASE_URL, approach="restart_browser", request=request)
        login_page.login(TestData.SQL_INJECTION_USERNAME, TestData.SQL_INJECTION_PASSWORD)
        error_message = login_page.get_password_error_message()
        assert error_message == TestData.LOGIN_ERROR_MESSAGE
