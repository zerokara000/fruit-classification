import matplotlib.pyplot as plt
from PIL import  Image ,ImageOps
import torchvision.transforms.functional as TF
from torchvision.transforms import ToTensor,Compose,Resize

#Image 图片类型,里面会有一些图片操作
#加载图片
plt.rcParams["font.sans-serif"]=["PingFang SC"]
image=Image.open("../水果分类/images/1.jpeg")
fig,axes=plt.subplots(2,3,figsize=(14,2))
axes[0][0].imshow(image)
axes[0][0].set_title("原图")
#颜色反转
#ImageOps 图像处理工具
image=ImageOps.invert(image)
axes[0][1].imshow(image)
axes[0][1].set_title("颜色反转")
#图片旋转
image=TF.rotate(image,45)
axes[0][2].imshow(image)
axes[0][2].set_title("图片旋转")

#水平镜像
image=ImageOps.mirror(image)
axes[1][0].imshow(image)
axes[1][0].set_title("水平镜像")
#缩放
image=TF.resize(image,(100,100))
axes[1][1].imshow(image)
axes[1][1].set_title("缩放到100x100")
print(image.size)

plt.show()