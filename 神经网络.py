import torch.nn as nn
class MyNN(nn.Module):
    def __init__(self):
        super(MyNN,self).__init__()
        self.Net = nn.Sequential(
            nn.Conv2d(32,64,3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            #第二次卷积
            nn.Conv2d(64,128,3,padding=1),
            # 50*50-->48*48
            nn.ReLU(),
            nn.MaxPool2d(2),
            #24*24
            #第三次卷积
            nn.Conv2d(128,256,3),
            #22*22
            nn.ReLU(),
            nn.MaxPool2d(2),
            #11*11
            nn.AdaptiveAvgPool2d((1,1)),
            nn.Flatten(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,81)
        )

     # 向前传播
    def forward(self, X):
        return self.Net(X)