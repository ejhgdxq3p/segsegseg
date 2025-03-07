# Medical SAM 2 在 Google Colab 上的安装指南

本指南提供了在 Google Colab 上安装和运行 Medical SAM 2 项目的步骤。

## 环境要求

- Google Colab 环境
- Python 3.9 或更高版本
- CUDA 支持的 GPU（推荐）

## 安装步骤

1. 克隆 Medical SAM 2 仓库：

```python
!git clone https://github.com/MedicineToken/Medical-SAM2.git
%cd Medical-SAM2
```

2. 使用 setup.py 安装依赖项：

```python
!pip install -e .
```

3. 下载 SAM2 预训练权重：

```python
!mkdir -p checkpoints
%cd checkpoints
!wget https://dl.fbaipublicfiles.com/segment_anything_2/sam2_hiera_small.pt
%cd ..
```

## 数据准备

### 2D 案例 - REFUGE 眼底图像分割

1. 下载预处理的 REFUGE 数据集：

```python
!mkdir -p data
%cd data
!wget https://huggingface.co/datasets/jiayuanz3/REFUGE/resolve/main/REFUGE.zip
!unzip REFUGE.zip
%cd ..
```

### 3D 案例 - 腹部多器官分割

1. 下载预处理的 BTCV 数据集：

```python
!mkdir -p data
%cd data
!wget https://huggingface.co/datasets/jiayuanz3/btcv/resolve/main/btcv.zip
!unzip btcv.zip
%cd ..
```

## 训练模型

### 2D 训练

```python
!python train_2d.py -net sam2 -exp_name REFUGE_MedSAM2 -vis 1 -sam_ckpt ./checkpoints/sam2_hiera_small.pt -sam_config sam2_hiera_s -image_size 1024 -out_size 1024 -b 4 -val_freq 1 -dataset REFUGE -data_path ./data/REFUGE
```

### 3D 训练

```python
!python train_3d.py -net sam2 -exp_name BTCV_MedSAM2 -sam_ckpt ./checkpoints/sam2_hiera_small.pt -sam_config sam2_hiera_s -image_size 1024 -val_freq 1 -prompt bbox -prompt_freq 2 -dataset btcv -data_path ./data/btcv
```

## 注意事项

1. Google Colab 的会话时间有限，长时间训练可能会中断。建议使用 Colab Pro 或将训练分成多个阶段。

2. 对于大型数据集，可能需要挂载 Google Drive 以存储数据和模型：

```python
from google.colab import drive
drive.mount('/content/drive')
```

3. 如果遇到内存不足的问题，可以尝试减小批量大小（-b 参数）或图像尺寸（-image_size 参数）。

4. 对于 3D 训练，可能需要更多的 GPU 内存。如果遇到 OOM 错误，可以尝试使用 Colab 提供的高内存 GPU 实例。

## 常见问题解决

1. 如果遇到 CUDA 内存不足的错误，可以尝试以下方法：
   - 减小批量大小
   - 减小图像尺寸
   - 使用梯度累积

2. 如果遇到依赖项冲突，可以尝试创建一个新的 Colab 实例，并按顺序安装依赖项。

3. 对于长时间训练，建议定期保存检查点，以便在会话中断后恢复训练。 