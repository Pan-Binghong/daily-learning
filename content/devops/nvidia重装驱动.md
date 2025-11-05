---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C54KEWT%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwMWKtobHfwLY0nLOJntkgBTt1%2FRUTJaFw7oBgpeGZ9gIhAO0Rxogk106Quf8ab3Ucg4g2wQJNJSK1aPEOWuXSHA4ZKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzvwtafQ0H1RZ3uTl0q3ANRbw3vNQm6vfV0JxfmZXnYz0N%2BLFUrXtcTgmTSkO%2B7h7XW2s%2Fcs%2B8us6plFOKfnKJBzN6rsq8icjmTC82mBEVuMY62A0tHwYCMA2iwECX1xehSeRjP7osd4XjinyiuzoP8OMCYfFbDJYMVVvhCpBfN2vLzd8obkcAnuGae%2Fp%2FsAw9EgfEWTOmnrzyvn%2FayR%2BHKCctBVFTAbyLEb02N4pIRPVLoWDl%2FupWhsZ0Qn2R7iOR8ObS8yBCzucYZK2WTXFkvQ8KIgJFL6ZPMYmhWkqqftw1bPRJHa7Wg0CL0k0coAJqRmDhoKxWVzsbCXX%2F3HO0a7ADlpHMd6WX56Yskx%2B%2Ff7SgNhzQUfx52iLw6oSGZYdtGAU4LDLY7hdZN6%2BqMUdF4leN6tn9lF98tEWRDTcMNBbL5LbfXKnwjXkgRTNK%2BKIcbwh8%2Fb3%2FghQVp9kOwEdnH%2Fb47QP%2BTPkJyt%2BGGU9vx4UJu3Jov8pvW5c9N8MKNV%2BmApKXNWp26%2BFhG9dYQ%2B7jPLdTCt1WigI4kLhHRQlwB%2B7RgeGqCTtogj%2FocpcFRDAV1q1p7Wbsbwm2wmGw8dPf%2FxG%2FExK6o1umIRR%2F8OlDInpf0d8ESAt4DKm5sAT3HPfAmcG1NwzIcgm858zCSo6zIBjqkAZ3xjqn0c2knjvKKLcVJewgmhlHQUK%2FPoWQtkrli0c7o3hbQ1t%2BwHeZSttmHW3%2BsSvwhWj92KBgGZ0G1QSE0TYrkUmyO5mTCIt936XWgw8SslJSua%2FzmLeDJjZtQSS5qIphV56B6O8mpAdH1%2FivZ%2Fy2S%2F9WccvnmkaUEoigIVenUpfXTGUMOPDvYkAy9ZgX8XF1UvcQo%2BXI5baGugPvGlGgZtSQh&X-Amz-Signature=4d19c5070a4ffbc5d8870cb4c02097c654b02e6e58fff8e7b6f66e946c9831f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







