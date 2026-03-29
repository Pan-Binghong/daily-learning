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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGAVUEYF%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCICZGbuC5f9YcQsJrEbeBZo3%2BWSoWFPEbymylnuhDVQSFAiBRu0nlH2cWzTnH%2BzEt0dfYP3Cd6RmOuRCwV5eqz8Mxoir%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMWKX2NZ%2BbkLd6C0MyKtwDlhq1z%2B9Ya8FzuUYcJw4aIWetycS2Njor%2FbE10jTftuMp4OFz4gz21auQz1M2831k3qkBmU%2FyTFLLWpGJUkiTsHeHzJ275mU2AgScv68NZuhsf6dIaHis0zx5KY51EWyIjuDsPOdO%2FsO7DSuVCPEeVLO79BYGQkQgvvCMXqZrV9CpS43oCd5rzxKH827nNdWpt4YhscfChuU8Yy%2FfWC86VBh4W7ichi9W9AL3gJ6%2BpnBoVKjeoD%2FCDX3FMUdrlPb1GvLQpk1DV1jFyk9RSg4plaRcbcedYPOLjVNZbJQ%2FUKw3DBPBm%2FBbvH55YRgGrOoAiGBlGDtwllgMQf7je1UXM6IkMx6ssCqqpngU0Nx7gZ4iZzR7rPKEGSnzveuXPj5%2FsUgs6aQ63JpfHWK%2FeWTVzJcgrneUzZlMcS%2BuY7JbgdwGe6u35KwwVpqJ38FmCf33jooP12lMxsLisCnU%2F6EQ4gvGrjiIhN4W6LdizxPLg6PJZAjVmg1TNf63I5jo4Nyyh%2FEuRxYbghokvykExBGPOLKbWL5zlwIsln7JA%2BxIczF4gCBoHEJCzZ%2FeUdELENBgd8r%2BKcA7B%2F9X3GRM9U%2BKhrHOL1CAyngsr%2FhHOkXdFkxteSL4z3lcSQHjGOwwor6izgY6pgHVO9NYOEd2419dKDezevP6EO6DukwWa5zBb88KaZI97I1zx5tixYg7CV8tiEwfzZYkx8XiaKw%2BB7xpTHwwcG8U2%2FBnXi5Mx1lltdp3AFBZCka2G0zq1LumHD2UciTGOfAANJcETSdAHG9vRoy7wIpv519vudE38FDuGi33mSq79e3cXBWCY%2F9UgHGM6G%2F2r78uw6H6KKmS7LrL1b%2Buz8ODxo1MPtHO&X-Amz-Signature=5bd07687a54bfd3ad8c89d2c532b17ea565d2fd62d50d1fcf0b81583e9c0a193&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



