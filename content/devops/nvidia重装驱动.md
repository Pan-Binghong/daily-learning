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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ST574M6P%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD514Y3LkBsnFLeVCaw5yBHpxJO6ptAibPRTFcE3EY5kAIhALx7H05As9HN0%2FQ7DpA21JgqvffU5EqsLNrBQ7CYCAVlKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy0xD27LP%2ByswUb0%2F0q3ANuObcQEVJzJeX2mKAqavcFYbWTQEnlEuIS6Oh4D%2Bj1WcYd6vPS45gqJg7KkVZx2MZwxc34RAu6JKW5xrieRT86zLPQRMjP1ndaIj13yqkPpA0nXUPpwPPUr9LOzr%2BgxXoK3eURWkuu1tj9SOYCbuXEpRJRtRjzuhVn3MkiDZGz5UUIY1NH1KVVF9mkweA04FXZB5bJoB9xX4I3dMw%2BEVRR0xbRfRfhs9iJ5pmvq4Gx2BuwHJRiZONIUOv6ywnu1Y7ajUDoPCwVekF6hbPSdzYF7dXjtOKDC6vlP%2FZ%2Bc6YXQ6I95xboHlhiKfjvUDajB411qgDqqWHhriHjiQvNPIlsB0FQ8MSUU01YsbZV7Gl0Btj%2FwA%2F6vjpO3If7QUYhAaSGAsTLAN%2FuxeTl5P68YknuepGUtgzc9a6%2Bt7HhMEaBQDfz%2B9NR4Z1jd9T92ZI6RezN0PV8zUd5FdQkkK2aITWFSDZiZi11UKbRM0fztMgacDvycODzJ8z%2BzKU5avkK5ugZRFrVhAMI%2Ff7pjEkjXu1DybSaTvmOYssKe2HZvvw23MCWZBZRLJr%2F%2BCaODRtTgLtAZUC8htAmURWCh0e%2BMSyKi%2FfOnbTq5SZAAKGnYIECEUYxMn0sAXQCGGmekDCwn8fOBjqkAbvh6aMPKTShFfda8786nq%2FeuS5JYGjHnga0nKPTHdZmXqVD2qglEC7P87ip%2FPOiriKqNyWC6u1eZhIZgnTSKdZ2L6RpMd%2FKFNTDOuuBZGzfeS0pYEL9G9gdRMcBQ2eVlJqo5TYQTNqFrhiNkL2S3LGIulpaqjZEx%2BMrJii0h01YF6KoPEkq7G7CLTSJ4QAWS7QPocHOke6HzCIbfN%2B%2BbnV2UTvn&X-Amz-Signature=3ea93b82db8169b9eb8b9d7bf59c55c9f93c515b5e2edde9ebb7798550fee9ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



