from PIL import Image

img = Image.open("image.jpg")
def a1():
    # Область для обрезки (левая верхняя точка (x, y), правая нижняя точка (x, y))
    area = (100, 100, 400, 400)
    sor_img = img.sor(area) '''обрезание изображения'''
    sor_img.save("cropped_image.jpg")
a1()
print("Изображение успешно обрезано и сохранено")


prazdnic = [
    "День рождения": "др.jpg",
    "Новый год": "нг.jpg",
    "8 марта": "женден.jpg",
    "День Святого Валентина": "вален.jpg"
]
def a2():
    hol = input("К какому празднику вам нужна открытка? ")
    try:
        holx = prazdnic[hol]
        print(f"Вот открытка к празднику {hol}:")
    except KeyError:
        print("Открытка к указанному празднику не найдена.")
a2()

def a3(name, text):
    image = Image.open("др2.jpg")

    width, height = image.size
    font = ImageFont.truetype("arial.ttf", 40)'''шрифт загружаем'''
    draw = ImageDraw.Draw(image)'''объект для рисования на изображении'''
    text_width, text_height = draw.textsize(name, font=font)'''добавление текста на открытку'''
    draw.text(((width - text_width) // 2, 30), name, font=font, fill="red")

    text_width, text_height = draw.textsize(text, font=font)
    draw.text(((width - text_width) // 2, height - 60 - text_height), text, font=font, fill="black")

    image.save("pozdravok.png", "PNG")

name = input("Введите имя человека, которого вы хотите поздравить: ")
text = f"{name}, поздравляю!"
create_pozdravok(name, text)