# -*- coding:utf-8 -*-

import colorlog
import logging
import sys

from logging.handlers import SysLogHandler

from demo.errors import UnsupportedPlatformError


INTERACTIVE_FORMAT = '%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(message)s'



class SingleLevelFilter(logging.Filter):
    def __init__(self, passlevel, reject):
        self.passlevel = passlevel
        self.reject = reject

    def filter(self, record):
        if self.reject:
            return (record.levelno != self.passlevel)
        else:
            return (record.levelno == self.passlevel)


def get_stdout_handler():
    handler = colorlog.StreamHandler(sys.stdout)
    f1 = SingleLevelFilter(logging.INFO, False)
    formatter = colorlog.ColoredFormatter(INTERACTIVE_FORMAT)
    handler.setFormatter(formatter)
    handler.addFilter(f1)
    return handler


def get_stderr_handler():
    handler = colorlog.StreamHandler(sys.stderr)
    f1 = SingleLevelFilter(logging.INFO, True)
    formatter = colorlog.ColoredFormatter(INTERACTIVE_FORMAT)
    handler.setFormatter(formatter)
    handler.addFilter(f1)
    return handler


def get_domain_socket():
    """Get the default domain socket for syslog on this platform."""
    if sys.platform.startswith('linux'):  # Linux
        return '/dev/log'
    if sys.platform.startswith('darwin'):  # macOS
        return '/var/run/syslog'
    # Unsupported platform
    raise UnsupportedPlatformError(sys.platform)


def get_syslog_handler():
    handler = SysLogHandler(address=get_domain_socket())
    return handler
