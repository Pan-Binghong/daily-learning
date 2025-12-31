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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG5NALXY%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIFiUXtSWy%2FA9%2FTq4pmLigbLuckspKV44wOLNkZJdNTAiAqMg%2BhYWqxunekez5l32gAEMQJF1Z18eneejpPAnK1oCqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0Q88t30z2xPSQO2IKtwDG4YBj6oUdL9jMigeHiEJjodel00KnO7Lkq27Q6iqvFdvRGLUnz6cCOnJl83Bxp6Td%2BHKR4ANdR%2BAxnMHi6gNWls%2BWSfdyC4m%2FJ3sh3PB%2FHAa1JzukNEunh1wgDbxhRX206cI8QqcjgBcbAe1GORxAD42MEpt%2Bel6vzthq6dK81XVzX0mLMff30Y%2F8fST%2Bm2jFC0NaLXc2jUmz6qXakx168JzMgSPSQMi1dJNlRxn1nzw2pPqgBgdvF9XOeZ%2Bv7oGIhqs3OIWk4km3ytKGJZetNxI00C2vKf3HzodEXPHSOKkG6hbIhlTwsklNleKxQ2t4PGlmSpq1Y5A%2Fm86DZtRuKQk04ZYYzo9nJTluu4wIPWFxWe%2Fle0%2Fe%2F4KLtck%2FcphXOCciVXaJE0lKrmscZQjcDbj8iy849giO%2FEiWndWKu3S7d1t1x2s5etFFKwH6LtTfND7bi5%2F7slJzor%2FLU%2BS7JGNU7qmtjaJzFWxV3Hbi%2FlOdZKGYIFsnwmh1ups94brR3%2FfWhXqweLDMSlcmq%2BTclAUxREdI2CW%2BGg8JADiPx3fJsgWd5M6BQcet1OyS4H74AZaUcyvXbNzAVbbQ7psL%2BhpdTrwV9Iw4hp2ZSVFtIctyJJqTy9jLXSupGQw%2BuzRygY6pgFK1gFsSTjCRtuyfrUJDxQ7vlCrGmXmTkaksz6%2Fl8PLy5qnKRqrL0CJjOk%2FM4tXFOWq7vvbBJdoSd3i7bpd5Z5jjRiZ9uCheEljoUW2gXx1vR%2BgAxo2%2BayAeWYCXIibOJjWaUOXwp0Su0Z%2FIAppYoopfrcRp4A6G6DE2rcw%2FRtuntM%2FsXYPZpXF3v2Qme%2BjP02hvgX1IOH6S4u2mHCeaskicucBKhtW&X-Amz-Signature=1f4ab562b232856db67d9c54a9465a13dc1a23361665cb7d85a29a39b4c6c99a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



