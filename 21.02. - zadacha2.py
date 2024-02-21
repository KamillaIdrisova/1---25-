mesto = int(input('Введите номер своего места'))
if 1 <= mesto <= 36:
    if mesto % 2 == 0:
        print('Верхнее место купе')
    else:
        print('Нижнее место купе')
elif 37 <= mesto <= 54:
    if mesto % 2 == 0:
        print('Боковое верхнее место')
    else:
        print('Боковое нижнее место')
else:
    print('Неправильно введен номер места')