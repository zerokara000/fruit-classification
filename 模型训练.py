from 数据集类 import MyDataSet
from torch.utils.data import DataLoader
from 神经网络 import MyNN
import torch
#获取设备
device=torch.device("mps"if torch.backends.mps.is_available() else "cpu")
#数据
train_set=MyDataSet(r"/Users/davidzero/CLionProjects/水果分类/水果分类/trainset_lable.json")
test_set=MyDataSet(r"/Users/davidzero/CLionProjects/水果分类/水果分类/testset_lable.json")
#超参
batch_size=64
lr=0.001
epoch=5
#加载数据
train_data=DataLoader(train_set,batch_size=batch_size,shuffle=True)
test_data=DataLoader(test_set,batch_size=batch_size,shuffle=False)
#创建模型
Module=MyNN()
#创建优化器
op=torch.optim.Adam(Module.parameters(),lr)
#创建损失函数
loss_f=torch.nn.CrossEntropyLoss()
#转移模型
Module=Module.to(device)
#模型训练
for i in range(epoch):
    Module.train()
    for j,(images,labels) in enumerate(train_data):
        images = images.to(device)
        labels = labels.to(device)
        # 梯度清零
        op.zero_grad()
        # 向前传播
        outputs = Module(images)
        # 计算损失
        loss = loss_f(outputs, labels)
        # 反向传播
        loss.backward()
        # 更新参数
        op.step()
        print(f"当前训练第{i+1}纪元，第{j + 1}次,当前损失:{loss}")

#测评函数
def evalModule():
    Module.eval()#开启测评模式时，参数不再调整，并且使用最稳定的方式进行计算，准确率会大幅提升。
    cout=0#统计测试了多少次
    true=0#统计正确了多少次
    with torch.no_grad(): #测评不需要计算梯度，节省显存
        for i, (images,labels) in enumerate(test_data):
            images=images.to(device)
            labels=labels.to(device)
            outputs=Module(images)
            for j,output in enumerate(outputs):
                if torch.argmax(output)==labels[j]:
                    true+=1
                cout+=1
    print(f"测试结束，当前测试{cout}次,正确{true}次，正确率{true/cout*100:.2f}%")

#torch.save(Module.state_dict(),"Module.pt")