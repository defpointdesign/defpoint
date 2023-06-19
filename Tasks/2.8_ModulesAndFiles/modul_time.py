# 712
# Напишіть програму, яка друкує значення системного часу. Використайте модуль time.
# Fri Jul 26 19:02:02 2019

import time

current_time = time.localtime()  # Get the current time as a struct_time object

weekday = time.strftime("%A", current_time)  # Format the weekday as a string
month = time.strftime("%B", current_time)  # Format the weekday as a string
day = time.strftime("%d", current_time)  # Format the weekday as a string
clock_time=time.strftime('%H:%M:%S', current_time)  # Format the time as a string
current_year = current_time.tm_year  # Extract the year from the struct_time object

print( weekday[:3], month[:3],day, clock_time, current_year)