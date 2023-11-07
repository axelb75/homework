print('Задача 1. Заказ фруктов')

order = {'apple': 2, 'banana': 3, 'pear': 1, 'watermelon': 10, 'chocolate': 5}
incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00, 'bergamot': 3700.56, 'durian': 5987.23,
           'grapefruit': 300.40, 'peach': 10000.50, 'pear': 1020.00, 'persimmon': 310.00}

total_price = 0
for fruit in order:
    price = incomes.get(fruit, 0) * order[fruit]
    total_price += price

print('Итоговая сумма заказа:', total_price)

print('-' * 20)


print('Задача 2. Игроки')

players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

players_a_team = [player['name'] for player in players_dict.values()
                  if player['team'] == 'A' and player['status'] == 'Rest']
players_b_team = [player['name'] for player in players_dict.values()
                  if player['team'] == 'B' and player['status'] == 'Training']
players_c_team = [player['name'] for player in players_dict.values()
                  if player['team'] == 'C' and player['status'] == 'Travel']

print('1. Все члены команды А, которые отдыхают:', ', '.join(players_a_team),
      '\n2. Все члены команды B, которые тренируются:', ', '.join(players_b_team),
      '\n3. Все члены команды c, которые путешествуют:', ', '.join(players_c_team))

print('-' * 20)


print('Задача 2. Игроки')