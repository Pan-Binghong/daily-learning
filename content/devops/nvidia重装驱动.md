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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI5O6VY4%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7RrNH4TAaGeiKxCkPIDdPN5fFrJDYR47OtqXWPSbM0gIgd7kPm73PReIlU2dPRb4GvytzBlorhAs9UvSdfrvpjAwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFDO58InjrL%2BzoJUMSrcAwFAQIaZpHMIGwWaAOcqO9oc54WxyaOGzT6ium0Huv%2FuZTwNDEaOwPGe9eBLUZajbJjRrlIuKHWZSicb0gS8KA%2FBngPxdjZxPEFIKz9UHuBg7NMxnyiECy%2FJFgyFFXlv4pJwYWP1ST5qCw93DEYP6ieGdoOsqKldTL4C3SzGAdYq8q2pS4sMocmph3YGtVp2cBmaoAXtc6fyjqX9tbikbP6%2BzwBG1SBUpjjrMF4Kdz%2B1%2BfX1cD%2F20K%2BQEEfRYryCZpKJx9QuOjgYFUzPMbnOecMatl%2BaRU9Yx1%2BKG6nDbqwR6IKWV0hIhuIJzeuzoABcQREjRDVA%2BQbRA83he4WpXLDUeTnO8tgtAYxwB0dnUkDdmZhR683elpC9JU%2Fe0JcgOUPZwbC9pnPhnEU59i0qzdul3FnBlRCxEIGApZGMGFo9H6eH%2BhSavd4FHy5ivxGSAUGrJ7zr3GKlv5KzBYnA3Ej8%2FaD3FCtfVwJ92qacur09hQ8G9I8naTcEUsAYKkJWJKQEIXBVy8eOSfPyGFI2p7mzWS8obFvqvvz8l%2Fo0%2BypT1Z2ZghPWjiNlRRWgyi37o6eIR6WGYmiTGK4Qb5CoX0um7TwTX2wtGMWZvM8zR4JEludKxVkqr1k5SRmSMLWVsMgGOqUB6EdKe4B9Nb6uov3fPNQFbKhJHxzZpLap5PUM5p7xZiFKxhusnyiEB7uDCHP%2FtoGmTRbsEsO%2BTipdEEQv7Bg643x9I44lZFly%2BJvMO5%2F%2FjPR3koq64G9doTzxe%2BgNPaQRv7jhQ8rO5zbYWpsjrqnrkhaCowwh9bteGaLWobW1QOUDKpSzJPRko9mLMp5GGwR2t0xeYCrsJwcZHTTfwu41cWpIyw7H&X-Amz-Signature=6512092da92a31492f0451b6143925883cb605280e94c55324b0c04a2a9e068e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







