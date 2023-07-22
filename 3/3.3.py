print('Задача 1. Задачи компаний')

main = [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1]
first_company = [0, 0, 1]
second_company = [1, 0, 1, 1, 1]
third_company = [1, 1, 0, 0, 1]

main.extend(first_company)
main.extend(second_company)
main.extend(third_company)

print('Общий список задач:', main,
      '\nКол-во невыполненных задач:', main.count(0))

print('-' * 20)


print('Задача 2. Вредоносное ПО')

first_message = input('Первое сообщение: ')
second_message = input('Второе сообщение: ')

first_count = first_message.count('!') + first_message.count('?')
second_count = second_message.count('!') + second_message.count('?')

if first_count > second_count:
    print('\nТретье сообщение:', first_message, second_message)
elif first_count < second_count:
    print('\nТретье сообщение:', second_message, first_message)
else:
    print('\nТретье сообщение: Ой!')

print('-' * 20)


print('Задача 3. Пакеты')

message = []
bad_pack = 0

N = int(input('Кол-во пакетов: '))
for i_pack in range(N):
    pack = []
    print('\nПакет номер ', i_pack + 1)
    for i_bit in range(4):
        bit = int(input(f'{i_bit + 1} бит: '))
        while True:
            if bit == 0 or bit == 1 or bit == -1:
                pack.append(bit)
                break
            else:
                bit = int(input(f'Ошибка. Повторите ввод.\n{i_bit + 1} бит: '))

    if pack.count(-1) <= 1:
        message.extend(pack)
    else:
        bad_pack += 1
    pack = []

print('\nПолученное сообщение:', message,
      '\nКол-во ошибок в сообщении:', message.count(-1),
      '\nКол-во потерянных пакетов:', bad_pack)