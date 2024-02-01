print('Задача 1. Результаты')

import os

path_to_first = os.path.join('task', 'group_1.txt')
path_to_second = os.path.join('task', 'Additional_info', 'group_2.txt')

file_1 = open(path_to_first, 'r', encoding='utf-8')
summa = 0
diff = 0
for i_line in file_1:
    info = i_line.split()
    summa += int(info[2])
    diff -= int(info[2])

file_2 = open(path_to_second, 'r', encoding='utf-8')
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
import random


def find_file(cur_path, file):
    list_path = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file == i_elem:
            list_path.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file)
            if result:
                list_path.extend(result)
    return list_path


file_path = input('Ищем в: ')
file_name = input('Имя файла: ')


list_of_path = find_file(file_path, file_name)
number = random.randint(0, (len(list_of_path) - 1))
readme_file = open(list_of_path[number], 'r')
print('Содержимое файла "' + list_of_path[number] + '":')
print(readme_file.read())

readme_file.close()