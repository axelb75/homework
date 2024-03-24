print('Задача 1. Машина')

import random

class Toyota:
    color = 'Красный'
    price = 1000000
    max_speed = 200
    current_speed = 0

toyota_1 = Toyota()
toyota_1.current_speed = random.randint(0, 200)
toyota_1.color = 'Белый'
toyota_2 = Toyota()
toyota_2.current_speed = random.randint(0, 200)
toyota_2.price = 1200000
toyota_3 = Toyota()
toyota_3.current_speed = random.randint(0, 200)
toyota_3.max_speed = 240

print(toyota_1.current_speed, toyota_2.current_speed, toyota_3.current_speed)

print('-' * 20)


print('Задача 2. Однотипные объекты')

class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 0

monitors = [Monitor() for i in range(4)]
monitors[0].freq = 60
monitors[1].freq = 144
monitors[2].freq = 70
monitors[3].freq = 60
print(monitors[0].freq, monitors[1].freq, monitors[2].freq, monitors[3].freq)

class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = True

headphones = [Headphones() for i in range(3)]
headphones[0].micro = False
print(headphones[0].micro, headphones[1].micro, headphones[2].micro)