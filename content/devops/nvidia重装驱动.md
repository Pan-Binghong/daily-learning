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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEY7RYXG%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2%2Bttf6aIK21Oj6z%2FJ1yFJU5L7xvYq22cuWdEu177d8AiA6aqiycpJ8%2FKc6ng%2Fq4B2ceB7q%2FzVj86p6MO6yd4v26ir%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMZp9%2FnygDRNUdxDGQKtwDTLyFr3xHdzJ2OID5NSXb2Avu8kXt7FzTDl2638y%2FczQ%2BRX%2Fl%2F8fttDkYkXz1vG8A6VQThTtwM1KIQgp90K8gzP64Sebg87JkLkEiqrOSXIJEL1BomQxkFKU%2FuJO17JDKC5kvYWAUwKwufYPR%2BwhwrBmuQhfXMurZnCjZLN%2F359PDKXv192Ul6SeuIX5YezC%2FdedzEUe8dRKVJ9hstAuVDEqgQvMrgyA0%2FyWX31lP49DqrQ4qp0%2FgwwdPtLCpS3pQt14CkaE%2Bb1NEHrfd2DIMT7mLZXFS5WgwfFYqaNUwZD1C%2FKaxJnHQwRn5oEVMmaOEykhOzW%2B3HILQq%2BJmtiX9GmH5MYTtpS%2FA0VZ%2FYrqc%2FzTaMokTZTIocXGSEhK1mYzcTKsClSg1qY6F25RP%2BasTMHk8l7%2FqdU1702GanJW8OOsrWHcl%2FT4RTbqHMyLZxlR%2FTJgqmojsNKWFKlcNw%2Fp3a2KMcjS%2FFuQ5xuPvUrgB0tZguQRAoobMP1rZrqNRNTGE%2BW0Ju53nt%2FpiEQ0OCnViTzzz3tKLmL53IsAv%2BCgoYKQWSDJpNsKbonpquqqm%2BpNYGsQAtAp2jrrffJnddQiO41WAhwvSV7eQV%2BeWOkEtkfeAH3rx0CM9tKPoA2swo5blywY6pgGZBGDtnoJthuwKaLS6CAkiawcx%2FbB0x%2BiS9TqzncpCDxlM8PHz8BsygLZM5b03ZXbBStp3CQfbFtpLF9ZHnrfwDfbCiTXemN3Q1KertJzH%2FYTDQOak6Fy39vZRuyIIMg2HzggMCVYjEdsZz%2BtsANf2Xj%2Ban98gCWG4gS8qSfq20qWoiym7BuYii49G4PKhTJyuSDHPxhIn%2BKUvjP7ID8qK4tOHtJPt&X-Amz-Signature=afd3cf374c1ff4cc91df70e929e20a5cd092181d96c7f765272ba7e1bea023a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



