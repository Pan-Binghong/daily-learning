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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663R3BICXE%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDBaYwAn7uvtONuTzKvR8loyD1FQIQZ0AghhwhuEBb45QIhANox46hWlPeyes6KnPTERDyjR50LIZX44XEYPBsoozZnKogECPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwaSTRlXHZOqKbCBIwq3AObhGM8KsbonVegqq%2F%2FyC30F1C2pefdCsSYgJGnUKIfnzCOq1mcrk8uBTVFJStCqoKqXOff4%2Buqch%2BQZn6ebxjQHeyz%2BRL3pNtls6WQ3XHo36I4p6%2B0XcVsTZ3vhQbufiJ2ppGfDs16ahogLlvSmqR43wiRWhQMvgq59b7YVge34BeWySdY8hj54TEelwaxUZw%2FWmImCrY4pKsQobMAbmnjE48pVNJC6K5iOQIHQnYAdBEOYZ6JtSGUbsLdqF%2FHueUvxZRx0rqrA9UoMJiJqqAakr0YU3qACiAsZu4v%2FGAgbrUiZO%2BdT7fHafNGREG7QxWI05nyvJnOAbbX2vu%2FXDzexiWM3QymjI9hlfFxhgYJ3kfvlZdQ0j5MeDtF8am9Lg4HLpsZaom9VeFI4s8JMMbir9uGOuwkmSMgqzYuTXBXsBbrAf2IbRgBCO74%2FV09P5PPN9NjEgHrianarFvs7doVuHg3HfdJvl%2B8RMYaYyz%2BGby0tb9Tkq28G66add7r5FAGkgbh9rIYQYZOx%2FYCOVucvPVCh%2BB8N4al7LOxYUmekLrmdfsTxcYm7LMtNVppJESgvB452JxxFwja2LBBOAD4Km%2B%2B5ctNfEJY9SAMXIle5H0%2BIrqV3H4Wa9uT6jDNiNfOBjqkAQzmaehWN8PYCj66qfAjyuFXMcMZN0NOm4nppiwKYhGhY16SrvacHHPRzitAErSzV%2FTsRXBal8SkL%2FQ9GOE76CArEbAIHshHgDbQZtgM2UW9BrCIOrdlMy0ZB5Dr2ch1i0jbx2j8WGVxtWGfkCqOGTOju4s06xLfQutQEuhjgWNLSBDnSZOi4oltGJC0799x1wUOZ7SRuYtOa0Ugw62FTkyLsEuv&X-Amz-Signature=045f19f32cb75316bf0a12d05dc44bc6f762d6f18b989b676cd8a3bea90b5415&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



