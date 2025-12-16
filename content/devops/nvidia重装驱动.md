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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MUGGEXF%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDbS6Or725afmOKyOXhD3%2FSo%2FrVhfGEQKvsEhxXEsGXWAiBDThoT7U08X1dgpKp0eNeN3f74sNs9h5DTZr8Pa39QDyr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM3NBOyb0a5hPPV9VbKtwDlOvpHnsGa260VLiaJvJVelLtKwogru6Chzaj9AY6hajnA1yWazTc28%2Fw3%2B%2For021fqvZx0tPGt%2BJDMn%2BoZ5DN83zun2S2Z8bBKDVIVkJkvLLcfq%2Fv6brGoZrLROgLWNI%2B4tYhmmem%2BjWmvfT%2FqIpeL6hKpfGztb%2FPuR1RR5L%2B%2BoTD23H4m5V6TvIHeZ3CnofH70%2BLDFPgJb0GUJ4E5BYZhgoPn8SA%2BboXZ8IxS1r2Unk9qqbaM6jfTDr%2FvRbnGSYN%2BCyiRDvYIl1SJnCVsI2NLevLY3ENyih%2B1PxlOP20n2chm%2Be6dTiUlo8bFqABcJhDXCrLU3qCrC8kdos1lJR0C%2FEVFQUgJkYVjpeGcbc89qc7PG0BspLkPx76H3VxK3A3hmfkcrikGjP5VJkA1c6JtGVLBpYoGcNQXb6%2B%2B%2F6o%2BhWHS2LhYZiOIBLW9jrBZya4uZQOn5ljEH2AQtAFHMnarDeyq6W738k6UupkE6yn%2B6nDS2qX6h8fRvWAg2i1ZMrI4yVkwxNwUggR%2Fo7v9Y1T7ZTtOBsjMOuC3IbRMgZyCMPT1QEjjfy%2FCbVbHu3EDS%2FPftc%2F%2BLfiV7GPM1Q%2F4NoS9DSAVqMgo2qz2ZM8UVrf0pMq5yCa9lt58nBEv0w9YyDygY6pgHUE0AR4frBZCz7%2BDGWSSZ85r1EGf3Bw7Y6jRkckM6hGUCmEDBcJwGo7Wptgma9sjzMqrpIXio4G%2FO8JEKiQDwpMIBQ%2B1eTT%2BlLlR2N6sw8DXoV4kA0onJjMoYhDjMVNTLqrsPvxYkSYgyBNnhN5vjaRdZCfOo0FjDmRUykfiMNvRqZwh8NCcNkgA3fDnHObV3aho9NYyO3qvcfCO7PNrW8LgY%2F922D&X-Amz-Signature=45e6bc77548b49bed85c1745a53ea5a0d6f9cdca647be2ab480f9294ef95bb9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



