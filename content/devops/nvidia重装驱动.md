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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDNUMXIQ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T033000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC84WlT9iQeJNTs6s3mYkDBlqoF5r3rmjsmwa%2BuUGPhDwIhAKVdh43yAyvrOhJya2cW8HYGpOgCyKOQ0Zf3tuTkQaq9Kv8DCHwQABoMNjM3NDIzMTgzODA1IgwF4yZCqmKzo9VTXFoq3AP7WHPlruG6%2FpwN9FDskK7rPzckeB893qvO8axPuNwWEmlcW62h5LOoe5wN%2B3xMJOwhYxArmY%2Fsjix4FjGyCEKgY6gSDeAxcM8zRXPlhnVOdt2lNjQ968Mfe7rpUzE5tiNaTDc4cHDFy6a11ri0BK4A1g%2F2mUGf9R3vYS7z2Y7Js%2Bs3avwSoRS3YrEGuSqXHtiWWO2R2fqq0pROBe1rYGsNlPeAMaYOVrhrPkU8IVYcmEydVAAQ%2Fj%2BaYs2wxTXUhxGTPQEFC%2BehAzYW8z1OYLBDazObzZBdJfeJSJVZFMFfyeSUbTXwpQr5yGS5QA0yhIOuqneHb%2BRdkpf70JOYtfAyjACxWGZBBZvm41vkw8BC8AwcGj4lhCk%2FuvYWLU3Z92mi1fzw2K96pH%2BC5%2BZ6kYYGcLE7J%2FXA8a9go5LDghveW0W43ZnKjCprXbdNyXue7Dgbq%2FaVR1HAutMOFw7wJi1k5oCstc4O%2BD6qGDNWd0EIf56yOx64gAAWZXduWswYxEGOLLucAtL5%2BB2s6QAVTME7a4fvi%2B7dwTE1%2BXa5u570TTnzSLUHi%2B6yltHmLyFN2xkTBqzyXJxtFFU13j%2BrEmCYorwR2PdF%2BZrH2WHtTL68vYG9qljh1fRl95UgazDsouvLBjqkAY%2Blfwglya6e5KGKqgMS4%2FVdW02QGmAvbFTNJDAwG%2FWbytV6aQcZlLbUcnvo%2B%2BwR61LNcvm1KKLerSlz%2BfWwJXbJzNwS9VUx0xYSzai52klKjbNowDzaAhrlS17FAY9DD50TS4hRGy58UHoYYMl%2FPnHjCgdgealG%2F5PrsndirXdbXOO96hXra%2FsoGoaduNkpUXDpfHPRtK%2FPNKKvEPXJt6ppQcaV&X-Amz-Signature=91d8047c504a516b4621283a3b9997b8d0db1f76dcff344445cd88ddcf89f721&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



