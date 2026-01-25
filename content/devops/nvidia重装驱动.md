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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEVKXAPH%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIB7Xllmuk3a1ZfkstbGFy6LnYPKndK9lAgtKY4mfUDOVAiB2ResLsECbcqTZjx4zhcKU%2FzjrVZNP6%2BV40FrhZa2bmCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMd42%2FJjIQ6YgfIWLBKtwD9nGmKV1vT4qTbFv%2FkMlVz4LhaVEw%2FlpIvaDVq7nBfFPDt9Gzvvc%2F4WSu7eZqE81B%2FgWjQKBztB7aJ4LGVzhrvqKtQlP6w581xHhEqBq37fxCL4vruP24bFFD%2F%2BAKZWhgtkSqjuxmKmLHTsx%2BnyaXFwJztSqOY2mYy6beL617wIi1m8hJbaw4JIOd9MhwshRAK1Y1DQY3%2BdLDWsFUxEUseWzLxfhibuCSPphTFaSIOtFWNPVaGbNQOjEXWH%2FTYBw8GarcmTguZglwOPaxfqlILcAUKxm9oQiAIgwou5WfdPAb5VLTK5PHlclFwLJjbKLlHexapZoxyoGBVeZqR6TSukj5azwFBKif7htZxPL9k0sSteE9rVzieBrJgIGDbrvILQZKrY3%2FCw8y%2FG7UaAW1GqE%2BSCIi1lGp%2BjS6eDFW2RGnY8Vtc2IEsYKeA%2FWmdy5x1hI1u1MRY9UFTWHO56I9ccezRMJw1GCb8BD0HSO2mBbwy8LhDLywIyjJ%2B4i9wPKC3u46lkPt27Z9A55agNDNZgYmJ%2FxucwxmTkL9lCSo5YqBmI5ZtgnoODAt3WKTScGVF6nZ0WgdSpaVNX%2FbCBf4nMdHP7cV2oPCsaS6ptwHBZkHHEvoRZlvj3QEzY0wgoXWywY6pgFVtocIm4%2BoFcVUanT6x0Ww4P4nzBl%2F8Lraq%2FVLojQQX00yNV3f13PpvgK%2B5ne7UA1RatTmFnvZdPr4rWx%2FM0wBd%2Bm77lv6HWGmiQ9EBiLsaLwvuzd4yn7eUQr4x7t3PI4DBArT8TXQTywCIJSccbp9DYxL%2B7IUDce9MQTu0x00kmDN81kLryF1OyaMAsjLReu%2Fb519dliWCJsPdHike7odj5fhsOlM&X-Amz-Signature=859ded3a13dc96ca9c9f4720ed3cd76bf590fe3144a912f656ef3976b9810c0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



