import time
from kit import config


def delay_after_read():
    time.sleep(config.DELAY_SECONDS_AFTER_GITHUB_READS)


def delay_after_write():
    time.sleep(config.DELAY_SECONDS_AFTER_GITHUB_WRITES)


def delay_after_notification():
    time.sleep(config.DELAY_SECONDS_AFTER_GITHUB_NOTIFICATION)
