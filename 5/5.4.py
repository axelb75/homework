print('Задача 1. Шифр Цезаря 2')

text = input("Введите текст: ")
delta = int(input("Введите сдвиг: "))
alphabet = [chr(index) for index in range(ord("а"), ord("я") + 1)]
new_text = [alphabet[(alphabet.index(letter) + delta) % len(alphabet)] if letter in alphabet else letter for letter in text.lower()]
print(''.join(new_text))

print('-' * 20)


print('Задача 2. Путь к файлу')

path = input('Путь к файлу: ')
disk = input('На каком диске должен лежать файл: ')
extension = input('Требуемое расширение файла: ')

if path.startswith(disk) and path.endswith(extension):
    print('Путь корректен!')
else:
    print('Путь некорректный!')

print('-' * 20)


print('Задача 3. Удаление части')

string = input('Введите строку: ')

if sum(i.isupper() for i in string) > sum(i.islower() for i in string):
    print('Результат:', string.upper())
else:
    print('Результат:', string.lower())
