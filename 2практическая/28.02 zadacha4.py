import random

otv = 0
r = 0

while r != 3:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    chel =int(input(f"{num1} + {num2} = "))
    if chel == num1 + num2:
        print("Правильно!")
        otv += 1
    else:
        print("Ответ неверный")
        r += 1

print(f"Игра окончена. Правильных ответов:", otv)