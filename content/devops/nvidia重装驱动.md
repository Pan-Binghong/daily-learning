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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JRTPWU7%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCHPqwArzFvPCQjTG3FbnOtRfIHrIuBYhX5UmtXjLXl8wIgeZd39Xy5bcWnw7TRsbswDyNo4EGbJ2DRi5nAS5T8GGoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpkvMdzZPxT4VO43SrcA8vCTdGqrjIzp%2FPSrwo%2Fa6BjOXh3f8k%2BeQXX01vo2MLFWe%2FyhwSnIMBu%2BFu6%2BqEj9Yj28K%2Fdp6%2FKFNxR8xTQcvEzxTwNw8OPeYWA2aDBhOyMLNl2vryoP%2FKtgjOTHJb6nN9jDJ%2FBn1FhsYwfF45FI%2Fu%2FWySeSFKqkeyXHFzrtTAMGnte0TJETo53mgIU8WQHM18j2%2BjzsoiNL39RucfsfgI1Loo76ZjV8SGQjKC6Dv7Hylonir93c5v389I6o6w5i13yojdRenwJ6VanBZuWOJazUEJmmH%2BGHOOstpT%2FUe2c6SuaIZY73t%2FUY71rwtKpTiZJvTl3g7KH8PxWETWBR%2FqLt5Z%2FgGxNcHCJ%2BTeF%2FpBEQ4gelDDW0WXToTKq%2BgwDLnfojIukp14L3AyD0erJw7E7HtxA97eumYKwwCfpbRzOAu0uH%2F5AA%2F39JDPYoPPR5is6mzzyVf%2FGYXufKrtrtwmhcJyzBykR5b3rGp2CuhqOophTPbEA3LAqutt7dijrCA070Y34hbayyvcM3djykYh8pFgHkelH4xvCPKP9gXGMV9ig605Z8zw5cGhMRSJL2xjDKNFCuk2K%2FMXWB2IuKJ6xlgxUVWrK%2BCtdG7Pr%2FrkBGgCaZ5aAGTJQOleoMJm9hs8GOqUBu9KMxaPq3z02fiInx2%2F2bHv1K9tSD44fjPuU4tseLwPTxhVuRsbgSsLNkUp%2BwqTou00SgzzUoUt98iA7RR9foWjhIDHI1enJUnUCyuvgQ4dz%2FpaFq%2BpJeKMCpCQTUsOqbKkUYKGcb09b5DkQ2aO0qVWgcuu%2Fu2oZCaioprbzJhlIaOOQWIXpm1A8wXMcHGt0zo%2Fi3e44vjH66vQT6npANCW5C4fZ&X-Amz-Signature=66edb7a99b29d6945f0b63c7521c0596a806adb147e659d63d54a72225700a92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



