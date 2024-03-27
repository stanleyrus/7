from datetime import datetime, timedelta
import datetime
import time

# t1 = os.getenv('datetime.now()-timedelta(days=1)')
# print(type(t1))

# print(t1 := datetime.date.today())
# print(t2 := datetime.date(2023, 1, 20))
# print(t3 := t2 - t1, type(t3))

# D1 = {"MIMI": None}
# print(D1)

# t = int(time.mktime(time.strptime("2024-03-06 22:44:42"))) - time.timezone
# print(t)
# res = []
# print(len(res))

from datetime import datetime, timedelta
from json import dumps
import time


# registered_at__gt={unixtime_start} и registered_at__lt={unixtime_end}

# load_date = os.getenv('JK_LOAD_DATE', (datetime.datetime.now()-timedelta(days=1)).strftime('%Y-%m-%d'))
#
# dt_start = f"{(load_date-timedelta(days=1)).strftime('%Y-%m-%d')}, 00:00:00"
#
# dt_end = f"{load_date}, 23:59:59"
# formated_end_date = datetime.datetime.strptime(dt_end,"%Y-%m-%d, %H:%M:%S")
# unixtime_end = f"{int(datetime.datetime.timestamp(formated_end_date))}"
# unixtime_start = f"{int(unixtime_end) - (3600*24)}"


a = 45
c = 'kiki'
d = {'d': 432, 'f': 'dfsf'}
def fn():
    global a, c, d
    a += 17
    c += ' miks'
    print(a, c)


fn()