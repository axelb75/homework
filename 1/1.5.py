print('Введите первую точку:')
x1 = float(input('X: '))
y1 = float(input('Y: '))

print('Введите вторую точку:')
x2 = float(input('X: '))
y2 = float(input('Y: '))

print('Уравнение прямой, проходящей через эти точки:')

x_diff = x1 - x2
y_diff = y1 - y2

if x_diff == 0:
    print('x =', x1)
elif y_diff == 0:
    print('y = ', y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print('y = ', k, ' * x + ', b)