# 713
# Напишіть програму, щоб відобразити поточні дату й час як у вихідних даних.
# Використайте модуль datetime.

from datetime import datetime

current_date=datetime.now().date() # Get the current date
formatted_date=current_date.strftime('%Y-%m-%d')

current_time=datetime.now().time() # Get the current date
formatted_time=current_time.strftime('%H:%M:%S')

print(formatted_date, formatted_time)
