print('Задача 1. Улучшенная лингвистика 2')

list_word = [input(f'Введите {i + 1} слово: ') for i in range(3)]
text = input('Введите текст: ')
words_count = [text.count(word) for word in list_word]
print(words_count)

print('-' * 20)


print('Задача 2. Бабушка')

incorrect_text = (input('Введите текст: '))
correct_text = ' '.join(incorrect_text.split())
print(correct_text)

print('-' * 20)


print('Задача 3. Разделители символов')

while True:
    congratulation_message = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')
    if '{name}' in congratulation_message and '{age}' in congratulation_message:
        break
    print('В поздравлении отсутствует одна из конструкций.')

name_list = input('Список людей через запятую: ').split(', ')
age_list = input('Возраст людей через пробел: ').split()

for i_man in range(len(name_list)):
    print(congratulation_message.format(name=name_list[i_man], age=age_list[i_man]))

birthday_man = [' '.join([name_list[i_man], str(age_list[i_man])]) for i_man in range(len(name_list))]
birthday_man_str = ', '.join(birthday_man)

print('Именинники:', birthday_man_str)

