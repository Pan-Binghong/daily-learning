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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UC7IMAX%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgckZuvFnq0grMCAZfotTZRIY5KBHKC1SUQXtSZSVHfgIgb8c2OH0yD%2BGWlkzQNjYO12QRQRVaTMDz09JGeOtf8QIq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDDQ9xkI97Iy0vLIBrSrcAy%2Bpi4ZylAKn1TPduLQ2XkVvM1Q9AACkN5OuS6YaytMqty7RF3b02m13uznvG6KGzO8BpGphVvLeXzLfOrGFj6tQdxkclHSbzaumMCz%2BMP8z6SHxanmgkIEYCHKOrovlm8pJVrXSyRbtM2wJDkXqPTwYpTNIDw7JR2CeUMQz2dXSSrZJl3SWJkymDme4fpYV4nTQ%2BSsLxzUhcnrNhqjHcaU1UIow2ZAUDl%2Bsjj7cQI52vJPh8x2nXY3QhOvzeu8t2QdgK1vWcK7VsNfNOhebSkzob0Hk1RT9TQo1AXOAHtmRGw0mtc0UMu%2F6jzgmGqBBXuMjVltFdXCXk13%2FxJA1cPeLLEvQuL9cxOoo1CQuIgR0qrJru2BjtS5PvlLsqE%2FVRncQuXylMjm7dubRh4sXVPq24La5pLyWkBskcDahXy0LE%2BY1DP3moAM0Ej6F05qUmrkRriHkp1zzJy3ubagRXHGIjVajzizsmHvEb%2F5WN6%2FDv2bbQcGC7JiZjIhZKHpU54KuMNNHYaeuwudHwcyUOHLp%2B%2B3j6qQzYEBEysmplU2ZQ7y4n%2Baend4jASf6XJBosGKqqMOZIz50o%2F9B88IC60QOYWpEhHKmXgtakR%2BpP3DnikQTlYvMQ3Z80RimMJHB38gGOqUBDqyG%2BfEaXi2EMAaWE%2FISjaKh3J79HsDeS0ybEKCwrW8Jn1ZNiWD%2FG%2BTnjnm%2BRAzucMaMaXzBLusCDhHWpKTBZhF%2B6f3KDSZIk%2Fht%2F%2F99y48vhsIsRy4lNLLw0WAlsginS1sBZmJVXlMMIkW4etsWinCc0ZQJIW6iNxCWd4Bnh%2F7PRegbF8OIe8jd76Q%2FgNHjCfeXbu9mlibXScvavQ6kxYizwQUT&X-Amz-Signature=bac0a46cd071b50879594232b62c85508a70f843aa1110a1ec26589ca4e67d78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







