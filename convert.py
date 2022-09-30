import os
import PIL

from multiprocessing import Pool
from PIL import Image
import time

SIZE = (75, 75)
SAVE_DIRECTORY = 'thumbs'


def get_image_paths(folder):
    img_prefix = ['png', 'jpg', 'jpeg', 'bmp', 'tif', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd', 'cdr',
                  'pcd', 'dxf', 'ufo', 'eps', 'ai', 'raw', 'wmf', 'webp', 'avif', 'apng']

    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.split('.')[-1].lower() in img_prefix)


def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)


# if __name__ == '__main__':
#     folder = os.path.abspath(
#         r'F:\DeepLearning\datasets\11111')
#     os.mkdir(os.path.join(folder, SAVE_DIRECTORY))
#
#     images = get_image_paths(folder)
#
#     t1 = time.time()
#     for image in images:
#         create_thumbnail(Image)
#     print(time.time() - t1)

if __name__ == '__main__':
    folder = os.path.abspath(
        r'F:\DeepLearning\datasets\11111')
    os.mkdir(os.path.join(folder, SAVE_DIRECTORY))

    images = get_image_paths(folder)
    print(list(images))
    for i in images:
        print(i)
    t = time.time()
    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()
    print(time.time() - t)
