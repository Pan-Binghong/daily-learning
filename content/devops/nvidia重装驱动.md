---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-12-04T09:08:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOSNZUVZ%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIQCTRT6cAVM%2Fv6G2ReaCoSSiZVWeTsi5am6k9yDkaHEV5QIgUc3E1JJTxm8QP9bKGX%2B29afMP6pRfe4ALNxU6jEiyT0q%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDPY69xbVg7sypRzj2yrcA1PQflPO9Mzt206Uqz5pxubmhVJDTGx%2B8ZpiQM5GJs3qasLeazd2JHyCqXSUTHawm8Fm23k9tpDfRXYtvk%2FKV4Q%2FczlA3JERKZDQa7VL7ykK%2BNEmqIUZBPYHtKlbw5hgK7E6aITXRMbIE%2F32jVrmJoYEWZmL4YO0PtI2px8ZjSKnRhZv33o7CmV4UtSq7yuLyxA2l1HP1n0HoPF6OzWkxtO1YoKNzgFGIJ3Nw6UW9Otzjirj7ws4zgNRueSCV6ixGzWTA7cE8AQTSvnMqCUhppjDiBfXN%2FEE2oigYBDjg82nGa73QGaxv710LzfbGroPHpTkqyHWogTvOcO0oGW6hYkQ1tMnvOw04b2Qux2kf7MQN3wZMgwaIvEaCbySeD8xhxDEuRQGb49tr9Yhy3RTlsHsEwTHsXtN4qkTzZFnK8XmaI%2BvgyB%2BhfDY7XpfBBJbv6R9vrWyVsRFOxz6iauhDhTEh3CX1P9sI6q3nPeTO%2BCGMJRDZvzYbPHze%2FWtg%2Fzs2TpzJn0fetUn%2FWWtzy1ceoyOUcbWGvuXimoFXQHHXG2btyW9uTabDqvdxPxV3WXUw%2ByW830smaH1OYK1NP42hRpBeq2sKox9AtpjdQKf9ZBfffeiERXgAHVNBBgiMJSc7MoGOqUB0N825QXfL2cpiNbFBVZMkNyukynsmIOji55NeEZm9JWsHLlE8XFunDZjRN8WYJ87IP5a6rV%2BEYvMUOgxoLD097aqw6Ys6OiUqtDwAHHD7WfxhxLkeirFzm8L30Vo%2BBvLukY4VUAVqnTh6I1Ge6%2B8FgGnS1K%2BGqxPtWu9qFkrjRnP7x%2FfvXNczABAQ3qgH8WIXJs8%2BfgkRoEWfoqGxyYOdvr3irgT&X-Amz-Signature=892709e187b73ae07cb1cc47e68a809ca5d1b9c6dee2d3c2294b5d80119fef36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



