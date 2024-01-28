print('Задача 1. Иконки')

import os

user_path = input('Путь: ')
if os.path.isdir(user_path):
    print("Это папка!")
    print('Список файлов:')
    for file in os.listdir(user_path):
        print('    ', file)
elif os.path.isfile(user_path):
    print("Это файл!")
    print("Размер файла:", os.path.getsize(user_path), "байт")
else:
    print("Указанного пути не существует")

print('-' * 20)


print('Задача 2. Поиск файла')

def find_file(cur_path, file):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file == i_elem:
            print(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file)
            if result:
                break
    else:
        result = None

    return result


file_path = input('Ищем в: ')
file_name = input('Имя файла: ')

print('Найдены следующие пути:')
find_file(file_path, file_name)