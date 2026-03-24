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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643AM7MVJ%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDUiPCxa1g3x1zLif2KNqR4LrFVnQb6YhceseyhjRWyKgIhAJ6kYTBBn4TxKK34K3XpbS%2B%2FEx4X3EiJ7QbmIDbB7D0jKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7fyimrnDBBpTipkcq3APY4zuoQRgcQ0k4yMo5IsVTQo4kOexjLgSw6tUsiBWVdhTiA%2BhTkiAUFnIUW6tUwVD2QqBclm5XZKKswWIVCJblYANOHmkFzQXRgYQ6Ps4YWFB6kP57F8XHygLwjPGJh8SE7ncjeBrO4nq3CFeTndbQh%2FYhB6dGbcyzpFcvtl7ZhUyJtbDffu09uMH9Mx8bu7x9yrj%2FALX5Ylw7cA1v1PE2gEBuAx53nGQ89ZEynD7sG678xIzWTymQdrRBQhEK%2B7DtqbDXYMblEd5wBlHcw%2F1orP34uIBr6BBFluqcsHD2XvJDZ0RwFyypjlyIzAjUh7CWl2xbTUlw96dIkb68u5FPpmS%2BcrfEX1bn9Szk2ApCjOR0I%2BX8Ifyl1zvN41da1ejvJQIwbE5Iah89%2FKkCnKpc8K3HOGuOAw%2BX96itUeNsF1%2BuEf8%2BcgBPzJweOl%2FMGQkH22omqNqBUWnc%2BDVFt1UNE8QPsrrnKVXliX3Dq%2FIYaAD2IHY6r%2BnT72JdCNQJW%2BQcADKB914Dr5lnHGg6pQTcEq7JKDNdTbrhE1IJ2YoeGPeps8uLonpKLQ6g0V5kcLYZjvlbjMoLFZkvp%2F%2BmmH4A%2FZNl9%2BBJrIdq9o%2BFOzNq9l8zQqe1HenaNkNxrjDW84fOBjqkAYLHAmGV7%2FG9X33YyTTodvNCmSrdxXboUCOmbdj1%2BXf0cnx5bR2rpej0XJShDQBVbzrN8GHommxoQLO91IVJJAHdRua39CyFwub%2BLr8hw%2B7vpE0UK%2FzhAdi2XdUHZtqBldoqjn5XOdZP%2F7365jq9QnKnTtQGFi00vaDgNRJGTf8yqVeoJu9lbERuXKVjrG3DR5W4KCw3wxc4IqOs6pAeXYPhyK%2By&X-Amz-Signature=6fedfdcbb1578ba68eece337c351afdbf5c7b8089ad3b5210aa08a031700784b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



