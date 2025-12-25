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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGKCRGLC%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDa6NIIkBBPObLviZiDBTv4kgtxlEZHNowTvtyW6VZDngIhAJlOlsZuKSILU%2FwNV3yRnE8myjmTV5JbFp1MjlXG90CEKv8DCDIQABoMNjM3NDIzMTgzODA1Igx%2BGO0aa%2BMshlrK79Eq3APyR4Pjw%2BOpTgnHWeq3oFFx9q2YSZgX3lr3%2BdSkZu17mPLlq2u8BscEYdTpnAvxTJk3kvPLCn0elmzwgs%2B9AsMNE0rl%2FW8G0GCbJABHKxjWb9q8wRM6zOThr%2FsdSjXPQcp9x92UM7V53AdD35IlP3ToNwHu2lUH%2B5nVuxrC2F2jxqpTrUBzfGxB%2BVIwpjliUbu98l8Cyq%2Bg%2BWs2%2FPfRoUi03Ka8vsAsTijq7oInFjigns9s%2BuO8d8L9BR5s%2BzmJm4yeQ7tWGOC%2BWyKn5ostNZYKgE47N2q3btcdgM3uNPoq0K%2BTdiCSly3QONk5nyvza1Wr%2B4ZYndD7%2F68undUY8OuM60TicJetvqn7QxVJayAEOa3uLw5kUjoK0WZfaOtYdLpgHbFbU8P6U6Pkdcmz9Gv6%2F0l6L8V5LGU0dDa9CsEtj3415RxGdTS3BbfW3fq1zwlVQHmDr0%2B7SSKC9kG0P9qcJo2MXatoUwczZTGBdfxhyxC2XwGJFpnRTghq3MQeP50V4%2F4zG1S8BVEFSG%2F3CbwrA9%2FCNia73k872idw3IjZIN6dAb4aN7aPznFXKuKHIAD4gWPU4GPJHOPrhtLBkAIq1c%2B9h2jlVd0Dp%2Bz40nffbdj2TlZZN8%2BGQOTW%2FzDRn7LKBjqkAVV2GpTV%2F%2BrAKO%2B49bUvOL%2BNChF1r%2Fx41auSAWPn546oiQSmNu%2FCEOHoirkZYmm1KBzcMcJBWmVl15QtKLs2u6Dzh4DVi4zMcT29t%2Br2Z49Drba4NKcjTcjCtZvl4CY2hr7t%2F5xynoUUAC%2BMEcO%2FN1P%2FiqDLwLr5aVpITUNOmuEZthvOHQEd1V%2BYu%2FtX1Tz44RmqQCbn7JqChz8%2Bk0BYLZ9CO3TM&X-Amz-Signature=2ab4bd3ecccf34b59319185c61be452982d4c2844fd4d69f4b9fb89858ca5483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



