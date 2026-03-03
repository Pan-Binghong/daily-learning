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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QND6HGSE%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHPiFz8at8IRgUrWJcCHEYUsbdmF09HAwe4Jmio5FUf2AiEA06SXrsoSC%2F%2FH%2FPiTYIilCuc6SfRUFWD5W7o4vFgA5vsqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHmaX7EWQb78Ei39zSrcA6Q78vDNVEe8EQOlXShv6p1KfR893Dch6f9x2EbSKTEfW0CV3RGAkOC31gX6bRaGkXBxkqu0dGTdDcjnCyKU8SbPDM9xw4EKqoDlcfoACA8sHYUMzJ1hZVTM98h1f%2F0lvtcaXJ0MKDIQmFE0dVkZsDJZRntB9JImXTe6U5uuLpkaXtfi7jlTQVYjCvkYrauGfU4kt2syXQILlzLRqCMYGwjvHMpa9MuNpQuWWUEq34IBNFRvhvQ1nH8TWAouHwxJzFJxc57FdeXHPQMm0cIfpEZg1lBw7urrCp9wm3S%2BRT0X2Y9dxErVCpkF9XJvC5KteuY6YPHREr8aRpZuuLK6zZEbpjK6BwIRckVpH8mOoBrdf4dQUCOlMiEmLBi4dM%2B4mtlWBxtZW7Xx9XWKgflV38KiXnjUiaYM9SHjLRZTOm7tjVSDJk7eUofokRFlecTdlZMHIvluyxRtNXtjrp%2FX297B1W7DcodOHoV7SSpfWmOzijMBrWOxJCYDlSbM9PkGNpglBMw9COktOw5hbAF38Lid%2FG6UpWNOWAKMVgpKUgSeoaXqjEuMYw1tsu76MkA%2BjglvSKRNICTIm9VqHqfwHvXPldT5dDkW20GN%2BCGqElOqGMe4z1DeNCfypo%2FEMJK1mM0GOqUBdzcF9aG3MFmDiK%2Be1nG2EYNZUMDUdC5COW1yoS6%2FJJKN2SRz6G2MBEIQy6jBgYI2T6D%2FHXN9Po0BEQy24wPdbfGWAV5p7vu4yfHJpsYAVeDhFcFlgdiCMIMxHtBFnNShFul65maq2GKMn%2FLOKixuz6I5bmh52GCgV6w2P58r%2FUdxqUOcavk2k4jwDSJ71KTZ%2Bn7cw15YS4r%2Bnzi3PNhvMTmmRL3q&X-Amz-Signature=84f7783c0f020910e7eb07f0dc71e69d284db44d8e1cacea5ebe68cf1fb3a516&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



