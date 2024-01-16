print('Задача 1. Сисадмин')

import os

file = 'admin.bat'
print('Относительный путь до файла:', os.path.join('2 курс', 'ДЗ', '9', file))
print('Абсолютный путь до файла:', os.path.abspath(file))
print('-' * 20)


print('\nЗадача 2. Содержимое')

print(os.listdir('..'), '\nСодержимое каталога', os.path.abspath('..') + ':')
for path in os.listdir('..'):
    print('    ', os.path.join(os.path.abspath('..'), path))

print('-' * 20)


print('\nЗадача 3. Корень диска')

print("Корень диска:", os.path.abspath(os.sep).split(os.sep)[0] + os.sep)
print("Корень диска:", os.sep)
print('Каталог:')
for i in os.listdir(os.sep):
    print('   ', i)