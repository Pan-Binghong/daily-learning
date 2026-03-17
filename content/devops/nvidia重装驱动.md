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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UMVYATF%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICOnTVWRMuyXR59jpweL4fgFYKAkNeHVV9Vs3OCDA%2B0VAiBkwdVHdAzUSW%2BCnq3W%2B%2B4f5v65cv%2F70N%2BAF9guWjkezCqIBAjj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq%2Fp%2F7VpIFjJhnTK9KtwDDMNtkcPFJhUuTUn%2BzC5JQY9vvGvGFX5gZP6VMY23vFl1mOOj8sMp77LJZ0Q8knI67BD%2BKSD64BaodJcgoWj0ohlUO3PYpG7mZCYLNBJLTWD%2FmI5rGeRjSiVDSHuDmzq8yODo%2BSjwYiMv5K5j4EYLO1gzSiGx%2BqyrsvUyQ9oHuXxtLAdHD3%2F2uUqcYhxsB8mCU5fRt3cAZd0sSX5jE1XjoIFtQfSJZUanu6zsw3cJ%2FuHKReMkd%2F5yczxYffwJUsFn1BO1tzpPq9r7YTl%2Bll%2B2RR0jZS3XDdDdk1p9SzxbhOgU3Zcbw2uE6lRfUUciPqWifCwCfOb5rmrzCJ%2FjYGrwGDow43RwU5VVDY69qS55Y%2B7JKNxt58x5ZUlLWIbcvQfdz2Nfup5EDKDUPpIFSeCkwFL6xF6bau3U%2FX%2FeURFwsBxJa%2BKcehklz4zLM%2BFc2y5qIWb%2FR2J6K42BPf5uRtkLBI2flHr31eZVhD61UVsgf9emM4wjipenOOngPl0mQpZd%2BQ6tTPAO300Yw7BYxH6p30ZT9m9pAfOrZDn%2FKxA1f%2BzXL1sXnQek6o2lthwerVvVraK8%2B6uCOyVLba36bMjqyjoTZBHgQ9cXEYOvyuRTrRARu4FRSWf60wNiKQww1ujizQY6pgFBV3ISL%2BGR93SO5CERSgFfeo88%2FDcSmqyZQ35n4d8uRYNi9V1ys0PAe6uzCxiGRKAapjjTTgAiC1qdF%2BN6nHDHJVSkqcjZSrpuLmSSoOB4Dp1PqHHGozT0azSPlToh4Z%2BDeJt%2FPzldxjCSmXTZa8lYhuy%2FFnx5WOwcO4JmVqMhrzyzWjbw7Szv4MRCFamOoBXSMabc9cbA%2Baby1m%2Bv%2BRRS%2BsgE69S0&X-Amz-Signature=dede8437407678905fb496d6b94cdc8d3b40a9f194a60a4466d8bdc20ae399d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



