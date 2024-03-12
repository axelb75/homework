print('Задача 1. Матрица')

matrix = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]

for list in matrix:
    for num in list:
        print(num, end = ' ')
    print('')

print('-' * 20)


print('Задача 2. Олимпиада')

N = int(input('Кол-во участников: '))
K = int(input('Кол-во человек в команде: '))

if N % K == 0:
    teams = []
    team_num = 0
    for _ in range(N // K):
        team = []
        for _ in range(K):
            team_num += 1
            team.append(team_num)
        teams.append(team)

    print(teams)
    for team in teams:
        print(f'Команда {teams.index(team) + 1}: {team}')

else:
    print(N, 'участников невозможно поделить на команды по', K, 'человек!')

print('-' * 20)


print('Задача 3. Лавка')

goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]

print('Текущий ассортимент:', goods)
print()

fruit = input('Новый фрукт: ')
price = int(input('Цена: '))
goods.append([fruit, price])
print('\nНовый ассортимент:', goods)

for i in goods:
    i[1] = round(i[1] * 1.08, 2)
print('\nНовый ассортимент с увел. ценой:', goods)