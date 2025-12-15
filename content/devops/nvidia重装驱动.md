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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WURSSPL%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDCmRjFCwIpNJFZOpDdiqUH%2BXZIdESd7CoAqnzPyNXi2gIgZQ%2BUj1eJOej06gug94buXN4AvrLb7tmVCJAX07ogoakq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDMHwypi7cbsQDa6O4SrcA8bRtRj7mNV%2BqQ38eO1J3TGSBG6VQr2kZIbP7Kckba%2B%2FTGERnG0f8FdTed9PGAyKC3UkwftW13VXR8HMAnUasDBw%2BTO02r3IsQWeDhZ996pjAEXE0knL3fznopddjKgGzqtoPKsOlSJsoulFyb0jhwgvlzrE1WmotsUOZuTQrPhhXIdJva2%2FbGPGa7q%2BpIp6Y4hflNe37GuW23Wc5Ju1F63yRRGNVXbIQuUITBkTWMQVWM2F46O11fCIjyj5PvPmI2wR8vrizMM%2FmkI3hCO5WQpX6wRMeclyPi7lZcQ%2FLcCq4hX2vgAkSwKIZ%2Fc4EUjZKyQX82DXsaPau00%2Fsovm8zlw7ALuGX7VzktF36wjo8einE2uwH0nqKHptgYwSm7ZR%2FDU9Q3ufzK%2F1ACwMoi6DEQp6H%2Bl9T3dx54dQW6Hz4OeZ2yxH8dRlLSfbRPmP2mYBQVecNRGNJcbUjc9MX0ND7XaybwMef4jq8Z1OiRUSlZ8uJrWf85s0b3ETmFZ97Tr0lgWwYURAevCJ74G3u1Jwg%2BGZJc3FwqqLzqbLShO9N18L9n2EQQIaUqWGeN%2BwEeytMrRUjvHA7iQgervMfE%2FgMUegzp3x1SZxu2DJAfjnwHEBkNU0fkGYq9XoE7qMNra%2FMkGOqUBS4inZcZSNH02U62XAm%2FrTYWph3iJx3xsRYiRGovql2HOTHyjrLySIe6ck77YnIPJ76KfFsHZ4KIIjjM5T9S3ADLwcv54Y%2FKzc5tVr4PiVfWOkS7NXlNm%2Fb%2FGKpGP20rv3dIkDqxHkmDe2mkvVRZ9xbA8%2BnJc5sxlM28yEVnS8cyG8Efz3PmGheavClNfHJZB0XuktIqNAn6I6OAUbDnXy0xdDMtv&X-Amz-Signature=b6e44423499f6d31a3b1df1d48388f4e8dcdfd32af59e62f0e6bec8b4031ec5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



