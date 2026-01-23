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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HC6NQ6P%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIGjoVNXRnbLd3a98bgTDvvd%2F4OSjp%2B%2FktPYhJCgB8BOqAiEA0uyxzTR2pd2FiJm27dd6LZIgg944FYsRaMhqt5aXJlYqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCPhbyNW4msOSRLRjircAxoz7rhyBBPuIPfukO4WSz2i2Qmw9gxA7HHow6mYwzhhOX7zTRKcrDtUPPTqiZBD%2Bxd2Zw7YcrT78evJ3R5lpPa8xQiYTDNg8ndO9q5muB09UDLES01wbypnoXr4zgswIz4WyxmxF4EuI00dcr%2B23dxn2pNYWfka9RBjg%2B4hQS1xgeVZtRUPMLvmPfzj04V%2FJoYMCNZtxaRDSBRPbjXId4lC54AXfAwrIjZrVh%2BlXc8TU4CSV6CFc9AD3yFAISK27JLANziNtfAbBeNTSIG4VVs7QgBP9tiwNJJtu3aXV0h8dZSrOdK%2F5gpLD5qxUJ8iv7YhuRbz8N25GrUaf1JyOuS2rZZMmIanNVCBmUldwzUhydZUgYJXPUlXU3LuAziqFjbbm6PPcTPBSa%2FWB1JWd62g6qs6lVkEvWmVjDwrjsxQrpvUGz35%2Be3P3ebadNvLM817RUFgNn1%2BHPItrvb%2BH6uvnyvYRGGyXvq2usYxN1DuWjyauaGU3ovC1TqudF5DZNtuoDnhEHzsTG6w%2BFo3wvAGq1YJ%2BeZptvaylHFLGm3jAF2xvmn2%2BrUG0RWeoMUNefu0C1LWjDT3gsrypCwYVetjEyELibDUpiFiLk7vjdCb0EZVPmAku72PS%2BRJMIOvy8sGOqUBfH1Fx%2FHHCkn0N%2FzpbuMftC4DIJ3ROKjUcUaAGJwRwFeZUIRApAlh7Ra3JL%2FvgEeSVnPIgjnxU6fKPqp0Q%2FpOILjNsHVqHQiELw%2FIx3bk6bSKqRw%2BietEEHr5ngdHOcoHf%2FCKtmFVBUDEl%2FxkEBgWcLUQ%2B3YTsVB1SSjNlV8ud%2FirIpOOSPafLbi3rjjGeKRo2MK%2F2uJ4H%2FdChMH%2FEeV27n34kiT4&X-Amz-Signature=84ad952f55642c314cc266293909683a12114e2266b9ba5a1e2684bb9d310e79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



