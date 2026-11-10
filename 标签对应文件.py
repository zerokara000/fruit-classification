import os
import re
import json

dir = os.scandir(r"/Users/davidzero/CLionProjects/水果分类/水果分类/fruits/versions/112/fruits-360_100x100/fruits-360/Training")
str_to_number={}
index=0
#用来记录已经保存过的类别
already_save = []

for i in dir:
    if i.is_dir():
        #提取文件夹名称中部分作为分类标签
        #使用正则表达式提取
        name=re.match(r'^\s*([A-Za-z]+)', i.name)
        if name is None:
            continue
        cls_name = name.group(1)
        cls_name = cls_name.lower()

        if cls_name not in already_save:
            str_to_number[cls_name]=index
            already_save.append(cls_name)
            index+=1

with open("str_to_number.json", "w") as f:
    json.dump(str_to_number,f)
