print('Задача 1. Сумма чисел')

numbers_file = open('numbers.txt', 'r')
summa = 0
for i_line in numbers_file:
    clear_line = i_line.rstrip()
    summa += int(clear_line)
summa = str(summa) + '\n'

sum_file = open('answer.txt', 'w')
sum_file.write(summa)
numbers_file.close()
sum_file.close()

print('-' * 20)


print('Задача 2. Всё в одном')
import os

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


def get_text(file_path):
    file = open(file_path, 'r', encoding='utf8')
    result = ''
    for line in file:
        result += line
    return result


file_path = 'E:/Life/Python/2 курс/Python_Basic'
file_name = 'main.py'

list_of_path = find_file(file_path, file_name)

scripts_file = open('scripts.txt', 'w', encoding='utf8')

for i_path in list_of_path:
    scripts_file.write(get_text(i_path))
    scripts_file.write('\n' * 2 + '*' * 40 + '\n' * 2)
