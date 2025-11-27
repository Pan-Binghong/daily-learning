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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZNOQNGLT%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDqRfomLzCAeJNvylDVGeKW%2BfaKwCZvToxH8Am1ZHXmGgIhAO2Mroex2JlzlxBp4BQtiodq8YNUh0%2BUwCIKG15qAZ3sKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgztmnyYyFlMlNl03%2B4q3AOZSTSTYVaMN4g3uk3U0%2FkRSUjkgfpoMQLtkEYiX8zdp9S3jOPFYJ9GaJ3IUDgs67Gcj5Sc%2FCQipf4uCwuAexZEnAqow6TdLS47N6fVnt1sAJRiZP%2F%2B%2BLT3vnpcp%2FO%2FH45AS5SK09%2F%2FrrDys%2F4rc47Ft16KxjCfzMQU9btwbKpz7PC37SZIP8MBUXbuqaUrFlTN2y%2Bd%2F0MOBhIvz4wELoQ47Vx4Fn1WpG92zuIfWMeNfMR09F1SyW9MssJvWbTC9cHH61XmGGttYiVi%2BFAgBO6BXugwwOrgif3N%2BG2uHM8W%2BL79VPzSFt%2Bn4l%2B%2FGafQyEGE7HUdS5wbRoOvvyWkYM17BduEdG3Xho6AjRN5PD%2Fn78juQ2uYLPLvR0Wzi%2FEyhdFOhVale%2BHpnwxccIffEyrYLEgBAngu2oWj5zimt0TBYrwZiEJIl8lfocVRS4rwcboJyA1E%2Fzt%2FaMGSkmdMzlVEGA%2FM2GEB4M8XNBdAQ6KoaDNmjCW8zGmGueYDojmDRF20wj3QHXhOM%2BpJYNL2ViY6mu4NY%2BjxI0Fg%2FKfKVXxRDM%2Bgy%2FRZFt82tcC%2FmhrmnkEOpc%2F1824UcHJ22Grz%2FjnDqolrhVfSxJZ6ZhekwNto6JktFp7Mdcztm6Bz%2FzDnzp7JBjqkAVYU3BF4XKnyldhcyLdeeNip2VZQu5HEbTVI0fG6Zt8xugYGm%2B20RT4t97RAq0uKwgoLpUjGAzzifbJyceXux1YVZreimkrmsv6Y3sR%2FrI3Hl8zgrvTorsdi2fsHbXWhvVj9BgWD7QEdjKvDr79qMYQOf9zHJAW%2BXrzApSQvvWFqDg%2BDY1B04hcP%2Bvxvu7RqfKzZhGTY7bTtFh65MvBf3ODaQvjx&X-Amz-Signature=055ced44dca20cae9776486c8d7e67b7d1c0899127c21defc211484155c66099&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







