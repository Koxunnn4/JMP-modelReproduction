# JMP-GCF模型复现

## 运行环境

- Tensorflow 2.5.0
- Python 3.8
- NVIDIA GPU + CUDA + CuDNN

## 运行指南

- 主文件JMP-GCF.py可直接运行，算法选择最优图卷积层第3、4层进行BPR优化（可在JMPGCF类中修改层数），附打印迭代过程并且保存日志功能；
- 日志保存至logs文件夹，格式为txt；
- evaluator和utility文件夹中存放辅助函数，无需改动；

### 参考论文：联合多粒度流行度感知图卷积协同推荐过滤论文复现