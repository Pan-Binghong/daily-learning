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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNGNMDHB%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDjmaLS6Vgp3m%2FLdDUdtC5K6rUuTZ08XeFGNDOq25vk%2FQIgUtfmDAx%2FZz8q6ox3JzdT88C4kcDMB2gvds17AAeCmKYqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsjpMIi6USQzooQLyrcA6W01EcdpCb1UmdvWx%2BW28QGsl5h0Dilf3Yb6fKfSQwFGeb3AchTEMfcLWojz%2BcmmjZwT5SPpsdnIz3AayENonNFIRpRS5JTby%2FKqNoBtfBapPOl2aFkAly1riuFYewr5HDy9M%2BRln6F55piSI1tkom%2FtnaRq1cZA%2BXXjyOZfAcvc%2BYBL7hS7K3uU3ndJ3mRSBZyIh8swwZA4OqJ3Mtzh4aHmciC%2BcQdYgO0FnvZTrOEDWFPlkvFNGLdQtNGMI7PZgXFaaxl7d5CeUlo%2BKrFUy3a0ta66xyIHJCQ4XLsX6ZqpvzfQOJrlwrXGPql1C6zkeYYmvbdHOeapg1KEZvLqzAulXqPw0Dx64QmP5xof8DZffU7gjvs8f7FFDvD3dB7WDvnNFHfi6Q3lhTYGIuvn8eximFMGKgSuwtl72RqVSBMzY%2B6s0NdZYlucyuI0%2F%2FrutiftigvGijSR9xJ6VJuhVomlMz9mM8Fw6WwiVt%2BzXfW%2F9csNsRNGr7tE2dmFR8jidGXmEX9DPDaaiq0sgRlRcwvBpt1tU37Ii%2F9jrMGFtC%2FqeY6zEuywv%2BNeWuj7JrBprq4%2FoHwdE3LvuzPifsztGJBlpvAHY3zxHsGYl2R61EPJCznERqmizpWJn8sMLGG6sgGOqUBiR71j1X2XAU7MZs9GP8WOOM1K1nQjMsfbJVtO9y0qAA7U%2BsSEbxUQ20n7nWPBQnf7ef7MnNsnKt1RY88UjCk5i0JEOySP%2B6gus4X9P0GQpAGM2U7CuzghlFcRSKmSQsxtQ4dLNpYQKXwUvP22EIsJrVSBbRRmUmjzLH7zLYLY6DowjCIUkFfL0sjChk2LpmECUJuLOunE2MSnr1qOIOwjmkJo4ja&X-Amz-Signature=ffbecb16dead6e0079434c0a5be1eda497e3eea1d6a6640e052c929462ab0df2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







