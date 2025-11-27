import pytest
from selenium import webdriver
from utils.config import BROWSER

@pytest.fixture
def driver():
    if BROWSER == "chrome":
        driver = webdriver.Chrome()
    elif BROWSER == "firefox":
        driver = webdriver.Firefox()
    elif BROWSER == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {BROWSER}")
    yield driver
    driver.quit()