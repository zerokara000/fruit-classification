import json
import os
import re
#搜索文件夹
dir =os.scandir(r"/Users/davidzero/CLionProjects/水果分类/水果分类/fruits/versions/112/fruits-360_100x100/fruits-360/Training")
labels={}
index=0
#遍历fruits-360/Training文件夹
for i in dir:
    #判断i是否为文件夹
    if i.is_dir():
        #提取文件夹名称中部分作为分类标签
        #使用正则表达式提取（表达式可问AI）
        name=re.match(r'^\s*([A-Za-z]+)', i.name)
        #搜索Almonds 1文件夹，拿到具体的图片
        for j in os.scandir(i):
            #制作图片标签，并添加到标签字典中
            labels[index]={
                "image":j.path,#图片地址
                "labels":name.group(1).lower()#图片属于的分类
            }
            index+=1
print(labels)
#保存文件
with open("trainset_lable.json","w") as f:
    json.dump(labels,f)
