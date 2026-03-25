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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHUHCURX%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKSHX9KXDHMMawfks%2BlgS2dvURaMWEJgbd80cU%2BlLIxAiBj8xWj3j50i%2FnDpqTyhwLhxOdY257xtBOmJ3W9wcFydSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmX7Wy7Y4ZPeTnNRTKtwDwU6hFUWm8yHpdyOOC4jdwIyQq7aAwaDncNY06hxIU1IkmDH%2Fcvc1MIIHkG%2B9yngVftrzt4jY8hPNe9gL42DxoZfGg6iNtldCLv4f8DQtALOjNzJZGx4uQbndvpnBDwJ7n8KlCGxalVtCUWj11aZVpnvkToQbFlHS6TZkAuwdzt7xrWgNw2oHP2yy2PM6UCY4Lq6tV6wb3NJhhumhz%2BSVwK83e%2F1dLG2ned%2BZJvpX5VjpybU8uSyNNKG0QNELR25WLscTQDjg3vkN5iXApacfptsNNysnArWjh%2F1PP1aU4zg6qfi55W8R7zevwIUNT1aqHIpa1ptMW0Kqw%2FIJ508sHGfn%2FRCwarrPtQV6eeO0S1XVjO%2F5ORYtUdFLaqY63W93u1S%2F7EvC3GQ5E2bzH606CHCT3v9ZCKwaH1Rmwv1XPGIT5SBf590wNnESHBC%2FCG7DUqHt2ABWFoth5Q2iLkxf0LY5wGC0O6kTLXVQISW%2BxeGlFoiXSDpFIEYaht8fhje1s4VH51ZMqfzDPviXp7U602CX6Ct%2Bb2VKarm6cIMKvD23UeQSlmJ3gEIaeQfykqGHSGp5gAsuAXTmtSZBzIdhTdiiYB76%2BiuYfLgffXXkimjo5ZRz6uBtXNcD3WIw9NWOzgY6pgFBiqKSIfmvVfPPpQaj%2Bw472v8xtS2MixyGOloDY2d3vvuSDiALbQRrkHzPQ%2F9aUdHcLGNpZuGv%2FaN23JWfhx8CjjDLEorAlSr%2B9olt2zGnccSgP%2BMOKGrkHvz7gCi943gkTj7ZOi8mkp7q9z2PKYt1IPIkiMLFsyaJE7guko2oQFJ1k1HTMGeNqtNAYJFBPnYRsPn%2BWiIpw0zbd5zkmA06fLI05rp7&X-Amz-Signature=9ed952ee1633f8dd4da3ac1acba1a17d98a8e357d6f80b43f6a72cce36636281&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



