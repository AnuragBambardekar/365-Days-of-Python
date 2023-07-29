import logging

logging.basicConfig(format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    level=logging.DEBUG,
                    filename='my_logs2.log')

logging.info('Hello World!')
logging.warning("WARNING")

# Print doesnt give us so much information

import other_module
other_module.func()