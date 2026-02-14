---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2026-01-31T04:33:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O4RJVBB%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDV%2F4h14EZ5SN21%2B%2FMxMOBJu%2Ffrle7VVVkFl36nTpIV%2FwIhANNMvhoRBUiGAKrEcemGJw2866J9hNONfmD7dttHWmyjKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHG665vCmtcndUGJMq3AMX955T9akdD77OMMtgNxci%2F%2B8fxSHte1fsEgDZs6lalD1tYpBukERk3a%2FNSeDwuZsvBPozONSeSTSop3h%2BMPABt96aGI9IS7jurPy0rNy9d4iGtfru0j9fcxoSoAC%2FmYLxjec4X7%2BL1eWz%2F2XPhLtIwBVBQWsFlBLOLqtOVhwSJ2xFTzvVuyYKDkWMG6YGRBR49Ob8tSc6aE5qRgdIu4m4a99Z0a64IAe%2FYRZIAHKRhihW19wnlgoazRUe8RH8P28803Or97sUd%2BnjsMg%2F452G9hDDC6QzXrKmn65%2BAyYW%2BTwunfbJPhmWfl4j8zGLvneWX8tIKP4Ia%2BVxGTbUHdYJY4aTKvljJkrh5avv405nuvkFBYDDCAeqsaxOJGoTQn1SOzDtkq8InYdd1WQqQ0MyXE%2BCEqgJzaSOe2RqUbT7XCB3s3OX2K6Knt7vm2fJrj6jOHtrw5OasFqKfIsOKFK%2FbudjNTwLDUXw%2FKODM2T5HaLnTy%2BfgDjhz8P8I%2FLjhqqCOyJh89wut1jdOEKpupptfaKAwceSW5LmMC7tokWxPUdZLH9GQAS5xvchxttePyy2vwLWR9UGUk3gxhHgv4vSDZYfGL%2FCMlEeGy5zNniOOEh8ZI7fa50caao6tzC3wb%2FMBjqkAWPDMOATleijQU1quBcf15I%2BZ1Kambg9EdmiblZhLeto0wEZHEkvTQMcXKyu%2BhAX5r1YKRQGtzqDR3XA0vewNaKGyc8nqcQYMsJK74Sv6vj5zGWRu4Pk3MkR2MNAL4kzrsiJ%2FypWMV2cGrbp3WJRIzZF73UKCYthny7xmVcmadm41tg60BoE6kvE6KwVar9upBXcAbfy7n1B9FFfxUKJ41DJLlpH&X-Amz-Signature=05aca783a8852774bc0674beabdf1d1574267cab21e76fcdbb0aa637b478c85b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.





https://launchpad.net/ubuntu/jammy/amd64/nvidia-fabricmanager-570/570.195.03-0ubuntu0.22.04.2



```javascript
# 1. 停止 fabricmanager 服务
systemctl stop nvidia-fabricmanager

# 2. 安装 deb 包（强制降级）
dpkg -i --force-downgrade /data/pan/nvidia-fabricmanager-570_570.195.03-0ubuntu0.22.04.2_amd64.deb

# 3. 启动服务
systemctl start nvidia-fabricmanager

# 4. 检查服务状态
systemctl status nvidia-fabricmanager

# 5. 验证 GPU 是否正常
nvidia-smi

# 6. 防止自动升级
apt-mark hold nvidia-fabricmanager-570
```









---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



