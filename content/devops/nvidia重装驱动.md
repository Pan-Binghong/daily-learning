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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPQINKIF%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQDIG0vTtsvi6cSWOBHwtDwb%2F99iWtroHCVk9qKIaDRnNAIgKFwh%2FOH%2FJUDnvGoVN4DvMFPU8GAndfJLZzrGdabdfMUq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDDcYnoETucH2LXa2KyrcA5lrDbrvtIjf%2F9lPdhjsQOxgjBk%2BEjvrlPjcuIAaJHLpDElb0DT9w0Pyhq%2BvVMJWYbgkNi9h3a0JlVPpssk1fjv4Oouf1%2FkqRksaE5nKcxmLrSIETZrGoifyZt26bxqI3I%2FtwmExTDLrCEtpTCr6SbLcjHU5F8%2BuhgykLBca8D48SwbtVgrB6sNLQfbno73MDvJvtxgLVC3ynG24of2y%2BYHjHZCWOkBNYxAOJiUze200ve04NaJf%2Fo9XQtEYkLIUXp%2FmLPwW17zDKxfdUGfzV9wQnTWrayZR1VQzmLEQo1Rz9hfvuy1GIkSb7hmqYDPkP0M4dP6prTATRQBTMrg8IMrWoATpkpV9BbtxSJ4IHp7uQeZ1eBAUafzdikmhBJCYvu4ZjjTVyaOqugrOL82j5e20JYxR5YxRCU8qd%2B1kBLnAe%2BDUrAnV%2BvXOARRGPcBWxSpL9D4SQDRxkBZxF2uPg8owTuAOXuAm9klVdvBJbBhh5fH5aQSDZ8Kqysggmhk9WWYyDp88btLKu8oCRyySGUrvcRCJBk9HuPHJZGtCN3zbd%2BiN8y5eHh0bH6jJmsMvtk5HRgR8pZ1LJFAtF22sOju52yZfwSbPjbWPuETetWAWvrpdpNh3jFpCtghdMODO0MsGOqUBOyohizL5W3IZg9bQ94xXKLFbZLYZWsOxgnEyrclXTZ08n521bidr7MkSM6cS2BcVRH8NGs8DPqhtPz%2BQNQMadqT3AeS3J7waLNgZQHaZbN1uutPgmDCqxqAW5UupV0JPzvEILBg%2FKgYnLWs5ld9rb7oXSV71GgE%2BZRaeZt2HtqtdMitP9cHU2rH0bwWzkGAwSkAu5yHPxww3vNMtCeknAVVObtDi&X-Amz-Signature=cb11f000e7fb82d663970191d6fc0c137269313e9c115bf0da0287ffa9dd702f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



