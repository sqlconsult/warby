#!/usr/bin/env python3
import datetime
import logging
from pathlib import Path
import sys

import logger
from read_inputs import ReadInputs


def main():
    """
    Main entry point
    """
    # Create logs directory if not present
    Path('logs').mkdir(parents=True, exist_ok=True)
    
    # Start logger
    app_name = __file__.split('.')[0]
    logger.start_logger(app_name)

    module_logger = logging.getLogger('{app_name}.controller'.format(app_name=app_name))
    module_logger.info('<<<<< Starting >>>>>')

    # command line to execute:
    # cat user_inputs.txt | python controller.py
    read_obj = ReadInputs(module_logger)

    # read patterns
    read_obj.read_patterns()

    # read and process paths
    result = read_obj.process_paths()

    for res in result:
        module_logger.info(res)
        print(res)

    module_logger.info('<<<<< Done >>>>>')


if __name__ == '__main__':
    main()
    sys.exit(0)