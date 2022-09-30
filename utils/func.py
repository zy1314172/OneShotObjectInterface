# _*_ coding : utf-8 _*_
# @Time : 2022/9/28 19:03
# @Author : 浙工大曾友
# @File : func
# @Project : pythonProject

import os

# 获取图片的路径
def get_image_paths(directory):
    img_prefix = ['png', 'jpg', 'jpeg', 'bmp', 'tif', 'gif', 'pcx', 'tga', 'exif', 'fpx', 'svg', 'psd', 'cdr',
                  'pcd', 'dxf', 'ufo', 'eps', 'ai', 'raw', 'wmf', 'webp', 'avif', 'apng']
    return (os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.split('.')[-1].lower() in img_prefix)
