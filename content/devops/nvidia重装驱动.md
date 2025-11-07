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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQQQDCG2%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYpTzKubDuPtAdWfigX3QI0ZvZLTu2SDhWR%2FsWnswuVAIhAMZlOOjg6GlayQ3m0FHtRTkkBMo1J1E4JgyNHkKpDU8fKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz1o1HIiZThGWmzchwq3APILKQ5W487CS%2BrDUjqe%2Fjau5S85iUBvQS8cwzf497CUGLWUjMWNbyOYMOyahSsBjNKXVAKxjFH3jL7bIy92W%2FJqgqr5ORQncEF%2BwMAvLjceEXzKsB56B6gY7Jri1k1H2al2Mr5E1%2B3ojfbm8rAnAljU06ARIXQbIHz8R7990%2FX%2BdsKMo%2FIqDaWzmURCc6Qe9gyiciKdV3Rrm3oEvxXAMjkh7LMHNi7v%2Bo%2FcIuo1SDq9vJS55UFXt0Cwa0wQ2L0ASRxbEo2qlBUtQD2Ur7FKeCWQqdiAfsRcA%2FXTbFCRH2xXEKsXULgdsyj8WwIcdvFDLyZi7CPRYGlZax2cCwTx4Ksu5jCWClNnxHhOHtfLxoZBtb6r7EMzpNWIDILirxABDeFCsaqIiKguR7LsOq317S4XuLP8MHlYaAiBXJoLENYWnDYI6i8WAtkPFTRWFqRb7xia2CoIQ%2FBrTgUmQLhO933S432VMCksBaZK%2FVyKOymUawvl4CPSB2JeBbMEcFek7hFNBOhpVgJkPlLXRNVegzrkMX1fcSUGVCFgjGo5lZioDrmjLgNqaZRQi0g4fXvWXTExfmAL5oFUEvGe9zS8NKuM6o6VqoKraH%2BlgZFFvPLQr1bXRYipfR3p5lIpzCHtbXIBjqkAXRxlDrAbPaneGZoMCD%2FpJOmqXL4osfPnAb5NCfMytAsSlF%2BwR7K0PSVBYe5V%2BIHLAvgI7jmfIU%2BgAJiVqvTTzLTLyhDlkVzKjWatuKYgsLwmG3PUSGDJAd0ZpkQiyZAMXuM916jNKat%2B%2BUQ5fda%2FZqJNMCIAoHZqJViEFHHhm4HU0v0qb8qeZuOlcA7qlArWRXbpiHv9k6a4IGNJZr7csDEBqdE&X-Amz-Signature=c700d0e4aad8e532c80e3d134ae4868a17967b9f5c0165fb708d3f0a79c5337f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







