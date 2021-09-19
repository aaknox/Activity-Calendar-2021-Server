import logging
from keep_alive import keep_alive

#configure logging for server
log_filename = "ac.log"
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename=log_filename,
    filemode='w')

#start the server
logging.info('Starting Activity Calendar Server...')
keep_alive()