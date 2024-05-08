print('Задача 1. Координаты точки')


class Point:
    def __init__(self, x=0, y=0):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        if self.check_value(x):
            self.__x = x

    def set_y(self, y):
        if self.check_value(y):
            self.__y = y

    def get_x(self, x):
        return self.__x

    def get_y(self, y):
        return self.__y

    def check_value(self, value):
        if isinstance(value, (int, float)):
            return True
        else:
            raise ValueError('Координаты должна быть числом')

    def __str__(self):
        return f'Координаты точки:\tx = {self.__x}\n\t\t\t\t\ty = {self.__y}'


point_1 = Point(14, -17)
print(point_1)

print('-' * 20)


print('Задача 2. Человек')


class Human:
    __count = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            raise ValueError('Имя должно состоять только из букв')

    def set_age(self, age):
        if isinstance(age, (int, float)) and 0 <= age <= 100:
            self.__age = age
        else:
            raise ValueError('Возраст должен быть в интервале от 0 до 100')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__count

    def __str__(self):
        return f'Имя: {self.__name}\nВозраст: {self.__age}'


misha = Human('Михаил', 47)
vera = Human('Вера', 24)
ivan = Human('Иван', 36)
text = ''
if 1 < misha.get_count() < 5:
    text = 'человека'
else:
    text = 'человек'
print(f'Всего {misha.get_count()} {text}:')
print(misha)
misha.set_age(99)
print(misha)
misha._Human__age = 77
print(misha)
print(vera)
print(ivan)
