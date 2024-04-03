'''num = [87, 2, 23, 4, 0]
pol = int(input('Введите число:'))
if pol in num:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!!")
print ("Список чисел:" , num)'''

'''spis = [2,6,3,0,87,23]
povel = []
for i in range(len(spis)):
    if spis[i] == spis[i] and spis[i] not in povel:
        povel.append(spis[i])
    if povel:
        print("Повторяющиеся элементы в списке:")
        for i in povel:
            print(i)
    else:
        print("Повторяющихся элементов в списке нет.")'''

'''a = int(input('Введите количество элементов в списке'))
n = []
for i in range(a):
    p = input('Введите элемент')
    n.append(p)
r =  [item for item in n if n.count(item) > 1]
if r:
    print(set(r))
else:
    print('Нет повторяющихся элементов')'''


'''ch = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
b = tuple(ch)
c = int(input("Сколько выходных дней вы хотите?"))
if c == 0:
    print(f "Ваши рабочие дни: {b}")
elif c == 1:
    print("Ваши рабочие дни: {b[:6]}")
    print("Ваши выходные дни: {b[6:]}")
elif c == 2:
    print("Ваши рабочие дни: {b[:5]}")
    print("Ваши выходные дни: {b[5:]}")
elif c == 3:
    print("Ваши рабочие дни: {b[:4]}")
    print("Ваши выходные дни: {b[4:]}")'''

'''days = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
weekends = int(input("Сколько выходных на неделе вы хотите? "))

weekendst = days[-weekends:]
print("Ваши выходные дни:", ', '.join(weekendst))

workdaysst = days[:-weekends]
print("Ваши рабочие дни:", ', '.join(workdaysst))'''



'''group1 = ["Ахмадов", "Петров", "Екимова", "Поспелова", "Анисимов", "Зотова", "Токарева", "Зайцев", "Свериденко", "Бречалова"]
group2 = ["Воронков", "Сидоров", "Белкина", "Керган", "Кучинова", "Ковалев", "Белкина", "Федоров", "Горхов", "Уланова"]
team = tuple(group1[:5] + group2[:5])

print("Исходные списки групп:")
print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", team)
print("Длина команды:", len(team))

team = sorted(team)
print("Отсортированный кортеж:")
print(team)

surname = "Иванов"
if surname in team:
    print("Студент", surname, "входит в спортивную команду.")
    print("Количество вхождений фамилии", surname, "в команду:", teams.count(surname))'''


