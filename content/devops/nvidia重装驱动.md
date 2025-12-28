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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VND6PGI%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC3%2BICbp51amSbKHU0dYQ%2BDrIaINFpPeH5sbG4R1gWMYAiA7gmOO5zxjLDLtUjEttKUZPod3mF3Xe91FWBv6SjhYRCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMnHbeJXRU5keXWZkhKtwDJMc6pe%2Fzv3UrkZOui5QDZsCKGcaQHpsQR1ii49aMNCP1X0CGVu4H3vHxEkLpLQVhrFodcebRHTmakGBAYdzYSzWsur6RI0kw5JxRlRt1D9%2FAkWfMV056CKStmrq4QXhMrMvXdkHc45BeDdK76meJOp5PQESZvrDnCeOYOMnoxoS%2FTQIDxzDNdYwu33v%2BDmHZ7lclk30dp%2Fgm8LMymErotN4n0juy4%2B7MAQbZJqGF%2Bc40VM02qP%2BMohuScxLS0dYwQN1kLhx2mcGguLP1ywT2IcA8QHntGm3p%2FTCTBqYufCd%2FiDDgZBhMn2TqnAW9G6K%2BV4Os5jYfKhf%2Bg9gy8u7sYFgcEcFJXVbLiitedH16byFxX9Jpn7BO37C5QHHPEnfcG2smlqEJLsdrP7wHz%2FSlcpZW3CNIfCC1sr35XNEeZ3uuU%2F8KU1lyD6JgRgPJ3CwDUs1N3Q6YqLXxixT5sijK1QhuGVqJCNiCwBxbxEwVszOLMweDajpN93XShV2AklxaJ3dIrTRKiYyPITDbEmUsNemOUgazYXLxiZVF3aZIbTiAY3NJ%2BOSJNDGoSWSrFx%2FtoSMjEpNCwgU%2BNMH9gSBmjeexRCNwb8dCRyqOOuiwDgvGoXik%2FgiwH16Yj6Ew%2BPfBygY6pgGpfJOfNR0yTD2AIx0I9zKIKSmSRXjU4mK49YO7vo3%2BweTt2ZUJXhHE7DMo165lfIcJAaMZ0jHk5R%2B6n6k6rS3S1jQq2f4EL1wdgJwP%2F8tCYRd4nLx336DiKHXHP5MhcsQfjB7QZzUx3L%2B9uFheIh3BwCa5IXs9444tE0VpxcaQEO3hmK9IwNis%2Bd%2Fc8KcXmIVRctj23EjrxhlGLEx9CLwdgGvUeQy4&X-Amz-Signature=a84420867f13510d7f18c370cf38b80a8310dae04785afdf78496a36bad53145&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



