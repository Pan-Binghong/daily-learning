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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654T42IJE%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQCMuRETsmGHObu%2FHZXqIpNzvPLFARqNXmYaJY9qGVGEXwIhANTforWKGJU7Bs%2BnqXVp0fNvTLwoKjLnzaLkmo5pdfomKv8DCAwQABoMNjM3NDIzMTgzODA1Igwdzq1gmcDjKeRHvK8q3AMg7VyyxGIdpscSQ8VroKx1n89lQHWObi3VGCO9%2Bh9tQB8Vx3uhBYDPCHtBl0ZudJqugU0i%2BhMq4%2Bub69v6uswy8t8u4PuPR9yyEAsKQVlqP6xsu3GAiid2SbX%2Fm37RbhRe0QQ0bPg%2Fqo65xItLVUsRp2RAtKRr23Qo5%2FY%2F52PEbIyeNjaLTrbNP0%2B%2BqcEidiYhCYBM7Aby3cGRqHDlD27KadWV38vMkogSxdNTroDGAxlINWT%2B07aKEPDzu3HysLJtpGMPqRWJtGIDpLr5PHErHeR3Sba5XOQ3qBMg64Kk6zWYBRrU8Nafq3E7JPZVmacKfi52f914TOq3Qht0zi%2B5db6NwyZqrsR0yrFt4JdH8WRSTFxFrq6sCXcdb7Yap52YRgc9AQjRQ5fUFSIrb1WOfm%2BaDotW5KslQ1P%2BQV4%2F3DLeWNk44%2Fg9%2BDkUyKrJM97LUHkxtl5fatn9ge0bze4WYFckof7rGp3wN3mvbpgyGQfGtV%2BMq0Y7waSCk%2B0WGHyF9vX8P77vUdH47t0qO21%2BtxIBLTmiwQFevfirZ0ULpVRV%2Fd496tYekV%2BB8lWz1p8XTR0wLb5wqOuC%2B%2F8A3aVchg86O06Rw5%2FaSRmVlY8TpPqbHkQjxR1Yh3l2JzDYstzOBjqkASM3E2x85KMBZeOXhqjkvW2UGYe8VlVEBO%2FICV5hm%2BxBlgPTJSDqa8BJT5cgtMPkKyB%2BShWgzzgm818cHI8wNdMbC0EI%2Bur2gi7kE3FK4Uk3i8%2BVp0X9kFUOrrn6Q8VikxbIRnuxGNio%2BNfCzEThWRcKS5iGx7E8MxGQ1iKisqqHxuIPeSCwQI9Kll2fCz1fOdmCo%2B3wVNyrHxUG%2BHJ4vR1qGEsd&X-Amz-Signature=c0f4646e676a2c919493a01752ab7311a6063fee330c51469a366d1961424d85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



