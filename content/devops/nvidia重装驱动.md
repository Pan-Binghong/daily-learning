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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGNIWYFF%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIATy5DrMznErhpR1jD7bPJsh6vRFF39yB6zn0XdZVfbtAiA2ymkpqfXtEoMmPWTNAZqskkUY6EZlXp1%2FCUaKDB4ahCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1wQlFXdCh%2FchlG5mKtwDfNlmmnAret0T%2Blw2X1LKN7mVIyIuxkT%2FFOnd9keRRBTeGTRWJLl6OKoLNe9PUpXZCcSMOmXY1t%2FAACzGhkm6tC0QQ9ZhjL9mp9fYXy97J7KCw3o4REFlP%2FIKYOy4%2BPd4haiwPHc%2BB1UU26%2FC3OJOP%2BtC%2FOqNzz%2Bde7aDQ6%2F1zey2SHIUY4zrzJ8hS9ieXdg0v0hlRKjTr5CPBs%2FMYO9DlcXXnEkVI9m1y5k0WLlIfRQ5i5QyIbBW2ZiM%2BzXFBFhvGE2xcOczdEOrlMxiaM%2FdImi%2BLfPNBeRXSD81TzUO72RNxjGemoEZp0i4AWRHYrEV%2FsTIb0MDIgbi52pUrk17rKDkCcZhbzoQmLzoiXMdWppmADE5WMmPHcmFfaQOGSe5XgZw0DuwA0BVKNxjxcd57zXCKp2sygVvKNetFlO%2BHuTFj%2FfR%2BkXKKtMCcQcBb6TbH2twC2Hw8v%2BKgWhCiqEK28mSd0PB%2FnDbJKiZojRqW9gep%2BEyJacWSDwy%2FXSb9BdeZojjqetchh7LlL%2BUh59dBtULqVRiaPzB4fu0Dar7TtTqR9xuZb5Ze3wYdgryy9v2wlhUyf7FIoefYlnNIMEpkMVnvaePQO7y6VWqFeUay0GqdbGi8yA8FLu7OvAwkvKvyAY6pgHFw%2BfxN0espvRxeq5RsZ%2BGJbuObQsP3WPk4uQ1V%2FcYhMFNnH0tKWalMjizU%2B98B1WOdgIKhwLNHMtdj1%2F7VnazJfyE43Z47zDyZeO2wyN15rcXj4X0zc2swoHPF4JVdGqrNHhidRuhEHKmdwt9PfOOiGpXQm6sEqjAbDt%2BCQ%2BxYB%2FCMUEsXyhH7f86vY9VIyAtQk%2F2QUxRwA%2FjZa4ShrE1XGESnF9e&X-Amz-Signature=9590d955b7144153ab56693d621c3e4eac85b78126bcdcd390ba69ec254f0f63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







