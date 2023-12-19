print('Задача 1. Кризис миновал')

incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00, 'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.50, 'pear': 1020.00, 'persimmon': 310.00,}

print()
for k1, v1 in incomes.items():
    print(k1, '--', v1)

print('-' * 20)


print('\nЗадача 2. Сервер')

server_data = {"server": {"host": "127.0.0.1", "port": "10"}, "configuration": {"access": "true", "login": "Ivan", "password": "qwerty"}}

for k2, v2 in server_data.items():
    print('\n', k2 + ':')
    for k22, v22 in v2.items():
        print('    ' + k22 + ':', v22)

print('-' * 20)


print('\nЗадача 3. В одну строчку')

print([i_value for i_key, i_value in {0: 0, 1: 100, 2: 144, 3: 20, 4: 19}.items() if i_key % 2 == 0])