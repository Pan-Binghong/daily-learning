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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJJ7OGTT%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCmGQW%2Fzul5ZDPYrIQ5B9adeMubBunGLCVRBOpzjruV%2BAIgbSwtXfZA2sxQE47kSyyTcPOHSirj%2FuhV6v5dUlQkCl8q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDFZ8r2F113M%2BKRm31yrcA%2BE4o2WcM4XPr%2F0euxzmbPbg0P8wGCINemBSy2BDCUalTqHkZ1HVhD31432dcHCzCF9zwrTmqV74jmVmL%2B%2BiwYREYpYSiXGXMNfJQhrVVwcG4AgM5K9t8btwpLeKMJpxgn%2BoR6ePmMqEkUJU3SlpLc7J7IYlYqA5YPMM6Cq5d8pg7t4ump6JjZVAY2Hh0LjRIctFaJ%2Fv4H7lfgCfZiY0dy8wtFe%2BQe09X%2B6CSr47%2BXU1BgILHEZTy3ZMXTzixUfUob%2F8H7WkMn8bucRkPVbbivIk3sGbjZBNAsTk2zx88u%2F4DNedFfMNTNfRDZHON5AfVkA%2FCzByAGFg5b9mruhLeI%2BUksCsWCFb2aT%2BaRZirFItiJOPdEiwwVrVAJaq%2F31wIM3o9S6DjAS6RMMSFL4XNuJBdg1EpTwDWAqGwctD2EzgyXPdHrhl77sbyPgd4Ez8wGP73hX6kHXZG%2FYeT%2B0cYJrYJEA15QQiX6IHkPJKEbYS%2FqGgEx5QEBAFdlbfsz0%2B3xvioLZsq7cYjP82LvPQ%2BioWuFZdmbW9guwf4AV1GjaM6RqcgcDjCX2H2F3KrbCVkuIsjKpVa3dhxYyUS5uYxmoe0TjRJHbygoG9BL1%2FVGmodtcKk9lYM%2FLul7HEMKHvm8sGOqUBKzuc%2BRq58rmGHHydos%2BNKcIlZ57mYdnZXOsmk2%2BQ4yRJFuNjC03%2BJbqyxpjO3COrJ8SlNuSkx3Pdbrripfk9N%2Bvaooo%2BzR0tYIqKtwkNL8S1t%2BG%2BRUg70jm3H003hPNtKMg8ZgwC6pgYWbAbhFkrY15P4LUpd2j4EvgOZJjYaEybyIVLpdbglXQg%2FSHjCP1UuOwlPmMXvrnniw9tYZuetA4skWY2&X-Amz-Signature=5b730e06412f74e7003710bf5831ca334bb46cde9f8dabe54a17aefc860e177d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



