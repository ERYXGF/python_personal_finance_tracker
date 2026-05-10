"""Logger module for the Personal Finance Tracker.
This module is responsible for logging all the actions and events that occur in the application."""

import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file, console_level, file_level):
    """Function to setup a logger with both console and file handlers.
    Args:
        name (str): The name of the logger.
        log_file (str): The path to the log file.
        console_level (int): The logging level for the console handler.
        file_level (int): The logging level for the file handler.
    Returns:
        logging.Logger: The configured logger instance.
    """
    # Creates the log directory if missing:
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    # Creates the logger and sets its level:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Checks for the duplicate-handler trap:
    if logger.handlers:
        return logger

    # Creates the formatter:
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    # Creates the file handler and assigns the level and formatter:
    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=1024 * 1024, #One megabyte
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)

    # Creates the console handler and assigns the level and formatter:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)

    # Prevents records from propagating to the root level:
    logger.propagate = False

    # Adds both handlers to the logger:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instantiates the logger:
logger = setup_logger(
    name="finance_tracker",
    log_file=Path("data/logs/finance.log"),
    console_level=logging.INFO,
    file_level=logging.DEBUG,
)
