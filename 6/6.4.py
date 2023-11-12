print('Задача 1. Пунктуация')

symbols = {'.', ',', ';', ':', '!', '?'}

string = input('Введите строку: ')
set_string = set(string)
quantity = len(set_string.intersection(symbols))

print('Количество знаков пунктуации:', quantity)

print('-' * 20)


print('Задача 2. Семинар')

import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]
nums_1 = set(nums_1)
nums_2 = set(nums_2)
print('\n1-е множество:', nums_1, '\n2-е множество:', nums_2)
print('\nМинимальный элемент 1-го множества:', min(nums_1), '\nМинимальный элемент 2-го множества:', min(nums_2))
nums_1.remove(min(nums_1))
nums_2.remove(min(nums_2))
random_number_1 = random.randint(100, 200)
random_number_2 = random.randint(100, 200)
print('\nСлучайное число для 1-го множества:', random_number_1, '\nСлучайное число для 2-го множества:', random_number_2)
nums_1.add(random_number_1)
nums_2.add(random_number_2)
union = nums_1.union(nums_2)
intersection = nums_1.intersection(nums_2)
difference = nums_2.difference(nums_1)
print('\n1. Объединение множеств:', union,
      '\n2. Пересечение множеств:', intersection,
      '\n3. Элементы, входящие в nums_2, но не входящие в nums_1:', difference)

print('-' * 20)


print('Задача 3. Различные цифры')

