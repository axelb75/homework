print('Задача 1. Зоопарк')

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print('Зоопарк был (изначально): ', zoo)

index = zoo.index('kangaroo')
zoo.insert(index, 'bear')
print('\nЗоопарк был (потом):', zoo, '\nМедведя посадили в клетку номер', index + 1)

zoo.remove('elephant')
print('\nИз зоопарка убрали слона и он стал:', zoo)

print('\nЛев сидит в клетке номер', zoo.index('lion') + 1, '\nОбезьяна сидит в клетке номер', zoo.index('monkey') + 1)

print('-' * 20)


print('Задача 2. Сокращения')

def sort_list_pay(list):
    index = 0
    while index < len(list):
        if list[index] == 0:
            list.remove(list[index])
        else:
            index += 1
    print('\nОсталось сотрудников:', len(list), '\nЗарплаты:', list)


list_pay = []
N = int(input('Кол-во сотрудников: '))
for i in range(N):
    pay = int(input(f'Зарплата {i + 1} сотрудника: '))
    list_pay.append(pay)

sort_list_pay(list_pay)

print('\nМаксимальная зп:', max(list_pay), '\nМинимальная зп:', min(list_pay))

print('-' * 20)


print('Задача 3. Кино')

def is_film_exist(my_film, list_films):
    for i_film in list_films:
        if i_film == my_film:
            return True
    return False


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня',
         'Проклятый остров', 'Начало', 'Матрица']
top_films = []

while True:
    print('\nВаш текущий топ фильмов:', top_films)
    film = input('Название фильма: ')
    if is_film_exist(film, films):
        print('Команды: добавить, вставить, удалить')
        command = input('Введите команду: ')
        if command == 'добавить':
            top_films.append(film)
        elif command == 'вставить':
            if is_film_exist(film, top_films):
                top_films.remove(film)
            index = int(input('На какое место? '))
            top_films.insert(index - 1, film)
        elif command == 'удалить':
            if is_film_exist(film, top_films):
                top_films.remove(film)
            else:
                print('Такого фильма нет в рейтинге.')
    else:
        print('Такого фильма нет на сайте.')


