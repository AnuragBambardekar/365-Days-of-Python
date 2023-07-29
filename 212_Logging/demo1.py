import logging

# directly add it to the logs file
logging.basicConfig(filename='my_logs.log',
                    encoding='utf-8',
                    filemode='w',
                    level=logging.DEBUG) # filemode='w' means it will overwrite


logging.debug('DEBUG')
logging.info('INFO')
logging.warning('WARNING')
logging.error('ERROR')
logging.critical('CRITICAL')