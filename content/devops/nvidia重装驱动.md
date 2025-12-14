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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BUCZMM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC%2F06RuP3zxuZ7Tjz3eLOxYnNzO4y6QfYLYYJNtjKBm8QIgKUiatNZtdQoRanvmQ3b0ujwojivXHPx%2BUjeEzh%2BKB%2FQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPsCUL2QXSY5e%2FhRqCrcA%2FvfOSvM8V05N10gU2NuAKQTlc8pCn26W7hvF%2FzmGhpLHp47RBpVqj9eJXvitX6HmpYfrw1A1WE8mpjy9%2FvyjWua35Y73VggVaP5eUVi9Z%2BBWyOPVWCEBPwkCnnURGQd%2BXGJ%2Bq%2FzpUzFZxTaC1TmVpYitemnAGjWzWXn3fAh256fEMuntx7KGxYKxk1zFsW5rbyDHModdJwX6wrf6IjZwOaKdYyWMgqn9Th64dgOTNFSxUtFx5vs7WKXpdLphsn0rf5en2%2FvyDCmWB6BWu37KYR5Km3wfyCMons2aqr32bxVp9X%2F1Xn43xW%2Fh77mP1Pa9BoBdg6amvz%2FVdBzWuCjQgiLuMEdD1VeEkZikLLBcpE38f0cEq5t0q23jnOvw7ifGAt4nUPMOmT1iAXRdFB7R%2FxlBr7srT2imCE%2FlnRYfzvb3VlaZvV0JCxAXT3muURaSeeNgYCNbJ3Ls9cIOEm70igHy2dHJ2OokXb6Ao7AimKwyxMU1MV8QQRsu%2Bpv9mPNvtYbxW2X%2BfQzgQ%2F8M%2F0Z9wp0A3%2F%2Fcpd%2FHeEcJrQtK%2BMLAzdpNSo6LdNuEpufw4dq1gpdbbndPVZD18PCXtikCCYe9tmmAelKDLIsTLhZ9u9yPmKor3snEWE1QO9mMI2w%2BMkGOqUBBpJ7LWXL4QE%2Ffq%2BmWSR1cTJMkcbY5In0CVMYvGEnUaN%2FcHdVQALvYg%2B77VuP%2B7ruiDKQbwnoeD5P%2FiHjpwlEOViQ1yYB9MR7n9QJukXlKcq%2B62hlHcLnyF0aa9JBruJ4k%2FcOuzXA4TXeDvH6kSCZxdkRvcYRUqYBhSerEhqKM%2FXDtnYMgWo2SeuynTF53CcJaTv5oqYzRj%2FnMYGPsrLd%2B6jIz094&X-Amz-Signature=81580a2d1b4b76f79e045e1b503b35c8a2b86f53051455629d78df48e5b9e8fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



