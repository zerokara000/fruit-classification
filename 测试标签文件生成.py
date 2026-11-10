import json
import os
import re


dir =os.scandir(r"/Users/davidzero/CLionProjects/水果分类/水果分类/fruits/versions/112/fruits-360_100x100/fruits-360/Test")
labels={}
index=0
for i in dir:
    if i.is_dir():
        name=re.match(r'^\s*([A-Za-z]+)', i.name)
        for j in os.scandir(i):
            labels[index]={
                "image":j.path,
                "labels":name.group(1).lower()
            }
            index+=1
print(labels)
with open("testset_lable.json","w") as f:
    json.dump(labels,f)
