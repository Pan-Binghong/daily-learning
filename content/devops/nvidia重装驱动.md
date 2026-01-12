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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667266EPCL%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIE22eZz1DjSdkP8WN%2FzqGrC%2BDAVsatqqMMgUzWFz%2FPHMAiEArmpG0Rddkz6J5E7z5Iujs7YXD7imXhgi%2BImY3iwPnN4qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHvUgdg3wYtB8sgxircA%2B8yyVQkSfN2RXIsrWF%2BZCcSIPWiF5wjt8ZnTwWWkeUagTqvuWM9T%2F%2BWqBs8xpCNJ8VLERbdqyn8DQL%2BPcOV8sl14%2BbUrYKL%2FsJ1Lh2RWeAD0OSOBxd5j7M7HB5AU%2FNkZ0RzCV3L0ZnebogBtUgKjM7nVUhUEXDZFsIYHycgBpJm8bG4HSk%2FB9m9R9GnX6UUOa%2Fwib6oSutv42IXcMGmDx91tpNRzmnAr5%2BSaRPPkpL1kc%2Bob1MCplxPWOKP0VyF8jB6EfLozD3SLjk7TbOa6WU3beQgchIAJWVusz5M4juogVTcvedYZasi6sTvoL8HcQH7%2FT%2BQUjkPsIFyx2NVevmKiv%2BgMlJ%2FL7rkXvaccPhRoEJx10YpnCim1rFM65stDuYCEeQotFZRca4opM9mdCip%2F4MQbEIGUnlDKMY8a44%2FyB90kEzic2kQlQFmcsdNGOASmCOEUJ%2B00O%2BJ%2BBHILJL%2FmCTTvjnbOAms7j%2BfL3FkySP%2FQXWLqunIJd3gVrjOXmZ8JeLj4Ww%2FvThe7oOhB3O2cyXcGEuJou1K5Sw9a8BLn9er44WINY3%2F7Jng61hakHbHMHSgERr4R6TB9nOj9SwJJDhSNDaGi1OXscyGlelp%2FcYpK10CjF2a1tHZMLP3kMsGOqUBr3W1QLaGZhDLtZWHLpda6tzqkEkR5A51VQ6FaREnELXI1jfmkZKbPg%2FjELaD5lI9a%2BelZuuFIidFDyIBTbOGAaJNESIDkCVQnx3TpgQ98%2B7nM175UGk9SUOIUvhKUB%2B%2BIWeAhVsqTLYO4QgacUud1jcIShoxSwOZZ3MWnxnwJJVSpMOJbglf4UnwT4VsCaP5fO%2Byp2ZkMjJ%2BR1Qtg5obTEdFnqWR&X-Amz-Signature=dc59fd7e36638959ceea9456472d7085d8a9068bddc3a6637dc217c574c4d834&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



