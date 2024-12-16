from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Navigate to the specified URL."""
        try:
            print(f"🔗 Opening URL: {url}")
            self.driver.get(url)
        except Exception as e:
            print(f"❌ Failed to open URL: {url} - Error: {e}")
            raise e

    def find_element(self, locator, timeout=30):
        """Find element with explicit wait."""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            print(f"❌ Element with locator {locator} not found within {timeout} seconds.")
            raise e

    def click(self, locator, timeout=30):
        """Click an element."""
        try:
            element = self.find_element(locator, timeout)
            element.click()
            print(f"✅ Clicked on element with locator: {locator}")
        except Exception as e:
            print(f"❌ Failed to click on locator {locator}. Error: {e}")
            raise e

    def send_keys(self, locator, value, timeout=30):
        """Clear the input field and send keys."""
        try:
            element = self.find_element(locator, timeout)
            element.clear()
            element.send_keys(value)
            print(f"✅ Sent keys to locator: {locator}")
        except Exception as e:
            print(f"❌ Failed to send keys to locator {locator}. Error: {e}")
            raise e

    def wait_for_page_load(self, timeout=30):
        """Wait until the page is fully loaded."""
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.execute_script("return document.readyState") == "complete")
            print(f"✅ Page loaded successfully within {timeout} seconds.")
        except TimeoutException:
            raise Exception(f"❌ Page did not load within {timeout} seconds.")
