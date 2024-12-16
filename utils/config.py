# config.py: Contains environment-specific URLs, credentials, or other configurations

class Config:
    """
    The Config class is responsible for managing and providing access to key configuration
    settings used across the test automation framework. These include environment URLs,
    default browser settings, and logging configurations.

    The settings in this class are used to standardize environment-specific configurations
    and ensure that the same set of parameters are consistently applied across test executions.
    """
    URL = "https://stsfmspoc.infotracktelematics.com:999"
    BASE_URL = URL + "/login-test"
    DASHBOARD_URL = URL + "/mcdashboard"
    IMPLICIT_WAIT = 20
    EXPLICIT_WAIT = 20
    BROWSER = "edge"  # Options: chrome, firefox, edge
    HEADLESS = False  # Run tests in headless mode by default
    LOG_FILE_PATH = "logs/test_execution.log"
