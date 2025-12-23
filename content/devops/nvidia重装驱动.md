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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666P2PKRI4%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC%2B5yDoWIMqwZKlv%2BvhFb0occ0X4kjBmo5ZGRPmOAvDDgIgGeFV0%2Fg2VW%2FXcI1kKrvWULMd%2BWSr3%2BhS2B%2BWc5P2CkAq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDKKSUKfoGFJtHIODwircA%2ByuFsN%2BzLPdoEsDYhb8VlOYcV7q7loyK7Zq3AHmnWoRCCRVDYLNIGGcq4%2B%2FC6ewRvjaeKsjuxpoPyLh8GmqU7kW%2BpIwZ3%2BQgym%2F8o5fN4xGyGCQqu0VNwfGtaEpuupAwQLw%2B6GkwxtiBA4%2ForXNo8A2JUjZqprioso3j7FMmQuBBFF3qZfOtOQKtvNNp9wauyKPdVeugkxpivCfET9mx9WW7K5JL5ib8wiUTI4evQzCOvUrNYrBqEPuBt22QhiJCC7X7KWH3sMoInIjzEJTQwZfoQ%2B1rrRMmbMXlP6MlHV0Peg29tRt4UPNuMaEXLBJ2Xf7NHGGS9Js22J3BfBQYYT9d4Og%2B3OyEl6ynexuhpsmHTZ2isbHicLu4KwqlY1DJ%2B5neLuLgoS%2FpINDgXtgZK7OJ6coKPbxgn1u%2FevWCstSWGpSwn9v0D0kh2j5Zo6OPpnYwnAvwDNQhAR0RlVHiYyWkaaQMp6L7Ol4AhdrpFh46a%2B1KRUiC9bmyB05O40qMWl4m%2FLpG3KFKbUaHWxISvVFdEocUdHaZLfn%2B4i9whehvl2a7QHeZsRt1g%2FL5NxgBxEIAqq1yCiGpMnOX6h%2FmnH0Jtu%2BbL3%2FezKpDwxaKjbOmRjfGE9L2MXa2WSDMI79p8oGOqUBWT78cuYRq2DB0wPQYVb7UQL6BNClTdoO0robnoeGxERONkvhHn6JLh52LmUcAgVAbL5%2FVPwdUW1N4eWSJ%2FAnVw9EtRqJ8wZOD%2BB2FApkeay%2FhaaFGk4PCcodZAmEIJMKtLUOD4Ctg88qJZyoXKpgjVqiBsmy9mPHrVTAJjXHrLrO6%2FNQ8LoegE%2BIzO6BAe61eZ3F7yuo7sr4XFt%2BG%2F6p%2BPl%2FDnGw&X-Amz-Signature=e9ce02ec3c85e16d84cf4e589b1b4bfbb078adc4c27b7fc3328a5b2d26e241d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



