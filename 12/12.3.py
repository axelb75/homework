print('Задача 1. Корабли')

class Ship:
    def __init__(self, model):
        self.__model = model

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def __str__(self):
        return f'Модель корабля: {self.__model}'

    def to_sail(self):
        print(f'Корабль {self.__model} плывёт')


class CargoShip(Ship):
    def __init__(self, model='Грузовой корабль', fullness=0):
        super().__init__(model)
        self.__fullness = fullness

    def set_fullness(self, fullness):
        self.__fullness = fullness

    def get_fullness(self):
        return self.__fullness

    def loading(self, cargo):
        print(f'Загрузка корабля')
        self.__fullness += cargo
        print(f'Текущая загруженность корабля: {self.__fullness}')

    def unloading(self, cargo):
        if self.__fullness > 0:
            print(f'Разгрузка корабля')
            self.__fullness -= cargo
            print(f'Текущая загруженность корабля: {self.__fullness}')
        else:
            print('Корабль уже разгружен.')


class WarShip(Ship):
    def __init__(self, model='Военный корабль', weapon=''):
        super().__init__(model)
        self.__weapon = weapon

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon

    def attack(self):
        print('Военный корабль атакует')


cargo_ship = CargoShip('Сухогруз "OceanShip"', 140)
print(cargo_ship)
cargo_ship.unloading(140)
cargo_ship.unloading(400)
cargo_ship.loading(170)
cargo_ship.to_sail()
print()

war_ship = WarShip('Эсминец 21644', 'Калибр - 4 шт., ТА - 2 шт.')
print(war_ship, '\nВооружение:', war_ship.get_weapon())
war_ship.attack()

print('-' * 20)


print('\nЗадача 2. Роботы')

class Robot():
    def __init__(self, num_model):
        self.__num_model = num_model

    def set_num_model(self, num_model):
        self.__num_model = num_model

    def get_num_model(self):
        return self.__num_model

    def operate(self):
        pass

    def __str__(self):
        return f'\nМодель робота: {self.__num_model}'


class RobotCleaner(Robot):
    def __init__(self, num_model='Робот-пылесос', bag_fullness=0, value=0):
        super().__init__(num_model)
        self.__bag_fullness = bag_fullness
        self.__value = value

    def set_bag_fullness(self, bag_fullness):
        self.__bag_fullness = bag_fullness

    def get_bag_fullness(self):
        return self.__bag_fullness

    def operate(self):
        print(f'Уборка начата.\nЗаполненность мешка для мусора: {self.__bag_fullness}')
        self.__bag_fullness += self.__value
        print(f'Уборка закончена.\nЗаполненность мешка для мусора: {self.__bag_fullness}')


class WarRobot(Robot):
    def __init__(self, num_model='Военный робот', weapon=''):
        super().__init__(num_model)
        self.__weapon = weapon

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def get_weapon(self):
        return self.__weapon

    def operate(self):
        print(f'{self.get_num_model()} выполняет защиту военного '
              f'объекта с помощью оружия: {self.__weapon}')


class RobotSubmarine(WarRobot):
    def __init__(self, num_model='Подводная лодка', weapon='', depth=0):
        super().__init__(num_model, weapon)
        self.__depth = depth

    def set_depth(self, depth):
        self.__depth = depth

    def get_depth(self):
        return self.__depth

    def operate(self):
        print(f'{self.get_num_model()} выполняет защиту военного '
              f'объекта под водой на глубине {self.__depth}м. '
              f'с помощью оружия: {self.get_weapon()}')


roomba = RobotCleaner('Робот-пылесос "Roomba"', 10, 22)
print(roomba)
roomba.operate()

war_robot = WarRobot('Военный робот Стёпа', 'Пукалка, Шмыгалка')
print(war_robot)
war_robot.operate()

submarine = RobotSubmarine('Подводная лодка "Калоша"',
                           'Перделка - 2 шт., Плакалка - 4 шт.', 150)
print(submarine)
submarine.operate()

print('-' * 20)


print('Задача 3. Кастомные исключения')


class DivisionError(Exception):
    pass


with open("numbers.txt", "r", encoding="utf8") as file:
    for line in file:
        try:
            clear_line = line.rstrip()
            first, second = clear_line.split()
            if int(first) < int(second):
                raise DivisionError("нельзя делить большее на меньшее")
            else:
                print(int(first) / int(second))
        except (ValueError, DivisionError) as exc:
            print(exc, ':', first, second)