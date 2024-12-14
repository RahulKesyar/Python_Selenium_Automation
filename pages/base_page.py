"""
    pages/: Implements the Page Object Model(POM) for the better maintainability and readability.
    base_page.py: A reusable base class for the all the pages (e.g., common methods like click, send_keys, get_texts).
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        """
        Initialize the BasePage with a WebDriver instance.
        """
        self.driver = driver

    def open(self, url):
        """
        Navigate to the specified URL.
        """
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """
        Find a single web element with an explicit wait.
        :param locator: Tuple (By.<method>, <locator>) e.g., (By.ID, "username")
        :param timeout: Time to wait for the element.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not found within {timeout} seconds.")

    def find_elements(self, locator, timeout=10):
        """
        Find multiple web elements with an explicit wait.
        :param locator: Tuple (By.<method>, <locator>)
        :param timeout: Time to wait for the elements.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            raise Exception(f"Elements with locator {locator} not found within {timeout} seconds.")

    def click(self, locator, timeout=10):
        """
        Click an element after it becomes clickable.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise Exception(f"Element with locator {locator} not clickable within {timeout} seconds.")

    def send_keys(self, locator, value, timeout=10):
        """
        Type text into a web element.
        """
        element = self.find_element(locator, timeout)
        element.clear()  # Clear any pre-filled text.
        element.send_keys(value)

    def get_text(self, locator, timeout=10):
        """
        Get the visible text of a web element.
        """
        element = self.find_element(locator, timeout)
        return element.text

    def is_element_visible(self, locator, timeout=10):
        """
        Check if an element is visible on the page.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_present(self, locator, timeout=10):
        """
        Check if an element is present in the DOM.
        """
        try:
            self.find_element(locator, timeout)
            return True
        except Exception:
            return False

    def scroll_to_element(self, locator, timeout=10):
        """
        Scroll to a specific element on the page.
        """
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_attribute(self, locator, attribute, timeout=10):
        """
        Get the value of a specific attribute of a web element.
        """
        element = self.find_element(locator, timeout)
        return element.get_attribute(attribute)

    def select_dropdown_by_value(self, locator, value, timeout=10):
        """
        Select a dropdown option by its value.
        """
        from selenium.webdriver.support.ui import Select
        element = self.find_element(locator, timeout)
        dropdown = Select(element)
        dropdown.select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, text, timeout=10):
        """
        Select a dropdown option by its visible text.
        """
        from selenium.webdriver.support.ui import Select
        element = self.find_element(locator, timeout)
        dropdown = Select(element)
        dropdown.select_by_visible_text(text)

    def take_screenshot(self, file_path="screenshot.png"):
        """
        Capture a screenshot of the current page.
        """
        self.driver.save_screenshot(file_path)

    def wait_for_alert_and_accept(self, timeout=10):
        """
        Wait for an alert to appear and accept it.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            raise Exception("No alert found within the specified timeout.")

    def switch_to_frame(self, locator, timeout=10):
        """
        Switch to an iframe on the page.
        """
        element = self.find_element(locator, timeout)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        """
        Switch back to the main content from an iframe.
        """
        self.driver.switch_to.default_content()

    def wait_for_page_load(self, timeout=10):
        """
        Wait until the page is completely loaded.
        """
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    def close_browser(self):
        """
        Close the browser window.
        """
        self.driver.close()

    def quit_browser(self):
        """
        Quit the browser and end the WebDriver session.
        """
        self.driver.quit()
