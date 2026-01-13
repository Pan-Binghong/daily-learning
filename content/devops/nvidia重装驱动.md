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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGKP2FJO%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIGm8YwVf5IIb9ivSypfX4xpAUCVIOB9P02iehQsGVXCXAiB4AlnfnS7ccpv5k7ufVcm1mfYs5O38Mtes5MIXg86ZCiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqyAfL8UpOJ93Ge%2B1KtwDEajD78a%2FM0cuB%2FGHy7hs1ZU%2FYRsyiJYenrnqOwrtxtZUL1NVGF4d33G3qJctlj3RNAmMQeGxQQddIkn39WaOd50naJtLViaaFPjKo3nKHcXkayAwgLkrBYrPYEu4IvQnr5Sfl%2FatJOhxNJoHpUbMMyqowBjlvvARBbHmAIvy9n0Oq7Z5z%2BbXnFipgljzRRu8F%2FMOehB5mHL76zgehB3ogBZSe%2BuTGLlT7KXx4M%2BRjEGQtEVuMCfc2MAwnLplxCKvOimFYymEjoE4VlCaHdfv07FcmX0Juw7IVhTvn%2BdupFA3EGxNpy1plDkQmHCECO9T3WlgWYl26%2FSGfxFkJHJuyqzqC6%2FGvQPiz8WICSSxzppz22vNp20VS%2FlqAMnaulzsqazQ8I%2BkVb%2BZ5AeVGXqAnY6Y%2Bq03gHeq4Jgj7BoR9Qk7ZrfQNbvRzDNt2Xhx5cEYppzk%2FFKuX5koy6Y9ljr0dqk6hDHxpSTjCwR2UCqPfJBrRPu4x7wxY8BefoFKq%2FA%2B6694zykOQTYgf3KOh8xiIUkLdd3LHxNyEolotPtzQUo33W1zaDADg0IKd8f9fDkrnKKoRUX3nfKIq%2FK%2F6uWK6yxknDh%2FDkoFWrLK%2FCLTgRNbALxwzj34tZw26ZIww%2BWWywY6pgEey9XTs5G5IxmbexoHqOFphmsjIvdhO%2Fd5y2W9a4tHX50N%2BErrIFDwYMPng6gF6DR4oyWo2g%2BKXAG8D69G0OKW%2BX3HIyT%2ByTfx9SFbwMLpE7CwTQ%2Fqf2VoaJitehmsS73PU4zf%2Fk0mpGSxHOHw1wpLarI%2FCl7d16f%2FQHMBbJuoVq2zQMdpZYpgVz28geKTsbzo%2B7BoocEVzWtYgyXKfghYC%2FbVrDxy&X-Amz-Signature=e6afe73e40f03e777c5576462ec1619951602921edf398a470187914df28977d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



