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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG24OYKL%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICP%2FlBVRQN7V8q0yGAIfB6%2Bs6DJODHdvnA%2Fuu8hnb4UuAiAeyqAr8C16igtIzXl2nNkS8Ib1Nu2cXBOi6od9JsCQVir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIM2VKSE5VSeOVa4EwtKtwDAQGJaJAQXZNJ3HHKBjWwmDaPgZD8fs5jRo9a2UWvT5uv33pNKvCPIOSFdVpLXDN0pFC21Cc7qQJwBG6J9cYx9ji7ceyltVVMb8c%2BIWgQLJP9IoX%2FK6%2B0MJeXXlxKZxJzb2t%2BSLkTg4WdySVzI7vAaA5V%2BosWYyktkJHAL89bI%2BQPOj56PurZZlgY3jiauvFMAkUmRvNe1dkLZ9HsnrnrI1SSZs7FUbuWNIEJREUQTmAiN%2F7usrKX%2F85WG7MajXaN0IdjajbSDddI9cKU6acUex%2FIgKsE7vzIBUKzkP%2F%2Bhr2MxWNZw8tTEw%2BVJM2zyQTz3dhKbMYlLgsVdWiiXWezfcD5Y6yx0zDgPMBDS4%2FlD7TmmhiGrEKII%2BtZpx8aPeHwaQVjHCSFedBgrMEly2lPoz7Ts5MrrlLoELit0Slz5xrXT3X1xjyYdjYgzQXTy3fQXKzLcWSCdSOsTzDIYAEnlfrnAp7WINnpmK3FfI7o9zFm%2BXsRQTJtvHWcfC60WXbakc1mNIneCcdNK9nbD8gHCKHHJO1AaC5qZWNHqMujXf%2FAWNNwUUV1mXEJYrQF%2Fe2GWg8JIl6EZL0pXGsHgvPkSZl8UUlwnv5lcFqu64CeCmUNXOk6gB3c4ZxGcL0w3tyOyQY6pgFmuMSsJRogHqN%2F1zz139IIhXciTdFzro9FZzrWiFSdgMxxHKikDezmzWefrWsCjrHK86Ze9dh2AZn96ZtPABCShUrt8nJjSiLmHCNA%2Bq6g9aS12sOpOVjEDAeA19Bv23Tb%2BMRWWiMo9bXbiczmy2E3kRSnYUMBM44sNFj6Hq3SvVHr8rBTsVueoGgI6scBdkLNlVtOH%2BtAU%2B%2FKGrUv%2BlY62TnlTgjZ&X-Amz-Signature=a49d1450cdea4ccc0301492a56f41200572f261a9b39568a66572237dd60ea59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







