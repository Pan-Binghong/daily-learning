---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2026-01-31T04:33:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOIKFYWN%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIBDPyORnQYohXwvMHHy%2FG7YUmn%2BKSsX6ZanhBnQ8BxiRAiBTrISQ0bVHAsemZ1bk26TVfwpKOKwjjMfImo%2Fe0tTh7yqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjFgPproWoHv%2FIKBZKtwDyOVd0KxGOcNJaM9NTjf%2BXEixxY%2FOx4zCKV69tmOJ3UjwyQbHhpEGfFzZh%2FTQTiR9wWmR%2BoYUWhc5S3S3%2B3PVEUBgbUUA0ehInZNQXo8NyPo8ODH%2FcgBNCtLwV2%2B5kUEP690M86JycwVTtMIV2PSlGplOCqhMb5mWQss2j7VaGg8AMmYxLPENSENpVLfLmGjcr0XbnI63BXjgbWzKy1FeH5W9ceXz2ZRLeIZTccWSInYjIthPNxv3xnpY6RY%2FE49j6LJCLHCMpkOjEcmsq3vOGqIUnY%2FMPp06PDRV2I%2Bff748lSM7JJc5T34P%2BlpslUwwVQxn1Yh5KwF5zuU5N2Qvs%2FCPWsWzmnRbyC4c4khVXU4zFO%2FLdrRxxdGU87%2B1jkbkl7wuLsCyK%2B%2B3o%2BdwTjFAJoUE01Y7qmM4Hs1iqYoXus9Zyp5M5%2BwLHOfhyuyB%2FxMhraLfHeGFDJM6ogykXXOfVvcQsrjZZCONrAAWVH3WDSHlqdRfGsH92PBwoVeO%2BS2RKJkEwS7KeLKjGlfBLDW8j6uKImK8jiEgLf1GxVxzDXnbS0vXlucHJUCWdC9rOZqQCSJLRyrQvsku9ZVBthiG9n5%2ByXrXsrO0X4oiaKRmAQr97fbo8wdxiQ%2FNpqIwle6WzgY6pgEzan1b1z6gdAQb%2F50OManAJ8ptYCKbWTfMY5W9ZyLrC62Wg9IQ%2B2inUrKum2dk4E77UEBK%2BZfYM14V4ySPBu4mpAT3ozKly5SAFPaiHNnSQBEDsT44NE42RbWrIf5cxMB8Z3%2F%2FfCOwoX2tsMu4RxsSQFcUYzH7TWt6HSs41Jb7jR%2BkxzjW0z%2BoQENeGt64h2z7ykt3y1QLy1BRpcQmq6TMw5sjMZjl&X-Amz-Signature=11c0b82527b7d4ead86491916e010d5203ae0408b5d1027478a690154bd477db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.





https://launchpad.net/ubuntu/jammy/amd64/nvidia-fabricmanager-570/570.195.03-0ubuntu0.22.04.2



```javascript
# 1. 停止 fabricmanager 服务
systemctl stop nvidia-fabricmanager

# 2. 安装 deb 包（强制降级）
dpkg -i --force-downgrade /data/pan/nvidia-fabricmanager-570_570.195.03-0ubuntu0.22.04.2_amd64.deb

# 3. 启动服务
systemctl start nvidia-fabricmanager

# 4. 检查服务状态
systemctl status nvidia-fabricmanager

# 5. 验证 GPU 是否正常
nvidia-smi

# 6. 防止自动升级
apt-mark hold nvidia-fabricmanager-570
```









---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



