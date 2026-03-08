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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5JL6P2O%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIBuS2ZXw0Mwikce4RNWMVAZ0OcgUFXApwu8qOjBxY91%2FAiEA0pjUgDYw9WOBkpyDzUObn%2F5s1dwJgsCfyVsiZOPwJUAq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDDhqqKpooBr%2Fp0jZ1ircAxOWIeKLoAg7xbYdQEu2G17p7TJ61zMqIqDGTL0jeP%2Bfx1hms3vb2pr5SMPN8sB1oloyrjSep9GIGVAcrOp6df5Nob3bAuXYijLXjdwZ68LUumz%2BQSGRzPChCFwcQELPaKGUE%2Bb6%2Fp2upzqP4kVg54qsoGzlbJ5XTIyMKrVkuKYwL1tVJNmkA5mww%2B3w%2FaR67sQHWQdy%2BPoueePnHc%2Fe961tlwqFQKJAFoSbDbDyfn6Z%2FcoMmfIDligl0Dj0S%2FmrY%2Fpfia3jo710y%2BjKwLdieUPQNAyZ6atpAyX%2BK8rsF3D%2FSNvEuX3NXw0quxfZ4BPF3CMz4s01Qh%2FrpxCUpkmY1J%2FWwjsssr%2BtkhC%2BfnNwOJlf4lquKWgX2Vkamzvx3x7TMyNUDgXAvon57z0t6PwEVzmkgqs9ndT%2B4EQdXUpSG10M7zoOo95nSqJyeQEljS92qSLFY1a0wAvXFcTeX9EZYSeuLN%2BxMcDGkRWYnxtIM6IiNCa%2F9xJRYT7mntikExsn1ggvudR%2F12Ab6aadLUVzOAYU%2FWEMo1bDpV75nTb1Ps%2B9EkR0GD0u4AOdNulnoER7atfb6mi6p54nASNQnx27Nzw2o2DGrwgRcsepTE6XfAJH%2BJJJUMauVyYtl38PMOLBs80GOqUBsbB7LhKABfj5rR0ME1y3OKvgX%2B%2FdwOUZBeeWgRlXTjOaFr08etxRe%2BEezbt5McaMyZ2gCWz32m8hAoYApfQ0pqeuiO1zkYVdXnlEw1Dt1uaCPl2E%2FfMb%2BkD7Uk6ua4Eo7BFcon1PVyAutULx%2Bmzyc3i4RslcjkqgCMT9LneHLM%2BK%2BYzcEDLdhC9DR9HyHQ%2BQesN76CcK9qtq1sfSmGU7RSL46yRe&X-Amz-Signature=d770fc14b6e641532ffc79bdb9fc983ff9fd1b6163486942ecd79d10a726b319&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



