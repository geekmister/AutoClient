"""
@Project : cd-auto-test-client.git
@File    : logger.py
@IDE     : PyCharm
@Author  : geek mister
@Date    : 2024/1/5 17:50
@MyHome  : https://github.com/geekmister
@Desc    : init log manager, contains
            1. support print log in console;
            2. support write log in file;
"""


import logging
from logging import handlers
import os


# log object
logger = logging.getLogger('mainNodule')


def init():
    """
    init log manager
    Returns:
        None
    """

    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

    # divider by file size
    # RotatingFileHandler()
    handle = handlers.TimedRotatingFileHandler(filename=f'{os.path.basename(p=__file__)[:-2]}log', encoding='UTF-8')
    handle.setLevel(logging.INFO)
    handle.setFormatter(formatter)

    # init console object
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)

    # write log in file
    logger.addHandler(handle)
    logger.addHandler(console)


init()


if __name__ == "__main__":
    # the under code are test code
    logger.debug('debug log')
    logger.info('info log')
    logger.warning('warm log')
    logger.error('error log')
    logger.critical('critical log')
