# 水果分类

基于 PyTorch 自定义 CNN 的水果图像分类项目, 数据集为 Kaggle 的 [Fruits-360](https://www.kaggle.com/datasets/moltean/fruits)。

## 项目结构

| 文件 | 说明 |
| --- | --- |
| `神经网络.py` | 自定义 CNN (MyNN) 网络结构 |
| `模型训练.py` | 训练入口, 保存权重到 `Module.pt` |
| `数据集类.py` | PyTorch Dataset 封装, 读取标签 json 并加载图片 |
| `数据集下载.py` | 用 kagglehub 下载 Fruits-360 数据集 |
| `标签文件生成.py` / `测试标签文件生成.py` | 从数据集目录结构生成训练/测试标签 json |
| `标签对应文件.py` | 类别名与编号的映射 |
| `图片操作.py` | 图片预处理/查看的辅助脚本 |
| `真实图片测试.py` | 加载训练好的模型对单张真实图片做推理 |

## 使用方法

```bash
pip install -r requirements.txt
python 数据集下载.py        # 下载数据集到 fruits/
python 标签文件生成.py       # 生成 trainset_lable.json
python 测试标签文件生成.py    # 生成 testset_lable.json
python 模型训练.py           # 训练, 输出 Module.pt
python 真实图片测试.py        # 用训练好的模型测试真实图片
```

## 说明

- 数据集目录 `fruits/` (约 8.9GB) 不纳入版本控制。
- 大标签文件 `trainset_lable.json`、`testset_lable.json` 由脚本生成, 不入库;
  小的映射文件 `label.json`、`str_to_number.json` 保留在仓库中。
