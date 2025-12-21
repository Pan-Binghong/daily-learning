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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KGKPCP7%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIFcoNPQI8Oh6AVYelk8kFnP3eWjGNSXzC87NWgOHsOOXAiAtFbaZREjmEEx%2FXtE5ZImAFEFGK64P9%2BNFxFH9ClqZqyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrjoZCOhV0FY6jRoOKtwDzDk%2B%2FPz5FuTjzavt2Wr%2Falnuml31UFPNIXC4L7SHnw%2Bc08VWDnmrqr2MNgUoLl6zNRERBoBTVvA0LuuVbSGYryJ2IYkfOIPIDCWOWAnMnJpVbUd7MoyxtKRlRkFfcxsXIaBevsP%2Foo%2Fz70ET9V7U%2FxhqiM9%2BbzKOecb61%2Ft8ix%2Bp8yOlA86PrAGXN83k2WPeUODJbwjIUMcvrO%2BVkPutFW6HM5Y8pYG7hpISt5xIKoRiWAsinE0Qce6%2F8JWrqGlLyq3ivMEK64nTffH8oQSvNN9kpEVH%2BlPfQ6OEYTmV5kliuuMmlGngHK1DC3e9fpbeBZUi18p4dL5b5fzKqjZJy%2FbP5ugWmK2N%2B26%2FOCaT1aBC7njML6dW7EKFIy%2BFXESR5CyIgDKPHgG4Q%2FvA2%2B03IGktypAGySZmH4dzisY01368KWUn2JxbAydoihJXHZgQKOU9Rbv8D7HfKUL8YndthVeOVdpmMGHy1JpigK8wlGfunAGr69GIXWzwOr%2F%2Fzq9aAhlLBGmDx%2FFt3wo6Hj7d2dolff3UjET0E3%2Bb%2FWexpG8aP%2Feq4OBy1fe%2Bv1z7FmAPFCheQv2GsWQwNRRsAT6sxVFblYGOVtH8TIzIP%2FhM7PhqtKigSkGBPLRA97IwkPicygY6pgGRyuyq%2Bz575%2ByoIVYi%2By8cVarec9m5vcUvtze8m18gICaDPg1ezk7%2FkEc27djwhSZpqI%2Fvk7OfQjMc4rr7QBnn3DqfUR0k42h5Yx83NRCKeuoXlAEOI3EH6C0Hgl%2BAX7FYG5mzNhhHMvEE4U%2Bga%2Fahc3doium8EnXbWe4IQKkYg7zQnog9f%2FwFOQDJwTK6BBmoNVf0nMZYXV39%2FUiJN58krr%2BMg6Io&X-Amz-Signature=59fdd33dc9a8370a5283a01dcb96fd914ca834b3fc6e54cf1d31ba126a5f1a13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



