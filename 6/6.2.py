print('Задача 1. Склады')

small_storage = {'гвозди': 5000, 'шурупы': 3040, 'саморезы': 2000}
big_storage = {'доски': 1000, 'балки': 150, 'рейки': 600}

big_storage.update(small_storage)
article = input('Название товара: ')
if big_storage.get(article):
    print(big_storage.get(article))
else:
    print("Такого товара нет!")

print('-' * 20)


print('Задача 2. Кризис фруктов')

incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00, 'bergamot': 3700.56, 'durian': 5987.23,
           'grapefruit': 300.40, 'peach': 10000.50, 'pear': 1020.00, 'persimmon': 310.00}

print('\nОбщий доход за год составил',sum(incomes.values()) , 'рублей')
keys = list(incomes.keys())
index = list(incomes.values()).index(min(incomes.values()))
fruit = keys[index]
print(f'Самый маленький доход у {fruit}. Он составляет {min(incomes.values())} рублей')
incomes.pop(fruit)
print('Итоговый словарь:', incomes)

print('-' * 20)


print('Задача 3. Гистограмма частоты')

text = input('Введите текст: ').lower()
sym_dict = dict()
for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

for i_sym in sorted(sym_dict.keys()):
    print(i_sym, ':', sym_dict[i_sym])

print('Максимальная частота:', max(sym_dict.values()))