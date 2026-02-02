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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUIPFO6E%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIF5ntEozJIU2rFmtGRW%2B%2BIKujXiXz%2FwX%2B2ZOzplKXtEaAiBJhCnxkgtMX7NJY2MHQxu%2F3c4ZHbvf0INnluXtLksU8CqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2F1fqmLzxriP%2F2QS2KtwDwXVWpanIPmZNfLlT78%2B2LVl6wfOK1T7UdySjfu0qaIW9n7vbSiwKGBwAWRb4e8PHIVlis4eTTy4rlJPQyxCKHsXgh%2FdSCRq74ARMYqYjWDoEIVFbIKumyLpUUb4pu3dcKZTkdIY3h5C3PWwsPkg0zlxxcKSE3Sgz%2Bu6DMN2f4dZxERijsEM%2B%2FRBuyIcj537TnqsyxUMe%2FBjktcY%2F2srVXTGmpYIfODliHdGRS2YEvvq%2Fk8794juUbR7puZArOC%2Fysil1Gp%2B6INgSsgSHvCv%2F2VOMjYmBp1Dte3LBhQPHaBNa96LeahzWUwKWfcSXItqSfxTRJkoZjCmcyvF%2FnQFNUp%2FxQK73v%2Bg4QgGGOwxjgJZBechB01mmpxB7Fnv8s%2BD5fwMlcVyU20%2F%2BxZ4dnrkPeif2vBaMWQfrBr9hU64P1Fw31DDyrkpDXze49iBQLPo2vdE1cbt%2FgyUIHQBJPIexeaDT%2BgrXjtb3Ek%2BYn%2FUuT5zr2JH5qWanw0zSPyO6jIaE2%2Fa6WMqJpdrsZZMCb8XN%2FjU%2BOR3%2BaQRe219ZLXBRdFYODR6RfrzE%2BgrXCC4QH%2FXHgD4%2BUjfOJFKNt%2Fuu4DD2paQjsLHiAS3cTgnxxpkUJ0ZjOKZ5lBHxqTxuFcAw3YeAzAY6pgGZWnCqwuKpIXbKrV%2FdMaJhJsBSY0N2fUKrj1Dc0AOqzHA6nVIrY60u2wyql1iZ5AYYQ1UvqqLQA8CgQprzIl%2FvKmtfa2En56EyHhvKY968So63kkJOvJFICFhxaJfQT6LxcYFOF4yIWTEddARbsejFna0nVfqT1Cw80yPvwDpus%2Fw1AATXWZHBA3KT0BI7D1sOMs2hMPgyflopyYNRjMMStycs3k9T&X-Amz-Signature=844fb7f43d6d7864c9664e51c23549d7f30b8223226ca9e3823459c2d04830bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



