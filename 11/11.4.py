# print('Задача 1. Машина 3')
#
# class Toyota:
#     def __init__(self, color='Red', price=1000, max_speed=200, current_speed=0):
#         self.color = color
#         self.price = price
#         self.max_speed = max_speed
#         self.current_speed = current_speed
#
#     def view_info(self):
#         print('Цвет: {}\n'
#               'Цена: {}\n'
#               'Максимальная скорость: {}\n'
#               'Текущая скорость: {}'.
#               format(self.color, self.price, self.max_speed, self.current_speed))
#         print('-' * 20)
#
#
#     def set_current_speed(self, new_speed):
#         self.current_speed = new_speed
#
#
# car_1 = Toyota()
# car_1.set_current_speed(180)
# car_1.view_info()
# car_2 = Toyota()
# car_2.set_current_speed(140)
# car_2.view_info()
#
# print('-' * 20)


print('Задача 2. Координаты точки')


# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def info(self):
#         print('Координаты точки: х = {}, y = {}'.format(self.x, self.y))
#         print('Всего создано точек:', self.count)
#
#
# while True:
#     menu = int(input('1 - Создать новую точку или 2 - выйти из программы?\nВыбери нужную цифру: '))
#     if menu == 1:
#         print('Введи координаты')
#         x = int(input('X: '))
#         y = int(input('Y: '))
#         new_point = Point(x, y)
#         new_point.info()
#
#     elif menu == 2:
#         break
#     else:
#         print('Некорректные данные, повторите ввод.')
#
#
# print('-' * 20)


print('Задача 3. Весёлая ферма')

class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class Garden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка растёт')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('Картошка ещё не созрела')
                break
            else:
                print('Картошка созрела. Можно собирать.')
                break


my_garden = Garden(5)
for i in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()