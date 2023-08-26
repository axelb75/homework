print('Задача 1. Список чётных чисел')

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))

even_numbers = [num for num in range(A, B + 1) if num % 2 == 0]

print(even_numbers)

print('-' * 20)


print('Задача 2. Магазин')

import random

original_prices = [round(random.uniform(-100, 100), 2) for _ in range(12)]
print(original_prices)
new_prices = [i if i > 0 else 0 for i in original_prices]

print(new_prices)

print('-' * 20)


print('Задача 3. Отряды')

unit_1 = [random.randint(50, 80) for unit in range(10)]
unit_2 = [random.randint(30, 60) for unit in range(10)]

unit_3 = ['Погиб' if unit_1[i_unit] + unit_2[i_unit] > 100
          else 'Выжил'
          for i_unit in range(10)]

print('Урон первого отряда:', unit_1)
print('Урон второго отряда:', unit_2)
print('Состояние третьего отряда:', unit_3)