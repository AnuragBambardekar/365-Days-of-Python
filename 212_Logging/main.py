import logging

"""
The logging module in Python is a powerful and flexible module that 
provides a standardized way to log messages from your Python programs. 
It allows you to control the output of log messages, set different log 
levels, and route log messages to different destinations, such as the 
console, files, or external services.
"""

logging.basicConfig(level=logging.DEBUG)
"""
prints all issues above DEBUG level:-

DEBUG:root:DEBUG
INFO:root:INFO
WARNING:root:WARNING
ERROR:root:ERROR
CRITICAL:root:CRITICAL
"""

logging.debug('DEBUG')
logging.info('INFO')
logging.warning('WARNING')
logging.error('ERROR')
logging.critical('CRITICAL')