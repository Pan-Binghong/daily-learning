---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
draft: false
tags:
- Linux
categories:
- DevOps
---

> 💡 安装过低版本的驱动,想要更新,记录.需要提前准备好离线的驱动run安装包和cuda安装包.

---

## 1. 卸载

### 1.1 卸载驱动

如果用xxx.run文件安装的驱动,用以下命令进行卸载

```markdown
/usr/bin/nvidia-uninstall
```

### 1.2 卸载CUDA

如果用xxx.run文件安装的驱动,用以下命令进行卸载

```markdown
/usr/local/cuda-12.4/bin/cuda-uninstaller
```

---

## 2. 安装

### 2.1 安装驱动

```markdown
# 安装
./NVIDIA-Linux-x86_64-570.169.run
```

重启 reboot 

### 2.2 安装CUDA

```python
# 安装
./cuda_12.9.1_575.57.08_linux.run
```

> 取消勾选安装驱动!!!

```python
# 配置环境变量

vi ~/.bashrc
# 最后添加三行
export CUDA_HOME=/usr/local/cuda-12.9
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CU·DA_HOME/lib64:$LD_LIBRARY_PATH

# 保存配置
source ~/.bashrc
```

### 2.3 安装驱动管理 

```markdown
apt install nvidia-fabricmanager-570
```

```markdown
systemctl enable nvidia-fabricmanager
systemctl start nvidia-fabricmanager
systemctl status nvidia-fabricmanager
```

---

## 3. 测试验证

```python
import torch
print(torch.cuda.is_available())
```

---

## 4. 解决报错

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLTI33H4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuA%2FOpz8n2ZkhSHtAVgM0y284VlgNS3UJc3KttqdIrWwIhAJHc0CiWrnAQL0%2FO%2BZOPLJPJeQvKY5TZsoo%2BIlOQcqWXKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgybV1BKF3%2FXTYrPqEIq3AOHkQy6x5a7YGvJhOAfdSVuCf5QVwoxULpUm4Yted1cNPxJiZOzCuyMakS3Jj%2FOQqhDZMlDPPSxb%2FCZGla08oqSeeQsUPZdNDY7Pw8nvLcJTg0pB01ywiD6ZivXD41RR4hizFJ5OyFwtszlEjiTvT03%2FoOvcxaZYUrLIuUCGGP%2Bz7SZGNWe4e5dKnQr9M%2B7uU1p3bzS399esWBJwFmyKf2tgOX0hkYjNKQRdiUEGTsKsQJDm3TH7TJF79jFNf7OkxW%2FpLISNPKduCQHmMYYLUPWDWKJUB3D4A6tFMLUrJhVHi3Cw7fdY3LCeYp6KAeYG3s1a%2FdM2Mx8aysIA%2Bn%2Be1egfFZco1mPzEP0iXUmUCJtn60tc6bai7iCOjCJpauI8pJlcFclYL3rUhZjxytuQIw2H0E96wvap0enRI9Z75Af9dHvIwRWibfdXYS%2FDvYxBiWTdwEaOJtoWfWn3lTLIQA71nUu5oA3KVHsbFoeNNRuSpOW1XLuBXMMgYZq0sovvmwdlszhOd299033VPGiFl6UM8oZRi65OA0TflsuQGjOeVlI83rKoxB5JU7ANCOpRs7N16lgbxIOUHhZRpK5m8ud2PajmaoaBoocmRNKDOwrQo2XJ09TatOK%2BpYp9jC%2B8q%2FIBjqkAcjmSsIUexyUIz1BaIYJmxnWkG%2BuiCo8sBIbNUB0mbR9F27UaBrg9hPkGqI4TG4eBpxS6S93JJsDGZ9Pl88pJp1PidfD3UsiG1sHgESS9COn0CCAm7lAYHy1BR8qu06WOlwYgqVRkRs9KptqTD21%2F9daWJhmDCxGZTr37E0v3jIF4lzSgwph51nH4uELVEvNUz49fKv3VjDfO0hxIp%2BAr4grEFit&X-Amz-Signature=e793f0be7d09dd5c618b0a2a1a4ebd39b6998af429a43ebdcf0c27a5972db24d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







