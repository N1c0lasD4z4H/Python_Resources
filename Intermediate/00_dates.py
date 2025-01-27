### Dates ###
import datetime

# datetime Agrupa los dos tipos de datos fecha y hora
from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
timestamp = now.timestamp()
print (timestamp)

year_2026 = datetime(2026,9,11)

print_date(year_2026)

from datetime import time

# Time Agrupar datos de tiempo(hora etc)
current_time = time(10,6,2)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#Date Agrupar dato de fecha (año etc)
from datetime import date

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2024,9,11)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,current_date.month + 1, current_date.day)

print(current_date.month)

print()
# Operaciones con fechas
diff = year_2026 - now
print(diff)
diff = year_2026.date() - current_date
print(diff)


# TimeDelta

from datetime import timedelta

start_timedelta = timedelta(200,100,1000,weeks= 10)
end_timedelta = timedelta(300,100,1000,weeks= 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)