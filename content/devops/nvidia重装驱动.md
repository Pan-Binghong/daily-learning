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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TH67EC5V%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrYobtTjifsWsx4p6u7jLRaCi5fr0WCEOqVi8ER9KimwIgLoLbKHTS8GyqeTIU7xoUJ4c12MUqH%2B69ISraFLogyeAqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAyNUzW0QPu%2BlouxlSrcA%2BRGl%2FNGemLRdRm7akc2yOZpG9rxUOJqC4zbUewOeQhEHxi2XzS2zqPXoMK%2BUf6Kly9pK1wxEYWkCV5M4utJqjH28%2FXQk2mGmlSfslxX2YbsnoOMlzOnBDYHa6Nswj789wHben40S9%2Bs58u9i9YXM21iBT%2FwSJxblCof08WMoTm0EJHYQ8Zj4kujQ3xMz15wWtQxSSS5w%2BDDfzZeYdSGuhGBalYBJ63q48raMGRZ9QsdtPjhw6x6zu20QHyp2aVScxamZcJEWk4y%2FA16jyYlicFlAen0E6RHihfXtLaEuEUEYx0qahtXRuWOrMm6xNbnz9mMJo%2FghTCbaNWDyC4%2FNTIuPoOiN3B200b4kvVpM4%2FpE1OfaFVb%2BmOnEt9VxcwkwZuN29GKN67D%2Bgimt2qKvMDJtb7dwoEGq79gxwneSF8tFceSaDchD5%2BDvleuAghTuK%2BsXSAh8aY7d1U7DMRL%2F9zs6930uWNDvkbTFS4TYEhMSWWacVi24N%2FvVS3DP74P6uDiJDK9qnX7TjTgOmlXghOj7qq9V%2BcmfaRfRh3%2F%2FUNJ1hUV54s%2F7i0Qvy6tjNz%2FUBAhqIrgsbO3g1782SHdXaYhw4uAqpGdmobw4osrsFsuw2ouKDtYwqN7yJr5MPD90skGOqUBqaV7dycoOzWYE87JlQecNbJKl8oKK%2FHCDQoalttcYKJClqJAOMNlZpurGTejkGOxNKveGxXZkhIWORKV0UhFKkqPnL2Yk8TbirnQ%2BRdItP9R2%2Ft0H7PjKIn%2FkSD38JJ434Tn%2Ffl%2Fjh3ODB9Z57hlqFCxQI3IDHXVeQwy8PHlH%2Baj5FzbNcIyW01i0eP3dOZD%2BaBztYcAoTNP8aEH7xIzi33kKo4H&X-Amz-Signature=3b62c547d8c892017d734d4a7ba86a31bb6bcf30b4cc3431fe11f9e16cb6943f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



