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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHS7IW3B%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIELmCesP3qfAr9SG1P7lq6A8SEgGoniYA%2BJysuQv8xR7AiADrDVlxcDk0yyh9DEBfqSSeCl%2BkZEmGH06vMArObfdLSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIM93YZd0MMktAuKcEAKtwDNsv9gR0zWPhOl56UFfIcJxMhcDnm4ED7LtQ1Ra0gP55ZdQHMEcxnZ0pUtTmQ7APV406BlzXcyiqHUZxBYhqsCVkfYiJJo76nSa%2FX0P8TE3HWwodNmahjCFT9okhyZ6zDuqyNOIgxhwSlsdYUvR5MyG%2BlqrBHUTmxTqPkXTYLJcHk%2FTxrRt39mEbTEDFe35xxRSXC32d3aeLtTkyxHwFnZffydST5Vf52InX37v3JMf2%2BKq168YusgKtyUTtBA4lblBHkY1z7PPUNixDfAMzS6Iexcaj75tKClfnaXVyTfzYraqiH5doGyPx6K%2BARVkXVQtC%2F%2FGKPDk1eNHKLRXmDLn%2F9onLlURoXergPosL1KdZcwJYIoBP5bj2GtExjTtnkZuy3%2BrAPhggniY7k1rrfCqdRWSwnti9Mzmlxn0ttHLZ4Fwv0zbL3uMDkvnZ7CE4BbqHVhCqE2LYbyLA1kqxKoUoUWl0dGjkW%2Bh0UXzAAc8HKUTZwBlZGlJfhnL8zIrorsNDEdd7G1USY1Y9%2FH6BglQ1Zl8HbKu3gfCAbqjE%2FjEY03QDMGE3HktJa5BXY1QqPgT9CaxDICq8i%2B4dPgi5mZb%2BMthAwinR7TPjVuKldho79AJ0F1BtuNhTX6hwwmY3zyQY6pgEJxpCR8arzQCFEr1anY%2B8JdJ6rFeeIpAGdArOOihZ5BhSLjXmzO8CIdKaknMqmN6%2BPbv8idh%2BjWwmmZ4BfSgRirwWPpPqjEaVpT6j3WMzuRvUJmsZBolw2E4hk1GWywQiTRTqQu4DRrRKi8oX%2F3%2Fay5VLmmRCV2oRs%2BizYw0KF3F5urRkz90mbmDH8XvDcJnpO0peOgUElmrn4rkPOEOvmXIZ2uLoP&X-Amz-Signature=3489d212e844444f5e155141ab791ca4c02e20186a8172acc991627ad3fcd62c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



