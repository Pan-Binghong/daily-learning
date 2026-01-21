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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5HXN6UR%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCCcARN6QgckWvOJ%2BF5%2BHSTeQf9Iij3G5EIFO%2FTYiDhpwIhAOPcbLTuAsVymer8BbyLcGPphcXPMByCceFwdf1iiV8lKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsiZ9UC35kctZ3JBIq3ANHJN%2F0ojQBzAPXobfF9Is2OVeVYYeHjT96WyJyBSh%2B8DfGGd%2BvCSkYUvRL7J1ez00j1bp6bFzXYI7ra0peWV9tDRKANG%2BoipzKX00X53xTPSLtN%2F0d%2BNu3jDkVd3TiP%2F34qVy2gxhVq0lyrf4VB3Dun5yQa1cx7yt%2FLnFaUCwXwSTaHLe0YGSFM15T1pMXj2b22kEL908Ho6ZEJGbCF2toDaVq7QXqErEVgcDce4Av5yWojm5cRLBBQKFzMoXB4MWO%2FB5mUTrdhF%2BWs3UIJ7DtXJHix56BqveSeODT34qat4ySGApPIyq7glXTN8rL7eaIZ7AxlS5aId25KR%2FIjsEHlIUcvofvTcdM0jbagyk0jZLll0g81Vp3FKDtE%2B8stLkH0KGL0vcJOXKpRBO6gSXVCdZJT4sbZwmVCdkUNNU5byTh42Bt4OgtDOzMNjNPHjf4pEIpDYWKrgvLFsZnbu6q%2FJGYGTt2b%2Fo40M2RQOlkNONDobYJQmkYQrMZH4TVq4b3vqsq82LAnC8vtxjc2YE3NiqJFN9Lqf%2F5L3vqhA4HpN1yuBe5GG1fuuB1%2FQ%2BBjNuUzkYQ9KvVDB7zhjeOdCxELrVmvXmNFHAxY%2FHMBQW85cR23YHq%2FhtEXDD9eTCj2cDLBjqkAcZE3E4g8Ij%2BNqaa9D9M4l4by0btQTeZUGPVxDix%2BsLGlk0cLzPS50n0fSkV24vA89Fhu0u%2FglFOeV12mXZRygw2Ur8UnQZk5mt%2FUJXGB26w0BiyIFMgbXHAMfbLo2Rm680uIey6MUwaUyJyxX%2FL8uLu3w4OVYKYL4Tlk%2FVie7D%2FAsWuokxEhWJ%2BRMPMZ6sTXe64GuNYZmrmaRzlKo5w83z2Z2eQ&X-Amz-Signature=1eaa47255c43a6ce8ea27e6e1d5398971186f15d77086c9a198cdc9dc9026ad6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



