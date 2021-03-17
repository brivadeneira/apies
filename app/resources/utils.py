from datetime import datetime
from uuid import uuid4


def str_to_isoformat(str_datetime: str) -> None:
    """
    Returns an isoformat datetime object if it is possible, None otherwise
    :param str_datetime: (str) to convert
    :return: None
    """
    try:
        return datetime.fromisoformat(str_datetime)
    except TypeError:
        raise TypeError(
            "Field 'start_time' "
            "must be in ISO_8601 format: "
            "YYYY-MM-DDThh:mm:ss+00:00"
        )


def log_event(logger, level: str, msg: str) -> None:
    """
    Write log messages into app/app/resources/logs log file.
    :param logger: logging instance to write messages (settings.logger)
    :param msg: (str) message to write
    :param level: (str) info, error, deb or warn
    """
    log_id = str(uuid4())[:8]
    log_msg = f"[{log_id}]{msg}"
    if level == "info":
        logger.info(log_msg)

    elif level == "error":
        logger.error(log_msg)

    elif level == "warn":
        logger.warning(log_msg)
