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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD5YPT43%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICFKdW7MGmuIX%2BzFonW5lGUrhgCcm0T4oE34m7e6YizWAiAtk0ErUveWVmrdRdFg9timZaXe51bvPprfrIikGHFmLCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMvIq7ri931n8tJvoNKtwDfVWfF%2B8f6HlXDAHR1Vku7BZ7mChXeGVw1qMXYQfpuE%2FEFmZ66YP%2Bu2fdNd7ZgUTImd45VK2s4hF6OTVm9Me04Y041SM%2B6jLQYPCwocl4lPGnpdjQL11JAHZX3P1VUyD4roL4SA6rcs6RNCJvZUp3JRao6uP1NybykEuNZYc2uYST20HXzaELuWEWrdSsvtoctB0jsV38Qyt%2FaR%2Bh3r0iLl328XWlzVjPv3ZvFmGP5YIb%2BB6No%2FL6YO0mB0SaBHMY0STwqdFp2tMXAqGg8uBhFEUVPAJD%2BqS15WwkOWWZNJ274vjv1SKq3osQT%2BQt6EGHXiNUJOYNZmPIv%2FZEIanmvwkHM73zWChxcDs4%2FCHTkiFlxWawQpqkKtUBw7QXEA%2FcTFXw0dEMvls6I3TNLFN3OrbUnVqV4RwJQP8J6%2F4V1gMQr3oXzQWVoa92R1jQC9u679sXmWo2RPvNhgUHOo8Es6RZXeQ8Dhbn4F5cZhx6P5tpEkJUxyIhhGSYNlNdUROWeuC9L0UTWySukYK9B0rfhlumqLECVdt1mWcscsVSagpA7QrHxkZiB0V6ai%2BXmeUa6fdCddHm47%2Ft9pCMMqkChsn2vK0fKh0n0ISEmkTmRdiBQZO0P4ZPBudEGj4w05aJzQY6pgEhQL9%2Fcg6QtxRIlWpb63H%2BPuWu3yKunJ1%2B0pM2xM3RM9FG9G7TE09WgTwsM1TcxR1SP47DLa4cTS7FcMCSltDk5dLa6BHCIA0Q8mKjEyj9K0%2FYAsU7fb%2FLLoTU81Uo1R2FaEHQgTJZk0S2WN4NLA5cgHXnZP8iOafMRc3ioh3OHrAVlyq7q%2B4twJJ1yIRtnzxZaeza1uCa6Fpq0IuyVhBTK%2FoA%2Fm%2BG&X-Amz-Signature=8764dc5784944f76af572507f5cbbe3e427df10a9fd8b91bb66dae9eaab00a94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



