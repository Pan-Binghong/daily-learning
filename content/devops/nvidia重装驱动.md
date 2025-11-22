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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C24ROWY%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDAw5YUFtwp3v8m08IJLV9pbpU29S3YNvC3zLl8DU8OLwIhALE1vztjPtkiy0me7Hiig1LXED23TZi3kUZ2MWAXR5w5Kv8DCBwQABoMNjM3NDIzMTgzODA1IgxR58baYz%2F%2F%2FMPLcc0q3AOT%2B3p9pAplJRaMe7xUpJRDW%2FmMAYibO%2BGO9nD4KWArAGY%2BTMf0aZhqKIuiSWfHnxi26rngoo1d8Sj%2FetPGxRmbkPO7RKhYzI3rvXiYemorogtL4joeAGZLTJRQDXPRgVR2HM2PD2CSwskXFao0Kc0C8hmK%2Bk4vOwbaCLruM5lzGzL0CB1jOyGuk%2BpGSPrrVxfp9foW8v3sx5yKoZIEuGv70GTbDN6pk2y49y%2FFjg1RXAfeEUsC9KwzKRvneKin2L2H015kBpggb7EXevePgBbE7oRZu%2BQiseyy34Oi8Iu8aXDrnyy7u4r%2BdOgppYwyTnrAOQ2Ba39Z6qu8cAnMrkI1xBxamIieubA3DcH%2FKKWXs9R3BGflqT%2FnLuS2HQc1SGvv76AnvN3bxYFoSnpOYTMcpn5Iye2eUKbEjJtIfzB%2BIOPW8LSmty9jD3t6x06HQGeQkHugFBmwhJhfJVIC0ckifd7nvCQ0S7Phn5T3WbTBxzOJqiprhAXCf1%2FCyNciADId2ZxPlaUa5%2Bcl7AO9L9VS1feLdDJizbn6SdIn0r%2FXemaOrBPsUlF9kwe1M2dX1lH074grbXdRALtdejU7z4E1erS%2FlxId4MHReUseRJEX2WTqQWul54ErOW2SwDDFvoTJBjqkAe0UoM4KJtDDyxhhL0Fj2F4NjbFmkc2vmAn4%2B0f312tkcYwTNx0IXBYhAWyENn%2BZ8LV1%2BjWqWzzFxFNvZeMvYf9jjForQCg9xEph%2F%2BkfQgHxHQvOXa2b2iE4YMocN2d9J3UZQq49lPDCWYhqrbg3IoIrISnIzwgYAgijL81Aati3MpU8YD6ypwpcglEQrr2M3IOXxHOtgu6dCgoHeF3PdUxN8%2Fi5&X-Amz-Signature=ce0c11f92403ae2c6d5b626238791263aabbc9dbd2ceb99b6c755a2e6458697b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







