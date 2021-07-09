"""
author : Franklin Gallardo
date : 09-Jul-2021
"""
import time
from datetime import datetime

TIME_WAIT = 5  # seconds time


# process time
def format_readable_date():
    date_begin = datetime.now()  # start process
    time.sleep(TIME_WAIT)  # wait
    date_end = datetime.now()  # end process
    date_process = date_end - date_begin  # timedelta object
    print(hour_min_sec_micro(date_process))


# format human
def hour_min_sec_micro(delta):
    hours, remainder = divmod(delta.seconds, 3600)  # hours
    minutes, seconds = divmod(remainder, 60)  # minutes and seconds
    return '({:02})hours:({:02})minutes:({:02})seconds ({:06})micro' \
        .format(int(hours), int(minutes), int(seconds), int(delta.microseconds))


# main method.
if __name__ == '__main__':
    format_readable_date()
