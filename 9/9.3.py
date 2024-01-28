print('Задача 1. Результаты')

import os

path_to_first = os.path.join('task', 'group_1.txt')
path_to_second = os.path.join('task', 'Additional_info', 'group_2.txt')

file_1 = open(path_to_first, 'r')
summa = 0
diff = 0
for i_line in file_1:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])

file_2 = open(path_to_second, 'r')
compose = 1
for i_line in file_2:
    info = i_line.split()
    compose *= int(info[2])

file_1.close()
file_2.close()

print(summa)
print(diff)
print(compose)

print('-' * 20)


print('Задача 2. Поиск файла 2')

