print('Задача 1. Текстовый редактор: Возвращение')

#text_string = input('Введите строку: ')
#text_list = list(text_string)
#old_sym = input('Введите заменяемый символ: ')
#new_sym = input('Введите заменяющий символ: ')

#i = 0
#count = 0
#for sym in text_list:

#    if sym == old_sym:
#        text_list[i] = new_sym
#        sym = new_sym
#        count += 1
#    i += 1

#print('Исправленная строка:', end = ' ')
#for sym in text_list:
#    print(sym, end = '')
#print('\nКол-во замен:', count)

print('-' * 20)


print('Задача 2. Соседи')

#string_S = input('Введите строку: ')
#list_S = list(string_S)
#num_sym = int(input('Введите номер символа: '))

#sym = list_S[num_sym - 1]
#previous_sym = list_S[num_sym - 2]
#next_sym = list_S[num_sym]

#print('\nСимвол слева:', previous_sym, '\nСимвол справа:', next_sym)

#if sym == previous_sym and sym == next_sym:
#    print('Есть два таких-же символа')
#elif sym == previous_sym or sym == next_sym:
#    print('Есть ровно один такой-же символ')
#else:
#    print('Таких-же символов нет')


print('-' * 20)


print('Задача 3. Улучшенная лингвистика')

counts =[0, 0, 0]
search_words = []
N = int(input('Сколько слов? '))
for i in range(N):
    search_word = input(f'Введите {i + 1} слово: ')
    search_words.append(search_word)

text_word = input('Слово из текста: ')
while text_word != 'end':
    for index in range(N):
        if search_words[index] == text_word:
            counts[index] += 1
    text_word = input('Слово из текста: ')

print('\nПодсчёт слов в тексте')
for i in range(3):
    print(search_words[i], ':', counts[i])