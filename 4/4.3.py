quantity = int(input('Кол-во товаров: '))
list_prices = [float(input(f'Цена на {i + 1} товар: ')) for i in range(quantity)]

first_year = int(input('Повышение на первый год: '))
second_year = int(input('Повышение на второй год: '))

first_year_prices = [price * (1 + first_year / 100) for price in list_prices]
second_year_prices = [price * (1 + second_year / 100) for price in first_year_prices]
print('Сумма цен за каждый год:', round(sum(list_prices), 2), round(sum(first_year_prices), 2),
      round(sum(second_year_prices), 2))
