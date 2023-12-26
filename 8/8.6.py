# print('Задача 1. Работа с файлом', sep='\n')
#
# def checking_file(question, error = 'Неверный ввод. Пожалуйста, введите "да" или "нет"', quantity = 3):
#     while quantity:
#         answer = input(question).lower()
#         if  answer == 'да':
#             return 1
#         elif answer == 'нет':
#             return 0
#         else:
#             print(error)
#         quantity -= 1
#         print('Осталось попыток:', quantity)
#
#
# print()
# if checking_file('Вы действительно хотите выйти? ') == 1:
#     print('Выходим из программы')
# else:
#     print('Остаёмся в программе')
#
# print()
# if checking_file('Удалить файл? ', quantity = 4) == 1:
#     print('Файл удалён')
# else:
#     print('Файл сохранён')
#
# print()
# if checking_file('Записать файл? ', 'Не понял. Таки "да" или "нет"') == 1:
#     print('Файл записан')
# else:
#     print('Файл не записан')
#
# print('-' * 20)
#
#
# print('Задача 2. Накопление значений')
#
# def add_num(num, lst = []):
#     lst.append(num)
#     print(lst)
#
#
# add_num(5)
# add_num(10)
# add_num(15)
#
# print('-' * 20)


print('Задача 3. Помощь другу')

def create_dict(data, template=None):
    if isinstance(data, dict):
        return data
    elif isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template = template or dict()
        template[data] = data
        return template
    else:
        return None


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        new_elem = create_dict(i_element)
        if new_elem:
            new_list.append(new_elem)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)