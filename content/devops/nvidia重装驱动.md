---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-12-04T09:08:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJMS3JAG%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC8xs1mVk6yoY6OWut9ePNJ%2B%2FcjN3fcsXwN38iARmVBVAiA39R3yFcfnAtNt3K6LKj%2B8imTLhO8iLBgIWJC99E2v%2FyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTq9ez1MR9c8CDFW3KtwDrjR8kPmIpCt07IgL6RSElq1%2FMiv35%2BjY6NfKpnWNf1wp%2FBtQ4fT%2F7LcmQWaeNZv3nWz4wgnL0LdFIvZKegQJIfvUTp%2FnOzXkcfhnRz8p85%2BVyS91bH3nVNcwoO79P5adsb4jKV7SC2L3AvjckvtApUTLR8ymiE13mCirZHrX9VI5ux2kLqmouCw65CbgFGps2G5K230UTGxA6vefYws%2Bi8yIbbfcQZo2Oy7lvYoyTMs2u45KOW4kAgCvifbBp05U4mFJzvOGiTsa8MFz4mC5KTk%2BrZBV1osQWJGDVXVFQT%2BlD70Nza5ZaaswQztn%2FdJY7RvnY9kgCbSNLEo6cwljQBmRBCW%2FEI8uq0FbWTrpNlmK7TIFkCIUpLkuIMWM6qPyD2gZ8hLEkrTqM%2FUhg2lohKpQi5poQCXvX81eAi6QyobJNtbpoxFQLNCyiba2tm8b3kwAcC15EI8p3STxw86rZ2qGrE1dkKvMgyfazLf9ukeeaNccnzL0RatrCL19lgLclK0Y2FNue51y1y2ntUmIdYQ8P3q%2BAyEZNNnf5J5q4ZawvJTWsruHTv%2Bxsx0hiY7RQU6mAKXuU5Y7GVIkx8Eib8aBZBCC0AgDNeKoddWVxqGbKL%2BiUIrET0e%2BrvcwlY%2FeyQY6pgGvhVc87cu8YgHKOOKCbWT6oGBqu%2BzjC%2Fv4cnVtpXlMyubO1%2FNYB2DeDtZm4FPIfLKBmwbvZgkUgoNxOfVncwdjlV8fkSHBxMXthVwdXXAzkANGrD0ddwYYSr7WWJkI2MSFhRqf67m24yPyp2pvpwy60wc5mZgSLVMMq4Har%2F5y%2Bc1YhY1E2xVdekhyfVP2C8%2F4HcOK7Xv1ytX%2F2gpkYpfDfnnKqePb&X-Amz-Signature=13502cb20bf9b52dcbf9adba458ada5ebe5fd5c91c5be2251cc0d6e0b1f85984&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



