---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2026-01-31T04:33:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWOXP6DA%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T034027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIBRF2Vqg9UyCMuXZzMQ%2FqYtrrfL9G%2Bq%2F4MiYREWRWdwOAiA49ZWa03n4tgnetWmtnGtgkTOPZerd1bESPTuPzTl0%2Byr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMPmBwS0LvM6Ig1r7yKtwDo7nmU9TtrphGI0kX6OvXBdxIOAsPSJArPcNElBif6wRNlzfAEA%2BKKb24LLm%2FvrGiF8eDBk3FlOi7bHO%2F8qxzPUqjrukkgjIRQ8WHrIbWzA0%2FTSLHjoC4GtFDhSU4BBSJZQQ%2BguyQ7w0hcLlWAKxGAuHmxU%2BUIGypUMR8cpd6T8GtxAVsCWIFO%2BFd0mvT5Wzit2KWY9FYxfbyaYJdmFHrWh2oHJuYm8IjxgyyTFNTrmrruJDrzL%2FKxXxC6sB3SlHLCxGcWab6LXdxGepjBLy9mtRyS3RBiAYiUDO%2BFsKCgwDnn1Fxw7dY0jvb3cctJLMT7BIXz0lsQDtsrbT3w7cHL5g4U6aFamBRB3yYiQnFiu%2B7S3uityamjEQftFEHAmov6u6hrJIOFipalSA41DlIh2eUYraq%2BbzUxEVH3ShtG3meLH0uTxRj0HGmpF5Xg2%2FJo87oqQDpOT7dyD7X0pj0nk1JKvKcN3XTneUyTePjwWhhGOdstYp1kU3WxnttMHJsa1S6XNs%2Fiz1lGQ0lt0vStYXCSl6g1q%2BIi0EtOceNS0ncznv8sNTxyz8%2BuWXo4b4Q2i79%2F17D%2F1UV7jK7z%2BieCVX4wHP1Wx47QqMIvwrCT2kJqLyuaP83pPioekgwxunmzgY6pgFYZCaBcWtq7VtAQhyal%2BFnzkB2XIPF%2Fj3yBfj1P4vUMhbzOr0AMG4lM7BRvk7%2FJUgDogBDE67dRKnsYl5GQkIX6yytS8iNTs7%2BwAp8DPsKuUx05nrALDwJlyZ3%2BuyFr%2B5c5GGzYr4WehINR2N8Xx%2F66%2BhlpepAtybdXhgyLpLux7tHwGzONv8rMGKGJBMzvcinyMqJxiQZ98lq7GQyrq5h0rcMHmtt&X-Amz-Signature=4bcb206c44455cf04b7014d1d498b79a73492556456ddc15361fc90c0a23f8ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.





https://launchpad.net/ubuntu/jammy/amd64/nvidia-fabricmanager-570/570.195.03-0ubuntu0.22.04.2



```javascript
# 1. 停止 fabricmanager 服务
systemctl stop nvidia-fabricmanager

# 2. 安装 deb 包（强制降级）
dpkg -i --force-downgrade /data/pan/nvidia-fabricmanager-570_570.195.03-0ubuntu0.22.04.2_amd64.deb

# 3. 启动服务
systemctl start nvidia-fabricmanager

# 4. 检查服务状态
systemctl status nvidia-fabricmanager

# 5. 验证 GPU 是否正常
nvidia-smi

# 6. 防止自动升级
apt-mark hold nvidia-fabricmanager-570
```









---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



