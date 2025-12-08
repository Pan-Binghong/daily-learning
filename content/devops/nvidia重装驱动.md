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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJFH5TYR%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGqVs9Ed6Bo4eLYIXfbXSUctOjth3i8PY9q0vUlMiOnOAiAV%2FbMyyMLf1P7vu7Xqaiwm%2B%2FuA9phH0W6xn21V1LFXDyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgBZVZ%2BgGasCp8qzaKtwDCPI2s%2BcWogxyIs1C8G5g%2FineXIDyaZhxoksb6zj79AchhO9h9QB1GVowIM922dgKwcnPKAcalQoDBCrgtdjzqsytkF373GMx%2B25hj41s%2B%2FRgdXWr4KO6LssnKiL5CjC468HJxv%2BXLI%2Baphg5PsnZxTY2vQlLGFOeEmy2PNyTapSJU2zd6TGldF5ywB1BoDV16kgdsfGemDLRXxh8tN0lzxq0ublPZUuThth3jg2%2B5tbZ6l424efqvl%2BtvOk8TraC%2BeW6VmHWR0GMQuF7EJySETuvMZWzjn9WTFDjG718Jj79fO%2BjQOBhqCra%2FF0ejakbi5D1math83Ks1VxLV2uNamg7VwmyladVeOXDPAo2srq7Utjibo4lKwwzaBWRHm31qRfilfCFbK8r8vYubFZ302gvi9xTZ2qtUxzUkONM1Qtlhg6jsknJTFtVbxu3FMTDVJowscKYOAlWmRoJyjGN3En%2FH0m59oM7jgzrR3odR7dO%2BimTtdrjzZ2y%2BUaHnCs44UF1tfjnfOl7I94zjz7V3HbTUnw%2FCw%2B28ascK8Kp9dPjphvjr71XbttwNz2lnK9XWst9FB%2F57bc5e0SCzfF5OSmekNHwUlMCzUX2nVOKnerSk1ruQH4C7vpzGogwl%2B%2FYyQY6pgG4soDfB4b8SEG0VZdRnVKVB7u5lTNE3LyNacjKLTGIziJt9twzJFqgea7wIkBNwVNoNuE7RlLkj7xA%2Fy%2F%2FYlyU9kzSocYZxRuL8awhpBlTlBEmMIJQHoqEGJfKDkMOBesT5%2B1LYI4whUqN2rWgbmHyZZ5zWnUWIHRtCqKUU1GxW%2B4E73dTSgXrMalUKyEcWfp3FtOXR3jXXqJg1RhLVFW6oCHE77ke&X-Amz-Signature=40fea4acafd47d8ecdcb94e1519dbf24ea7d081e9c2fcc5561a2c0f9a4c9cf39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



