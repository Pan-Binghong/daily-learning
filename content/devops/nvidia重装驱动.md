---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2026-01-31T04:33:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623U5EJ2E%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCICdRcWkN%2Fay39%2BGA8f602C0obQLMkkdgJgPbsF60OPveAiEAv6gfThTmCaVlH6sD1FLHOYBZcfd4LLpfBRqtCgvotU4q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDDa4snbBhw9Fas%2BVlCrcA7R%2B97A49oZNqbLKrPNERPjjaRkrPYeE975EM1i7JqnUZZzEPZ11R05ektgecN09bbgkIWR1BZBSHi18JhnkFGF%2FGfxwNLCP%2BZgNSn1L2xjMQYh4HmkhufELoOsVNgAMV3CU2I5MDlV4lKk1d52nscQSs4sIpVd2YJ2pL6KSXWERc5NspM6MNGqXkLJfJEc3iou9VqjY81ew5ex3xryUQUZbZhv0ie18s908GE5za7sext2PAncvtD8lPr1ePi5p6qJqwvTiNv5X%2BVhpgXekLppk35NfiKZ%2FfwjCvNpZybjl%2BupnXc5Xr0tHa1SmRnEfmA%2BeGgXpnBcGYV3czwWIJtB1A2ARwNF3f5zd2BRMEVBVQpOTSEWAqxPXXHV9tytrjbhE85Xm9%2BBCOsmagttPgfSMKiFe8BDwnCNQXLBOrN%2FDfMoRF57UpzRAgp4h%2FqQePmL1ZmW2wDI%2FINoN3WGWOoVmt5MO6fOeKhX4nbeaDt%2FNFeUXqIPe7lSs5zMRNyZXopStBJOtRKH4itU18lRz7o0Wch2qNhTgt8Or3TI27jlexn6jvLStPPyk1zliiOEJk3NdRzJxhcniX72A4p3OPa24njXko4rBb2Lw2F7vonFPsAmxYP0WVQRoxstvMIW6lcwGOqUBg4YbX%2B21DCST8xlNztl5%2Fp6EVxIeg8qLxE8EKEm1LmSz6MgYn3pXuxBdWfjGWzxfEUFeH6BAc5vhap5KuPeCiUVHa8TfFvlMHm2fIX%2BTFy24AFNbOMr%2Fbfhv8wHWpFPENZXznzePmwQf%2B29j1llhAj9xw3F1Md4IW0hyCThX2fLT2tWdFc%2B%2Bpyg%2BfDo5f5onTiQOe2pW31I3upPgTriS5RkdRW6g&X-Amz-Signature=203c445e1befe7c25a16526408825677627d922297bd7717e8f8e43618a0cea5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.





https://launchpad.net/ubuntu/jammy/amd64/nvidia-fabricmanager-570/570.195.03-0ubuntu0.22.04.2



```javascript
# 1. 停止 fabricmanager 服务
systemctl stop nvidia-fabricmanager

# 2. 安装 deb 包（强制降级）
dpkg -i --force-downgrade /data/pan/nvidia-fabricmanager-570_570.195.03-0ubuntu0.22.04.2_amd64.deb

# 3. 启动服务
systemctl start nvidia-fabricmanager

# 4. 检查服务状态
systemctl status nvidia-fabricmanager

# 5. 验证 GPU 是否正常
nvidia-smi

# 6. 防止自动升级
apt-mark hold nvidia-fabricmanager-570
```









---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



