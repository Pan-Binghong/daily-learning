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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CGK7ESP%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSE%2FBht2R19a%2FX%2BhaQTHTLWI3RXIi0K3vixIzoP6JP0wIhAJo4Q7MLM2hvLO54BNrN%2BUwEqiedpUp3QO7U3XX0CaP9Kv8DCFwQABoMNjM3NDIzMTgzODA1Igwdf1s8kUZiHgPpCi4q3APuYcPvWXSTY6OdxlSsKIaE1hty67u%2BYSqAtX%2BBfCPmq2ibr4gr7tAUb%2ByHN0jU28Iv1sXqFvW9YdEiJcilxsboTzlmYj7E9vLabqtOZzsyXEeO%2BKI5kgk227nLBn9YJy9oz30uVhnV%2FshDfwU0UonUU4ptovbhTmknMCipjzSivw6qp%2Fyi4g1oBba3K%2Fpi0Fl%2BFciNa7THQBZ1qhchgEmG6E%2FpoiWOKpad4fLIkEUxE0SPph4jIkJfhpSjApBFIV2WkKbkmwueeBPWde6%2BBk2BLi7b6ut3NJVhlCL%2Bh7MdCe%2FZnrsG4q74oriDDcfCs7%2BqJ%2BlzrH9PvwGp6N7hA%2FSo2aMzlZZTzaBlhmHplJlTRPedbq1GhNduPprsZtjZJcYdMjPN5exuN5zfXRSsP%2FosgXPH4BWYBhimz2T%2BK%2BV0qDawc%2BqcIrzscPJkXWuoVAfK9bVKJVFAdTyl88gW%2BoJ4cfUL0ryMRHrwpOSupCQxXYhq4rHz0pnj8He6kbch1DpmQKTE4C9Tqb3HYnQ3atcdXL2firI8hDV750LXAnqA%2BKkLfPlGbaiIZyozpfSpVKW%2FePEx5Pfkc2s8KxDZZ2IH0kWttXqvpl6JHmHp%2B2WkTLwSSxLdDnf98%2Ffw3zCrmqbPBjqkAXGz5a16skdL3nV4xcS%2FpnA3YphCpAI0XARrZhKiaGUr6Zwdlw6Bp7pi0Eg7snj6v3un5RugFZkrs2zf%2FyNhGrsFcQEJFj9xAnWePlMwCXJSv%2F5kCrbJ7Wbil0lIIRuIfdzmccvgU2TGMIjrVVieKLHFnrknvCEO9h%2B%2BFboBVIFAEPdmpL5B59Y1Fsq4P60e0DAIjoLp3bPaszyA%2Bnur1gmXmxFn&X-Amz-Signature=faddaa50d39a20bfc37bf9ffae2d2bcd1eff35a722b7dcd10a4d459f49b60f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



