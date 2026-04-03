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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZO2TU3ZL%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGp74CgZS3OKYawWuUOEAJWUKc9K3QUI%2BUtKORITrLw%2BAiAOtjtuwHIb7ZcTqvGorrqeQan1Sh6kdVEo%2BQOq%2BFwV1Sr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM5ytg%2B1iROltk3ujWKtwDmwbMcRf0Wg0GQkvBm2wsl%2BAXT7bZGXlDJstU9686pHLtpxuXVSx%2BxTuzxUli%2FzinOqlFA%2B0%2BwjDOco9CIHmDoiHrLp6Qh9NjukOMugqGe0bUowOuuVavkbRu2p4g82mfH5kLUGD10GbkOcc%2BqA0crU3JWmd7vk%2FxZgdYW9iItrRUwxmOM3wUN06vRC8nEecUck459ihgFHpm88m1HbQ%2BMN3a9lILE0LtMJOW81D28OhWMiNjeCfJ%2BJbynuj7Vd6BQYqhgK3Ywt8ieqi9eEKtcxUUA65voAqMhSygqIX7slKa58I0Jpj%2FUewdN%2Fh9Q631i%2Fk%2B00wf8p3PwQAob%2Fv6%2BcgMyz%2FA3lEWN5K15A9RP5kkhM6bQC9Wlf8EEY%2FmZhZ4NuOyeCo7PMaGRynCA3ZeEeygchnrLCZ%2BKWZCkMHYIRAehp%2BnxBxfMhA2ON6Z0A83vlhp4rpryIWeg9qYdsoUrPT9ay2JXl2Ql1tjP0V3hUzVEWpkN%2FFsI7YkgBgurHTt7cbfmIKDfs1z3KlEOmPmuz5XGd%2FGBQ%2FqU0jqW30URUpiVjiBYwzlCGSY3FVBzYyL%2BsD5WGPRA7e4ENH9ZYiyz%2FjEXBFSj1a3EigNrEFZwXlzBoiDxA9yYFoHzIIwqK%2B9zgY6pgGrcxqDDWuv%2BF%2F%2B26av4WHeLlhxPxlBkismSQ7Nqy3V28LyDL7XR36a8PFAWFCYmDPi4RCF7b6mu07yGkAiXpJ%2B7Aly%2BZldcqQKc%2B0SzfLuxxeH8z3u1WZulTEAnFVUFAPyOJNmll92OiDGy1gBT7zgwem%2FNoub3DxKF1ddApIOk3LIJa2wyXB%2BNYVhUXuuYpCaePTYak1xnMGbZ48yimC9z9lnek2%2B&X-Amz-Signature=a229485a85c633fddec1419573a2f18e63c12e74f4ce6a305799fec376a3cb37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



