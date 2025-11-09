---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WR2AE6M7%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIQDMEmHo3dLF45MYxCfpNAuaWGEWGiffXypWn9CCaHioGQIgYwUtmW1HFSIToYeiDevoCAg0hxPyEtnC1UOF3ZuWLpoqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJFU2dUbyiGHQVfBMircA5f0NQl0j%2FFAvMSAfaGOOfBuPGNfQg0xT3xgzquQb8D2vunV4vZ4v1WHn4%2FdmgW2TP1THUUJtQoS9lUZ%2B326gj%2BDHJTDCVxIDKnrQuQteBp1XzjUQefg%2Fdjko8rcj2sOAZ6zRUTwEU0tO4mQ23YEZrAhnjKYjDWMUOdoO8kZsJeOpduDGUzQwLMxStAZmZ1X4RxicpKyZlVbpV5zAqJ91a174J3SNFFVtLBm49%2BTn6ilGj49aH4b7VAgqgigWksLHaNZLPu2pAc292VVwaw3wFmRzzOzz2Irtaa0okkdTdmkE2RJCkkJI%2BNW%2BR1RZv1FyCaI2MJwh9dmyJ9BEzHoJEkAkxIb%2FxFYZxWL6AFTI5Dpz3c9gPDF85ZMHw4JX8KtUfnfxeMLZJYlLdxeJxVoxAHpGgbkiNB%2FC9NBIWp5CfFjZdiZHrEc1m49lz7V7PMPK8GkfYDyUcBc02aQPvpqrDHSDJwlZc7TVQdetJH48zqnLRRc1bJfhiwwwCf1UacJqWBtqxuLNEUStoAMrd30CpqV5vmKEo%2FjpGP0AhR0%2BTN7%2FsGZH8p1MU4M0J6wQ8k%2F%2FN4RotQgvwKrKDEEh7%2BGqGoOann0%2FpUAFcYpJ22%2Fqe4zIRvJSb0RCqrmslS8MJW3v8gGOqUBTuxRBqppBKgcIIUqdSaAVfxUCtmE69ihNHcnAwaBmyEklHPFpLtyG1z3C%2FAeVpEiO64koKzftkR66yCmMxMdQZr%2FG40sEvODELJnN8LF%2FVi692iczhkFV1JFZGZ7ixGgwKs4GxH8ygw3OHCklwhOq%2FJBq0BITk86NqOqy3%2FpSTn7e8MT3XN5fJr%2F7c99TkDJqMjB%2FDgiGoKczMChlX2xjpPyXRnj&X-Amz-Signature=b0201663514687c08767695902a2f94b59267c083606ee3d3f073fc782aab5b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







