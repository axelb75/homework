print('Задача 1. Простая программа')

user_file = None
try:
    user_file = open('10.3.txt', 'a', encoding='utf-8')
except (FileExistsError, FileNotFoundError):
    print('Проблема при открытии файла')

try:
    user_string = int(input('Введите число: '))
    user_string = str(user_string) + '\n'
    user_file.write(user_string)
except (ValueError):
    print('Нельзя преобразовать данные в целое')
except Exception:
    print('Неожиданная ошибка')
else:
    print('Запись прошла без ошибок')
finally:
    user_file.close()


print('Задача 2. Старая задача')


def main():
    input_file = None
    output_file = None
    try:
        input_file = open('numbers.txt', 'r', encoding='utf8')
        output_file = open('answer.txt', 'w')
    except FileNotFoundError:
        print('Такого файла не существует')
    else:
        number_list = input_file.read().split()
        output_file.write(str(calc_sum(number_list)))

    try:
        input_file.close()
        output_file.close()
    except AttributeError:
        print('Невозможно закрыть несуществующий файл')


def calc_sum(num_list):
    summa = 0
    for num in num_list:
        summa += int(num)
    return summa


main()