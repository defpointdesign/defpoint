# 733
# У вхідному файлі записана один текстовий рядок, який може містити пропуски.
# Запишіть цей рядок в зворотному порядку у інший файл.

# file1=open('input1.txt', 'r')
# add_text=file1.read()
# file1.close()
#
# file2=open('output.txt', 'w')
# file2.write(add_text[::-1])
# file2.close()

# 734
# У вхідному файлі записано два цілих числа, які можуть бути розділені пропусками і кінцями рядків.
# Виведіть у вихідний файл їх суму.

file=open('input.txt', 'r')

list_i =''
for i in file:
    list_i+=i
print(list_i)
file.close()

res=[]
for elem in list_i:
    if elem.isdigit():
        res.append(int(elem))
print(res)

sum=0
for j in range(len(res)):
    sum+=res[j]
print(sum)

file_out=open('output', 'w')
file_out.write(str(sum))
file.close()

