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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YSC56CB%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbFfXVkCl2m%2F9lSc4CwOG0fEseJjrH3CJLbraUm7uLSAiEAoxxcCH1az8XOT21yPQ4GgDHEb3GwjOAcJU4voivnmqAqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF7evFhrQ2Cj8tqoWircAwOOKzbB%2FcNRp5Z0PEN7CmK3XIQqgbp2FHQ7QJRoDah0BCv8u2LRRmMz8kwIELtsw13WrG1fEQ7bRmU5Pptk9UriAest2L5cujYA5rsvEjYsxCJK7JWRS8rewluAT8UodUGpbmWBUKauU5I%2Fq7T7epB%2BQ%2F8iSzEz285qHOg2893P3lb6RZRIn6AR3NK4mjfbY9w%2FUNp%2Bfd%2FtYyXhg%2Fnmo75BNpHsa1KXq26hYCLML0TWpvPxHcaxSIQl2UWJnIqQ00nf5AgcQ2FPLZo%2BSJkAmlXM7lpyfjFwjfFCYCnh76XtnEyOEkdWRSlh5XvWTlHe3mo1ge1er47l6rreHMquPBhyWxggBWoRIppl%2BbPATkFsI2J93vXSIX%2BsBUYh3GsCejMHMvB%2B54XpbM7zvBGcnaQTh4cXp8UJ%2FQsuDorNUzfrz3WcTPJHH8zI%2B2XosktK1eHQD1pkB5mZb9kRRdAV350YOjbzRNWveD9Xyw2hD4ubgMimCXFG6IxzdE1O7igfrk%2F4zP7WquKEBcWxryQhLSI%2BSIin67o5Gl%2F6pzkKbpzWqINGJiy2Cmr9EzxDgKb5ohdZUXaNoUBh%2FWb%2F4I6Z%2B86MQ0C1UJ45CX4FSZ%2BfhvMCTqSd6%2Fnu90vgjFozMImOws4GOqUBFf9dKiijB7DhL1%2FP3a4VMi4lloEjlOWRNeLLlrtsJKl0mFTLLf5si7461Wl%2BVYE9e7sDI%2BejaQikr7KWS4yaigPTLDORqpLEwC00FEpFTgmNV0wepIVWJRemw4B1ZoQfnNf6RG5MmN2X2fWpJ8HdZfblS9IDtAGwVkmzog7ntgEVbmVeJPGkkcYSlaWVQdkcU09%2BArmXhJszHaMvVLXlbYTh1%2F3N&X-Amz-Signature=100b08b097a4132536ce7d87c52e57a536fe95806c2c96395d2a44c558917a7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



