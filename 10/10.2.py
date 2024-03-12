print('Задача 1. Пятый элемент')

BRUCE_WILLIS = 42
input_data = input('Введите строку: ')

try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except ValueError:
    print('невозможно преобразовать к числу')
except IndexError:
    print('выход за границы списка')
except Exception:
    print('остальные исключения')

print('-' * 20)


print('Задача 2. Возраст')
ages_file = None
result_file = None
try:
    ages_file = open('Ages.txt', 'r', encoding='utf-8')
    result_file = open('result.txt', 'x', encoding='utf-8')
except (FileExistsError, IsADirectoryError):
    print('Поймано исключение файла')

if ages_file and result_file:
    count = 0
    try:
        for age in ages_file:
            int(age)
            result_file.write((chr(ord('a') + count)) + ': ' + age)
            count += 1
    except (TypeError, ValueError):
        print('Поймано исключение данных')

    ages_file.close()
    result_file.close()