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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ML374RT%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BTTUbRoksjjiJhvwyX4Ki6sHCRH4WcBCQtbl7hT7jvwIhAJ%2FhIt9Ft1kfvLCBp08tcYa0rZ5UkHROCqaILZgzHEXzKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWZ3ZHxYwmBXzyQTEq3AP%2Fv%2FvGeu3JG5Kovj9shAK7rxZ8d%2BYVh7NzeALfOzaDSr3opKFmcWiDFJGxjVDe8XPnAgv7BJQKcgTww%2FWRgx9KlIpoAnkmlGyjMVmJmjUX7T64jgz7MFsbujn02c%2Bg0%2F3dvk5qcA0vQ%2Frj93HLIBZRTzWWBAY2EgL2iDrSTR%2B3RHwj90nAcKUwz%2B3eOa2M2T4Jc%2Fc1xYP1MUO92T5ESXy8xjkFG58n%2FdhqmfC8r2VdwQcncQfQ0zFPd9ks5ol3dFbXEURK%2BbKGDN6ZnDVwYekeiNpbFqMUrOZo0R12GMrm6wWMIezNoYYJMKuzUr375groH8Z5xOP2XP2bxbb6lznEz4UFXmKuAPoF8cre45omAZopyngCEZaQCVfBMPKazrCDvWXlJim9sjuBbMJoe1Ubw2J22p8a2pvtkxFecypigWqKV2wKL2zoX6IfEIFwxE7b7csTOI7hHsrKk0ir8uzqb5iKBaUPaRK3tbEwLcavZhdBDe9n%2BkiYWEeVFmMZYXiIH62gTfrbnkAfzKvPVzKosrZ4xtVeppWoCx4OksNQHnW1cQ7zT1kFWFJOX9p7lHNGp9aJRvBx3AzEretErjECJ4BG7Nz4jls%2BFYbWHtvUQCfQCWSsrfLDicMZbTCqhZjKBjqkAdmr%2F8cttH4JlEuPIubrZwKgMaiHPDGKb1pRxcYCTnhr8QpjVHfA33sTg%2BD2BQLIHEQwU4%2FEXTO88XSC8eWJdtW19VkcCV3kHXvdvmRZ0JGTUEToES4bvD1eTl1dbiS0hlPz%2BCNcxb%2FNs4Ap9WxoI7EMSwW0FrVCfE%2B2VfjBAzFXWwYnKPws2BqvkYwIjh2VEU3Kxoxe7f6yN%2BKazkjk%2BrQ1lgEk&X-Amz-Signature=5b0a828c2cb03cfa06899817bfa39cb610b3375b7b7f689b75e27206ea823109&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



