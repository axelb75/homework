text = input('Введите строку: ')
symbol = input('Введите дополнительный символ: ')

double_text = [sym * 2 for sym in text]
concatenation = [(sym + symbol) for sym in double_text]

print('Список удвоенных символов:', double_text)
print('Склейка с дополнительным символом:', concatenation)