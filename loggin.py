import logging

# Initialize logging
logging.basicConfig(filename="sample3.log",format='%(asctime)s %(message)s')
my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)

my_logger.debug("Donde sales tu?")
