import logging

logging.basicConfig(level=logging.DEBUG)

x: int = 10 + 10

logging.info('The answer is: %s',x) # for backward compatibility
logging.info(f'The answer is: {x}') # still works