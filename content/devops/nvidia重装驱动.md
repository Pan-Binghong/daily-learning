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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSJP7AKV%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxI%2F%2F07KbFh0CXAo%2BX2ccGgdPG%2Fq7lEf5MCKHw15ejuAiA7fwJF1eKHFUrLnbzx7dhviRiQrfjUIJKXH4P%2FJOyL6yqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrCPS3pplHJoUZ1F4KtwDQjA67RzLDagwMYxeQauI%2Fw%2FPtvDV%2FIBI4kCgdooE%2FWAgDD8ANveVJJ2W4eWpwgswuXXV80VH2D935kr7%2BlijcfQdTw8NQe2ftLBFSrgm7%2Bs3Civm0OCgR8TeKiiYJleNrM5eTCpMQJ11WCB14h6nFP7n%2Bn1TkBY3fTfmODHGdsslJOdNjAbFBZVxaDA8RxXzbqY%2FFULZVGpVhCIs%2FpuzT0QfVUsy%2BF1wqL3zcpJJNPM1PGIGCPQlX%2F0aIQyBWfLqN7byGE%2FdoRVs4h6sj%2B8zhbArEXuj%2FdXDtviMYyMESjiwGceo08l8MmjXyzafd2VIhSn%2FdAgVmS16uqBlkUK5IuD13r%2Fc6PzxiO4qvZfSZaw8mbvNlxplhnkTyKEFTv2emTDz7MHZCjJe3Z9kmMiQLib1%2FZoML3H7xM7GVyu%2F5G3Ivli25IhUBDc%2F8UnjjrGeyb%2Fkjj%2FQcyOtSiPK04iW%2Btkj8edmgdA2VoGt618UlAE609Z7HHKcnbPSfgxrFEZJwVDVM5P%2BWgAm57eMg0HBJ9kg7Fa87Vv4u576p1YqFNcAIIXcmEGDlGeMtIIRNyM34%2FIFsqSxu8ttqk%2BqoKIt4fOZ4X%2FFF%2BpNLWbkXN33BmgNLGRSpqC0zcGaaFgw65fvyAY6pgFHjfcGq9V5jwCCgscc%2FVWHuJ3%2BgMSjxU5tQfPi%2F2zwlzoevmYhM3p2%2Fvk%2F6v7v9dPb%2BfsO1patT90JABWbKpMrOcGalyDnQ4XmJtOZlBBdwmj0dFxdy%2FPJTzXGz0pt7HnKzdklDEMVYPr82xHPEOus97ic4TEyEku2r8hos%2FSay2E7hAaCUWqQamVtyC0KmqjtpltYIBlXE7pbg3XHNmQJeZe9ofCC&X-Amz-Signature=225cfcc99d19de21165158d56305ccb5e5de956e3139b2a46bbe6b62ba4fc774&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







