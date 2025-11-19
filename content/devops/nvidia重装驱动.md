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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZV6E3LPO%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIGWpX9RymgohC5SeyTVeqDvCm9FuLxvdOiuUxZJ3FJFyAiEAhT8QWJii2b4FMmJbmyWw1bvB2KRIRBoWxnKZ9JAxncUqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJPV3gj9ageVbLnYbCrcA06FMG2e1Z3UZIw4NKYlvdl48hXVWbIaXzDM8YfwcEOwBuxgDA7NkcfNz8BChXt6rt1D4eoeYUyPxmoTzP34l80hOb%2FmizTEGyR07PkuA%2FhtgRmOy5mlKm4ba9XRUWFma%2B%2BRXGGMU4cNF22zNEPXEUvdfYGZnfAhvHRTvP36TcjfF00Hi3xpaIrJMGP30wWKU6fQc0UXGQsG5unWuup3OfBmgKgkkcClLizmjxmDHGKA4PeHcWZ%2FjzTFEA7yzBCcXM2UoGIxH4N6myBaRZNvjmSK3%2FgJG56GdIFESF0x3r%2B9pjFfSGhxMqqYS42tVjIjiAIRaVhySaqR3DM4%2BOIbta4e25kXCTFa4hshIn1pkr5kyLNazxexIGDS47B4Phi%2B5xm5K7sE6CV%2F5uacf0DLWAzjAyDQFxYYiipeu4a1Fjw4zg90n19wwPrlA%2F7tJbFIcBrsrDAwJDER%2Bc6%2BHQyA0syYo7gGBSg5gb5EArJ56u3IMuY0Cs8kbNyLPIuZqM0mmny6KEupmaWb1nsbxJrJlG98ko0uy2scE%2FSEWUcJ6Q7W8%2BP4E7vMEur51jnAXFlSVowB7HVx0FcXilW3E6kZa5rSuJBJxZaj1iQW0SLdf%2BknJ3Cq7MVo64ypkaN7MIbL9MgGOqUBzdOpinIG0KWouPJDukoNgFJod%2Fo%2BW8NT4e0WVLrIwke3JIJjmGIkQZEqWbDLGUh4w2S5rRr9XRwJlcyPAHYdYJq6PY%2B9KF780hnYj4UzIx81cYkvJvLLQ7zz6g20PEpPmHwvnmQDV8aJJ5cBpk88Y7G2DJ2QsSQ32qp4MyanmoCNKjcI8RyWAuTxbdqqy85x5QJp0wnzoOEGfzDKlreFGbHCF9Nc&X-Amz-Signature=1c543b1047083c0c73d24e288d4659899c28760f9e5503ef216cd6bd41e023b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







