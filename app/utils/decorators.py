import time
from functools import wraps

from app.core.logger import logger


def log_execution_time(func):
    """
    Logs function start, success/failure, and execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.time()

        logger.info("%s started", func.__name__)

        try:
            result = func(*args, **kwargs)

            logger.info(
                "%s completed successfully in %.4f seconds",
                func.__name__,
                time.time() - start_time
            )

            return result

        except Exception as exc:
            logger.exception(
                "%s failed after %.4f seconds | Error: %s",
                func.__name__,
                time.time() - start_time,
                str(exc)
            )

            raise

    return wrapper