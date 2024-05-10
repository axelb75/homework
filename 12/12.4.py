# print('Задача 1. Юниты')
#
#
# class Unit:
#     def __init__(self, name='', health=90):
#         self.__health = health
#         self.__name = name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def set_health(self, health):
#         self.__health = health
#
#     def get_health(self):
#         return self.__health
#
#     def take_damage(self, damage):
#         self.set_health(self.get_health() - 0)
#
#     def __str__(self):
#         return f'Unit {self.__name} имеет здоровье {self.__health}'
#
#
# class Warrior(Unit):
#     def take_damage(self, damage):
#         self.set_health(self.get_health() - damage)
#
#
# class Citizen(Unit):
#     def take_damage(self, damage):
#         self.set_health(self.get_health() - damage * 2)
#
#
# unit = Unit('Bob')
# print(unit)
# unit.take_damage(30)
# print(f'После нанесённого урона его здоровье стало {unit.get_health()}\n')
#
# warrior = Warrior('Солдат', 100)
# print(warrior)
# warrior.take_damage(damage=20)
# print(f'После нанесённого урона его здоровье стало {warrior.get_health()}\n')
#
# citizen = Citizen('Гражданин', 70)
# print(citizen)
# citizen.take_damage(damage=10)
# print(f'После нанесённого урона его здоровье стало {citizen.get_health()}')
#
# print('-' * 20)
# print()


print('Задача 2. Полёт')


class Can_fly:
    def __init__(self, name, height=0.00, speed=0.00):
        self.__name = name
        self.__height = height
        self.__speed = speed

    def set_height(self, height):
        self.__height = height

    def set_speed(self, speed):
        self.__speed = speed

    def get_height(self):
        return self.__height

    def get_speed(self):
        return self.__speed

    def fly_up(self):
        pass

    def fly(self):
        print(f'Летит.\nВысота: {self.__height}\tСкорость: {self.__speed}')

    def land(self):
        self.__height = 0
        self.__speed = 0
        print(f'Приземлилась.\nВысота: {self.__height}\tСкорость: {self.__speed}')

    def __str__(self):
        return f'{self.__name}:'


class Butterfly(Can_fly):
    def fly_up(self):
        self.set_height(self.get_height())
        print(f'Взлетела на высоту {self.get_height()} м.')

    def fly(self):
        self.set_speed(self.get_speed())
        print(f'Летит со скоростью {self.get_speed()} м/с.')


class Rocket(Can_fly):
    def fly_up(self):
        self.set_height(self.get_height())
        self.set_speed(self.get_speed())
        print(f'Взлетела на высоту {self.get_height()} м. '
              f'со скоростью {self.get_speed()} м/с.')

    def land(self):
        super().land()
        print('Ракета взорвалась')

    def detonate(self):
        print('Ракета взорвалась.')


fly = Butterfly(name='Бабочка', height=1, speed=0.5)
print(fly)
fly.fly_up()
fly.fly()
fly.land()

print()

rocket = Rocket(name='Ракета', height=500, speed=1000)
print(rocket)
rocket.fly_up()
rocket.land()
rocket.detonate()
