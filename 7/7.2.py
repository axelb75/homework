print('Задача 1. Создание кортежей')

import random

nums_1 = tuple([random.randint(0, 5) for i in range(10)])
nums_2 = tuple([random.randint(-5, 0) for i in range(10)])

nums = nums_1 + nums_2

print('Первый кортеж:', nums_1, '\nВторой кортеж:', nums_2,
      '\nИтоговый кортеж:', nums, '\nКоличество нулей:', nums.count(0))

print('-' * 20)


print('\nЗадача 2. Цилиндр')

import math

def calc_area(nums):
    side = 2 * math.pi * float(nums[0]) * float(nums[1])
    full = side  + 2 * math.pi * float(nums[1]) ** 2
    return side, full


numbers = input('Введите через пробел высоту и радиус цилиндра: ')
nums = numbers.split(' ')
side_area, full_area = calc_area(nums)
print('Площадь боковой поверхности цилиндра:', round (side_area, 2), '\nОбщая площадь:', round(full_area, 2))

print('-' * 20)


print('\nЗадача 3. Неправильный код')

import random

def change(nums):
    nums_list = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    nums_list[index] = value
    new_nums = tuple(nums_list)
    return new_nums, value


my_nums = (1, 2, 3, 4, 5)
new_nums, rand_val = change(my_nums)
val = rand_val
print(new_nums, rand_val)
new_nums, rand_val = change(new_nums)
val += rand_val
print(new_nums, val)
