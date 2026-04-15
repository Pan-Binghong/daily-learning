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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNAMYYVM%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD82HB30DtvRAxxlP1DLNIt%2FQPKXJvpjQz7LIOmUsnW0gIhAN%2B2wxOKLBp6URhNachrRsXRBCdWDgoY2Gq4pvoleJVKKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxE1UQRfLHCa1vBjwgq3ANxR%2Fjqd3eIuR5HugJl0NTd4qeBAuMNWNQtJKldjfV8ZOJymvnWiJxm6%2FZQUsbva1FK%2FWYkddBrQWUWx0OhP5gSEa2hZBAMx2Mc9I0AFmMcVYPnWd%2B3fUVc8oZyL8haxvzjwZI%2FArhsK%2F51y9cMMyL1%2BdGcdAvv9jVztpIbjF2Cicuoq8vtG0XnjeH7i9q6CHs3YW0nOBk1QpH9GR8%2BKjGvMBfjQeqHTvIehgG4XExIfnHtho1yKfSr7x9TarH7gLa7gzuxI78Qnf6D5VORtC6l%2FMQSJRqMKtb9uvifmJmygP%2Fmxav%2FM5QNR%2F6rZbAelf0mJJ90EJdr0kGhEjL55%2FSRIl4Xk65uvafPpXAsYzhwfFcQ5pfNpnQixs4QalhnDTgJYsLuUkQ4SYEPq4JGedCQui2po5hjiaja6fjB1gN7347EPufArlTSF80VUN5D2XhdYy7ySua%2FE2lzClTyqObjWNRHyiswlcwezzkHZ3rzExCuTexvHVpj0SwWG%2BjZllB4SCDY7GFkSLk%2FcY10PnI7EgRDmP%2F5e7zDlJq8tDTsR82C9H8%2BLhBiVAJYs7ZPgHFn%2BT%2F0%2BalcjD2Nm27%2BSA%2BkwP6Nc6NsMKyzLNWv%2BFxwxue%2Fn4M%2BRo5GuuVvmTD9kvzOBjqkAeSpzVIJgd7GO4dWNwcwJ8qUmZe2yy8LsZH7tJRdFfqezbUIuvpeZmRT1hAsykTU4RzsO6cU31HoCK0agh7emOxYew6baKsibk2ugj7lispjBqGXIsNKGWo96ircaw3aLVpbUdsMX33gMmT2XdouG4T42CZ8J%2FHPB4mdvnuKW7nCjTjHIwcK3fUA3j%2F9f2BaXqDwBseUvCOhSHno5rYvt7X4piL6&X-Amz-Signature=a6e0dfec4a88ffab9dd52ba6d64e683c76b7b77cb4d10f7bbbc437f15e44a276&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



