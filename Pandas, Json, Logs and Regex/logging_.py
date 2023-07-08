import logging

# Create and configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages using different levels
logging.debug('This is a debug message')    # Lowest level
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')    # Highest level

# Create a custom logger
logger = logging.getLogger('custom_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler and set its level
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)

# Create a formatter and set it to the file handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the custom logger
logger.addHandler(file_handler)

# Log messages using the custom logger and file handler
logger.debug('Debug message for custom logger')
logger.error('Error message for custom logger')

# Log an exception with traceback
try:
    result = 10 / 0
except Exception as e:
    logging.exception('An exception occurred')

# Disable logging
logging.disable(logging.ERROR)

# Log a message (this won't be displayed due to logging being disabled)
logging.critical('This message won\'t be displayed')

