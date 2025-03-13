import logging
import os

def setup_logger():
    """Configures the logger to save logs inside the report folder."""
    log_folder = "report"
    log_file = os.path.join(log_folder, "test_execution.log")  # Save inside report/

    # Ensure the report directory exists
    os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger("TestLogger")
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        handler = logging.FileHandler(log_file, mode='a')  # Append mode
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

logger = setup_logger()
