import logging
from uuid import uuid4
import inspect
from api_helpers import post_log
from datetime import datetime


class DbLogHandler(logging.Handler):
    """
    Handles logging to the database.
    """

    def __init__(self):
        logging.Handler.__init__(self)

    def get_caller_info(self):
        # Get the stack frame of the caller
        frames = inspect.stack()

        # Last frame of stack is the caller
        caller_frame = frames[-1]

        # Extract the filename, function name, and line number of the caller
        filename = caller_frame.filename
        function_name = caller_frame.function
        line_number = caller_frame.lineno

        return filename, function_name, line_number

    def emit(self, record):
        try:
            filename, function_name, line_number = self.get_caller_info()
            log_entry = {
                "user_email": "system",
                "log_id": str(uuid4()),
                "log_level": record.levelname,
                "message": record.getMessage(),
                "created_on": str(datetime.utcnow()),
                "caller_filename": filename,
                "caller_function_name": function_name,
                "caller_line_number": str(line_number),
            }
            status = post_log(log_entry)
            if not status:
                raise Exception("Error occurred while writing to the database")
        except Exception as e:
            logging.error(f"[Log Handler] {e}")


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
    handler_exists = any(
        isinstance(handler, DbLogHandler) for handler in logger.handlers
    )
    if not handler_exists:
        db_handler = DbLogHandler()
        db_handler.setLevel(logging.WARNING)
        logger.addHandler(db_handler)

    return logger


def remove_logging():
    logger = logging.getLogger()
    for handler in logger.handlers:
        if isinstance(handler, DbLogHandler):
            logger.removeHandler(handler)
    return logger
