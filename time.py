import datetime


start_time, end_time = get_times('hour', -3, -1.2)
if start_time <= utc_time < end_time:
   # utc_time is in between