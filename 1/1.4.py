print('Задание 1. Таблица умножения')

for row in range(1, 11):
    for col in range(1, 11):
        print(col * row, end = '\t')
    print()

print('-' * 20)


print('Задание 2. Калькулятор')

action = input('Действие: ')
while True:
    if action == '+' or action == '-' or action == '/' or action == '*':
        break
    else:
        print('Некорректный формат.')
        action = input('Действие: ')

number_one = int(input('Введите первое число: '))
number_two = int(input('Введите второе число: '))

if action == '+':
    print(number_one, '+', number_two, '=', number_one + number_two)
elif action == '-':
    print(number_one, '-', number_two, '=', number_one - number_two)
elif action == '*':
    print(number_one, '*', number_two, '=', number_one * number_two)
elif action == '/':
    print(number_one, ':', number_two, '=', number_one / number_two)

print('-' * 20)


print('Задание 3. Калькулятор 2')

action = input('Действие: ')
while True:
    if action == '+' or action == '-' or action == '/' or action == '*':
        break
    else:
        print('Некорректный формат.')
        action = input('Действие: ')

volume = int(input('Сколько чисел? '))
count = 1
num = int(input(f'Введите число {count}: '))
result_str = str(num)
result = num

for number in range(2, volume + 1):
    num = int(input(f'Введите число {number}: '))
    if action == '+':
        result += num
    if action == '-':
        result -= num
    if action == '*':
        result *= num
    if action == '/':
        result /= num
    result_str = result_str + (' ' + action + ' ' + str(num))

print(result_str, ' = ', str(result))