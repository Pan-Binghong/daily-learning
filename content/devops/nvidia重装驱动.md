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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRMPL2C3%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIC067FFV%2BAFGeox1AEfRtDw4MIVr%2BOrnHd685FAe9j09AiBnvp%2BOHiTffzhNLfoSL6wOi8UV7QwHXHRbHOIuh3waUyr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMfbBuNkmLxRbnG7knKtwDOrPL9x4o1x9Ugo3AgfJSdnRGkjbJsaOX8gpSbEyhtGodl5qnTfa2txWCirxHF76CwmZyxzcfu8a2H5V2zYkB%2BlE3lYo95czh6DiCo0PetUi3ex044buOwHFmlqqv6376%2F4Juz%2FYrVdz3j1%2F9F7Mzy96%2FXjbGj6RpLjY6KahENC2t3GtXkXEws9G93Qh%2B9sE%2BAs4pEbwsJ4yagwD8zJx%2FxE%2Bns0fEPjGiTFIruFRDrKQey4NAJBNeZUumm6TjQ3g5Otn66dQMtpeEFEUK11o9VO9o%2BuGOKCqkmI2fTBeIevhC0T2dJfsTbZas4rifXmgjWpGNeeYxRr9CIFB9stMVsJ12ULkV92irnSnlLKIAAIh%2BtyYGbNFNrgNrLF7ylOOnUQpoaRb5ruh3GJIDIgWKO9HzOPV67qkcn2G3sw2wVYjdpWCUY3YRwHMAFcIMaqxPoWdJlvGpdfGfAbj1kepvehumfMjT3pVGF7pdXguTRheg4VtEVvufXfu%2B8S7Gs5DTsbUwmDglfqohajBHqq0gmqvuygtXtIxvZnBFQFkbTXDNGvvPFRAIv1iwsdn00B%2B%2FXNlsJhU%2Fp0xF5esuTXK80IVKuCtiv59YMerZ2E%2FR7C2WnPAjdch1hTZTkIIwiZrmygY6pgHnVziJ%2FnsCMGDIHoQtJ%2F2NQrU2d3LfqH62VcKxHH8Jy8xUZuXb8QZ8Le7FUU5jLrw6TPhJTsEcRQHClHFZikjstGimjxDBopiJiC3zgjfCmzs2dv8GfR2zcBMTXxymESUcKZtHDFWpUFpm9%2BnGFzJ%2FFFUjdgzZlD%2BSfqt1AnYCru4xG7wSabqcB7zKYKK4sar0P44izbLLwAV5DCJBRKjRHIROp3SB&X-Amz-Signature=b97be25019133b1f358c24b4bd218e258d88e3823dab4d79665202adbb43dbd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



