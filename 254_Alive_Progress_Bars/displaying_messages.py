from alive_progress import alive_bar
import time, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('alive_progress')

with alive_bar(1000) as bar:
    for i in range(1000):
        if i and i%300 == 0:
            print("Found!")
        if i in (450,750):
            logger.info("Yo!")
        time.sleep(0.01)
        bar()
