import logging
import sys

date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(thread)d - %(message)s"

#logging.basicConfig(format=message_format, datefmt=date_strftime_format, filename='run.log', encoding='utf-8', level="INFO")
logging.basicConfig(format=message_format, datefmt=date_strftime_format, stream=sys.stdout, encoding='utf-8', level=logging.INFO)
