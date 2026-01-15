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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WWHPYOB%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCHi0MbcqVkYRFGvnDK6iNpkTnoLuW5Se%2F%2FlzNFgIIaIQIgMXSJYQmBZXeXknHrj0LA3t61BlQjxvTCRchdpTVHwmUq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDKS1jCWyujTK0xSVoSrcAxhGX%2F4RVt1j1WFVPE8ahl%2B8FirHjY%2BNx1JD5aHKlYXneFwexJhZdKx8lRmMKfPZfmTqYWtrQC1aFlsJzZdD%2F%2B6kym4fzuzHAWWFsehSLSyz8UYfIljlUCxvEeiMSWfCF8IoLung%2BrY9VsU1S9UU6ZMnVG4%2BlX2hr9AJNSgmzE4K0vDRuL1P1Q4FbwW53%2F2LjZ%2FhBvm2NzLNd1Kw8cvZETBZdVaMEj5tFVhYlHtH0OXzP8bJJpotLygXD%2Fu%2BTXhhFKP3y0gifnP7O%2BZx4Q5cXL%2F%2FoxF03dhtxsoiUu%2FIW5ma5TQemKKm%2BN4QPD32MYLWM%2Fp3s3gBRS%2FeoUPC1uXku7sxCw9vCt9vcLRWrQFKR2W4%2BjwU2dpKJos57Nu56Dbg9MrQDoMQlOW1VbQpKR3IsRL48Vik01089rU1o2%2BzurULB0dObZap41rjq7kVGX%2BN5qXIeqBiomyKNHcDy%2BsoZ%2BjxAcA1ioNXSijhRERaRn9bPqZnv6tVyg%2BED4FbOIXMux3GlY%2FBm9Xu%2BfU0vj4rt2TeF8qbPpwlPTbsCVDtEtSeWtfyfcuMCYufgV9ngYMQcNvDHjwf9awgkFP5J6Qfu6Nl%2FfIB%2Fk3liqlHVLjd%2BfUtBk4bDj6h6ROjDCz5MMScocsGOqUB1fk0jSomKdV9Gn8HCNUR7RvsVtXXu9dSdGA3t8fnay5uUi8cpLLGBFdhnZGF2NoSrwH2qEK5id6IJPvgNv7A1io9xlIOiLfVH8%2BnBR8KdNydiILO%2BOTL%2BqaT7mhBMo9Pid4ULHyDOaL0rsTh0W7i4VhhhexwDuQFc0BCxBXQqOjqiiSO7K7BZ2jhkRfDzyt7vMtQIxQ7q0YhMkhN4f0r3LBlPE3p&X-Amz-Signature=6a3d9b234353395ae700e51abc68e6525a1c0429da0a9422686b73ca93edef7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



