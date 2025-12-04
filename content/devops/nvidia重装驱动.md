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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOFTYNON%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIDozQIlfMpV12XmK%2FE7sxmh%2BCFtJ9vp3JUL0pRlx1AILAiEA9Lw5pNdfsPURVZhHZ32gJeIaL5kjUPEkoj%2FKMDb3CRIq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDIWy2vrP5NHa0BKbuCrcAxQdslSEKmZCWnyDJX5MTKgFU83p8K7bygoj5dEUK7fMOeOVLlCldySsnkyHD0dlHjo3K4MU3Axrd3FDgxUDvAivhHYWjBCDC8VMs%2FrJ8lyZ8%2F5d8UDXC42cxsnrPIjeuKuZ5rzah%2FEudBkNYWT8KPfrbsoLWb1AuunWnySOiGLM3x4OhZ%2FFgf6mUc6ic0%2FMIQcBT8f49lAxjhGrvq6hKSrwD4QUiDtY1n9RhkPrXquSnw%2BjgQ51%2B84urbATwdHcuLuVUr0hjHPb7g9VoUkr3Gbo3mqOuVpcktlOI7V3%2BD4fv30Uav%2F%2BXk6%2BSeAMLrk%2BI6LyutHLqTwHxWsgoSddEG5x%2BPNXssbUA8aYgGDEOfIMbl3KfolZR6EfBhl0pF0QxI6%2FD2PHI0M2jBF%2FdcpPkQ%2BHWSzv1z4eemwaxOnDRZFhCl1APkmCWms16mi5riYH4MwUcPxr75roucBUJ8f%2F%2BWpjYa%2FHBdqmLhlLfBgzthY8PqS3KERVE0pbU6EELQZ0RlWCVM3qf6oPwpP%2BIXUIAsykP%2BHX6Z2WIbhUgRxnJUSmwuvnNIvCpaROySmCgUrtS%2F66CbdnK6%2Fh2fcp6cxu6wjkqEgByBWxV9h4K4lovep%2BB5O8Jzpj7WXOXio%2FMO7Uw8kGOqUBv2f278vXON9IGf2OkkyVRVZ%2BnS0sD9Yrnjp4x%2FkDUzkpS45yn4HD8wBA8mNzb8bNvJlWubKJoQMJ7V2rd%2B1bv3ISVYd3PltGTl6VL6Z5u4m92Dkrvfy2LEV2rv3J7E3QRaNSCCP%2FjZSQGUZbfEcLJjug21%2BQsBu2aeOehJzdbdYbQr%2BaiWNo1JtzEbV8ZEm%2FE4ioOL7%2FFjsQL%2FrA6SMxKzfBpK%2B3&X-Amz-Signature=9e1e946948db2858d0ed7b89d8f5a367b58e541aed0741db183cb839a7a74f2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







