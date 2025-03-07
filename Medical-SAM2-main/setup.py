from setuptools import setup, find_packages

setup(
    name="medsam2",
    version="0.1.0",
    description="Medical SAM 2: Segment Medical Images As Video Via Segment Anything Model 2",
    author="Jiayuan Zhu",
    author_email="",
    url="https://github.com/MedicineToken/Medical-SAM2",
    packages=find_packages(),
    install_requires=[
        # 核心依赖
        "torch>=2.4.0",
        "torchvision>=0.19.0",
        "torchaudio>=2.4.0",
        "numpy>=2.0.1",
        "scipy>=1.14.0",
        "pillow>=10.4.0",
        "tensorboardX>=2.6.2.2",
        
        # 图像处理
        "opencv-python>=4.10.0.84",
        "scikit-image>=0.24.0",
        "imageio>=2.34.2",
        "tifffile>=2024.7.24",
        "nibabel>=5.2.1",
        "pydicom>=2.4.4",
        "dicom2nifti>=2.4.11",
        "simpleitk>=2.3.1",
        
        # 医学图像处理
        "monai>=1.3.2",
        "connected-components-3d>=3.18.0",
        
        # 数据科学
        "pandas>=2.2.2",
        "scikit-learn>=1.5.1",
        "matplotlib>=3.9.1",
        "seaborn>=0.13.2",
        
        # 深度学习工具
        "einops>=0.8.0",
        "fft-conv-pytorch>=1.2.0",
        "triton>=3.0.0",
        "batchgenerators>=0.25",
        "batchgeneratorsv2>=0.2",
        "dynamic-network-architectures>=0.3.1",
        
        # 其他工具
        "tqdm>=4.66.4",
        "omegaconf>=2.3.0",
        "hydra-core>=1.3.2",
        "yacs>=0.1.8",
        "graphviz>=0.20.3",
    ],
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
)
