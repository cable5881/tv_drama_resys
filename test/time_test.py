from datetime import datetime
from datetime import timedelta

today = datetime.today()

# 2017-05-23 19:08:44.103278
print(today)
# <class 'datetime.datetime'>
print(type(today))

now = datetime.now()
print(now)

t1 = datetime(year=1994, month=5, day=23)
print(t1)

print(now - t1)

right_now = datetime.now()
yesterday = right_now - timedelta(days=1)
print(right_now)
print(yesterday)

if right_now - yesterday < timedelta(days=1):
    print('within one day')
else:
    print('more than one day')

day_now = right_now.day
day_yes = yesterday.day
print(day_now)
print(day_yes)

if day_now - day_yes <= 1:
    print('within one day')
else:
    print('more than one day')