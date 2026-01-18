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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GXUJT3G%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD13KszMJhxdbGeGvyPJ7GFNcXQ7MoBzi4xk%2FUIrpNFzwIhAJHG0XQ7y0pF84C67GRSslj%2FUwi9WIeUzdy%2FyX072sdLKv8DCHMQABoMNjM3NDIzMTgzODA1IgzN9%2FqDqmlhdXXVZ80q3AOM3knD%2FsjBs4rlX3wcQmUquKwL4FKqlz8iYN7fEIlFY%2FNvBReN6rTYl%2FD8ltr0324NPgjT4gTW9F96Lo0c1KC9CkiNHuZS8azkgLbBAu9nULlQ7ruzetWu0VdkrQUyASGj1sRSsqrALGatnhOm%2Bq62aNrkLi41fJHVJFPnXKawMCAMgm4DcDxY7BkGhQU%2B77pVGdTqr85RJuYa62TDTyMjfrFR9bT7POAwcf37RmuHkSSGIuO72lAo9kr9U42xcf7gS0QMEnMYaxGzgm7tBV07Rb%2BcLwdL3EDBBSmTxmjEgMewiSSuluJMaGmECnMlOLNKWPYDlTBcb5yADYFBOynqADB%2BiCrbA%2FJ9NZfVQb03uw1kR6KAJFbPS6U5jdQGo0QFAQLn17G9QBcbGhyYQrrtOUPFf0YiUNmtMTW9r%2FBDj1bCgy6wmhjYTCdfsPbDMB8DXz%2FgC3BQKEWEagT9%2FQ9YhBQHS2Wk%2F8Trl3X8mJ0eKiVHnL8IEiBC1z6i4ixB8GC4%2BjEHYo4XDPHryWRQ8ezwSzUPSj7We2xXpGAikVJDpyGg8Ot4XGiNXwaLPCYVxuy8vZYeVYAx1ZvTH6XR9jvzHDTQvvBzG8fdvWbDkpb87SXydHC0kzc%2BcMgegzC9gbHLBjqkAf1Ao0dA1PPpf538aHhf9jdNfqrKDuCxykl09rbMkW6FPKurxLal61UbKPYdCB0tc%2BHU3P8x3Uzndr64c1WNNevpPmtSqxmXRINOy14caIbe%2F8CKI2iD8idC2REA7aM7rPSMxWnUew0Yemc9bVcQoCO2u%2FR1OCNQ8%2BGbnR%2FW7T7W%2BfDFqs%2BcgYUzEzOm%2BxvEU8pQBAoE1Xx6d9dfoVSy9RiEXESV&X-Amz-Signature=f52394c0ebe231e17166222fc2b4feb168639955ee69cb6fd5a933712bb4e1f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



