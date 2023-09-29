print('Задача 1. Словарь квадратов чисел')

number = int(input('Введите целое число: '))
square_num_dict = dict()

for num in range(1, number + 1):
    square_num_dict[num] = num ** 2

print(square_num_dict)

print('-' * 20)


print('Задача 2. Студент')

info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ')
info_list = info.split()
info_dict = {'Имя': info_list[0], 'Фамилия': info_list[1], 'Город': info_list[2], 'Место учёбы': info_list[3],
    'Оценки': [int(i) for i in info_list[4:]]}

for i in info_dict:
    print(i, '-', info_dict[i])

print('-' * 20)


print('Задача 3. Контакты')

phone_book = dict()
while True:
    print('\nТекущие контакты на телефоне:')
    if phone_book:
        for name in phone_book:
            print(name, phone_book[name])
    else:
        print('<Пусто>')
    name = input('\nВведите имя: ')
    if name in phone_book:
        print('Ошибка: такое имя уже существует.')
    elif name == '':
        break
    else:
        phone_book[name] = int(input('Введите номер телефона: '))