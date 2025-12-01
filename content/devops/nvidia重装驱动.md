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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2SJPXT2%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIDtTAdh0WXjeWBFK7OnkfKIo7OV1pf0xOwMwZC1jMUYsAiEA9dFPI73EQ1z9EzOkJlAtKo0ILYxlTZ3z3g55utNZrsYqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEdqaG0O6kp3PyahqCrcAxtTPMZhP7NJ1nPWzdv4fMDcr36vYIy%2BJFQiN5AWPCX8YFG%2Bvn%2Fz7kqrp0%2B7tFsCl4B7rdiQkSYRHmHtoP3mc9q07L6p8jgdWZ8MFDBESM8N6RECGqohbp9uU2MQIvDTHh9cHKuMMUyrrMnyllEVjf9EKvCTOlXHvvzObQREGrUczT%2BvWtvJMxtAsZfm1sntcl1zHcpJq%2FkS8i2pKnuuq0cJCT81NtWvS4%2FGseWK3UOTNOWKXLwXeMOvtDtwVO7tUr4NiKs5IwFqas%2FkTnUPEMcu9%2BJbldQ2%2BHQmj%2B4LThY17ZRydP7GhNq1xetZIiJKu1Rioc0rTsqEkNgUzkAMyzXJMYO8iKQokj5qB9Oh6F345rT5UIanHUs4IVY46o6dvgglRe13t79NrKQMkUNW4LWfCx70UZnd2KCdVrbtIhGylBPU7v4I7qxmHzTcDECxHzK4HNzlaBGz9IldCV87%2FN3Ir3d7jc8r%2Fl5c%2F0DBlmHw%2FCJvgooqhryY3ZRgCqM4NM2iZ7lop1cmq%2F%2FUg9oFvwUo4sipXrBRebhVOhQrXH3UrXv5ksOWGU827eP8tWFYlNj3bNG2LOUIoX3JBQKOrXlEeLvpNKHBHSDC79vzhRqdb%2B3%2BkgJsSFu1F6E3MNWFs8kGOqUB%2F7KcO5pKFkXHJpTqAv%2FeMjZII4JCkyglRvQy4Vn05GyRxMHGFGZ20ZKjliZUMXQ7fs1fb0K%2FJ6Z6UGLvGEIfI4dDSX%2Fdm1moC3TAYUrnPBUfixg8xQxCsoAytDwwwB1NrR%2BKfbkukmuuFa6Zy5x%2BcwP5qJzfVLW6LoH%2FTaGeAzkKd1jE9GljqqF0NcRISTeLxQBwuC%2FLbTv119PZuWFwemUBbrHD&X-Amz-Signature=a9a243ef8bba6c7732d0a799ca820d20475556786251123fb4c5ff9ebbb5bb62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







