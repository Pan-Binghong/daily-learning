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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZZVA2QH%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034732Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAnsUrgPf51QzZoMm7iYxnVQqJwqJnpY%2B5cQOWUKUOmMAiA1NbEa8HlC2lJE09kF8EC6u%2BneNXE9%2FH0qdK58QnRwyCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMMYkYuxTowlnPR0UhKtwDEE6Gc1ssDLL2jp5zlQfYAif1Az%2FbP4OOGTpW9hrNsyZB%2BTnENxsx18cJQdEQm19SFK3kFpjDfRL5YHO73e6MSB38HKV9P4AMYE7jbaG4TeUuYf1O67froZgMGJgYAFj2nj9WsRL6k%2BMhoDNRQ%2FIZzDz7Lkx0sqOHjb2C8q3%2Fk1oKBfgiNdeidtPLNu6BnWOQop2sARVCnrq9Sbow7RmU6zdGQMSdFZGNeWu0AndCHCVgmBW9x9ImKnpqSLzHaYqNPb%2Bo9R0Ci6s3vcDvr%2BCGB9mUbhMNFGfUNwUg237sZ1E8Y89wq3ut5UGQ6VlcjX84KY6y%2BF8bBmzcCNpgQO22uhyJMPUQhSadGLqrBboxyrWYWSvuJbpXrxEysrlWu4uq7gG1SyUrbyWGPDo8UxKZMM7M1FtLE7ujAcQgphtn8GDqocFUdA7hXI92Fa6gGNspqqhtn6zMnQPnGLj8JY9ExJgqV2iNCpBS1CcCxW3t3LKbGva6qdlPBCjG3kgM9NgVdYEcpUjo1%2FEGKLWNuJGEnuCf%2FcZHNGuov1sCfYsXcrpJkJ3JO2X6TC1tGjWX5qKUUPV5SdviuSm9ZVdwwIeNvwEaXomxyjzLMEHyF7fg8qRYJWAK0DrTFfhsQWAwj%2BSCzgY6pgGr%2Bfi0TfWYGHvnuCWHuIHJP%2FlZPcnyS3bAu86KqEg56tgnRHfShmpS4lMoLx790bZkq7UGndjIE7P0womVySDeGzYmsDcTK7xxoTt7Ztm1HVqx4wTb7A1d0wB49c4F5YSLUJheqAujLVvY2JZv2GhG04IGXDouhrdUmRgt%2BVK1aTS0bD0i3oDSSEAFbEDeh62D8Tg1soNDUMryGro1aqJZolLPqYeX&X-Amz-Signature=988cc3b0793ff0e7afc0ae528abe46a98e06dd1055a0ba59651f2ec49f0f9996&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



