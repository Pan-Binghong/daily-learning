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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S227SS43%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T030027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFteNz0i0mzqN0B%2Fd9JUatiJvbpiLRkZBaaX%2Fe6dLnisAiAzqwBt4uPowWFIvFTv79ZqG555K6dIYk0PoOaugn8drSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMlDtREIBNWw4KDZu4KtwDFCyGj99sK7hlYUZtte6GVi%2BxNRIAhAB5q50zKPPqPKgxQHBmNfQOfD5fBJKXfOxBV0uNpwo8xsc6fVFs9SZs7iB13W5b0FXMpFOi3QYTY0aRB9Orgopv2LUtLevwfrn5MVtWqhKRwFnebu1XFm6F5mKKGLd9iI0pZ8Oc45iYbjkCUZjlWlYdNIwUo79Yi5Jpp4A3t4RiLKqBhyHv7oeTH1DzBmsBbRFHtRDqPf17CH%2BlPbNZ5ZmK1Ts0eFu3Jkn71wBwqihiM%2FaVCinnaakrn9rrqd2l%2Fd%2FHEby8TGsfGOyL7ylfiPskWgzawUoV%2BCY13GC%2BGJ7VLlDehjwOt5cUquQJmvZTWLtZCircQeBS373RGTs30SpWVsVMOJLzw3%2FkRh4QiWBdC7Vz9%2Fd3PoN6UnDh5RTwA34rzgQ987kBvBzA7pZfk7Gxlrz12YnRl%2FZshrk%2FbEyhwE9nvH8G0O2N89NKi3D9FjKNjRhj7tDM%2B4dZh4C9CnkEP%2F0oe0x4UQeih%2FoKtPZPsrsnDhUhl0YhEIeS3IvsnVZoYB0lb0Jvg6rL8WU6JZJLembBIJ9xgD9N%2B8r3IoitXB0%2BIwkA38xZbGNqrzyib%2B6Pyz0IaMHqeZ3RHfFkm5AvgAPZOSswuObxygY6pgHRpHxIP5cTWOg11K2LKHJNivLs1Hpwmws7NF9Esop0CXGjUCBoF6rEl%2Fyf24t%2FJF6Jy1y9dm6X%2FJoLMjg%2BJAEnp7oUL6p1FVEchEMiS5XpbQUHP4jAw%2BO%2BSwcE%2BH2kD%2Bee0m4%2FcXzrup%2BxllcnlKxbYSdwdfMp%2BVdZ%2FdeQUH%2FbSOAPy8%2BNc2sGlVSP3rDPvon39p%2B2HeJtiq4xa3w6f46wPNOjzika&X-Amz-Signature=0da82d6fbbae4fa438cb4808dc8243f2c90efbaadd7df021b74fdeb8f1a4182a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



