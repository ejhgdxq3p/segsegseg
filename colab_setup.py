#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Medical SAM 2 在 Google Colab 上的环境设置脚本
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command):
    """运行shell命令并打印输出"""
    print(f"执行命令: {command}")
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True
    )
    
    for line in process.stdout:
        print(line.strip())
    
    process.wait()
    if process.returncode != 0:
        print(f"命令执行失败，返回码: {process.returncode}")
        return False
    return True

def setup_environment():
    """设置Medical SAM 2环境"""
    print("开始设置Medical SAM 2环境...")
    
    # 安装依赖项
    print("安装依赖项...")
    if not run_command("pip install -e ."):
        print("依赖项安装失败！")
        return False
    
    # 创建检查点目录并下载预训练权重
    print("下载SAM2预训练权重...")
    os.makedirs("checkpoints", exist_ok=True)
    os.chdir("checkpoints")
    if not run_command("wget https://dl.fbaipublicfiles.com/segment_anything_2/sam2_hiera_small.pt"):
        print("预训练权重下载失败！")
        return False
    os.chdir("..")
    
    print("环境设置完成！")
    return True

def download_dataset(dataset_name):
    """下载并解压数据集"""
    if dataset_name.lower() not in ["refuge", "btcv", "all"]:
        print(f"未知的数据集: {dataset_name}")
        print("可用的数据集: refuge, btcv, all")
        return False
    
    os.makedirs("data", exist_ok=True)
    os.chdir("data")
    
    if dataset_name.lower() == "refuge" or dataset_name.lower() == "all":
        print("下载REFUGE数据集...")
        if not run_command("wget https://huggingface.co/datasets/jiayuanz3/REFUGE/resolve/main/REFUGE.zip"):
            print("REFUGE数据集下载失败！")
            return False
        
        print("解压REFUGE数据集...")
        if not run_command("unzip REFUGE.zip"):
            print("REFUGE数据集解压失败！")
            return False
    
    if dataset_name.lower() == "btcv" or dataset_name.lower() == "all":
        print("下载BTCV数据集...")
        if not run_command("wget https://huggingface.co/datasets/jiayuanz3/btcv/resolve/main/btcv.zip"):
            print("BTCV数据集下载失败！")
            return False
        
        print("解压BTCV数据集...")
        if not run_command("unzip btcv.zip"):
            print("BTCV数据集解压失败！")
            return False
    
    os.chdir("..")
    print(f"{dataset_name}数据集准备完成！")
    return True

def mount_google_drive():
    """挂载Google Drive"""
    try:
        from google.colab import drive
        print("挂载Google Drive...")
        drive.mount('/content/drive')
        print("Google Drive挂载成功！")
        return True
    except ImportError:
        print("无法导入google.colab模块，可能不在Colab环境中运行。")
        return False
    except Exception as e:
        print(f"挂载Google Drive时出错: {str(e)}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("Medical SAM 2 Colab 环境设置工具")
    print("=" * 50)
    
    # 检查是否在Colab环境中运行
    try:
        import google.colab
        print("检测到Google Colab环境")
    except ImportError:
        print("警告: 未检测到Google Colab环境，脚本可能无法正常工作。")
    
    # 解析命令行参数
    import argparse
    parser = argparse.ArgumentParser(description="Medical SAM 2 Colab环境设置工具")
    parser.add_argument("--setup", action="store_true", help="设置基本环境")
    parser.add_argument("--dataset", type=str, choices=["refuge", "btcv", "all"], help="下载数据集")
    parser.add_argument("--mount_drive", action="store_true", help="挂载Google Drive")
    
    args = parser.parse_args()
    
    # 如果没有提供任何参数，则设置所有内容
    if not (args.setup or args.dataset or args.mount_drive):
        args.setup = True
        args.dataset = "all"
        args.mount_drive = True
    
    # 执行请求的操作
    if args.mount_drive:
        mount_google_drive()
    
    if args.setup:
        if not setup_environment():
            print("环境设置失败！")
            return 1
    
    if args.dataset:
        if not download_dataset(args.dataset):
            print("数据集下载失败！")
            return 1
    
    print("\n所有操作完成！")
    print("您现在可以使用以下命令开始训练:")
    print("\n2D训练:")
    print("python train_2d.py -net sam2 -exp_name REFUGE_MedSAM2 -vis 1 -sam_ckpt ./checkpoints/sam2_hiera_small.pt -sam_config sam2_hiera_s -image_size 1024 -out_size 1024 -b 4 -val_freq 1 -dataset REFUGE -data_path ./data/REFUGE")
    print("\n3D训练:")
    print("python train_3d.py -net sam2 -exp_name BTCV_MedSAM2 -sam_ckpt ./checkpoints/sam2_hiera_small.pt -sam_config sam2_hiera_s -image_size 1024 -val_freq 1 -prompt bbox -prompt_freq 2 -dataset btcv -data_path ./data/btcv")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 