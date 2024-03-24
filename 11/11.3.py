print('Задача 1. Машина 2\n')

class Toyota:
    color = 'Красный'
    price = 1000000
    max_speed = 200
    current_speed = 0


    def view_info(self):
        print('Цвет: {}\n'
              'Цена: {}\n'
              'Максимальная скорость: {}\n'
              'Текущая скорость: {}\n'.format
              (self.color, self.price, self.max_speed, self.current_speed) + '-' * 20)


    def set_current_speed(self):
        self.current_speed = int(input('Введите текущую скорость: '))


toyota_1 = Toyota()
toyota_1.color = 'Белый'
toyota_2 = Toyota()
toyota_2.price = 1200000
toyota_3 = Toyota()
toyota_3.max_speed = 240

toyota_1.set_current_speed(), toyota_2.set_current_speed(), toyota_3.set_current_speed()
toyota_1.view_info(), toyota_2.view_info(), toyota_3.view_info()


print('Задача 2. Семья')


class Family:
    name = ''
    money = 0
    house = False

    def view_inf(self):
        print('\nFamily name: {}\nFamily funds: {}\nHaving a house: {}'.
              format(self.name, self.money, self.house))


    def earn_money(self):
        income = int(input('Сколько денег заработал? '))
        self.money += income
        print('Earned {} money! Current value: {}'.format(income, self.money))

    def buy_house(self, price):
        if self.money < price:
            print('Not enough money!\n')
        else:
            self.money -= price
            print('House purchased! Current money: {}'.format(self.money))
            self.house = True


family_1 = Family()
family_1.name = input('Имя: ')
family_1.money = int(input('Деньги: '))
house = str(input('Наличие дома (Да/Нет): ')).lower()
if house == 'да':
    family_1.house = True

family_1.view_inf()

if house != 'да':
    price_house = int(input('\nСтоимость дома: '))
    print('\nTry to buy a house')
    family_1.buy_house(price_house)

while family_1.house == False:
    family_1.earn_money()
    print('\nTry to buy a house again')
    family_1.buy_house(price_house)
