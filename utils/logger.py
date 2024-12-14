import logging
import os
from datetime import datetime

class Logger:
    """
    Centralized logging mechanism to log test actions and results.
    """

    @staticmethod
    def setup_logger(log_name="test_log"):
        """
        Sets up the logger.
        :param log_name: Name of the log file.
        :return: Configured logger instance.
        """
        # Create logs directory if it doesn't exist
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Log file name with timestamp
        log_file = os.path.join(logs_dir, f"{log_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

        # Configure logger
        logger = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)

        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatter and add to handlers
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger
