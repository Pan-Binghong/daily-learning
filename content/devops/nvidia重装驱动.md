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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T56UN7MC%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBT%2Bc5yq%2B2hSk5oVN66eH3gMy8l7%2FfOSsozHkDntS3n1AiBc6Pb7YejJOsPw37S11SXjtRKH56wpn47wJsInbiyKviqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWSCE3wT6Kc%2FCi5NBKtwDitu6XdKlB3AS3UlT9Z74F7h9%2FUzwsR6ZHSofZi%2FZqDyL8Q%2BoCBLmfhYIOzwkv8d8azDBas11CjCJyOvhmr1ibtAkuJDaa7DHOqJv2oNLIQLiGBa%2F4X3ry3yuiTkzrnWTMqprkuMvh%2BwXmChZQw6C6lCx3lTTzHYxMfy6Z3ckLMLBMBp3CEREMjZ9lVU9o%2FS127Kr9hTLu83IIbk05wvizJ1F0JF1mWoAINJA4qoeg1n%2BH3YgBayqsLriHPZ9k7W6N9ls%2B1dPC%2B5aZoCAblFy3iiMwf4l6RsjBVf5nQ55QJR8912wo9iqxPhQ3dMIeUnFuXF8ICt%2FgiVY8BWPsYlWa6bc1ReuAxlHFcZbB%2BFssu%2Fb%2Fg%2FCCSAGYa4twxVKAPLHn1x15plSRHg7MNf0qhSt3IEf5cRGwEPrSUTA%2FWTKlsTeia%2FOb1YwOMAosgEwU0nAnrPfHKVG8zauSyo6UyHCGPdRW%2F5IFU8nwAQIlmkklWqj8%2B2BMmLfFXO29uZCa7n1k5zapmYuMslUZm56UFzqfEEQwxBr6sTJki0DJEs0PZH9vkzASOdMBZ7Wza%2BDchcCcdv2wbE2NsQR5XNEGdI0Pqs2owFDl5t%2FDzYLbAag871apV2J9Lu67py8QfkwpfKvyAY6pgHpPHgDrJY2POHnH6vDiH%2FaIBBtQ6KC7Lf640678UA3ajBDtd8kf4lopc7NyAHYkcen%2B9ouBpNDXMuOZFscgd3InHxWDC5Kz5vm%2Bt1qToLW68YYNHr3TJitY6MKmDIO%2FD%2BjGHZtymbREtyLLvLtfUEtf4i3Ecjr4qeRFbicQ2SmRIHAyWQo9BondJAww1rRts9EBvwwZqB7mCvk3RhbKwpmAjmuKv54&X-Amz-Signature=1ed23e915616badc8973351a17b636e07c1a7bc0d0f6a0b2b4c7bb2d2b6a8e4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







