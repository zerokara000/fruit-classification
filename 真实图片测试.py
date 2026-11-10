from PIL import Image
from torchvision import transforms
from torchvision.transforms import ToTensor,Compose,Resize
from 神经网络 import MyNN
import torch
import json
#加载图片
def loadImage(path):
    image=Image.open(path)
    transforms=Compose(
        [
            Resize((100,100)),
            ToTensor()
        ]
    )
    return transforms(image).unsqueeze(0)

#加载模型
def loadModule(path):
    Module=MyNN()
    Module.load_state_dict(torch.load(path))
    return Module

def tool(output,labels):
    index=torch.argmax(output)
    return labels[str(int(index))]
if __name__ =="__main__":
    image=loadImage(r"/Users/davidzero/CLionProjects/水果分类/水果分类/fruits/versions/112/fruits-360_multi/test-multiple_fruits/pear_63.JPG")
    Module=loadModule(r"/Users/davidzero/CLionProjects/水果分类/水果分类/Module.pt")
    output=Module(image)
    #print(output)
    with open(r"/Users/davidzero/CLionProjects/水果分类/水果分类/label.json") as f:
        labels= json.load(f)
    print(labels[str(int(torch.argmax(output)))])