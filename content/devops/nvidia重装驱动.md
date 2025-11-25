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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO4FSYL5%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIENcpuQcvCwIYugKthEYlSf4DxwAk7gkNJmorxVzg1ypAiBfTsBIdpABkftluSHtnSqni7PQBMY66R485o8HpgrwdCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMBc917qhtIDrhz3AlKtwDuanGS4QPbnnAE6Perfsao5tKFipeDOPqKDFKX3a3CViOXDlsCDjacjWDWdR1t5KDhQKCivPNjaWf4LsQyswGzv1rYzVqnRK7fZLQoSs%2BYNvUT47g0Bo7M1mLbl8x739TshkOeONRC1H7zhxT2fU0OOzn%2BkOT%2BqcJSUf%2BV4xQpCdygYVUYR2xuf%2FnRijUcttXlwItJUoL9636jkaazPnBcickyhmXySlAlKqhuHiE1VS3jeJ7MfHSkObmBnBl8%2Bj48ave0YtnzidpPfmYN%2F5OCl5LfsEkmrRFdjtdAX0cJeHrrONmefnva2%2BaLR%2BkKQ2l22jy8umGXjyiW9Lk1Eyy%2BzLVp3mfeBOXCbZbaSM7y4seoluG4t93StHFsRMaTWsjVyqlflI%2FfpE8vUjtluJErf6EMCO4tGvEDRv9nybrvDoOp%2B2K9wv5E2svsLypCoacHOyfs5FcTc5dumbkloAyQe7mKWd1eZLVmvcmZfT3otXjBScNtjgjohF5eyxAh8gnmxtqLRDH7PR5STrb%2FWIhopRcMdFegNrMG3isbxKNhKvUA4UIihrphI0aK1rumNH57DuYaGsm8wMmUlvgsZLKHj3EK5t43Pkzy9zsV3aI7CpyvDETqkbn%2FuGSv8kwv66UyQY6pgHwFBnmgPLNctXEcu%2BhoaDrNlvMi2fsjBg4maPWvDjJtGIblCh7CEggwaL1xK3C11IlIiUztfT6KKPYZko9ci1%2FIpHlqOuRCLSjjCUxsw19ptEnSjuPJ%2FoaDgTRJQdTlRpj%2FJAylJVyduXsXZXm4duux90hwluN7C6d0zRI4%2BFN6Pl2SxNMrKf2WrcBZFeXKB%2B%2FiLjQAFp0HaBA2mjH64SdPh1Pekg6&X-Amz-Signature=b031a3868986e4db178d9a864f0fbcecde656b3ef9604ce4e08260a122482c88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







