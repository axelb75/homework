print('Задача 1. Имена')

# sum_sym = 0
# count_str = 0
#
# people_file = open('people.txt', 'r')
# for i_line in people_file:
#     count_str += 1
#     i_line = i_line.rstrip()
#     if len(i_line) < 3:
#         raise ValueError('В {} строке меньше ТРЁХ символов'.format(count_str))
#     sum_sym += len(i_line)
#
# print(sum_sym)
# people_file.close()


print('Задача 2. Логирование')


def is_palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True


try:
    words = open('words.txt', 'r', encoding='utf-8')
    errors = open('errors.log', 'w', encoding='utf-8')
    quality = 0
    word_count = 0
    for word in words:
        word = word.rstrip()
        word_count += 1
        for sym in word:
            if sym.isdigit():
                raise ValueError('В строке {} число'.format(word_count))
        if is_palindrome(word):
            quality += 1
    print('Количество слов, из которых можно получить палиндром:', quality)
    words.close()
    errors.close()
except FileNotFoundError:
    print('Файл отсутствует.')
except ValueError as exc:
    errors.write('ValueError: ')
    errors.write(str(exc))
