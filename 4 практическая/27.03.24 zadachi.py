'''num = [87, 2, 23, 4, 0]
pol = int(input('Введите число:'))
if pol in num:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!!")
print ("Список чисел:" , num)'''



def a():
    ch = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    b = tuple(ch)
    c = int(input("Сколько выходных дней вы хотите?"))
    if c == 0:
        print("Ваши рабочие дни: {b}")
    elif c == 1:
        print("Ваши рабочие дни: {b[:6]}")
        print("Ваши выходные дни: {b[6:]}")
    elif c == 2:
        print("Ваши рабочие дни: {b[:5]}")
        print("Ваши выходные дни: {b[5:]}")
    elif c == 3:
        print("Ваши рабочие дни: {b[:4]}")
        print("Ваши выходные дни: {b[4:]}")