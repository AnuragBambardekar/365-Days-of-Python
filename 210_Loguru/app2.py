from loguru import logger

def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        logger.exception("Division by zero occurred!")
        return None
    else:
        logger.info("Division result: {}", result)
        return result

def main():
    # Initialize the logger
    logger.add("example.log", rotation="500 MB", backtrace=True, diagnose=True)

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

    a = 10
    b = 2
    divide_numbers(a, b)

    c = 5
    d = 0
    divide_numbers(c, d)

if __name__ == "__main__":
    main()
