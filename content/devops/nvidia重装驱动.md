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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V2PD4XM%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD%2B2PjRW7gdA7EIpeVS4eaOQW4mfPLwU1zTSlhWwbDtbgIhANie%2FbdjAKkQA%2F33jU6fRjG3nQTPMj%2Bdu6HgEem79QojKv8DCCwQABoMNjM3NDIzMTgzODA1IgzUY7qgg1vmsvpgGPYq3APIXGQsSbDSt5fD2ds9xyQzIyhvOMOmBIhq%2BFN391NVYos7tq%2Fyg76E2gL8e2MdMb0Pdqh73fSFx7QfCfgyJHYepAIJznmD15uaS0JEqdkwV6OdYCM0QJSb9p3pnQn%2BlEIhWE1WwWZjQawlKE91j1OKADq5hY54oVoeM6AxHYvjE3kWURkunhgNqsxIZZ69E3NeIJcWY9qdDKpQRRdBsxUrbmIXa8BPvWNeMSJJpLAqw7bYiWvsn1bBjnTkXu9SgTgwmJyzRtPi%2FHOzizENwzKgEbPrENfQ6pBgmgaf3lP0qQW%2BYxTooQ1g4g%2FsuMvdOSFclQB5Bb3DmaDJ1ty0McmlQCBR4c8HN5a4uSDLaKMIF9teNQH1yfeTuQBR7nWkvbhpNnXvnDcmiyOlQ0Fw6ptDUJjMpOk%2FId%2F%2FVYmoXAPAlOrI8j6e7aFnexWspo%2FccwSdd1dagOfQcNOIJdMVhUrB7ihw7vGaodvnXWfZrzEwwWO6TsPh0Y87qpVwtcUywSltwXuoEOph2CMv6Ako%2BzVaHnWahr%2FKN7EoWepdXss5YQ94uMYQHah9cTHMFBDist%2B%2F6z8%2FgpUkaaeOIHX5idP7HaAPFtL5iRdbKy%2B%2B40De%2F4VL0QA5qdRzRS%2FHhjDK48%2FIBjqkAeKhRczEUCJL3gOin4Md%2BE%2FdCGwxCiOS04vx%2BARjN6%2FekK8RCGr8TYO7NpyyEx8WAQvkH4Tkc2kci0ngAoM48jMrycrV8Uf0rKUvc1SJWhRlH0wLK2q8azinoWureEPb0Wq%2FJM5QLvBO65t3XSxofmozLqOCSHCKTUFN8cDH2dkzJaiqNDTE4rpYcO7zURWwK75QuRxdcWlXJf8MxGKcQ5fOUjOH&X-Amz-Signature=7babccefb6e009708c0deef271a4e052b9276893f9c7d9f18e828232d3b4c0bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







