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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XQF4OSX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2FuUOKtuNeyKsyhHZ265274BHx4AkSXuXboPo8spFzTAiBWumXxn1vm%2F7KPgPoG6NSyqVjlBHvcNhz3OESqhoRg%2FyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMDubXll7hxB4YWreHKtwD9q%2BgPi7799ezgLymGz6TEk4mKcjECi7%2BQ8c9k3pXsiMgnm%2FH1XlbuKeJgxIaMh5s2XVIhS9CZPeyAA0ixH9puto%2FLvEQ0PNqEAiJOf7r%2FhLGWOzjmWrtjY0SkOD2gPrfDhjqgo%2Br0Boc2zSQc7fnLkEFZUXUz2gBsCtF8edPVoLJKskE%2BBaoKJG8UwyaVMM%2Fofs%2BufT6TdfIeYZH%2B%2FSjCQWhP%2BzhcIuC6jy5XUJeloaKjPKOxosj1WyaM58wvlIsK1Miu5%2BzWHBJTQjvbqKrzpc%2F6xTeq0okQY0srhQtmNSKNolZc9fV%2FzxzMb%2BQFHvajxarhL0LcCpt%2BUQck4ZrFqyvnToEO5qsEgxbmZC6%2Fv7C3IVlvASZkZMOUFzcI6bk0F4i4zykuAWiFCMPjc9f8kT5PMzQsZGcbkd8ulJGHdcfrXs%2BGVSSI6yYPo%2F3DRGROl4rpPk0PqQzocVQ9uHDdXi4L7euvRvJ3ZoEfM5HALFCI1S2RPrKrqkuAxEs28lnthGRwGs0vWMoVEXkBEk7Gl18H8I7ao5Eq7kS3VfI588NQZmdn3fbq7Q22JfuXuyz0yFgwRr4mzRNDqq1SObp3wvVZOkO20PEu%2F%2Fdcd%2FH5A%2BkO0NE3fUWK4kSLZ8w7MSBywY6pgHlSn9JEtT3BY8K1oh8sbHBw8tbjWbPN%2B4BRpP6y40sIzEDuZUwruP0NonVvqn7ZBS%2F2mTxsGoVl3W9bbuQXSGHqyG1A%2B%2Bg6T%2BnXspNYRDiDQLKm%2BpyUp%2Fb%2FqhM1q7%2FAu4%2FIYB2727OConqNM5O7P90lxGtPN3D7%2BaHXPedjTbzh%2BGXsm5BZDZnDuh9fOTxJ%2Fv54EKPIJ%2FxfrYTaLmCMJefB10W23Yt&X-Amz-Signature=df744162663054c9c82de6b3401f5e4320b729d977ca23a16bc08aa0d6356d88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



