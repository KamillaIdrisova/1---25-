word = input("Введите слово: ")
sl = 0
for i in word:
    if i == "ф":
        sl = 1
if sl == 1:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")