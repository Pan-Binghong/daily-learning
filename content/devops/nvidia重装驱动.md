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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAYP6NKM%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T032048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIAbUJ85FJnD748PVfYAVW2a9eruT3IO3W9rWO2f%2B92YBAiEAz0goxL8gnpChGh6bDKMxOlY%2F%2BMB6gWCIB0%2BCZZIqmooqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMo8ckRhyTDxCeooPSrcA%2Frwrj0BCDwm%2B4RmvfMnOZm%2FWYI98%2F%2F45R0j1RBK%2BEtqjZ%2BbxP8IrvoUbOTCtj%2B0Tj6z%2FDhYiTeBiZVbPbzBwrukrFSLk9wsQ4UPtI0MukX2ft01c%2B2dKrSp1CvlNaANoRCvR3E6JeGupalhQws%2FHpzEMkHG9sw5AMBXQLX825AHPScERUUdrnAVoCWGR1geHh4lwqa%2Bo81CUqF0vq9GJ8oFZX4qepM1wGp80MF8SXTg6olbvVdGCD7o%2BVQEmMOq2rBmKUtDVVVYvKfI1lT5ZtV0iG0F6DTib1cczgWUCceMdJeP%2BwA2ABuCCsRqHLU9o6UqetKxvFb2N7tSoIBtwUyZqw3mjj04H2N8PwymzIb5qy7hIMFqcfDsWRrmZWqxbQlRqmAOyuBDmY1fbD0mp1b%2B7iiIiDvkPIxjmKxQ0%2FxsTcCPKhVwelNQNzPDAguPOtmv12JRWIEWPMHj9wnu0WvRiAtsVqtFRMfzCho5xfzeulWDhSkXBijG2YPUvHIwMk7qEsSZNYPfpaXCOO3klvvyPtQWvRDESpjgxMW6fGz1%2B34KKQec1ohY%2BdHmQnsJYjAjT7GCw54iRTVdQJcWNeDvjD%2FzcEToYaqOog8XWOXHOFmBk4AZcdqFAsZiMO6Urs0GOqUBqQSBAfxIld2vwxQlCKFYB50dcnjeJkXCdxRFWdhF7qhoPJxuucIkQPp9SaSNhHoBLjfkbY8xLkjr8CLh5%2B2Gm6%2FJiyco5lAzC8aG%2FXxefSQYs0b3dgaWhmLu6HNeFLgnErSLO%2Ft8QHrujdebyCxM2jdWAJFjlNP2j3JvnYckP7HK4u%2BGllqKBA5Q8%2FdJEOuhKQY8vuA2owb0R7Mg7fZ4b9oAjXn6&X-Amz-Signature=180ccdd8e301988462c260b05313a29c59d2ce5b4fd364d6b3a68edea1a13a86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



