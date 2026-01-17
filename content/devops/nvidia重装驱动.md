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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNXBNO5Q%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyKkYTulxERWu3UrmsWcljFCtxfoUtTeM0BjyaXgg0nwIgAl3d658WToIA95URVEa%2Fc3e%2FilVUx7P%2Bj%2BuQxwDxe3oq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDNNBHkZE1%2Frc9cOW5CrcA%2FzFOpHbgdOh9qPGqXL%2BwCc4T94PlvDLnqYTA3uPikE62k7Te71tr82Ym%2F%2FXwH6mSt5nTXgfuTzkRKPhIrAQ6ty73sw9rB%2Bw2%2BOp24nknUS3iUxnnJ%2BKDZxMe6GDRllye7%2F3pzTo251Zv4i7tMC%2BSqRrqmb4Fd1ZDbEm%2B%2FAIQeFG6DLyvOawZOnGy8ruSY28YqBmYnqQsIYrx2U4PdabIU8wWIykm1LN2A65J21N4Jd8YKRohGpLIoK7kIhmsJk2nwkZq4Qr6VN4kkXRFamSm5faNqzhKSz9kGO4%2BESzpwxxgHJpuZON%2B0sHlwM%2BCCzapDbdPkN3HKxJu14e%2FdU6UCf%2BxFEy8s4P4Wxw3c9T5s1igKm5umSROdGFLmILGASfkbadjCM29B6wbgHh%2BcWBITJS0nNZTZcYlYiiYeg23iewJXwl4QEMDN2l0FJSrjkmmoUS2krroWL0WctR59VXKyi7cz299o17VxmQRBYN7LksuDudfUcuH2xdGJUrB2da3o4nnpzvNWfRxFDNnC2kARS7ESJ2fj%2F51KzuNNDe8VrbPOH0tlwr8p0Klt8YhRXMrpI394xep%2BhDqcEOyybqQYqYjfgfluURyBWKBYnG37AFvphdULAaIlIG7PGBMILSq8sGOqUBOmXveJl%2BHqOFPaG2N1dKC5ilaQkAj%2F1Ct2wgTIUZ7XFZBG0Ogp4F9ZNH3vx8dBaXeTCcWNsubTV5VYGndRLrfQkOY2mUUBFiulSU4pdQB119VtkQbnwdIc6El9gM1u9WIzGbkY7nxo0HsOZdrunDj895hrs9V8%2FmZa79e4zFETH1%2FOp%2B%2Bgsj%2BcygY9MNw6bOf%2B5aMho3ftW9B360mdle0OeEoLkA&X-Amz-Signature=587413e2e3bb7da922a6ccb85a95922e76dcde6cb1b9b124dd8cb7007bd432fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



