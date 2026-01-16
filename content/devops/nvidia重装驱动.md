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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ6YNWSI%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCIH%2BYluOg%2BMTV%2B5a%2BUpale65u5nbxf2xhzgMN4vqyQLgIhAO5ZJ9mvMOkSBma3fRcaY4N1omNcJNjmOBL0JBl4gZSxKv8DCEMQABoMNjM3NDIzMTgzODA1IgzWIX9b4rxzrBPX8Ecq3AOKGDQs5BfB0HSlX%2FaAIlHwQpcwMBQ1M27N%2F89H6Rla%2FdXWCHfavqjdT86wjT7Zutq6%2BwhpguIH0EGXHD8hG%2F8nWjHZJkxqMDvGaSQP0UZF%2FAdectF2NO4VWqriHMxYgNjP6VGdP6Qor5c0QQ63oZb%2BCnrpVrS5luoiHNPWd5gEdoXy3PdB1Vc5B%2BsWDcvo2tyQqKu48f%2FEKIWDD8hH6oZYaYZf%2BsDmEwVggjqP%2BIDdX8dYAiTuN6rdwBRjETGpJvCNg0of08xaAkSVISUi2xWtznMJ3O9M%2FreQO3rNe4Q6wezHtbjmh2IGsvl79QgqDO4DqhUZI1po4yVvjj5t3kNP6nHbVMvNj1sBak3q5iOdLklovJADgHAIaijA72u%2F3RyatqqqgGqwJp62NJFtXBMP1pxkQEJyA181ftS0tAz7RjgnX5aLgkDjc5WOD40d3Im%2BC09J%2B%2FEYFBrtvAb%2FthWPiIkcF3ghCUl4qfzxtcJbAqb9GguubtzuKB%2BW7IQbyru3KRGRK2JEi1XdjpU0oXCmxSWnFdVk%2F1kPW9gAc9E4lzUnvZcwAE3PR2ECZoR5HTZ7CDh1Kn7zeWlfS8Rm2tgpCxYwp0WGx1Sr%2Ffyt4I8azJf%2BC0tyavTjYZXMgzCMv6bLBjqkAfPX38homNqyqdw7%2BonFK3r4p%2B3BVrsy8dTVHTJPKxEJvC6SvDzH%2BQ0QdytVi3vgWEkGizaZwD%2Bn3YBu6mBL0A0B0HUw%2B1hq2kGk8bHJtOlIPhwYP5rMznPXE8IKMEcq0b62r%2Fnl%2Bsb6YBLJwdATgc5m618zsSkHyNGCTrnuzKZ%2Bo%2BAQRoA8lOKMXtq%2F2%2FEDa%2FFWv22%2FFf66OAL6sqrZIjtaNgRF&X-Amz-Signature=08961d0da1491a0b2f3310e53645e0f8ea5a57c710d9c33005f4872018034043&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



