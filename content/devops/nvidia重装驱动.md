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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K22NJ5M%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIGA5TyqjTOy69LqGkf0JaTJeWlaZsMlJC33AiCjrsSoBAiEA8Baryt1RaFAdWZw2TX2eoW53KSegNrhShyaCQQoeZHsq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDAPcAKoeNF23UOb5ZyrcA8qjVMoUYmpTmhr2ktz9vW8WT99%2BOJceHZzn48yH1MKJGnHQ1MVTFvjB3R3D9RoBgYpX%2FleHAlLhYBc0fByCDo5bDqHca0GUuDowLRxd5nhjodLuX4XOBbf%2B3Ec7JQAiyrisy%2Fl96P9zMl0UXxJnyX99vepXjgSokXcQQ7J4kGb88iC8sR74aZ9qUp0fyjn7fmErhvj5nuPw64MSpFP4wU%2BFRqqDetYMTmRvIOqNAAQY4bwDW4hJ%2F14kc9IrA66RYMKk6KKy8XvkpUk0K5DD6uMXUQzbpTsIx8JnGxUH65a0HLOVqUe3%2FQ%2BZatg5MhxArxm3pRELv0YrQp8A5pXYVIeHfHeeilZIV1dUTfSQuuT8oZLQNggJU18%2F073pR6HBYD%2FqpD%2FC1TNSTQ6BQMsqYNKP2hUeGd%2BcMIKsBzp0IFKS05mamjVZ3vlbTpv0EOBmOD%2BzymgFUjhINAQbNOKk44rGfTgiyniM6Wdb8GP%2Bmo8u3wJREj2YEQB34jJTqlTNPnzBcmt6b1qy%2BriAcIbjGiGm7u5Z5ss%2B6iIzK9nc%2F0UjsESBK3baxi3w217edeRGxciK63WnOwSPRUKgzsg7r2%2B3%2FaK36eR8288drz7S9C6FS%2BnlIznZwPc2SwjHMLzAz8wGOqUBVTMzEdIgZpLQiHgenC4Yhf8sW5%2F7qpNj%2BIgkgSRXgrBFUbBUmAS43Y5J5TcsmBTC%2BaLbiHhXY3CxdPNFlE%2B07HL8JL9NRbJTmsjIIIWTQDncMTC2x68eXYUyBEMx72lTuKTChktwuhfFKSIUtrEiEhFBsieMNegQrJXZp38Di2Lbc0A7YHKZ2yHOUuGTyoWNjPDYnxdzW92LIduZTEm1nabIo4eD&X-Amz-Signature=092727128ea1de3ec13d247f5ad6914b30c1104e2c98a1105ec16f2f4cb0cb4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



