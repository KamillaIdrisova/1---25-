'''countries = {
    "США": "Вашингтон",
    "Франция": "Париж",
    "Германия": "Берлин",
    "Япония": "Токио",
    "Россия": "Москва"
}
for country, capital in countries.items():
    print(country, "-", capital)

country = "Франция"
print(countries[country])

por = list(countries.keys())
por.sort()
for v in por:
    print(v, '-' , countries[v])'''




'''word = input("Введите слово: ")
b = 0
sl_values = {
    'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
    'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2,
    'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3,
    'й': 4, 'ы': 4,
    'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5,
    'ш': 8, 'э': 8, 'ю': 8,
    'ф': 10, 'щ': 10, 'ъ': 10
}
for slov in word:
    b += sl_values.get(slov.lower(), 0)
print("Стоимость слова:", b)'''


