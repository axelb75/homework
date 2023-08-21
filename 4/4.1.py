A = int(input('Левая граница: '))
B = int(input('Правая граница: '))

list_cube = [num ** 3 for num in range(A, B + 1)]
list_squared = [num ** 2 for num in range(A, B + 1)]

print(f'Список кубов чисел в диапазоне от {A} до {B}: {list_cube}')
print(f'Список квадратов чисел в диапазоне от {A} до {B}: {list_squared}')