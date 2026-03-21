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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YLGN4VJ%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIEd%2BOZwQuCU2KEuOGWBBWIYxAq0rRvALSFMElWceyp0UAiEAl8zkD6v%2FWm8IKvLFtl4SUV2H5akXfu3WVfVLb8PzxUcq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLJOmWq7sNmhg8VEfSrcAxNLw%2FBaLHEduprf80%2FQsDN5vcqDn%2Fyj%2BWGc3FuO%2FLwOoo8KsaZvFVSNo9va3jvXy%2BT6Jb5xdqAzq4EUbguwxgAhHv6f8s7Mz1kCyA3xwEMJG5qSmmqjRskSXCKsxgnO666QHo1LXMsSn%2B%2Fcgagqnw4rknkqUmvg23mwSAASUcnlrw7%2Fgl2h7rNezUvT9DFZUealzlv%2F273uFdiOUqow3K3uPJ8fq1S2Ssv03H7xi9%2FipHZHCW5nDBlobaRoUqUJ2uoMrembT1EflZcyBhr%2BKqk0CsWKollBFd8Pdp8f%2FUTTzg3fMCCEywPUThla%2BP1pA1lb0EW8x1lIqpw1IYD7oV%2FsEeU7lrOxsVoPsdmXMjQ9aBO9N%2BXthUw%2FULIZZEN%2BRqEPMCOZZKWOIQ%2FuRFI4AOp47Dm3rlwhLy8%2FdfVqL5vDhdzPNmT7oWj3Z%2B59fYjE%2BYPHiKIJvENlEjSGYFt5K5Va1O%2FR19quH4JqlEtr8XrjOlO6pwX9EH5b8rqQVS4%2BjGYluOfABCZMXmthaetn3E%2FIRxzJef%2BaLx9hgUF%2F3tdkRaUwL2N0r3jGiXOO4utI0YjgYP%2BnKoATZc676gZc20S5CJLlKOhGap9XDyP8IB%2BnYXPLDk2oeoISt2HVMI%2BP%2BM0GOqUBW6v4YA2p%2FC%2BWqJpmYEq26AR46Mmd5Fqr2cDzmBHY4x8%2BE3OzBF5ONQvBxeS%2FMH74qSUKU9w2P%2BVZpkfB53yxm5yo82favAmfLQJLDd9mrzEVCvomK9z1rEzAdfyt37lTLFGknRzE8CpVwiz8OkuykHuKtgXRkxhh0zxfXrngSaDBMMIW%2Bbv91G5SEYMPUQfrWd1DdXeoAY6Xw%2F%2BN%2FCtbXnDV8ekM&X-Amz-Signature=498ffd336aad8ee826720c11471780bd4cdc6e3b95d5d025cb63666005eb48e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



