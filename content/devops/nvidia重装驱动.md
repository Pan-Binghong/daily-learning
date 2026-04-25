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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUG2AQ73%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqu303KL5Km7%2F8XgyG2Mr3MI6GT1FYADfyC3%2FdfXkliAIhAMvFkOvP4E2gG3pYa6J7Rs6TKKOK%2BatRCTIQkJ%2FfRS1qKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx4jFue9NlPj6jIgP4q3AME5ycEMlWR3SN6UOBYznjr%2FJXSJpiRtpnVqzVbslRxx4tMZFs9ieR%2FM%2FsKB4Jf%2Fnd8Kb%2B7h%2BhQJg77AK06H3fILuNiyPatNd2frXUM1yYN8H5BCzlQzAOZjBeXq3PHgkGuXA6Q7uD3FdB2bXJTXAveDU7fJYl6%2B8Bh4KyVCm1qWFWD5XYAeqEPSq6iiFDr211Pb5dx6jqFP2oxGTJQnbJLZXfcJKdtj3WYq52a2oxF316VMxWjab37f8txNnu2sFOPRc2wUlx1incfuW8JHF1dNCQEThvuraRHYk4VN0Fr9sBEhuyyppzfzJDviIDPUE87PAO1inYxF8Vg3R4OLkcCF%2B77%2FXkx9X7EFHVtZCyYFTa491tsch%2BarYlBLijeSuBMA2u74A7N1e2%2Fz570bqJ4hDgdRiNBCp47DB5IZMwMCIkVF%2FFaU4YBZs%2FUk1r16%2Fbsp0sm3%2Bvmsrs%2BLebDTmh0VtqgWHZEL9tL0LLklS8GU%2ByutfLiWVTmrJrffLFZALfvNY5rkquL1GC0Nf%2FDlWjAjxqJC6%2FAsRliDLjQ%2BdAmPbdz48qGwiN8GdKMih00NwGjteBp%2BNzKj7VD2m3xoxUVqWsbLjq0nhVzoHB1mvaihoOJFhSk6JSuPa7YlTCq8bDPBjqkAcD%2BhZ4BUp3dAHl8AXJEbTJgthaS5VNHvKHRryAt8HPoCRCFKt%2F746%2FJWJp923ByoxWwAzpr94ocO0aERQZrjEZ3i9JZkyHDvLu14mdiyu6IB4Anh6qK43bMmtL3NHZLOsidBs2Xau23rODpHmm%2BAf29QtTW7xc%2B24uw2kT1DhkO4YoZ74VKI65sLg%2BjF0ukUXup%2BPeatZ17%2FJFxHBKOjU3lX0OU&X-Amz-Signature=6665d3b29ecd883130779de3b344ac0ba0b11935a8221dc25e3a32490acefe76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



