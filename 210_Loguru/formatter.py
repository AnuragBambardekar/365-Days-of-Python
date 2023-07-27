from loguru import logger

def debug_format():
    logger.add(
        "_logs/debug_{time:YY-mm-dd-HH-mm-ss!UTC}.log",
        level="DEBUG",
        format="{level} | {time:HH:mm:ss!UTC} | {module}.{function} | {message}",
        rotation="100 KB",
        retention= "10 seconds",
        colorize= True
    )
    for x in range(5000):
        logger.debug("Custom debug logger")

if __name__ == "__main__":
    debug_format()