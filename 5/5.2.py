print('Задача 1. Заказ')

name = input('Имя: ')
number = int(input('Номер заказа: '))

message = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(name, number)
print(message)

message1 = 'Здравствуйте, {name_user}! Ваш номер заказа: {number_user}. Приятного дня!'.format(
    name_user = name,
    number_user = number)
print(message1)

print('Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'.format(name, number))
print('Здравствуйте, {name_user}! Ваш номер заказа: {number_user}. '
      'Приятного дня!'.format(name_user = name, number_user = number))

print('-' * 20)


print('Задача 2. Долги')

name_2 = input('Введите имя: ')
money = int(input('Введите долг: '))

print('{0}! {0}, привет! Как дела, {0}? Где мои {1} рублей? {0}! {1} рублей, да?'.format(name_2, money))

print('-' * 20)


print('Задача 3. IP-адрес')

ip = []
ip_address = 'IP-адрес: {0}.{1}.{2}.{3}'

for i in range(4):
    while True:
        num = int(input(f'{i + 1} число: '))
        if 0 <= num <= 255:
            ip.append(num)
            break
        print('Ошибка. Число должно быть в диапазоне от 0 до 255.')


print(ip_address.format(ip[0], ip[1], ip[2], ip[3]))