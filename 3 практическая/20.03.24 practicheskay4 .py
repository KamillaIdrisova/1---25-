def n(chislo):
    if chislo % 5 == 0:
        return True
    else:
        return False
chislo = int(input('Введите число: '))
if n(chislo) == True:
    print ('делится на 5')
else:
    print('не делится на 5')


def n(chislo):
    try:
        otv = 300 / chislo
        return otv
    except ValueError:
        print ('Ошибка, вы ввели не число!')
    except ZeroDivisionError:
        print ('Невозможно поделить на 0!')
chislo = int(input('Введите число: '))
res = n(chislo)
print('Ответ', res)


def mag(d, m, y):
    if d*m == int(str(y)[-2:]):
        print ("Дата магическая")
    else:
        print ("Дата немагическая")
d = int(input("Введите дату: "))
m = int(input("Введите месяц: "))
y = int(input("Введите год: "))
print (mag(d, m, y))


def n(chislo):
    if (chislo) % 2 != 0:
        return False
    pol = (chislo) // 2
    onepol = chislo[:pol]
    twopol = chislo[pol:]
    return sum(map(int, onepol)) == sum(map(int, twopol))
chislo = int(input('Введите номер билета:'))
if n(chislo) == False:
    print('У вас счастливый билет!')
else:
    print('У вас ужасный билет((')
