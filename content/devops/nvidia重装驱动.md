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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652UQGJUG%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDE1NKsAZ0rSMYJjl2QXc73RPnufTrTO2h7FdpCGQSdhQIgFZ3nFt7%2BljJFz0dYgC4YhB4R5bSXnuo8H7VSpAVDfbgqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFEk1UzTYPiNL7wfHSrcAxns%2Bi8kqJR1Y6u1PijPFn%2Bni39%2FyFj2NNIyCzUbgm%2BQ0ykEFRQn%2FpaYhAPRpEsgCb%2FB0vMhQdY7Wm8f7iMbqGu9D%2Fu6HaNyvjNNgEi%2BEfn%2B0Jx7DHvRUQjQ%2F22WDyci%2F86T6esDBXRj8bDj2c4LEtN6iBbwuWYkJ53LtAGw6wl7tMPaXOYxeyYbn7vHMi5Q5HYcBJnwdNyzAEGzPNfKKh9UMccWiEstcfK4qVopq1Vn0RjE8TDpCmAnpfFqU38QG5%2FvcdDwRqa3WzeOvURd8BvbybF9Ql9gcSI482%2BNTPm1T0brDuvFGrdBqO6UEWyqMKzi1pOEbM%2Fl1%2Fdk9KWnKoqS%2BjAiywb3MjhjYEkgK%2BWYgsCNwh6hj2IXxsulFwymwv8ZhrALW%2BBmn%2BZgr6P1OA9nkA382ESxRz509v3LfOoydQKBOiXAIjcV6JN8KqtrbEHOe8kN4qZChEm%2BhTFviHiFMYkBSg5QtHun4MGqCIgdmzIa%2FVDB9GH%2F%2FIgp8AaR1N8Wv6l2g2fdwk%2FLuTEa5F%2BSUaVwYqIDGQLMxi2P8dO1CujrY6T7BM2YlWuxai%2BleDNv7WWlBSU4YeDrG7ltoKHiBdbhXU1vpv8JuXYMqc194bhTKnP0P6eh2tsOMPmkjc4GOqUBFGJDEaJIdLfKMjD86%2BPkmPxT5AFGAAop5iZmIgjLa33Hm164xgujkbmHeAHCQP0tAmymmPIJ%2FSkpQpQuVhMz7l2ZZkVKy9RwQ73AyOhTfYeMf5bV6cLps88zhQjlwgs7PyVzoys%2FZdFNQvq3Qhjk6ylq14WQAaNTI25U8m6tWfBYMwFMgOAJc35xiNxJiOsINXtfQsKqbu36n%2Bnfu0Myu7Ia3ndB&X-Amz-Signature=bd2874003fa1f502a112b3e821471dc220a5900a6b4f1556e14e751faf072e5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



