print('Задача 1. Гугл')

#nums_list = []
#N = int(input('Кол-во чисел в списке: '))

#for _ in range(N):
#    num = int(input('Очередное число: '))
#    nums_list.append(num)

#maximum = num
#minimum = num

#for i in nums_list:
#    if maximum < i:
#        maximum = i
#    if minimum > i:
#        minimum = i

#print('Максимальное число в списке:', maximum)
#print('Минимальное число в списке:', minimum)

print('-' * 20)


print('Задача 2. Кратность')

#number_list = []
#N = int(input('Кол-во чисел в списке: '))

#for n in range(N):
#    number = int(input(f'Введите {n + 1} число: '))
#    number_list.append(number)
#print()

#divisor = int(input('Введите делитель: '))
#print('-' * 20)

#index = 0
#sum_index = 0

#for i in number_list:
#    if i % divisor == 0:
#        print(f'Индекс числа {i}:', index)
#        sum_index += index
#    index += 1

#print('\nСумма индексов:', sum_index)

print('-' * 20)


print('Задача 3. Собачьи бега')

dogs_score = []
dogs_quantity = int(input('Количество собак: '))

for k in range(dogs_quantity):
    score = int(input(f'Очки {k + 1} собаки: '))
    dogs_score.append(score)

if dogs_score:
    max_index = 0
    min_index = 0
    score_max = dogs_score[0]
    score_min = dogs_score[0]

    for index, i in enumerate(dogs_score):
        if score_max < i:
            score_max = i
            max_index = index
        if score_min > i:
            score_min = i
            min_index = index

    print('Максимальные очки в списке:', score_max)
    print('Минимальные очки в списке:', score_min)
    print(dogs_score)

    dogs_score[min_index], dogs_score[max_index] = dogs_score[max_index], dogs_score[min_index]
    print(dogs_score)

else:
    print('Ошибка!!!')

