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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W75Y4JHB%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDyKs%2F32gpPO%2B7EfGUbKc6Gpzkc6WKMhfnki4Mo2c3xwQIgYjlwUjdSEEezeTfw0V0xZlXxFLrnGS%2Fg7kfr1V8VaDoqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGlch1OCmeWWQdz%2FjSrcA4qwCikG4OlPcch7zOSpd5WwL%2FRn32HM%2FBzfhJM3xZwcDPpR1BZxwKb6AHixhsxxhqb0Xubch0NJeiT6imgwEwR%2BPjSEI1KP3H9QVF7fidZtVV1zOvgEFZWfU32DaZd0lL99hYY%2FkL8nLxstgedqqB7FLGjKHXTYSE0VUhSHhYDIb1oBudebK5yOSI0SBCz9lSZezxW17SpeK%2FqYWfzNjyUCNGs%2FOxyGEZv%2BRKsjlpYoDCc6jQDmx9z8R8u2pxKhdw2O22%2FCojPjj2gXQxUplyuxBjfvvFchviUDeXpiMZpvYbms%2F9R5UEG0M5%2Fq55pN6fpnRH1T8M5wcyxo%2BGP1NE%2BwTEzBHOUvG%2FqAssEFa7t54k1hPkkVnUbNTWrFezskCxIUtOAtxbBFn9CLzkplHLSErhVrW9i9qxSxfrDthC%2FeCN%2BR74IH2boVYXvgyysR22uaFiIOAW2kkRb81%2BqDVQ08wqgfjvyJz1Wl6EJ8AOH%2FB30vlq8MWf%2BoEQkW7vIKwHoZ09DPeUJBKGPvosqeNwGCVd7jz%2BOf0y%2Bh9dp%2B9BoFSRFHLN2yaBtqZV06vLStshxIZgSoB%2F7Y3euvfTsZZ4I8PJRBSccyAPypKf4cMyETKvGgArsOz6DJr6yuMIq29MwGOqUBbEZAjrJ%2FJ9jNk54udwFZFbUo6%2FWhwvcjdzy4Evl2uY8yAg%2BulwC2E9S4CCluoMlc1%2BGUojAC%2FhRy5s0QPRoPGdtHKZaX6F9YbIICe9d8ovediGxDi4vOU4YD4mM6hNLiky4er%2F3CSTJNT6CmTFSDataJA9Suz1cz6lNoFc%2BEIn%2F2QtiVRSe8vKzfAvvtc%2F2G%2BJhn%2BnlUrSgwOak5SU49MwD6Q2qi&X-Amz-Signature=06605d6095746b22371f49f322524699c7cbb1c4bfce02604d958086599e286b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



