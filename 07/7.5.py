print('Задача 1. Паспортные данные')

data = {(5000, 123456): ('Иванов', 'Василий'), (6000, 111111): ('Иванов', 'Петр'), (7000, 222222): ('Медведев', 'Алексей'), (8000, 333333): ('Алексеев', 'Георгий'), (9000, 444444): ('Георгиева', 'Мария')}
ser = int(input('Введите серию паспорта: '))

for i_pass, i_full_name in data.items():
    if ser in i_pass:
        num = int(input('Введите номер паспорта: '))
        if num in i_pass:
            for i_name in i_full_name:
                print(i_name, end=' ')
            break
else:
    print('Такого паспорта нет')

print()
print('-' * 20)


print('\nЗадача 2. Контакты 2')

phone_book = {}
question = 'д'

while question == 'д':
    surname = input('\nВведите фамилию: ').capitalize()
    name = input('Введите имя: ').capitalize()
    full_name = (surname, name)
    
    if full_name not in phone_book:
        phone_book[full_name] = int(input('Введите телефон: '))
        print(phone_book, '\n', '-' * 20)
    else:
        print('Такой контакт уже существует')

    question = input('\nПродолжить - д/н? ')