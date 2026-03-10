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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7TXEGS3%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIFGEoOq2IUDFczGHLpQFH3FUyuIVnJ%2FgB%2Flbk3niTe6yAiB9PIuRGiHsXTVadV4HxmGupTcT6HhYuQgVTg0H3fq0KCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMUDwyZSp9qDvUUSNnKtwDyyxMZ1bbcJF7LwOMBiXblByHORhhoNRrG8xisl1q0Eo7TqKM%2BJbom6qVVM%2FVzzw2dtzEifjj6EtaRgTOP5OjltFRDuVZBoMkNieMqjohmQ%2BQ%2BlxGIVucGnVeGiu3%2BeDafMw54ea2zNR55kygVCQ437Zxr%2FO%2BwvH3v%2Fnx5ZEz0aJXLOR0UdpZGr7XMWZT%2BZ3FzwENhORFTHPGZuQwwIUgWZZcJ5cwM6fJfkmgJ%2Fg3CkBm4p6bW2CazHdTUD812dp0jnwD7s9YoDJxHfQJ%2FUccFBbHvKXq5v5Y7JfnNEy9VP%2BexyhdMk%2F%2BVCLghzjt5OYctCit%2FAzNIzAWxi0HKjHLxAsQDVSB6pMYPGQkmA%2FDnJwHPBLFcKOwQdCkjVACxiEAMkyk0NfAzmiqqz5ZLeoRnCdxDxH4EIssOsoP2kpjCdARFw73RWg%2FOB5AtlcV8lfq1LbYJf%2Fl5vrKf650J4qOobqD1CxP4bAGRwiyE%2F3ASZG3MQiw6tgpwXh8NG4bcmcJGW5yr6SC5e2E1fe%2FEjsyYDlk0dYB0gENSkmdisOn3T0nFf30hYCSszOIH%2FkPWOj5EPQwa%2F2cAZfYSOoimjVV7R2c1TeyGFZ92R274k4oFDDnwuMa39SUQ8FGFYAwy5C%2BzQY6pgHkMnFILYzVsBqb%2B9fIb8E4pX4i6AGiT9HwELSles7QuQuDNClbLkdkvtsehOdXQxGo5FEOo67FweFN6%2B5Rd7mGftaivBwlQNLksg8a1zMB%2BDzmkPL9LHBnvmMGf7CV%2F5AKEn1war6Qj%2BIuYBaj0Pl%2FsIhHIThCkXp1RSkPmHecKSraOqvfOh8YIR2fQEageKoEZNTwdS7eHghwuvAQ%2Ba%2BM6NUSJuu7&X-Amz-Signature=7f0db94f0517ee5c16151bbad202efb4fcec11e37e542dd630caa03641a919c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



