import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


def get_logger(name=None):

    logger = logging.getLogger(name if name else __name__)
    logger.setLevel(logging.INFO)
    
    if logger.handlers:
        return logger

    root_dir = (os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")

    # 🔹 Build path: screenshots/YYYY/MM/DD
    log_dir = os.path.join(root_dir, "logs", year, month, day)
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, "file.log")
    
    file_handler = TimedRotatingFileHandler(log_file, when = "midnight", interval= 1, backupCount=10, encoding="utf-8")
    
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")

    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)

    return logger

# def get_daily_logger(name: str = "MyLogger", log_dir: str = settings.LOG_PATH) -> logging.Logger:
#     global _current_log_date, _logger_instance, _current_log_path

#     today = date.today()
#     dated_log_dir = os.path.join(log_dir, f"{today.year}/{today.month}")
#     os.makedirs(dated_log_dir, exist_ok=True)

#     log_file = os.path.join(dated_log_dir, f"{today}.log")

#     # Defensive check for path existence
#     file_exists = os.path.exists(_current_log_path) if _current_log_path else False

#     # Check if new logger is needed
#     if (
#         _logger_instance is None
#         or _current_log_date != today
#         or not file_exists
#     ):
#         print("🔄 Refreshing logger...")

#         _current_log_date = today
#         _current_log_path = log_file

#         try:
#             logger = logging.getLogger(name)
#             logger.setLevel(logging.INFO)
#             logger.handlers.clear()  # Clear old handlers

#             handler = TimedRotatingFileHandler(
#                 filename=log_file,
#                 when="midnight",
#                 interval=1,
#                 backupCount=7,
#                 encoding='utf-8',
#                 utc=False
#             )

#             formatter = logging.Formatter(
#                 '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s',
#                 datefmt='%Y-%m-%d %H:%M:%S'
#             )
#             handler.setFormatter(formatter)
#             logger.addHandler(handler)

#             _logger_instance = logger
#         except Exception as e:
#             print(f"❌ Logger creation failed: {e}")
#             _logger_instance = None

#     if _logger_instance is None:
#         raise RuntimeError("Logger could not be initialized — check file permissions or handler errors.")

#     return _logger_instance




