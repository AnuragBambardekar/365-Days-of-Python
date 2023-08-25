import logging
FMT = "[{levelname:^9}] {name}:{message}"
FORMATS = {
    logging.DEBUG: FMT, 
    logging.INFO: f"\33[36m{FMT}\33[0m", # all ANSI colors start with \33[ and ends with \33[0m
    logging.WARNING: f"\33[33m{FMT}\33[0m",
    logging.ERROR: f"\33[31m{FMT}\33[0m",
    logging.CRITICAL: f"\33[1m\33[31m{FMT}\33[0m",
}

# custom formatter class
class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_fmt = FORMATS[record.levelno]
        formatter = logging.Formatter(log_fmt, style="{")
        return formatter.format(record)
    
# create the logging object
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[handler],
)

log = logging.getLogger("coloured-logger")
log.debug("This is a test message.")
log.info("This is a test message.")
log.warning("This is a test message.")
log.error("This is a test message.")
log.critical("This is a test message.")