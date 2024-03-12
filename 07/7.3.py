print('Задача 1. Саботаж!')

string = input('Строка: ')
for index, sym in enumerate(string):
    if sym == '~':
        print(index, end=' ')

print()
print('-' * 20)


print('\nЗадача 2. Словари из списков')

import random

letter_list_1 = [chr(random.randint(ord('а'), ord('я'))) for i in range(10)]
letter_list_2 = [chr(random.randint(ord('а'), ord('я'))) for i in range(10)]
print('\nПервый список:', letter_list_1)
print('Второй список:', letter_list_2)

letter_dict_1 = {}
for ind, letter in enumerate(letter_list_1):
    letter_dict_1[ind] = letter

letter_dict_2 = {}
for ind, letter in enumerate(letter_list_2):
    letter_dict_2[ind] = letter

print('\nПервый словарь:', letter_dict_1)
print('Второй словарь:', letter_dict_2)

print('-' * 20)


print('Задача 3. Универсальная программа')

object = 'раз1, два2, три3'
result = []
if isinstance(object, (str, list, dict, tuple)):
    for i, elem in enumerate(object):
        if i % 2 == 0:
            result.append(elem)
    print('\n', result)
else:
    print('\nОбъект не является итерируемым типом данных.')
