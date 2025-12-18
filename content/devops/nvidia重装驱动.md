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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D2WEDGS%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHMCclF25Wpfulgl9GSvS1x3MIt9%2F7Ksaj2ZJGPWXa4vAiBApRwpjQco83vQ7jvMSMn8N09H1llJ7RrNLT21RrrADSqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMI07ydizMzoFJg5jWKtwD%2BBMDM1lQmTI3w9HpAPby5AqFmPZksClE%2FD7pfaKd45%2Bslm0VYbfAGNIktTE5WnVkmPwbcASRePVlRKsiOZxYSgqSYwK35NTD7j7rmgQ1gtBDzHuMBCOGNoYh8ULfMYIleafL%2FTZaTkjS2JlPq%2Bw%2BSWsBL3KAPNbGEKxjhSzMZnmMZ59i34zHjeni4Y3KFAHvBZAaNvomV8L4nQ1dAJ7Dln9WbxraNZ9cnXYtIYwETOecVIIm8nxBkaLEIP95%2FK8D%2FPtijmNGsHHqRcAzbpLUC8uNMqaxXm0UGCBEsXD7pU85inpItPcv9m5%2B3fxd5KP5YqCe6y8Pp5SeQ8TxYSAedbU3kTfR2ouD0%2BQr7S4Ej5AXftrKMc1Oldl7QiXfedT9WLI94flhvMh9RRsLVQZ6VWdH2QyKvYSvQGTUmCe%2FoUQcnZJEtB0LbSmmSzvXNPSWHReM8yws6StF2CZ5wqxr7o1vLJQhju3vBKjWy%2Fg6kafYYxpyoJtjOBufXARn62QTaxVT7DjG3BRmQ6HyG11d%2BB10hguk4dzwf08wzXPEbcAF9n13HITW648FETK2YhyPIOR3ndpIHo8G14T2kC%2FpyvEvwSWXeXkewTWYPfwfeP4UJgr%2FsmJx7ddttGcw8smNygY6pgFhqF4DrNrA7u67hYXbhHn1JKktc5ge3dcaiZ5ZH05Rk4p%2B9n6Z2pw9t5XUCmjeDJKxN0Zvx9BwrEhyvZyn1OQ%2BMuTXgdlVwLn7ktilnabzWUCApWUQCKItKMSjrNEqlPNfsiez5e1xyELA%2FK0Xg3r%2Brysx84v2hSrAUtmNOjVvgzD1vNs%2BaauI8nzNAicl7p9jPel5Rqhj1%2FMkkKkMcoNMRLXZf%2B1N&X-Amz-Signature=2554f7383f6a57603ce5cb1c0f9fd90c316eb5f57c34f9e2c3ddff3c87634771&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



