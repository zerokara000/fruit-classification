import json
from PIL import Image
from torch.utils.data import DataLoader,Dataset
from torchvision.transforms import ToTensor,Compose,Resize



class MyDataSet(Dataset):
    #transform:将图片转化为张量的工具
    #target_transform:将字符串转化为标签的工具
    def __init__(self,file,transform=None,target_transform=None):
        #加载文件
        with open(file,"r")as f:
            self.labels=json.load(f)
            #设置变量（成员）
        if transform == None:  # 判断是否有工具可用，
            self.transform = self.build_transform()  # 使用工具将图片转换为张量
        else:
            self.transform=transform
        self.target_transform=target_transform
        with open("str_to_number.json", "r") as f:
                self.str_number = json.load(f)

    def __len__(self):
        return len(self.labels)
    def __getitem__(self, item):
        item=str(item)#转换为字符串类型
        path=self.labels[item]["image"]#获取图片地址
        label=self.labels[item]["labels"]#获取图片标签
        image=Image.open(path)#加载图片
        image=self.transform(image)
        label = label.lower()
        if self.target_transform==None:
            label=self.build_target_transform(label)
        else:
            label=self.target_transform(label)
        return image,label
    def build_target_transform(self,str):
        return self.str_number[str]
    def build_transform(self):
        transform = Compose( #依次调用下面的工具
            [
                Resize((100,100)),
                ToTensor()
            ]
        )
        return transform
a=MyDataSet(file=r"/Users/davidzero/CLionProjects/水果分类/水果分类/trainset_lable.json")
image,lable= a.__getitem__(20)
print(image,lable)

