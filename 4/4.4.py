print('Задача 1. Анализ цен')

import random

original_prices = [random.randint(-100, 100) for _ in range(10)]

print(original_prices)

#Вариант 1:
new_prices = original_prices[:]
new_prices = [i if i > 0 else 0 for i in new_prices]

#Вариант 2:
new_prices = [i if i > 0 else 0 for i in original_prices]

print(new_prices)
print("Мы потеряли: ",  sum(new_prices) - sum(original_prices))

print('-' * 20)


print('Задача 2. Срезы')

nums = [random.randint(-100, 100) for _ in range(10)]
print(nums)
print('Результат:')
print(nums[:5])
print(nums[:-2])
print(nums[::2])
print(nums[1::2])
print(nums[::-1])
print(nums[::-2])

print('-' * 20)


print('Задача 3. Удаление части')

N = [random.randint(-100, 100) for _ in range(10)]
a = random.randint(0, 9)
b = random.randint(a, 9)
print('Список:', N, '\na =', a, '\nb =', b)
N = N[:a] + N[b + 1:]
print(N)