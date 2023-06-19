# 719
# Напишіть програму, яка створює список файлів з поточного каталогу, використовуючи символи підстановки.
# Використайте модуль glob.

import glob
current_directory='*'
file_list=glob.glob(current_directory)
for file_name in file_list:
    print(file_name)

