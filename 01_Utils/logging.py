"""
	Author: Luis_C-137
	(1) Create a log file
	(2) Change the level of the log to default
	(3) Give format to the message
	(4) Log something!
"""
log_path = ""

log_format = "%(levelname)s %(asctime)s | %(message)s"	#(3)

logging.basicConfig(filename = log_path,	#(1)
						level = logging.DEBUG,	#(2)
						format = log_format)	#(3)

logger = logging.getLogger()

"""
Log levels -----------------------
	NOTSET		0
	DEBUG		10
	INFO		20
	WARNING		30
	ERROR		40
	CRITICAL	50
"""

logger.debug("Just for fun!")
logger.info("Something did happened")
logger.warning("Something bad may happen")
logger.error("Something bad happened")
logger.critical("Something terrible happened")