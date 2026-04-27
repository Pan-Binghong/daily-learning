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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTOEYZOR%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD8Jl89S7uci8JqBITIZ0rHqDV%2B%2FQ66PvSBpeg%2BzayKDwIgOKueGSX7G9EfdTgUgHo6yy1HgGEi4hfmbsrrYWi6vQUqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIYi2UIj5aPKYiB6FCrcA1hGhHig3t5MOsfgwtVPBSun%2BjhIh58kkvBGtU32SaIQ60UJfvtAjVCZxvUCjxDqyWHk%2F5IQk%2BfG2R2v0ManF5wehePAxMMCOlGwkTbKuCvZrm7%2BI4H%2FpbqrYxcOBGeDQhsmP0MX9a2lROtLujB1KR%2BsSC1OViiDNy7BQ1aA%2BBxVdpo1RAJWojCEvgausQu9lZNw7cNZmQSIlSzX38WkFnjhzXrn0n7%2BywCWozgDjJ8%2BxeHb9AqEE1Rx3%2F4p1cF2E2Svxq0glieiclQ3Z3qU97wEt1kwYZsRNAhHjj8xGnrMomLQDryDj%2FRhCfIizYpC6TENEAscj3K%2Foi%2F9w4i4iUfo6jb4B2fafeYpn2nqsItWkc7ssvT2bKBk5O3%2Fyo5ZGJ6cJF%2B81ARQa1p8pLrU%2FCNVnWLjhVmrAQEAoxmCy33FO54ayx40Z2jTUliWGwz1XcU%2F4YinMQ%2B6QdlWhlItNcvMNX76OIa1BK2QYaSJsa86lZjbxmljj4zF6ejqx4tUTisxehuzEQaTTFLdeAA9jfHcHoCUnvSwb8xWfPvPvuqdKbngZCdsyzPdaRfUnTBEheqkFrv0MLyWQ0VKdsCaieFxGbD6YfJmLF%2BzHOrc6Zb28cDZDlek8T8XWSQ7MP%2B2u88GOqUBxyl5%2BgCaIMysB4BZTWf3pRdkdtyDxEDIX%2FZrQZ8uF0C3reI5%2BaX6IvXM8cVW7pEkKxv6%2Bbvkv1J2ryzpNYKRAO8nnc9J0YZqkosueoPw%2FueVhEI%2FhnFfqpH6%2BEtvuw5jolYFJE3Q0EzfHXLSn6R9U%2FpINIlBZQFY%2BzzEwCm1bW9DHUtBgZjwQd57yyZslUiNOrHzWBQWxac4keXtBzcjoFP4Qis8&X-Amz-Signature=d59a1c8c8e54238b0cb6107aaeff3a3e0756b96f054a7ab8b7abae092fbd01cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



