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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTFJHHJA%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T035034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDOg6wQZmZ%2B4bmPGlrSslF6ePcpUfsNk17b0Gc5f0BL7wIhAOW8XMa2F%2FxeuoFInSQ029qroAMu%2FzodCcjl4Ib8APXVKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZS0xZe73Qrvw5yzAq3AOyfGQHXx0vvSTdCrF76e%2BCLJwZCBBCoDqHWTxs%2F%2BdNPthZmku2m46L9ylukGcAG9LeXpRSQXK8SiuJR5t2v7WQlAxBbpHsYyeKfoOpUYOsebvecHmwJE65t4KSwCfP5n8AXWKpiF4%2Fa8cYgSV8aDgBtNd0GrYC%2FSAfJpj3qo57TJ13GG4JAKTSHrfSAkXQUCLrZPQ2IVplUd63GpelK20YHS%2BDUiT5vcLbqVe%2BO4QlhEDksQwJGqJrMffBQsjIO%2FPhq0HA8Xp0Nw1pJDhTWTaqdS058PoxD0ef72dVSA06gdLHIJ3zp0lfBnjemk1iB%2BrlozHF30LMxTfF3czeZs8bhTFeeynbQfiRVXTSpBkdb%2B3OzeECFvwFZBvsLBM7N1tHmzzYj8gD0gafTaemm9VVt1qiJZeaVM5quKXW%2FCMp%2FhTdDVALUmjXqXRyOGN0EhR%2F4X8e7SM0MsGleEyh9GhMQinqP8La6twLykC3CKCu%2FCyyfVn9LEcRl9oLwTX7axp9JZ5ToTToSb3ezQqjWfUyWwMN97CQCHu%2FnbLxDidD22Rcu7VSNaMbMJjxmwTK9ogW8me02AvzB94g4EMEsn01LqSqj884w%2BSYWjvcotmUrwIDBb4ys77daNKaozCUr4vPBjqkAee5YjPX13C3547cMJk%2FW33g39vs3qFgp1gPX1Bzf6hz2tVcgxYU0BBvZa%2FBLXtmykIKiaGEwyJUP7x%2FFSwum0tpCbLnUQ19fXk%2FIduhpdxt5H3EzTx8bX49LeH%2Fi1mAgZIjSPkRyN%2B05wIddfU68BchCaNJtQQURdlHUMc6G3kZU0M9QbJEde0U0SCNqmjiibZCplxBVBHmLyvOyu%2BmDEPe0NiN&X-Amz-Signature=aaf69c2c27a781a977b5cdfb1d8c074d6830f067f8a2d1b6fc1f3f3f89014ef2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



