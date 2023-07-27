import sys
from loguru import logger

logger.remove(0)
logger.add(sys.stderr, format="{time} | {level} | {message}")
logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")


logger.debug("Happy logging with Loguru!")
