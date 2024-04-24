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

'''def b():
    image = Image.open('hello.jpg')
    image.show()
    izm = image.reduce(3)
    izm.save('hello2.jpg')
    izm.show()
b()'''

'''def c():
    image = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for i in image:
        imag = Image.open(i)
        imag2 = Image.fillter(Image.SHARPEN)
        imag2.save('fillter.png' + str(i))
c()'''

'''def d():
    images = 'images.jpg'
    watermark = dd.imread('watermark.png', dd.IMREAD_UNCHANGED)
    # Устанавливаем положение водяного знака
    position_x = image_width - watermark_width - 10
    position_y = image_height - watermark_height - 10

    # Добавляем водяной знак на изображение
    for c in range(0, 3):
        image[position_y:position_y + watermark_height, position_x:position_x + watermark_width, c] = watermark[:, :,c] * (watermark[:,:,3] / 255.0) + image[position_y:position_y + watermark_height,position_x:position_x + watermark_width,c] * (1.0 - watermark[:,:,3] / 255.0)

    # Сохраняем изображение с водяным знаком
    dd.imwrite('image_with_watermark.jpg', image)'''