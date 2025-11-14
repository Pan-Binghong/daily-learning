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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUF2AVOB%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDIurWs6OqbKBm2grr7bBvuxSWC45571iqU7pZ27IoWAiAUdocKbi4DJwZ%2B9qDaTE%2F2pYhp%2B%2Fi%2B5bpa5FQE3QxfkSr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMt9b7FeCvwxDMq%2BfFKtwD7qiU%2Fo3%2B1gGIrkW7CKbbZIQ98Y%2B3fZe8U7audb3nEx5VaIj5F8lIdVEzcCk5HvP80w5FsV8PVEO19pBpE6IIyfmvdvijBCpMMRb9yhG6lxMlN0JGyykRxR2cxUSCtqc3WOsxS2tz9yvfEXgM3PvblzT%2BTOi7Oy2%2BSavU%2Bd1znQJCwjWgEnP8ed5XTRktAyg4UYBKKGSsi0VhwQVafRjLpcO62Y7Jmcrr8CgD9nkIZ0g%2FWWa7pmwpRZDxp9qGykWrp7zXK%2BvUsiVtysbhaU4zZRhrY2Z6gj9nFIUlno2%2FNnkZ7Ptun6L8uuMai6wVCp2WGjXwf3w9xQN8nwFR7ISuceLS3PFz4JcEUnuOQkyj%2F7qk3%2BaGFx6AFAekQRf8qH0Qt4KToPeYMzm3AxTOUii80kruxF39%2Ffm35fnVM2FRfTwZAZoo7UOH0wAf8CeXffm9N1krXsEVjeP%2B736O1RgNamp6E7SxQKFEx7jZZIT0XsAQGfYaYsSYw8CUJQQFLrbp7%2B7laxNB9m6NKx1VXyI6%2BWTSE5lz1K6u9COzSE0D4CAupbpWKwp6KxEhhSmf%2B7QGzkNqf3iiaPzWsEIbqzfnVxZZ8sZC078szVy6VHVY4OQkn5wktTqKD%2BnP8Hcw14nayAY6pgF8WMdqrEPhSM7nGHR3mFK6b79lDd34SvWygpxU7atrBnqIRmeD4FKQUAjICKot2A46ptElvusMQkI8bBCqF0IJLwSAZKny9BUkhcfNVnX005mw%2FMqNcWXXPnUbtfjPfB58c6wZCWuG%2FsxRPtPQHNxUoX%2FSDVf%2Fxk2ETLgJFf1Th57MqPllBoTdfkg6xoj0GMavxxc0UPq3IRVx0CeucpdUyL9RVlht&X-Amz-Signature=3330b71a41c4a07b538e67cb32d5a13aa8e34479cd3a6f046b89844c7245d6a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







