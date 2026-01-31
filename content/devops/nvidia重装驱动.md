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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7PONEK3%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9WetykdZ%2FkQaMZBaPvQ1z0%2BrijoegArtcYTZnNcE3AAiEAuw3BJ1fSxu3%2Byao2IzJOaaOYvxKnVSetPR1iKxQQD8kqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDnGu2DeKNaZ28Q%2B3ircA%2BXvyynrSU4GrBRLyPwr%2BxOQxY5n12jhOIVRox5o4TqMcjCYmgPcOFzThIghuvdmA6lgM81eZvzjVnHCYTy0N0h%2F85DhSvFpFoj4zlteik9WEIlM3D2VRnvsPMbMRDYRGhdg464bhTvmLXTfXlfhX4UooIu5CXx0aL7vky1xbKngBpFOQOMXXeR2zh5Yd1KYTdv%2FgyI1m1McEl7RygzixIna825GfyWI2S2teBVVcpZMg51YwWydzmeyPXmMkGMa4MwU2sI%2FM83VHq28ot8tpU4BEeqQfrNM5A%2FGnb%2FVwLFhGmb7RUt29w%2FuX4S7DGjFfReDM6Gs8OqBXqqNk7KiVj%2F23Wu6G1JqpMe6UF4ehCUEZBlsN%2FmlJB5D%2Foq0wpU1BnHM7am78ELeXnnaw3HE3tsjB%2BsfTIOsDQ1%2FdPlz6VwaULiN5sgtnFLe7OE%2F5CiMkV3o%2F%2B5WRbBxrHYYtwOKqOI7d%2F43nek837jmS8bHO6aT%2FV8ZV5DBiUVyADdjTdYZPkntrRRiKEn0vjZREBvQG0WFwEXo1KfdcQ3jMbKCUZWOcz3rkp8VWH66ORMm%2BzCqXoZ%2FFDXIzRBpoTn8T6G0fuxJOeIpCvzjcgYIIeSl6RpLWqHrLypDfsFbymg9MJXM9csGOqUB1V03J0LN1KsJLVDun6gMd01D2lepFnfLcvZtUTxLu%2FbeEyALKRYFSQDoN4CzrzkCX8hYOjTaM4T53%2B6%2FqH0JyQGoAU1BjH%2Fe6E1Kb55dSOUZN%2BDM02XESrZi5Go32T1Ll8OKlarfUvb%2BE%2BnVx4k2Sbz58PHfhAjAjP%2BMK0HWTNZD%2BwH1%2F2Xoc3tc9FSySqEaJOhVJjpV68tXRHl6W5EWR9lInhFl&X-Amz-Signature=5294a547d4933c5978bc9f1fe3d515a15316649b57c16695583b09207c2d2fb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



