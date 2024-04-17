from PIL import Image
'''def a():
    image = Image.open('hello.jpg')
    image.show()
    infa = {
        "формат": image.format,
        "размер": image.size,
        "цветовая модель": image.mode
    }
    print(infa)
a()'''

def b(image):
    image = Image.open('hello.jpg')
    w = int(image.width)//3
    h = int(image.height) // 3
    ima = image.resize(w,h)
    ima.show()
    n = ima.transpose(Image.FLIP_RIGHT_LEFT)
    n.show()
    n.save(C:\\PycharmProjects\\Idrisova-1-md-25-\\photo1.jpg)


