import os
import signal
import pytest
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from utils.config import Config


def kill_browser_processes():
    """Kill all orphan browser processes (Chrome/Edge/Firefox) to avoid port conflicts."""
    browser_names = ["chrome.exe", "msedge.exe", "chromedriver.exe", "msedgedriver.exe", "firefox.exe", "geckodriver.exe"]
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if process.info['name'].lower() in browser_names:
                print(f"🔴 Killing process {process.info['name']} with PID: {process.info['pid']}")
                os.kill(process.info['pid'], signal.SIGTERM)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, PermissionError) as e:
            print(f"⚠️ Failed to kill process {process.info['name']} with PID: {process.info['pid']}. Reason: {e}")


@pytest.fixture(scope="function")
def setup(request):
    """Pytest fixture to initialize and terminate the WebDriver."""
    kill_browser_processes()  # Ensure no orphan processes

    browser = Config.BROWSER.lower()
    driver = None

    if browser == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)

    elif browser == 'firefox':
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)

    elif browser == 'edge':
        edge_options = EdgeOptions()
        edge_options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=EdgeService(), options=edge_options)

    else:
        raise Exception(f"Invalid browser: {browser}. Supported browsers: chrome, firefox, edge")

    driver.maximize_window()
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    request.cls.driver = driver

    yield driver

    driver.quit()
    kill_browser_processes()  # Clean up processes after test completion
