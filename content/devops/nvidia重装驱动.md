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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2FA5JXP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAL3wiAW291zZVI3KdOAcFxFoy7yYM2wGoCu6Tno5LY1AiEA3MhmhRem9T%2BJ3rGBhPkXbbpG23%2BBm69olygmMLXZjEUq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDB3Xldgehpvk3MOS7yrcA4uYSSFsYPludcOdgK8TGtDicMqtWmAolb6d8lvQRHv8Ofuz9l6OTWJBGLdMmJNmQcPmiRqqn%2BQGJ8fDYLcZwU66gzPdvKwxHtCWvjiw5fYnhs3NFfW7tEze1Q65kWfLD3qGqKa1aO4txABeBHnBZVbw00rb2EWrLGpA%2FBxIAzm%2F%2B%2FjSX5rTsNgiUCBjSnx2y44G%2BKnPNksntpG7jwYT8I%2FgrDXCcYPfDQFGl4Jmq35038%2FWlxyZNgZzEt%2FbcW%2FEvaefYtYKRc6pUV%2BQCxEPHw1w2EGd5y%2FuOJY3JyWjCRkEuKYsfT8Wp27bdg1sifB6gQhVc1iw47KtSX%2FVxICRslgRXeiAy8YMlCL0yYXBQWReJdyk%2BSIytgWOPkMdoTXLexxFLz10uUZGr0aVo2OFOzIhvrbo4ysT5LhRWioaYd%2Fh%2FpgI0ABuwkaQ%2BAGDgL%2FYASbnVCpbt1BEybktbZStyXvSpaIA%2FI%2BZLQ6wvzoJa6S4NBKBwmcElJS2LCl1E2OSeME7Ta7HX8nGQASCh8wKP6eilt7qDGVb8sxvLRth2xpgMGug2ZcPv5OosS7vNxzCDy8pmEWCYkKvDxiEg%2BkhDh5GM0GgkQcZ9OQwgH8zav7Z2FGKQeg7saXFshIoMPyrvc4GOqUB8AMk73rzRQehCWl1cOPh3yMrC2bG7svilyyoeYKcEYXJtVAM3KjYaFaXh09cJ5FaiBYo8GEBcVNAazWIOveDnSkWLEl1Cx%2F%2BLKRA1MF9e%2BA1OOgPDO9%2BnyCzxUA%2FnaeFQ0gKr%2FGv%2F9NQq7UOAJ5AT80smwU0%2BLZ0J0fFxZBiR4pPofk%2BoJuV39kuot8e6ysR7vBeGBqXqwu78MFBsCTVbPOVFZXV&X-Amz-Signature=e389de8faf7efe7ddd6225ecbf93a326f3975fa68819334331e6bccfd09f15f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



