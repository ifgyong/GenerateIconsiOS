#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020-03-12 11:41
# @Author  : fgyong 简书:_兜兜转转_  https://www.jianshu.com/u/6d1254c1d145
# @Site    : http://fgyong.cn 兜兜转转的技术博客
# @File    : create.py
# @Software: PyCharm
from PIL import Image
import os
import sys
import config

savePath = ""

def create():


    im = Image.open(ImageName)
    if len(sys.argv)<3:

        path = outPutPath# 创建文件夹
        if not os.path.exists(outPutPath):
            os.mkdir(outPutPath)
            print( '\033[31m' +"已在桌面创建文件夹AppIcon" + '\033[0m')
    sizes = config.imageSizes
    for i in sizes:
        createSize(i, im, path=path)
        createSize(i * 2, im, path=path)
        createSize(i * 3, im, path=path)
    print('\033[31m' +"✅ AppIcon 图片已生成 🍺🍺🍺🏃" + '\033[0m')
    print('\033[31m' + "✅ 目录为"+path+" 🍺🍺🍺🏃" + '\033[0m')
def createSize(size,im,path):
    im2 = im.resize((size, size))  # 创建缩略图
    im2.save(path+str(size)+ "x"+str(size)+".png")

try:
    from PIL import Image
except:
    print ('\033[31m' + '缺少Image模块，正在安装Image模块，请等待...' + '\033[0m')
    success = os.system('python -m pip install Image')
    if success == 0:
      print('\033[7;32m' + 'Image模块安装成功.' + '\033[0m')
      from PIL import Image
    else:
      print ('\033[31m' + 'Image安装失败，请手动在终端执行：\'python -m pip install Image\'重新安装.' + '\033[0m')
      quit()

outPutPath = os.path.expanduser('~') + '/Desktop/AppIcon/'

# if not os.path.exists(outPutPath):
#     os.mkdir(outPutPath)

if len(sys.argv) <= 1:
    print ('\033[31m' + '请输入图片路径,eg: python autoExportAppIcon.py /path/xxx.png' + '\033[0m')
    quit()

ImageName = sys.argv[1]
# print('图片名字为：' + ImageName)
originImg = ''
try:
    originImg = Image.open(ImageName)
except:
    print ('\033[31m' + '\'' + ImageName + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
    quit()

if __name__ == '__main__':
    # for i in sys.argv:
    #     print(i)
    create()
