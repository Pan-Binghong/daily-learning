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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XASRMKSP%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIGZIW%2FNqdSjJaYEUILD6Q4awlh9CRQF%2BxRZH1GVCIogwAiAe0XyH%2FrqzfuCNL2cll5%2BpBUNbxzQ1TkxbApOVq2EiXiqIBAja%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCnC7kbF7MzQKFdBWKtwDNFatkd6GJJcCD9ngwRQvk4wDi%2Bj2GtaSzkn2aqyK4Qw2%2FewDlbsHa3pIM4zi31rN2FwAUdE3CQKXf2o69UAWm1UnFjUPhrhm%2FhTe35HbZxXF%2F43lkXFxw0utF%2BKQqg3jWpB4eNg%2FZ%2B%2BowlmDIZSkC82Hk1rYnnT3K97tauQ1ETUrY14l%2FiRktnSUkfdJTQhcX4YWLgr91GTIxBqaIHsDloucWBvvd2d2OkcRWcqSWfaaUNU6iZ94wNG13u2KO5Lo8wzy9BZKZCrHycOLNtH%2B6pppX1YojBkAtiIjxy4APobMHST49meTcftYacY7MBnsIQ6QliHdsnBZt8tavDwtoy8KAmfXsPdNqd6%2FF2tOuoG0VW5NFNNPSdun0MOiUBgWsj3KaZGEXV21mjpXmkNHCKPhajrYzqJU2lNq2nw9lrBgFGvbEgEe6QYg1mMJ77S2xFhNOPGgxPP1f4P2KL11Rqd%2FE7UE%2B4IVZFNw0g7Jz1Ow9EBmcOJIazCA%2BFDZsbh17eHMjl1nIRyzu6RIt%2BjF6r6ZfkHr2MseK1MUdkDatrNy4BwNtvuMjruEkIlpGyXwouBUW4NxrUQGJJO%2FnppUheK1YF5ne9k3o6T%2BLjYZ0d6vN9ZMxSFAZOiO%2FKwwoM%2BozQY6pgHLAvf5X5tJ9LdeZp9C9mHfQfBt1JV2TVZggDvq%2Bc6IpvFs2NLDCwexY%2BgMfL02B%2Fed1eVi%2FgFo0raGbMdqJNNo4VyAC0cgmANsMdFCzyhIK2aeSICZTGsc4dT%2FNLUxRqC66XvTRs7biWE2RlC81mLtelh8ZCBuhGchoBNocSvz0hxTV4onQgyTIId4%2BKVUNxjMfjQg3aBWIH2uBuoC9RruS9ApE6K6&X-Amz-Signature=dc8cbe8a8615f03ae653e8b04ed05b37debe65c9bcc749ea95d4f76b5aba0f66&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



