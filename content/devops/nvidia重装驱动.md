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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RARJIYAJ%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIH2tlg4knjTeKPyNLKoyN5pkzTuveXc8T0JL%2Fp1TJhoPAiEA4Smtn3PisFZI255jEOMRHVF0kON3IJBB842drToLAzQq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDIA%2FSB%2BPKsHIcoCkwSrcA7mqy%2BrW4TpzwQmsX5epMfYL6B1O1%2BGRByLKMIBJL62vtQjGaU0r7XHcBGQo%2BXNo1kjIUJfIye646%2FFQ4ncjOXPsvhFvQTxUfcr%2Bxubq4SagAx9F5rm%2F7Vd5Aq0x282aGOfpG0IVmq0uFGY3v3zKDAks%2BcYYDifTuRnUX7JIdHRY9ve6c8dDe959WOtvCV15vGo5t%2BK5dzi8gk99cVsR4dJjs%2FOFh9vCqtmSO%2Ft06nIQsEdPxDHZSCVzZWEXDEzUHFDFrY71WXZv6%2FBolNt%2BzoNvQW7MO2RhttdoGWJKCSajToan4tRWPaMRsonIhWzeiKrRHw1459beeSa0H32ZDKlrSq9tkJzl%2FkthlkTgFdh0rKvi2A1%2FA1Qj2nGJ%2FHXYVFqgoZRMJCpMAGUgfek3B9AcYgxdOgoA4%2F8PyHqCmAa4gXXTHCHZh0%2Fxd%2Fp%2B7jVUlXsxK2Cu%2FRh8rd%2B4hRJtDR5AyTLquOazn8tUG6JEnKBzpf8yEFB1VpSBa%2F4Y89BAvVS6qbA8dQAMdB6oe0XF4W0UhHJ9NZvcE0IZvyBUKq7CWqkCxJhl5dbkovtj2WgSPYgM%2BnUic%2BelvbTUSydiVijXeT6b2nufl7CAhtEsiW9lzZnWTTJUKUDeB4ezMOew2ssGOqUB%2BxowTfQnENrs0fMIiG17VWhobTLkofQkTFpRo%2BiybZx%2FTMps9ulfWt%2BHsA2j%2FtAnlJWDaH%2FuKfp7IfTHdkdQwo71079OkzyRsmYH1sfBwPdrslcTW6K9buYo%2BFsMJm065IZeNLM93YPra29enKL9kP6jxP4xsO0ijoUdsVZsfXMDAmFSs3z9hUIU5pGUeRnppcwtpFz4oFofjd6VGMLmR6Q2xtSf&X-Amz-Signature=814126c714413d0489cc3773de8088a58013db08f666f96c2312b8af9ffddaa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



