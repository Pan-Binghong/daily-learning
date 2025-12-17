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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KAMLB3K%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAFanAHeo7VrUX9YHnQqlgTmpQ%2BSTIrpogCi%2F%2BDnL6OGAiEAz7%2B42i4bhCIkuVZCBim1C%2FcuEIHqFXK0vAGUzPDBPacq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDAn5BI3tNinRX5nmUyrcA88A1f94kxY9upROxNdINasTXLiVSHQ%2BctiC39lXhe9x7LJwwOabNBFpNKbf%2FB3odlUy9w0ZG%2BW%2Fpjfd8H4e5T9DYQ4SfTuvaM%2BgA9LVocQZxz1bPphnw5bq4Y20lLRX6P00ZbPSBgekX46jvA5R38S7f8EOl8KRQDwVywLkOx4MXRbQXwuTA4H4Uka%2F9cHQfGvUrz5oex96z%2BbKLBi%2BXW83oOGjVLsDk74USHy5%2FTDmPKNtB99RVDdtD0ujK4IupbCGFrviBN7fFiKQRK%2Fg14nQMKzcF1gl1SATNRqXQZoVl%2BFiAAqFInpLe4RvH%2Bl4XQbXGr4mNSYKs78%2BYaJXuKBa5YNCUXjzxILappT9GAIGZfrUFArXx%2FVNcv3B99Q%2BkpjRAWlO0C6%2F3%2BsF4xSwLXRW3eAwn9Y%2FFHREzPtqnXtUSRy6BC24nFzw%2Bz%2Bj1pZokhanvudb8y1mgteGRGFqez%2FQkj2XWQzYau2t8C86TtMG1jVf%2FpgEKJUKEPyPiA%2F7od62xrjpu3chK4Wx1rJCMng2Phq6izE9zkHq7OcXJwlCPiEUgBsCRFfjn4v9cCvI2iZTWFwGR5YasjR%2Bhg%2BjGhHR6FhrOM6wHLViK9uRjZ3XzPAQqYxXNXGpD2OQMKKziMoGOqUBSW0rTHQO7OGzY83s6vynHQ0yfUJIEHwEIEq%2FXzJgR1ioWom5r%2By%2B51UBkb8gbS5A3tXNg7CpJy0wfBzNy5Tq5CAqGxsZ9IZhDRSS4ZkGRMoScHGpjEsq8uMoNJ1UvKFhUeIilikF1%2Fr28J1JYjEHC6OUETRYbk7QB9l9VMACLu%2BcV1Oom8lEBGMPuZB8Gs0Z9MzyDCEDwtvjuglJE9S0IoNTAK0p&X-Amz-Signature=249da349bc508f7c51a09d2ef098279d89068b23202aafff384af33f7bf2355c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



