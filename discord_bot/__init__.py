import logging
import os
import sys
from config import config

# Loading class config according to ENV var
config_name = os.environ.get('DISCORD_BOT_ENV', 'development')
current_config = config[config_name]

# Logger Settings
package_name = '.'.join(__name__.split('.')[:-1])
root_logger = logging.getLogger(package_name)
console_handler = logging.StreamHandler(sys.stdout)
# file_handler = logging.FileHandler('logging/app.log')
consolelog_format = logging.Formatter(
    '%(name)s - %(levelname)s - %(message)s')
# filelog_format = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(consolelog_format)
# file_handler.setFormatter(filelog_format)
root_logger.addHandler(console_handler)
# root_logger.addHandler(file_handler)
root_logger.setLevel(current_config.LOG_LEVEL)
