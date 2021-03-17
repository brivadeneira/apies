import logging

formatter = logging.Formatter(
    "%(asctime)s:[%(levelname)-1s]:%(message)s", datefmt="%Y-%m-%dT%H:%M:%S%z"
)
apies_logger = logging.getLogger()
hdlr = logging.FileHandler("app/resources/logs/apies.log")
hdlr.setFormatter(formatter)
hdlr.setLevel(logging.DEBUG)
apies_logger.addHandler(hdlr)
