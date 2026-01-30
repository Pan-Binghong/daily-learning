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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662D4C45AG%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T033122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMdV9IfvF7FXJ4GH49cH5M0sQ5v4%2B4up1J%2BvMn%2Fsz3OwIhAP4bHe37qZFSGPv%2BTYBzHwJAEYDmRvjhUVqKAf2IVP5vKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4jDNJ8ouQAGZOTbAq3AOa%2FY352x%2FXKefSchrawWMY6Sn4c%2FVPGYYY66pCglkCCiWlFZyniW%2F4o9NrWayGD7mCYU%2Ba8bbY8u2p%2FdqrT17OCO%2BjyKLx0l5qKMfqGMPKJROqDz8drsNYgl10TqUFXL39fVRkOm0cpacqb04nOhXRETaeZ6aF06whxCMlEoxntsk6BpzZI7fby5Vry9QZL4qWe%2FakblaYwBdvyNTRZJGsQK9iKPAZlz6X5Db4EZJhxRGBUx3mXknndZn0p0WH5o3qkjMGZtj%2BPQB3usq7a2xnm%2FmOL95Ckfhychk8OoIBsRtvA9yoAHYsQrlnJdioRrzMNaBkPmZeFWh31qSZZuFXnNaR0LdTUI3r8UWtp282ZINxQTDM6rXsPO6pBThUKYU8SM2VdX9%2BJOPLiJfaI1%2FA3FxqIFik2ak9mgznrN%2B4zWsqzRioG5ut%2FEe8bsaLgpEywl9eEUlDrEF9GpeBnfArV1C5iQk7Fn5k12g7QOv2tTiA1%2BfCtP2w9GF8bTe9UgexzTHhC50%2FZO0La9%2Ft2XOuKwPMqKgEFTd2yMe%2BTsCzAr%2Fqm0sjWAD6nstGyfZHOahEuv93e9Zl%2F95cm1mJUJFKxglq96xNkjAvziWqoItS55BdVjtXh0dkoJnQ0jCByfDLBjqkAfwFBKmvV3%2FwOV1rQz1lmFDbOvydwMPUBQjMDcNvIaMB9SxBSDNsI4%2BvNxh63VVl7FxXYenKZ%2BmJQ5HMKZc%2Fv90KgnV%2BVqwPb64fM6EhQRZmxVeBlF4QfxJEq8VaPq1qGTWUE1gSA3aLOa%2FW4sP5GItKmLskR93t%2FaJph6TtZJhvb01YVmMmAiNfCWkNk028UXLZUA0uy3e5T4GA6y3shIQhzX4z&X-Amz-Signature=d8a503e1f78a60d886a7feb25b10430ca22d518a48b4f3d621878582992a5b3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



