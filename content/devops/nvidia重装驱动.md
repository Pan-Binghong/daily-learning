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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5SME3B6%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCzJxut2h2ko3zUscvz8zph9glz8rDzbGzqLZzI%2FHuFGwIhAO6uVO5%2B0kq6hlScs0sAKNCwq5%2BTBkBy8N9UvfJzYjUAKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJLZyNwYMiUC15wDsq3AOXmGmGz6UkQ01BLcN9N11cc1Cq2tl6KiWirU%2BXagUGLmwpZjKY%2FeNWuUySZiHDg5vAfk%2FLZ%2Bqf4uEjEbmmS9Q19A5jp54tadcjNcpvItaNUnxMLn31FqHOIt20HwTMgQyLKo4ZJOw%2BUfGGR%2FfXZIVaHbvLToJhTBnS8g5jWtOFAuRJB0QsOpuySnesulLT1AOlwU2fIZBudo4QO4U%2FoOoTXW%2BEgjTxn%2B612amc5b%2FE%2F4lraC1jYLhz5uE%2BhSrrth0iK1D8FCYy8I5ydjSWl9mjYSzsafOKgIqlQKgu65GVZ2kji6lZK6%2BRZnSc02ojTx6HfWL9qIEMq7ux1hgvd2%2BrXYAgg9txLeLA3XD1PbfyDPC5kLg1Krpw9ukHHehk%2B1wq0YuQ5B1R1%2F75cFZXGmFXlUHlcgvSC9Fv%2FNazTrn7VB8ee0UuIcxijsZ8DCPdCxtxi52d79w63qgjYZlvCOqKiLdgbXPPJZncdMJ90NYjxu0C7i1oPKZhlJJhDyecCSxausWgz%2FNSUlfclROvhHc7Fz27WecztOszrArzcQ%2FQc5KOe5L%2FTzQb8rIK7ZvQ9AZJzdaJIhf6afdoTQ5httuoNFM64CqRzCQwXys0vMQVzMQGUWscd7nUXyN5xTCwtujJBjqkAVuh33ZLsN4y6MzuV%2BNkK3eEHgB%2FKDK6FwWlRe9WlNd7MQKXzll8KDY%2B3ulwsE0KlCPXB3JlDbe7kpC%2FqQfTY3wtgusp8rw%2Fuo5X8uCMSG%2F%2FqshFY3W3xVJ4DGjyfEbpPe74JR5gLeGgseARSzKN6Al6KLU4lZEnlTkx6IkLBMYFvzynn9TZn7TjdZHvCJFoykCDnRcM6hCL0pe4dyTjvz1wGENn&X-Amz-Signature=97f3d5e1f595b70b2d01ccab3072d4d4fc716144ff06ad44ac95c047d31f0209&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



