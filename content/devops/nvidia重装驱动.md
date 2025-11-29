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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655CMZXDB%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAduzoU75TkAkW%2Fba64tjwl0QbiPWCIR%2BdmTVgJtYcgKAiEAmeUInfTfWF8PJdizRgF%2B95eTubkmeJdKjIVLsb2oLVkqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH0bd1TWpXTZNJnDHSrcA%2BAO021p4dFK6lERH86yYMRtE59C4YiT%2F01aGlnSEka8BFvSk%2BPZNp0PAG8XVwZSupy6c8c4mlAMNMAr86%2BZJnUjnTmFo3%2FdZ6ckaS5WmL9PA7Niq%2BixuJ25nGzdtZKjmhXw3%2Bd3ezJRiMayAPi%2By7CnummQdTTe333yk6G8uasXz6W8aLnTKq2RrqDXfdWM5P3bgeRiOTDsfI2Ldzg8p0tpRk0SQWDOkm4epVnpIBDokNfARoQa%2FooN0yJqGxQTzhGw8uf7Whc095kiimELbjIwWCFpP6j%2Fq7yq1tyIm8jsKuLMJfSbeLtpiGxS97%2FOfQSTuq6NMLXJD90vUr0aPlgRTBedgs86%2FdFhGa1pU7dtOR6lMWlJyrwer90QDrluunJZoeKDYfafX0zU89%2BTD0s7a3xn7EfVTUL4S1P9RRGPFSgH8Gl9nAzE42Qlilsf2IhHLwgvTrsPaLHH3RXrn3dbLMPRdt%2Ff00YVIWWNtutWEzk4zzUH7AEoZrsbRZulEBDLVrNXMs2S2QwqXCpDAN6Ma6uBzDfXVLfBA4zUrZ4l7X44F71hT6xVSbHQpeo0TKx9KkitbdtIodgQuRO%2BvmuiO6crhTqvDCwDYuxBxKtqQrRcO8Db%2FQdL1GANMIijqckGOqUBxlLLa1Ln%2FWp6B0DQnL4EVHxlcERNjuq8a2nGVtoKLV7wYfqSdMTpiwqUHfVn0uH%2FvWBFszu2oL%2FFqQtx27WFdhH%2FvDFKu09zEufOSUBf0eevhSw4VY6S3cOHt3v0NdO0fNGuMeNUQ%2FqrX5wud8LZwGfQXkhBtURMNEIGYawdQky5C%2Fdm5NpLlIO%2FdXMBhcqjtl16JAJBZeIOubewqahzl39Ql0r4&X-Amz-Signature=4782d454ce41bfd7b71dc748998af8fac3ab0879035ebe47644da77c52d3e030&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







