
result = 0
sl = ""
while result != 1:
    word = input("Введите слово (для остановки введите 'stop'): ")
    if word != 'stop':
        sl = sl + word + " "
    else:
        result += 1
print(sl)