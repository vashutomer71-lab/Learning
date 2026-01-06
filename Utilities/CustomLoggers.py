import os
import logging

class LogGen:
    @staticmethod
    def loggen():
        # Ensure the Logs directory exists
        log_dir = "./Logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create a logger with the application name
        logger = logging.getLogger('automation_logger')
        logger.setLevel(logging.INFO)

        # Create a file handler to write logs to a file
        log_file = os.path.join(log_dir, "automation.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create a console handler for debugging purposes
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s -%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Check if handlers are already added to avoid duplicate logs
        if not logger.handlers:
            # Add the handlers to the logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
