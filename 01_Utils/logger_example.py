"""
	Author: Luis_C-137
	(1) Create a log and name it
	(2) Create file handler
	(3) Create console handler
	(4) Give format to the handlers
	(5) Set levels to handlers
	(6) Add Handlers to log
	(7) Print some messages
"""

"""			REMEMBER!!!
Log levels -----------------------
	NOTSET		0
	DEBUG		10
	INFO		20
	WARNING		30
	ERROR		40
	CRITICAL	50
"""

import logging

log_path = "bandit.log"		#(2)
log_format = "%(levelname)s %(asctime)s | %(message)s"	#(4)

# Create log and handlers
logger = logging.getLogger('Lumberjack')	#(1)
fileh = logging.FileHandler(log_path)		#(2)
consoleh = logging.StreamHandler()			#(3)

# Add formatter to the handlers
fileh.setFormatter(log_format)				#(4)
consoleh.setFormatter(log_format)

# Set levesl to handlers 					#(5)
fileh.setLevel(logging.ERROR)
consoleh.setLevel(logging.DEBUG)

#Add handlers to getLogger					#(6)
logger.addHandler(fileh)
logger.addHandler(consoleh)

logger.debug("Just for fun!")				#(7)
logger.info("Something did happened")
logger.warning("Something bad may happen")
logger.error("Something bad happened")
logger.critical("Something terrible happened")