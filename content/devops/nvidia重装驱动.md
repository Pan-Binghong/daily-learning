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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUDHVIIR%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDJH72Ddqfh1KAbMsL8%2Fv7h7KwKyKhPoTAH4Kts5DtLXwIhAJtpc7CNY%2FB16EMb%2BLzHG%2BKOYdbQhupmU3vzZ5EE8s24Kv8DCBwQABoMNjM3NDIzMTgzODA1IgxZnivhTZHTpuUWr00q3APKIf3LiAkEvHAquqiMGpTb6d7ovsZc8BjG5dWURZYp5T1LMvsdhNdQIw%2F7uHR3zLsfo7tlrkVKhXV6wfrQ16p5h4tYhApFoRPiBuIxu3eo5rZZ0kOUgoDCEIoXLMbiDk9Gs%2FFd1Uqnf6v7EyWQGTXFZvPfL8%2BkAnDUY0ey6inNmT5Wh2BJU9MFfuVXlDGAjZDhOfgX4uk2wOkK5QKw6yKHaqgdlFVfURipT0nEAOWqjy8t3jrv4e%2FZNoCKrMxefki2ymfPxVfecoRA%2BJpZn4GIZKWe8Gbjae6C04%2B%2F6BV2F32b7fgAL%2FmxOpaAYD%2FQuM8%2FfQAQvoCh7CZPuU7Ob20zc2DxJOnQAhAjp9lW5weeZqTPWWXvBlBU54vLnTHWJpbVvJZls3wa%2Bwc5shtByxLyCjRI0wSBUUo0pN3ZaxIHx6G%2BDX9nzympY8SptIaMTp9l6H7od85t%2FF%2B497RYq6VUakKCo2AZQ2CtoWT%2BV%2BtxBb0qtEPB7ijwW17CsMip8KpbCw%2F8g%2B17hDEy7OB6XmzVxX7CJ%2B8Hr7IpkUBWWQ1KoppVZJmA7ThJiitY0VtkEseP%2FrsDO9FyWHt%2FIxSP6Wy2YVWgRD03qrBozRm5iPyKz5b0xQW7znwqbsaAdDCN9v7MBjqkAZnyPZKYi6%2FXVk7VfxcdS%2BnuRfv3Ghx0JZJ%2F%2FhlOKBckkHMYWTaxZveic9vlNZ%2BNHorB%2F8VtOrZZ3JJh0T7%2FOh7Zx9aRW%2FLVNlCyVIB6RwfhYtgg8yVTprT93hgWrwQNlm5EBskY%2BTgTuD%2BiQEPNNKS%2BmR%2FmJyNfmf0ctU4kz5z3MhNfRSHu3tXQBSgyvTLAfX7scpnga3pzDkd4pVRgkKmLUsSG&X-Amz-Signature=0a56338906b3e3f6ca4b15974d82f3fd3911ab578f66d65da2302d4a1ee35a3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



