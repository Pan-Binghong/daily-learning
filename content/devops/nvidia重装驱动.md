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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVTOFEYH%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFFOYI0xQwln4KGaK91hNMcIwrR0%2Fq8bEvg17etadp5gAiBc%2BuYl%2BzEbnlyqKPlC0%2FJmH60%2Fvl1U52zqB8pWzSOkUSr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIM7jg8TRrBrX3ccuZmKtwDyKTG08dNnmzTP80BM6Gyoe3idDfUrqDuPQPdgN5sFj%2BVtXQFrCMsAgnPKluWwEuLVfdDPjaYqlzBGUL8dLzvUte3iWMmvcfwOubYYcsJG%2B9idzH9ly8JpOtpbbcE0zNZncxw6BEWQDILmmGOsCkmVu55WcpYhKjoJ19oA%2F%2F7QFLGedcOXsPnddv6ZtQ5o2kMgbBTX5oS%2BuKxtQ01Ar1qND1%2FwQ6kCIGEJOstV0QiSgmxQ%2F9sqCjmQS2proUBIP61EZfFb5Ue5kxmAWfJTRFSQevDPk8yZ9YGvfpNveSOoUJVBWcjy1fH0%2B7lH60chuGTIpyLMSlegojBjyt4RQImiw7m81a%2FvZyaFFiT8yINugAaFQrXXWz%2FiW2iTQdNkZyNPwychKTN0ROCY5LT60U73iyql31OFfnLLtmGMAQT07uL2gT8ZsChI72qWlyl4AvyMQ024S5BsMZfj8BzMUDYj9uBXpGk%2B1gseJyyq%2FMXbB5CQ7YVHbA%2B29Ss65napWxTkH3rSvJ%2FE3drC6EdbFK2mxqvteCFeeOz2ts0lNKeMLHSZTO29BDnJEj4iMltxk60%2BB05PFK%2B3vUfN8ebfrJXMi7DOKgy9uKF9O%2BMDJ9UvKCxS1EYeLogE4UeTcUwlrLIzQY6pgGCCK%2BhyCWyzVQNS9Rgf2N0vN8TV4GNXN1%2BxO5zbuZs%2FTsggbBiygAxhFFzVsP2%2F5s%2Bte%2FsB5%2FvOWw%2BDubkeDInSCyI9BGv6BNz8tQ2YpI5%2BKporqBIB8%2BqCk3qsvPeLhGzOPWl%2BPlJVLVOtGpHVHGHlQw67xSsHKPwaeqG4fsgGNW1MfhM4jAoBwv4gAM6OVP8a1XCYz%2F34a4Ih3YKSn5EVqHK7rkK&X-Amz-Signature=1a8de1b47ae8a6e48d31a45dfea2206f1ecfab2c0faf00369cb2881b5b5800c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



