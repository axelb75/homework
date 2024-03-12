print('Задача 1. Таблица степеней')

#numbers1 = [3, 7, 5]
#while True:
#    number1 = int(input('Новое число: '))
#    numbers1.append(number1)
#    print('Текущий список чисел:', numbers1)
#    for i in numbers1:
#        print(i ** 2, i ** 3, i ** 4)
#    print()

print('-' * 20)


print('\nЗадача 2. Очень простая задача')

# Немного усложнил задачу: теперь диапазон чисел не 100, а задаётся пользователем

#num = int(input('Введите число: '))
#numbers2 = []
#for j in range(num + 1):
#    numbers2.append(j)
#print(numbers2)

print('-' * 20)


print('\nЗадача 3. Контроль')

id_employee = []
number_of_employees = int(input('Кол-во сотрудников в офисе: '))
count = 0
print()

for _ in range(number_of_employees):
    id = int(input('ID сотрудника: '))
    id_employee.append(id)

print()
searh_id = int(input('Какой ID ищем? '))

for i in id_employee:
    if searh_id == i:
        count = 1
        break

print('-' * 20)

if count == 1:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')