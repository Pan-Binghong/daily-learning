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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UR3PMUU4%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIGKkBTz4e51nKkWuJAy2AoN4JFlHv7prB3KdoMIh8h4bAiB803oxmPOYRpaaQUQKfajuK%2BbioRjkw5WDwmmIo6z0%2ByqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkVtEx2EZGgmQsVSxKtwD4hCseK%2BDxtH47LXOz3Tt%2F1FKZ%2F%2BLo7iDtjdpzDczZh4SCO3WS4eQ5WGcm%2B3ljLwkuVEbJZ%2FnkmnBAgzXRNH4L%2BYZaVBqqHFR4eoVoB4xbWDDL%2BdjnQ1o4JtWPU8aA3CBaKbSbjOnQvSdn1gHZDfTOqDZZMLj9wJxFrOpf%2FatNCUblg%2BNYAtEju6DwEUL1ZGZe2pHNUuLDZPuiGHlHJv1u9YcIYaDUz1KKOF5%2Ba9toIWfa4tik2ftEGxqurA8d8jTzFTDKUuUKVY7VcEqxRPuUQ52gKIQa6EA58CXISW6aD1wdPQRxu6PY%2B9sINNW6eE51S6wzh%2B97kR8RgabcTIBbFMdVl%2F2%2BZS5yOr6vrRfhPjvlr5UbKw1%2FhGQW5b50eN0Wv1CG9RMeNIm2nYdaQBPJXCEm8VX%2FWRXSbwBYqfIrFWshpiF65b1VkptiNpEYrDQWjTpFUPuaWVPqBKH7yWqLBG1dl1ZASzzvp%2FQpLLS7wORJDRk9eHAjcj6l3rQwtCGqmdYX2wuUVOXhsdBmY9F3r73t5BKeSPbApJbGdkgoewbf6kRMiS3RvrYgd30cjEaKFRKB5FBJyZ13uzFoXY%2BXL51BnwMdgdOWW0%2Br6DkOPozLHJPb8y9h086%2FJcw6pzXygY6pgG19nfaNVw%2Fskjn3fxddcLMMBANR4vNDGndudb3oby%2FEOAfET7UVvPOO1%2Bc%2FceF9G%2BUynJShGy4MNF26atZ2DGVT8PYVbKSyplY%2BlBfq0frGFmrtX2C7%2F38tcF5avGzD9V4YtC%2F8B%2BU5SdNCPSnmJ3VJ%2BCqZbVoeIemDU5RelMlcWyxJ7T8y4bhPfaOs7hNeNGBoFvwq8mbwgtFrNlmIUubXGHApmzs&X-Amz-Signature=982c04bf99beeacc6be6a49299bf6aa520805a3ec066600898dbb6b7e4258a5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



