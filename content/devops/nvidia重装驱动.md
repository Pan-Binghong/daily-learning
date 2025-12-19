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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UXVFDR4%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHPPauQjZDu%2BOhtH%2B3goDcUbUZGJtAm49PsM9%2Fkh2DMQIhAM82baPuT%2BberJh2lWyukxkCM3tbx3qE3xpU5ytsd5KaKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxuXlKh%2BTxpEJevHX8q3APf5e0rg2JWKkeEyHFrvgXS%2Bd1%2BTXptdoKjGL3hincJI9gWoYuetgUpl6r6PNBpJUaxuSq8Rxi6A%2BhLqli9kKsd6nm5FSAG%2FqkfR8SY2GplaAoZ0AEpej5A1CoXj5vY4zEpf7mSXrTUZQMBJmtxrqRjEQ0A4I22%2B%2FxnnVmuYNcTH%2BuZlRoayjTm%2FhrbS8aAv9F56MQ6yT88PEh70Mz%2FqinKZ7Csu%2Fw1D1CRDwc5pdjULZdRpb1pXWqzj8dceezOg1vcddnP6ayZ49qe3WSMrA%2FsjiTrU%2Bpq1VoE7sXZoQmXxHVS3451aIjg8XpXkAonmYYs0YfpDX%2Bq0mExvLr5nLa8hojbUZ766sJ7qxigyW%2BmkfCShdsUdL8gdIUIBkkb06XygyO%2Fajd0PF8DkGGkMU0FYAqbFrlSCAnQtyWiSwlCwKlpXDW1Brf0OH4DPzMrGBjmCpiBlFHwodT%2FZe1tiAjJlkS1d15txV8v8OhyfK4o9Iae%2BYlQ8OYsTcFUwuVwzYTZycWK4lsdbQuuV5NaSYsS82fZ%2FhHyiEr3Mrqk2vjbSFQTFh01Zr8Vz9NtXp8S33KtE%2BFbE39nyCbepN3Vx52wW2aN5oZQfKpaRf4v%2FUAM7C4c8bDUy5kRMuXilzDg4pLKBjqkAWUqvCjB1z2FKZVpvZt%2B%2FGFAnbBw167d7bPAIXzyJ2Un5tPXRUZnXkn%2F0kODCLRSuSpthW6JLhegKkNdAD%2B05%2Bgkyzx%2F3ZjESEkgPlkNkk9eyaeupbkCFccgvDOD6XpbSFEIwb7Pxr2kH0JqsslLVQ4uGXceVCOMcXlk1sP9y7d%2Bsh8HHJb64rnnjW5RSFVI%2FdxoA28PY3LzyN%2B5MnoRjycj6IoX&X-Amz-Signature=9e0eb74e0805da5ecaff899f0edd8eee2037eb8f58e52d6e61c26f1ec95d3487&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



