# 711
# Напишіть програму, щоб отримати назву, платформу та інформацію про випуск операційної системи.
# Використайте імпорт модулів platform і os.
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

# 714
# Напишіть програму, яка друкує поточне ім’я користувача в системі. Використайте модуль os.
import os
import getpass
user_name=getpass.getuser()
print(user_name)

# 718
# Напишіть програму python, щоб отримати шлях і ім’я файла, який наразі виконується.
# Використайте модуль os
import os
current_file_path=os.path.abspath(__file__)
print(current_file_path)


# 720
# Напишіть програму для перевірки існування файла в поточному каталозі.
# Використайте модуль os.
user_file=input('Paste file name: ')
file_path=os.path.abspath(user_file)
print(os.path.exists(file_path))