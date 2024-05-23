# number1
from PIL import Image
import os

soufil = 'Учебные файлы/АИП/пр9'
tarfil = 'Учебные файлы/АИП/пр9'

if not os.path.exists(tarfil):
    os.makedirs(tarfil)

# Функция обрабатывания изображения
def process(image):
    image = Image.open(image)
    image = image.convert('RGB')
    image = image.point(lambda x: 255 - x)
    images = os.path.join(tarfil, os.path.basename(image))
    image.save(images)

# Обход всех файлов в исходной папке
for image in os.listdir(soufil):
    if image.endswith('.jpg') or image.endswith('.png'):
        file_path = os.path.join(soufil, image)
        process(file_path)


# number3
import csv
total_sum = 0
with open('zadanieaip.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader, None)
    print("Нужно купить:")
    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = float(row[2])
        total_sum += quantity * price
        print(f"{product} - {quantity} шт. за {price} руб.")

print(f"Итоговая сумма: {total_sum} руб.")

