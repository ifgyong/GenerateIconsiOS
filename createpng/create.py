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
import json


savePath = ""


jsonArr = []
def create():


    im = originImg
    if len(sys.argv)<3:

        path = outPutPath# 创建文件夹
        if not os.path.exists(outPutPath):
            os.mkdir(outPutPath)
            print( '\033[31m' +"已在桌面创建文件夹AppIcon" + '\033[0m')
    sizes = config.imageSizes
    for i in sizes:
        createSize(i, im, path=path,times=1)
        appJson(i,times=1)
    for i in config.imageSizesDouble:
        createSize(i, im, path=path,times=2)
        appJson(i, times=2)
    for i in config.imageSizesThree:
        createSize(i, im, path=path,times=3)
        appJson(i, times=3)
    print('\033[31m' +"✅ AppIcon 图片已生成 🍺🍺🍺🏃" + '\033[0m')
    print('\033[31m' + "✅ 目录为"+path+" 🍺🍺🍺🏃" + '\033[0m')

    lastDic = dict()
    lastDic["images"]=jsonArr
    lastDic["info"]= {"version":1,
                      "athor":"xcode"}
    createjosn(path,lastDic)


def createjosn(path,js):
    allpath = path+"Contents.json"
    # if os._exists(allpath):
    os.remove(allpath)#删除旧文件
    f = open(path+"Contents.json",'a')
    if f.write(json.dumps(js))>0:
        print('\033[31m' + "✅ json文件写入成功 🍺🍺🍺🏃" + '\033[0m')
#     追加json 数据
def appJson(i,times):
    for index in range(2,len(i)):
        dic = dict()
        dic["size"] = str(i[0]) + "x" + str(i[1])
        dic["filename"] = name(i, times=times)
        dic["scale"] = str(times) + "x"
        dic["idiom"] = i[index]
        jsonArr.append(dic)

def createSize(size,im,path,times):
    im2 = im.resize((int(size[0] * times), int(size[1] * times)))  # 创建缩略图
    im2.save(path+name(size,times))
def name(size,times):
    if times == 1:
        return "APPIcon"+str(size[0]) +"X" +str(size[1])+".png"
    else:
        return "APPIcon"+str(size[0]) +"X" +str(size[1])+"@"+str(times)+".png"

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

# if len(sys.argv) <= 1:
#     print ('\033[31m' + '请输入图片路径,eg: python autoExportAppIcon.py /path/xxx.png' + '\033[0m')
#     quit()
#
# ImageName = sys.argv[1]
# # print('图片名字为：' + ImageName)
originImg = Image.open('/Users/Jerry/Desktop/复软/BI系统元素/icons/logo@2x.png')
# try:
#     originImg = Image.open(ImageName)
# except:
#     print ('\033[31m' + '\'' + ImageName + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
#     quit()


if __name__ == '__main__':
    # for i in sys.argv:
    #     print(i)
    create()
