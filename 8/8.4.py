print('Задача 1. Ошибка')

import random
import copy


def change_dict(dct):
    num = random.randint(1, 100)
    for i_key, i_value in dct.items():
        if isinstance(i_value, list):
            i_value.append(num)
        if isinstance(i_value, dict):
            i_value[num] = i_key
        if isinstance(i_value, set):
            i_value.add(num)


nums_list = [1, 2, 3]
some_dict = {1: 'text', 2: 'another text'}
uniq_nums = {1, 2, 3}

common_dict = {1: nums_list, 2: some_dict, 3: uniq_nums, 4: (10, 20, 30)}
new_common_dict = copy.deepcopy(common_dict)
change_dict(new_common_dict)

print(new_common_dict, nums_list, some_dict, uniq_nums, sep='\n')

print('-' * 20)


print('\nЗадача 2. Непонятно!')

#data = 'Привет! Это я.'
#data = [1, 'Ok', 2.34, ['A', 'B', 'C']]
#data = (5, 6, 7.89, {'D': 'd', 'E': 'e', 3: 'f'}, 'Hello', '1312 ACAB')
data = {1: 'All', 2: 'cops', 3: 'are', 4: 'bastards', 5:['z', 'x', 'w', 'y']}
#data = {11, 'my way', 44, 33.2, 'together 69', ('a', 45, 'r', 'red', 'e', 78.9)}

print('Введите данные:', data)
print('Тип данных:', end=' ')
if isinstance(data, str):
    print('str (строка)')
    print('Неизменяемый (immutable)')
elif isinstance(data, dict):
    print('dict (словарь)')
    print('Изменяемый (mutable)')
elif isinstance(data, list):
    print('list (список)')
    print('Изменяемый (mutable)')
elif isinstance(data, tuple):
    print('tuple (кортеж)')
    print('Неизменяемый (immutable)')
elif isinstance(data, set):
    print('set (множество)')
    print('Изменяемый (mutable)')

print('Id объекта:', id(data))
