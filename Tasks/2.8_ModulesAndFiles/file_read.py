# 731
# Напишіть програму для зчитування файла рядок за рядком та зберігання рядків у списку.
file=open('input.txt', 'r')
line_list=[]
for line in file:
    line_list.append(line)
print(line_list)
file.close()





