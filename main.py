import os
from PIL import Image, ImageOps

def quant_col(len_list_imgs):
    if len_list_imgs > 8:
        if not len_list_imgs % 3:
            return int(len_list_imgs / 3)
        elif not len_list_imgs % 4:
            return int(len_list_imgs / 4)
        elif not len_list_imgs % 5:
            return int(len_list_imgs / 5)
        else:
            print("Не могу создать сетку по количеству фотографий")
    elif len_list_imgs > 1 and len_list_imgs <= 8:
        if not len_list_imgs % 2:
            return int(len_list_imgs / 2)
        else:
            print("Не могу создать сетку по количеству фотографий")
    else:
        print("Возможно папка пустая")


def paste_img(images, path):
    # получаем количество столбцов
    quant = quant_col(len(images))
    if not quant:
        print(path)
        return 0

    # получаем размеры картинок
    img_size = images[0].size

    # рамка для картинок на постере
    border_top = 200
    border_left = 150

    new_img_size = (img_size[0] * quant + border_top * quant,
                    img_size[1] * int(len(images) / quant) + border_top * int(len(images) / quant + 1))

    # создаем фоновое изображение размером
    img = Image.new('RGB', new_img_size, '#ffffff')

    # вставляем картинки в фоновое изображение
    # отступ у первой картинки (0, 0)
    x, y, = 0, 0

    while images:
        for line in range(quant):
            img.paste(images[0], (x + border_left, y + border_top))
            images.pop(0)
            x += img_size[0] + border_left
        y += img_size[1] + border_top
        x = 0

    # в конце создадим белую рамку вокруг постера на 20px толще
    img = ImageOps.expand(img, border=20, fill='#ffffff')
    # сохраняем новое изображение
    img.save(path + '\\' + 'Result.tiff', 'TIFF')



if __name__ == '__main__':
    path = "X:\\фото\\Для тестового\\"
    images = []

    for folder in os.listdir(path):
        for img in os.listdir(path + folder):
            abs_path = os.path.abspath(path + folder + '\\' + img)
            images.append(Image.open(abs_path))

        paste_img(images, os.path.abspath(path + folder))
