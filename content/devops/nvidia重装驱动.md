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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2AMCAAR%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHZxj4eIyPVFsNojJGJSZEuYa9OHO3IgjV3DX%2FDUb5MAIgfWGf9Tsslar%2B%2BCDqW1G5YODaH5lZSZNdjg8bwHPHP2EqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTiKz56DSKOu7ZrEyrcAzS%2BUOO5yX8u8mVtG3V6xl%2F1gdFPTsSrLnbQ4YCJK%2BT%2FGfpSjcCWfwKPLLUf07PfQGdcwZ3Taq%2FB1AvG87HvJ1S22Zc0mGfLbNkSubqihu0NWBSMfIjz0c6YbFWJt782kUp%2F%2BdX0b6O3w25zjz39v6DrDezl9WspiLuEYCVKxuf%2FIGJi3S%2FUHhm7gjt7Xu1XD9o45f5zEB2TDCj09XpNC9BfjSbyvLXiNacBFta5IjWiWl4I6MbjhW%2FCHhwBMVrMn12a321YDtLv68k0RaiHuPi3Zkfb%2FNldcYDM9k7JBvlwrM09JXJx7K9nWIuZn2JT3QtqmeHqxsOlGTuMcKWRrOi0yudXn6ODP1TsUrJ1%2BOA%2BzfAAl7ZyAxKXj7EglxacwwCfriJ7hQ2RVuYcOz3aWB9YsMMItr7U0xCWqvmhbqDVsJLEPFCoOKnKpNlnKRmq1t43V%2Bml%2Bckd3E8bXjdoLQ5WNxwljaP%2Boze3E7xDE8DhzuGSHXHQEZvLl3YjJaEsEesPltLEN7uWqtnmtkM6aUvbUOnzHY6dbgYuUMIEbV%2B3T1vKRbYEPcyd4WhJVT0%2F5gGgXc16zz9DTmvl1XvA5MUfiRs2%2FTFM9FfF9QqrJG42Sv3gPmogmPyHsNJ6MM2gx8oGOqUBPUDSXI50Z%2BkpnXl%2BqlNSLuJFi8dVSIj0ciMbpWpCp4kbsNbPXUOSjQYIGXtnjY3xn8cH0hXR1a62LcZv%2FXThKwvKaMBkiurK7rMypZjoQuwV6Aeo4QxAQPIPTlf9A1VI9il0RlfUq99l5XK4NJWvevXF0AwRyxlEjxTnMmkIPCgHkhzxFHwcfxePQmkFVfqs%2BzcemYZIC%2FQI4G%2BE1KaFxi4EwvIN&X-Amz-Signature=4ec13b04d5931ad1557e0687e169012eae06b7a7a06c221f8cf105b8e1723c23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



