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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH4AZ4H5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034050Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHM%2FQqx2Lf0wUolsg%2FyQHLBU8x1%2FniIoD2q7vW0qshz9AiAksEZnl6fy6vuuEBpfE9%2Fsd9t3xSQJgXiMXx0aR%2FzPfyr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMYdLT60JQBdZ%2FdepiKtwDEeZ0LOg7YlFLSiCUL5faRAbUbpXX68yHmyqRK148wZ20QcFVdUP8S6Nc6gQBSuKAYUjbnmYOdqOwn%2FQLujdgqHlM%2BLfAOStN9dBE8qrFK1Sn5UeDBFGR0DFLmrnBd321Ee3gokzn9056BEkFa53CJ4oDzNktKXn711I5x0RN4zKHmb2ga9ceY9zzkStTRchZKwafDnC0O%2FZi4nFYXXb40VIoFlkh83ujwwlIIDqrBTJ91%2BMBpClVZgcitTM%2B5jgMXse0NBqMK8%2Bf4%2FDoMGgLCQKjzsx4F77900ljbHo6zii8jZ68458ZLwXDr%2Bh6yRWwOUmw1MGQiSjVAAo%2Bp6lEzto%2BqUqRA1Mf9nvDim%2BrBv%2Flkp%2Bo1igcDMKyHbdVPjvIB4txjIgiiteqtIJrWKov29xF3dErByFHoBXl2KFL6OzPb24Q0GddiPmVo3l2hOXwvBgWWLJCpS%2BBUYYgqpgjRxxjN501QJNHPDATPf5F6CjGK4AX6h0KP%2FScAVsygTI%2BKjkwZ41D%2Fex2JiBPjOjrM4KEW0mIuIxkCP4mj%2FWsoTITuVmpOXyxHOD8qu1wjwWEohe5s5orY6rhUyvqrny2TNjYhd4Nzz258JyLq%2BYZpK68W0rowqPyb2ifEq8wr%2FHZzAY6pgHcCwFXHjVKwexnYczOT%2BpMdkysB5jGiGwmfIZq3YvM9yWb7BfSHE%2FZzSH%2BK8hgYxzqF6mkbvAgf%2BZtzUsv10FoD6SHmpdgHaeyBzm0c46QasOsfFC2yw1rVVwjoHKZyiZSrZHcgvtFIrHTuBzWVmZnFHttP0ehFeBDo4n5zlutwn73%2BuuZGgM5DAAvDoXMW%2F0BmT%2FJQK2%2FK7xUeLJ09KOI61JfkwKG&X-Amz-Signature=70ca6803f4c282af35040bb26b08417e0d3dbbe22d0ea558be2dcbee73f73f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



