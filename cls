[33mcommit e62df6e204beee7d87bdc6c88a0df8ff70c53a45[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32m1st_Branch[m[33m, [m[1;31morigin/1st_Branch[m[33m)[m
Author: RahulKesyar <rahulkesyar.infotrack@gmail.com>
Date:   Sun Dec 15 00:19:23 2024 +0530

    4th commit:Enhanced logger.py by implementing a centralized logging mechanism for recording test actions and results. Also added logic to create a logs directory if it doesnt already exist.

[1mdiff --git a/utils/logger.py b/utils/logger.py[m
[1mnew file mode 100644[m
[1mindex 0000000..a135d75[m
[1m--- /dev/null[m
[1m+++ b/utils/logger.py[m
[36m@@ -0,0 +1,46 @@[m
[32m+[m[32mimport logging[m
[32m+[m[32mimport os[m
[32m+[m[32mfrom datetime import datetime[m
[32m+[m
[32m+[m[32mclass Logger:[m
[32m+[m[32m    """[m
[32m+[m[32m    Centralized logging mechanism to log test actions and results.[m
[32m+[m[32m    """[m
[32m+[m
[32m+[m[32m    @staticmethod[m
[32m+[m[32m    def setup_logger(log_name="test_log"):[m
[32m+[m[32m        """[m
[32m+[m[32m        Sets up the logger.[m
[32m+[m[32m        :param log_name: Name of the log file.[m
[32m+[m[32m        :return: Configured logger instance.[m
[32m+[m[32m        """[m
[32m+[m[32m        # Create logs directory if it doesn't exist[m
[32m+[m[32m        logs_dir = "logs"[m
[32m+[m[32m        if not os.path.exists(logs_dir):[m
[32m+[m[32m            os.makedirs(logs_dir)[m
[32m+[m
[32m+[m[32m        # Log file name with timestamp[m
[32m+[m[32m        log_file = os.path.join(logs_dir, f"{log_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")[m
[32m+[m
[32m+[m[32m        # Configure logger[m
[32m+[m[32m        logger = logging.getLogger(log_name)[m
[32m+[m[32m        logger.setLevel(logging.DEBUG)[m
[32m+[m
[32m+[m[32m        # Create file handler[m
[32m+[m[32m        file_handler = logging.FileHandler(log_file)[m
[32m+[m[32m        file_handler.setLevel(logging.DEBUG)[m
[32m+[m
[32m+[m[32m        # Create console handler[m
[32m+[m[32m        console_handler = logging.StreamHandler()[m
[32m+[m[32m        console_handler.setLevel(logging.INFO)[m
[32m+[m
[32m+[m[32m        # Create formatter and add to handlers[m
[32m+[m[32m        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")[m
[32m+[m[32m        file_handler.setFormatter(formatter)[m
[32m+[m[32m        console_handler.setFormatter(formatter)[m
[32m+[m
[32m+[m[32m        # Add handlers to logger[m
[32m+[m[32m        logger.addHandler(file_handler)[m
[32m+[m[32m        logger.addHandler(console_handler)[m
[32m+[m
[32m+[m[32m        return logger[m
