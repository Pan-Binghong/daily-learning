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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6WQ3FUH%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCGwTJ2GZfLSZ810MpznyeDZcG4ZhSZrU%2ByzhfKdk8XwIhALn1ZG%2BjUqPd6M4lSiLo6%2FxexnwxvzCH6EV9MB8lWWv%2BKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6DvGQ7pX%2F99AUn4Qq3ANk9pTg8B%2BDH0MAF1GQsH%2B%2B%2Bhf2B2%2BNa4umt%2FFn71mdMjiltOmn9o%2BovT682l8HdF4wTQubANuocOpNwvt2tgrxy7N1%2BaiWnYU67g3TW7DxX1FvrAkKEy%2F38tbDCdNonaWHl1GEOK12sO8oSs2YLeLsnInkgLv8vaek5M2mwlpu4%2Bgo0nodTgvbSSsbD2g2Tomk56E%2F%2B%2BA4mJBV6YxOck2feJCLabhe8GWyOObtQoHMRlLeD%2FNmQLNH55lK1QsZfWgU%2FsTB9C4MNveqWWYkLKnHhpSoyd1ymRKRy7GwrrKGKY5F3zFyOHlM%2FdaN3aWul6i6UDLMUz8laXF8geAUHu2o3OuOELXiANdsO6ZOOZHtrNlJtDe%2BXlWH5r%2BmAqISf0YYLI4n%2FgbSB6bcRi1h9ONymeWI0W3aWOdN1twamBh1G6w209IfnDUL5WMRHH7Lsyf08jPQ1c9A4Pc9yZ8DPdkGTCN4FKpn0GbQVCjPvL1qtX%2BJJF0LVwftWI6NtkX2WpikLxQDy0%2BIqGhSjYG6mmYI47gcpAQPNdPFRmTt5rGXXhQHzENnNa1tPrj7X%2BpsucE%2Fm4c59NqHIs6WEjGeVS7Aho65Yl4xVaAqo4z1TwdRbkue%2BZ8bnujZWwO3nzCv8q%2FIBjqkAURf59iZiNDVCaTmV1cKHlVTgr64qAphIFXRvOGEe%2BOttVszv7d6IwsRO3qInpkKiRi6n1tYYEcDSpse7dGZ96yP%2BJU1uI99yF0ENTZNfvds83FbI5TMx42vDdFY4BIJM0E52WeLbZYhSvgu7K%2FewHDVh5f73GXyeWZ9V8y8Bpr2dxJ46yXXBI8xNMi%2FBIE8MnmQqNB%2FPWg34GkigFiZgP8V%2BhQL&X-Amz-Signature=dca2fd5d31e8e50cbbffe04e54c7a01db900f0c1e07046f870d8ac4e72f41acb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







