---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WF7IHHI3%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJIMEYCIQDKZbiybbTJK3khrdFflhj5vzbdMFeKoawYDtF8Lb2rIgIhANse%2Bpq4oMOUjBVebEsw%2FDmDv5h%2FIPBYYMSTTm%2BP9ljFKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7KhRMVXXAL%2FSY3dYq3APePmIeX5dwj%2BEdHHZrH67pgrRIed%2BMzS4CHtXwaU%2BRTMH2vFjqL1BEca4oH05GhhuPooixppwhaYtNJIHufB1M%2BGSaJPOG3%2BMHE6ZYk5%2BzyXnS1Z0lB2abNgWFAbWaON6Jje54WNd9CxaeQkY9TlATh3Jf2bFBnXeKh2SybpKxRGcTl%2FS0yAUkvZTdZl7hZAsBshrg3OZHJFFIIGbFtZFoWdbqSjYvNxLrwPyngBiSo1fqaXZAWNZLYTSfzqpB%2B5DtQ3wWPMiZuahQbrEqNSsKfOBX%2FnoshyNEQDY5%2FvR6tUUxIBKR7D61I%2BtcODS9w85txg5IObW34xi1dym0Hl1dVSJl3RXaNqHuxl%2BixGc9f6DdHmPSI3R8h1gH06jQU2G9NZ38CLoK6tZvMYj5NYOPX0oWPiS2WS212Gw3iK3AXKwoaPUXLKfVCD%2FUL9wt0rQbMmDkRZuc1yJsSgCz7ouzTEnp5ScYsz4RmG33r5rhhguLtsuYFhu88UKtpsCkSPnW9Puc5RTwmDO%2BluiQyavrDMWdLq1KxJV7x%2BjWwWZSJNLGvfBnxPvLfVGM3sDs3hi4xtsy5Qh4nSsaB3fEPMy3FUsV7oYl%2F8H1EZ2UUnB2NViAqfGUsYZbalRx5DCn163JBjqkAbYue5fwG2lO6ZEv%2FSlhVemTJWx3d1102ghXIz%2FZ78AhHeozgeMHbarOlDrjr4umEUoZiL4g9kclJRtmrcWVTSpTyEDG%2FmAxUbS9W3v%2F5141DSt0JssObW8jRyjX2IqlHyU7lkfYY0zp0BIx9%2FlxfAYjpe1OzDYSRO%2FVAzap8cM644f9aMt3fcIeyljlpxLzbJwJlqOdQh0hMrZFMfr%2FtzZlfa0O&X-Amz-Signature=672fd5793fbcd2a61ae066d0fca7da7667a1dbbe3493dfac9cdf3fc3e29871c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







