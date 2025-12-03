---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DO6DY42%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICGl8HZIvtzBje1kTNm4jiyzu7s%2Fxs2rA7jTboeKlZqDAiEAlZbgUvOvfHfgbckqqbvAEhBaJ9VNkp%2F4gR%2Fbxmc4c9kq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDGLbmSTK1XCLiw%2FMPyrcA9ryh1RAVx%2BG2Y5vPyev1KfaEoBbnxLDZ0hci3jT8l4dfOHBwLCjKAe%2BQtYxfQxlnRmlgt18djJdeTHNh%2FGELkoehYYgakXko27sOdhdn0Te8LN4HvTliU1HAEZcKwvHLk2CKRWmve0v4kHbloji0VIcpFA8pu%2Bs3%2Fwz50brHPie5%2Fb5zRZnq6d3FxM4hybdroNdALwP2E3YPPBfXRFRlGhlQGvKRO0N5IORJq0L%2F9QGeS62eZ5kGIkYa6ZICDDsrbGlkUfcDGQ8EUYwerOhBkYAHBvcBJJwrYOpW%2BIUJdfMCTwe5ooOg4W53LEPY2d%2FjD1c5FYkeF387MQ4F6tvNbcfsT%2BF8G5KFcA2C6jWJ9eKEd1wTJ8IeLplQD%2FGc5k%2BVsS47g89bQ8s6SofreXgjwcM%2FRj0COwuorUIZV9UstumPviWiXff4NUOjiOiCioH%2BwDWzZsg1t%2FLDKhCD%2FswRLpbahNS%2B5fjfm%2BrK%2BTh7huC55PXrqzJE%2BnsNiR%2B8PigbGw1sOxIFAJolxcIaL1to7kYF6zpObshij2J0eex%2BmSk01f1ovyFT7MatDzBuJFAZ9Udut39w%2Bc9FMEDfcM%2Fg5Yk%2BhTEXX1HgVRKP40hbNg1X4o7y1s70f0mo5KeMPWWvskGOqUBICtRkD8iaHQuJTqYX9WShlSIUPqtXUQFlWRtVpGfI2Vj%2FXSMnR7EZojb6TN%2BDkGD9RH%2Fg5J3Lez%2B7G7m82TitPrQoMhl2Rc0DEgKzGpGZw2IClnemLYWI5lceUxJGSz9DKzNoqY17Bynkz2EuKmk%2FqI0QTuDeg%2B4J6533JNVfF1UsdXqK%2FfVp0UGtq23CcF6io1ni7yzsNpIvOxaLBBpylYBCWMf&X-Amz-Signature=27b8816e91edcfff506fef9168cf127e53a007114c8e8d646ab34b085c2caa7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







