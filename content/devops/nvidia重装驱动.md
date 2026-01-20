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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z66YRTTB%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC2DZmh3FKN8yFeYRgAzpjUCE1uFHsQG3GM4wrBt9qu%2FQIhAMwPWcdHT0j%2B9qwIzjLWLUoq9cTU5yXgwliWHfaB8Ru1KogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwQxjYzdmfhEub8t0q3APLaS8ZKMi4kAKD5Gi5fY%2F%2BpGkpTFJDgjadwyFrJoRzjHQtbeu%2BO0Xkdi1hVSPC4t1BkOkzVqOHshmbky6cMr%2FhIyBHbMgK%2B3rqyGk1pmnsKQDPzdteeQDn9D945cvvhkws1I%2FKA%2BDIaawK%2BabruSeSWiMRkuIx3LKSObXmTQOEBS8QlU07%2F%2F0yCi14QiuNCURaZlksJNP9%2Boo0ul8JUoqfrnpCgvUVtlSgyxsvrENehS5f0b4SkHQFS%2FtH9aBoMq790xU%2BexvAaaMGEyI5YCk5ity29p%2FQYAFuwMHicbAVZs5ZxUaZbjgV%2FcGlLOeVr6NJnhlV%2B9oZTQUQZ027pZ%2FTsOaOkYviTinabgPLZcU%2FTHMVsfI8hKFf1ngtoQkHf6s2f16Zohg9I3clxcUDuGU1L7yNHjeoFA%2BNLUZnPozjpSjpTL1widvfWFTYssf0APF2ZOfUlY%2FlELRTHgPx7cPBL4i9NQDd3R79agEYSzCZ5uoLWdkvSgr5vaaeQKM9VlA01GHDlVzofyH9vvyD0PbVuu%2FCIz83TUn0baK6Aj1KZpATYBxPPisPKc1pifrgZacntOAD6QzeEdyiFj8iQxDtX1eDRx39eaOeF%2BoQCmBmKsolrUyX32yZLNflWDCP9brLBjqkASBJHg0AeVPkRZbmqhZ9%2BfP2gY9WecEE0gXv%2FwepSJt3JlNbpgnmGdSSX77KnU6DjlPgxGetTDRZF2nBx%2FenSmVTAAjxdSac31A2DQoLCS4wHCAKIespcvtpFn1LskF7nxYR6TAUl1f3MGH%2F8B%2FHnoHkHfxN9LkHIS5V52d9U3s09u9onvK80VAz3833%2FkUsHe5OMJsfMEY1ZFtHxA8QVqBQ73lW&X-Amz-Signature=b3edc46dd0d758278322bd3d48c4fe325d39630e7c9900735a6599820f4727c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



