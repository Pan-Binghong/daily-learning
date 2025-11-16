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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL2YBA2W%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDi8plALI2IW91kL1Jh0LYhfnP3euWxlUk5tvvkRnmuYAIhANWXkLA7miA2CZlnu6uEDzjC6KkL4ytu68403pk%2BRbNKKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVJrAnyMXn9lpobe0q3APb9ckLDebg8uob%2B5IyRuuG0JfmTbRphFfjMByyfb%2FsAEYj3Dz9EVMxqiCR0uzVPdeofotI3RPp07bKxXfYahNSWUoGr5bd3%2B49KSljaNTfBl9Q1eplSC0ZqS0vzt5K%2FnbUc%2BCEGLjcfuJy7WkGjNWowMwEesm2HbLfDiBVKogE5B987Q3%2FViJl5nf94RTDAwDFM9Wu41IqolaF%2Bg3YyPjkEiLlUvE4df2bljmGlkt4I%2BItzew78ZgepiX20iT8d5lKjFtTtHAL0H12vpGJ1ojfItzDV6NBCqx8VNLJS45bkak%2FVyC7%2FpHfiJlKh8nmf5OxAO%2FQLqh834BZu0ZsQ8S9rEyMRxz3N6kt7gczAVT5INFoJSsjr9jIu7H%2BMRLiXOdY%2F9zTmadRDu1Z92au%2Bu7ys6TKLBqdzcsUgx1sjfRmiYe9PvTgPEg8u4UyDTzAnGWOYOg9d0Fi6aCjXPFiAwy0pYUpghPFBvCclqw%2Fg5rHXSXRTaZfCa5coQjId2goPKB9ZZoqmdW4BOBy%2F3GMPtZPCP4Sqe0HBCgffLoW7ADKZgBsbTjVhcqTVDXH1rNsdl0HTIy2YdNPJTdOReLy0jY36oR13baksfURf5VW5kIatnGjxib50grADn4zRDCV4OTIBjqkATfmcTDuWxXul34bx3KW7IilpZ8sxUu%2BJFPOsv3skCR2mj1mnf7Cjc3fos%2Bxa0loZ1LefBBANSeEuBeDfEyf%2Fat8PsoBOFSzTThkfcX3NTE2vWQ75Q9qY0QEOD8%2BnBK7HLHc5T7ULXqS6%2BaVNJGTfBOhu9Cnrbog8KFB0PrSL%2BYmC%2FyOH6tLZ2eWInCc5moZ8C6CSyuG2%2FKMlbkZSFPNcA300SvT&X-Amz-Signature=97ddc209208fc792efe2ba5a8ca14901a32b012bdb4a6db9f425e447e3a0137c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







