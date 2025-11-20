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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJEWMNM5%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCICxqhKnt%2FAVfLtifR4WwZggWxSV6l9ePC8gQPgnOJw2qAiArsEd6Zl8021UZ7bwg6OJeET0C5PrMrXC3Yc64RpedMSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjub0X6Mo3Es7Ev0uKtwDOOnsphTCedQmmDgxu%2FONGllQkxKIOJDP3ia7jJlyoS2NvNt9Pi0FIsq63HE4I5T0xSWTK23ZtOMwN5J4ZyVC28eT5KGyO1HdhfwrdD%2FJWdbsayffvcefNnzq5Jk6xbgTT1SvDhUX06aUS49ibV3PVu57HnM0xq%2FG1LLsNnmdGQpo8xwxWiR7tpl0ksYUiLbJjJdzMI4InA7o5kVmY%2FHkzabxwyHb3XrWgSC2TeYUfNc8jfrpUwfv3fpw4UmSP5J7eBV5KwXqubd9Zzp0iXYNjPzrO2hev5su9BXGilRkJD%2F8QlU3ilBNxJ8twhGQhWHozP2qZ0nbdtmIlpoDCHz962DZKv0XVtoOuffqmaB97v6KrrhgtxoAWKIf8FAONuUobMn2xVOSGxiAbqp6CatAygREIqAuAIQDx%2Fq5R2EZxWD8%2B5jBY0ZapwwSBpBxgO0Y607ty4scQrenyeqWeIPOh%2FQPAxEIolBZ7rjqj1k1bfg7Oy%2BYbdKzHcIJOLj0bnVBrEjephzkmYC9FjPh3xtbQUOOvayhLX%2BQOltgyjUfEiPIVkw7gAYePPMBw4jLwOy3N%2BlTGVybL4I%2Fvpn3XennoWD4qjANWShmCR1cFJjU58nugBtdH0Un1HPtuoEwqur5yAY6pgGTnJXMMXSMBy0646MoEYQwFFfM2ZYcxOzZPBbYEoIs4ggvPbTyuX8oLiRWD4i2z9UYQJNC7V2%2BBHbvPuyHKUAL84ZfEsfBhQid7mKHMfcdqtVrZIT27OBGAOl%2BorNW4MTYDeLvqVBTDBQA6qpzJ2OYHYCTwTi7W5UzfaRb2Eoz118P3DGchoRmnD76n0FnzmXufcjM5c1KvGWLaLO5xZ8ruBsEAWtM&X-Amz-Signature=db6f73ccf34769d415d37f6ed239d4b1054ef587b31a5182dd624284646fc89b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







