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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSZYEOSS%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIGa4%2BgTqxDIPgXl7mgkg6in%2B8yn3mM4ai6G6IirhaddpAiBDhI7NfvUxJqE8L0aDt2GuCj8FXnQVguVpKEfw1eJdEyqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGRtdiFpohDRML1WRKtwDERYy2BVb5Kt0nNFwRLqELgqCmFltmVvO23yU3bdSZBglmDTGCnmK%2BhpeJqbTWVrf%2FbZDy4dQmJaG3FUetEAXK2X6zV4138JHFh09ncbG48%2BjKUGRFA0eeOkIl0vaEuxWf0Xie2LUugiHBclpR4ARyszfVcZY9AS%2FTClx%2BWy6XjFwechmk36K2pIeGtRRsvR0hLi6mrpQhq%2Fb0SmFrlQIgZWiQ6VFnC0bFv%2FIqBj7Klkm74awK44rrzCJoS48r8N4v4kgdBdudpFiEE%2BTrpbady1KXIJdlu0zvkTSTGEvkbtWOIBCmGO0NdjQjDEev9yFPZuUGRXLG0JvVJCdcIYlHltNrLHYjzJWamXktC%2FYRqhR4sd%2B6OM5dbDTFpIQZWzu%2FA4ayUNGoezGR6Tu1nmzJ7Nk%2BTjmZKzPY7tHJUtbXeTfc7ymoUDDSkkV5ZlPOBbrijYqNfzfGUasacVWPWI3fMr1o4kMQgWjg2cTQQgEzh2UcJjyUOsEcFMSpIOEHpkwU6aruUgNSwSE2ttjildLDgb39KAykyG3ZdgrOi%2Fo8uTcx5%2F3fUv5ezwr3laTzjrslOAmGJcEfopUHjYwdNxUpI0zOktX11vzJS8D81oF9hB8YwZ2DRxY%2Fh1uPk8wn7%2FjyQY6pgE3D0y%2BSgmZVUxShiNzDIHSbZmTFTpfZhCxe936IQ%2Bl6AyvqQcQwrMJPFOSDZTTIGYthDb9zVvoH2ResWYuiYHZ0vksLuY1WRNVRJLeHOokx95J8kKs4Kv1pag59gxi1Hi6cVt0mcWjG7k4SdTJuk48EeCZKXfoGUfV6BeAJsY%2Biad0D0YcgFoUPmCCh%2B%2FKEofVBDiY0w40aQzW9hYrEpEm3GDcghM1&X-Amz-Signature=c0f4cc8bf74a333009a939eb242324ef36a1cb17dbdb3354531ce3d14ae388f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



