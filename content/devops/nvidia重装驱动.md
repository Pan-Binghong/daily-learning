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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLN33Y6%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFgBDIKhVYgRbJvJEN1X2hpYJ%2BFkG8b5f2F7WBmD1HAGAiEAum%2BMp0UkXDy9nldwLok2hKmPbzOKF%2B8bt4SP3HxkSLAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFTxRH%2B8LtNjenSJWSrcAzS%2BgBa7%2FBky2fqvRsgymDEUDo7EeS6FJYVvxH%2BMqYaIQ9kUxIRlVRZH5kRGAojmcw4b44Bb1nxYF9BcycK7IYdsGuoDmC3Aw67N4PLy%2F1TY3TD4XyG0WPaDyYEtHeR3c3JtekNNpW%2FyYWCVH%2Bt4QBqU7suMTSklGuFfvDpvetBHYDM48uzZWpCMRLTNEBoJaX24tNiZOPN2xxtfWqAF2Y2I%2BH%2FpAUqVR5hyS3TtAP06iJGJK9o15%2FjT5Tnnk%2FBAYIrTnQtEPZj2MSSR6Eu8ae0dvzfWyqp3Ynr7azsflPqUwmHK6RU1HspvQ%2F6tdQKM78CHy9JJb3weS8tX9yJpO5n2bEUTYFlm3fCmww4z80gjyxf5miwrE5e6UDwFGz3YTUpPxy8MM46sCUb4%2BItTEQCEtuwWDc47uM3pWk581W6SRF9s3ZKD3e3xPm%2FHYH4IcVpjjWqK3BxhmnU1QznGPqAqet%2FhzkvCo88HheRiQ09kSplg7fEuW0SHVjEkXAsYCsGZNk%2Bnl5%2BzgR42Sa41EvW8CasZ4EufozJpsw%2FcW36IGm0%2F4ygJ1n%2FJ%2F3efa%2BNF07Ej%2BcJPDz38jaQIGNX8dULk%2BQW7LvcveZyf%2FIBOlhTryPE%2BKxHnqVwhLTv4MPb5hssGOqUBPKM%2FeyeLhL7E7vjgIWzCUrO0Xl1NQVkvkvc5l%2FfRy5%2FnAW0c6nQoX4fHHUHVEXcGe9l8d6feGDUlj0N9CS61qYq8gVALyt4xgaPqQ4QDjJ%2BFWMGlB%2BWRJz4xNrx6JT5oAq684GsnlMKYdORnHvUZqtWPXGrJQq%2FD%2FvLwDpIEIkAYCSESw3YZMmuV2CLatkwB0R5vTb1KH8R00K151naefO8%2BG7fW&X-Amz-Signature=867ee9ec7f0c089d79bd9b749a9ddb356a1711d1f602cf4f3b1122a0b5505c27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



