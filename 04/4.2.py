print('Задача 1. Кубы и квадраты')

A = int(input('Левая граница: '))
B = int(input('Правая граница: '))

list_cube = [num ** 3 for num in range(A, B + 1)]
list_squared = [num ** 2 for num in range(A, B + 1)]

print(f'Список кубов чисел в диапазоне от {A} до {B}: {list_cube}')
print(f'Список квадратов чисел в диапазоне от {A} до {B}: {list_squared}')

print('-' * 20)


print('Задача 2. Сообщение')

text = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

double_text = [sym * 2 for sym in text]
concatenation = [(sym + symbol) for sym in double_text]

print('Список удвоенных символов:', double_text)
print('Склейка с дополнительным символом:', concatenation)

print('-' * 20)

print('Задача 3. Повышение цен')

quantity = int(input('Кол-во товаров: '))
list_prices = [float(input(f'Цена на {i + 1} товар: ')) for i in range(quantity)]

first_year = int(input('Повышение на первый год: '))
second_year = int(input('Повышение на второй год: '))

first_year_prices = [price * (1 + first_year / 100) for price in list_prices]
second_year_prices = [price * (1 + second_year / 100) for price in first_year_prices]
print('Сумма цен за каждый год:', round(sum(list_prices), 2), round(sum(first_year_prices), 2),
      round(sum(second_year_prices), 2))