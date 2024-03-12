print('Задача 1. Challenge')

def calc_fact(num):
    if num == 1:
        return 1
    return num * calc_fact(num - 1)


number = int(input('Введите число: '))

print('Факториал:', calc_fact(number))

print('-' * 20)


print('\nЗадача 2. Степень числа')

def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

 
float_num = float(input('Введите вещественное число: '))

int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))

print('-' * 20)


print('\nЗадача 3. Поиск элемента')

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_val(str, key):
    if key in str:
        return str[key]

    for sub_str in str.values():
        if isinstance(sub_str, dict):
            result = find_val(sub_str, key)
            if result:
                break
    else:
        result = None

    return result


user_key = input('Искомый ключ: ')
val = find_val(site, user_key)
if val:
    print(val)
else:
    print('Такого ключа в структуре сайта нет.')