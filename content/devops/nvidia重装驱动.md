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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD4Q5DUG%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGWs3WAjh2OL9dm9sTXFuSgUUiNXPGP6F8TBw1sOwUueAiEA7xWXJB2CgeTHnv44J8mToCG2KD1s%2BzW%2Ficb9dSKJUv4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD1tnMEAq9RJII6rIircA1ItEnB%2B8HxM1vVuLh21I5Sdk51%2BdvMRdp8NF5IzG6UVRYp8%2BH2J4tukFkzGZe7Hrr0lYVPaK6q1dv%2BTzm8J8qHgBOu4Sa5xf9Cfrq2VvXyrQTP2vhCNNYr31lA%2B8%2BnKZSCCDccOysOC%2Fe3PISvTlGcXz5sI2VlB0to64Fd9JNCEYYv7Ws78qmJSrrnwS8JDs53X%2BTrRQ%2B1gzBvqZO%2FEyFCVzsKmt8bwWcbpH2NCZm9in42x%2FfIzbYnI46G5dPOmFnAFNt4LYkZgEZTz1i2KtoZB7GS4xroEgvHyQLBlS1xH6kzVHZMerebOIYSTCVm1e%2Bl%2BHzWdTOxqS3KCmOxz9im1hNrF3N4N5kDwK%2BNcX7jI4oLJnLxIpkQyBJslBERzRHinJitw9hy1N00H3S45m2dDEIuvaq27lWI5EuXuROEqgEffrxYTTmRAtCdktbZ7LoO%2Fvl46Mbw1m6DFpM5qZ6SVEyP2gnBVTe4ir%2BkeRMEL%2Feq6XO48pTIMNjNN5KNx3Yitiz36qy9iF07CV9QGfrRmMYnTB%2B7rSv%2B%2B861pMSL2Sp73uPUHENzSOIpx6MUmjhFk%2FekqwaFApBSBzNGYKDHHwqAnZUNW%2BAdPRJlevnd7Z%2F9Qb%2BFHQkeEeNV5MICXpcwGOqUB9jtYmUzm046eTA5GAvwTLXx66JEcwYASkIERJ3ogtcXrSnZfwuxepPs4onjtZqEwCslRtgnoyf0Vf2qxeDV6%2Bnx8RseZBuCal1NNpyfoo2jtYUdD0c%2F6FmLUE7o7S5h%2BeRxhGeE9KfaPRHRzQ4%2Bx3o4CbCMtUBm6ko%2FAvHvaOY6rz7Az2CwbCMFXL%2BzG0ujfff2xcZR7w6bI1%2FxVoEDZmO97c55U&X-Amz-Signature=6cd4762a6a7a0a209efc86f57b36484fd953146594a33d163b45b33f8c8f2a8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



