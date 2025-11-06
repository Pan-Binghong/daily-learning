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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWMZMXWB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVj4YaT5yIxkYMk0hqWLx%2Bvhw%2BsSpnIYh1yhWoKJliAAiBTia3oVmChiOpSTuG0l5nt%2FVFxl1sLCtGCMEdP%2B%2FAR1CqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxTDwqdn3wvZwY23MKtwDjj%2FDXNQbJFzRT8s4o4x72lcLvHZcMH3gl777S9jJLy2IrgxSzxwwM4luCL7ix8XWVS9cLx2g1G%2FhX%2Fm6CvNrnQD64IOxa1hBFTJqQDxYMhNvnzOZ8pZH0idmhd2SaLycwkWh3jmL5VKLp7WPVTSuBHZOeW5mazqRPmGvVfVSzCJuLbyyxW0TRi%2B1MIM%2FK9alAFiwg85VyZGn0%2FOky6bwWn79Z6hAiwhBVy8yZbN4ehrozZlPDfi1curAhNCM%2FfMMEwvDq98Bw1lsr%2B3QDw55i8UtOLluVneC4zMdNdQtEnpZkXMyPwn9HgVNZ6iJis4v7MDvt5BgfWmJD516GC3DELABv5GRA3ugisOfwdHX23dth4kVNr2D9WQGJziPXIXPUYZoZ7dSyRtINWDus8IP8t2DbYu7g%2BNNpN2FeizqPJxjIDc9gdTx%2BAOD1pcR9MLRGOYc%2BBHJNrVhPI7KMjJculbkytIG8ukmQSZJSsXBP0QfwnVqZZVrPIWyCxcJfVBv5I3%2FWUGNXYpYrj%2FQXzpXV49HqUQfoFyGWhpOevZL%2FkZb9rjMjAJJzZQuV5tLmClywm8Agt%2Blycg%2FL2j7TrePNMD4PFPvXX9BZonyXvE5bV4BYH6n8C0nbPH5zM8w7vGvyAY6pgHLRe3YFBdj1ATHU7onjFlxtkO7fDxJpiKo8YZHSjk1%2FOv6u7g%2By28F8IhI3%2BruYuft12zNvxHTC0VPfFtt30AU1hdqQzVQiYMRV7ylahYvRYIQ%2FjBuZoBDu77sdUEuVaTXvIMfNrxLLXmhUvKDpwfp%2BCkKkoBNv4xIA5ApQ6EzuNMvtLuHKO%2BPMGUZ1pN6qFXxgy5HbOwkb6sZ3zfnPFTxQiBDde2J&X-Amz-Signature=8850fde7b3ed90ef0b25fb8f454cbcc2fe5dffaf370f9e77843bd11d644a97db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







