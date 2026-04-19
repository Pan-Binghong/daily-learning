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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBPBAFAY%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIBhrNLH%2F0ZYLOSLUWqlYo1H%2BL8%2BzOm30i715GHKoQN%2BWAiBsgEGZe0vJfwiXtBb6Gs7iD%2FOnnCn0un%2B3%2BkKoNY712iqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BGGCKxylws8TEjFEKtwDs89dhJxO%2FVzhhn1JrL2rygdg3JOfhHQY1iQ5%2FkjPpKNQjqKtJ7JtMRUZAycRdqZLyBA8Z5aiPpoybUxf1721rp%2F7qjE8ViJbwfJRMQaLPfX%2Fl1OIIIwsvwMD2VxnxA7WJOQcNcIFrmJ2g5F06n%2BoTwMOUtJIE5KWi3Ku4QmUd4Bi%2FhXQ85uejZQczTYPZFiF%2FwYhJkjg8NXd76tvf9ZQNiKtcdrNuv8m63FSegXFeNte68QA7FxuGADRfeMxQcpWrZtk7%2BbAGFJMcL8SE9DN2D%2B6jVZS1HXchPsb55JXFUNFQczI60bpjgRaan2DDphCWYn6OtPll3ctcQJbcFOVFRdK3BeYi%2BB%2BlZupcb63WPald4wfffpmxkot3PK%2FiuPgpBAOq6qFv722h5nsBZQaVzT1VJ3sGL99sZO1o19UVxqpdkzZJJvb%2Bfeoq1pTJDQAb5qQIUoJJVw8fbtfVGtpTfPnLunPbkNGhCst29fx%2B8FNvmz2vADZkzk1dKCJCMwfCbCWSPsENkridDEf8oVMv9SPyZcw7epjuG57WQ%2FuRuLkc0SZmEk2KiACVoKIA7L3vaxuUDNhP0J0fiGYL%2BbmQqdTmoGVPYCncOckZdYyIrnRbpqjZfsN%2BqkL4hIwoNyQzwY6pgFNQAeKCoim74HdQgTiJ6rfDwpo20LuGztww9O%2BhNqo7sDnTuT0zGcJKuS96XIcuQXrY6sjMm0osaGY44Z34WkAHbjhWyjkpodm5dyLcniCsSrr2M%2BpL49xqLA8iE6UI84gjeY98xuJponpfGFAcQCpc5oXI8ZQ5mmGDbtjuHjLq6OxXqItq9wmXXoVNR2L4CkFfc5X%2FffbZ3ence2oprv4K3i%2FBheN&X-Amz-Signature=f71f779d3f41ba079fe86d67138a4c34ae3ff9617089fc605f98f93301b081a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



