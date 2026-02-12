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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSKFB47H%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIFJjU61Bv%2BNxVUNe%2BmEyDtcP21bJDgHF3ZPm2SAVO%2F%2BXAiAotF7rV2mfhGOerSgPIXcFRh7u605PtgzekM3j61McmCqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5Yne2OF3eiCuYYweKtwD7IRtjBbUQQ8m6zDdY%2BD8ahUGg0r9qXuSp6PF7BFPbNd%2F9tMDFgAO70QOfaPL864LA23OzYqNat%2F8NpE8HN1%2FtJSBmGoTzGZah08pRsDYjzgntxLwALzLk4LWhhkkTM4g%2FgJZOzCkeUwMyKma8cnMeaq2EB%2FRGID1tLUDiMhuTn7sTe3h59%2FhOuzFSywSmmdzfbuQkWHoaPXd9GuktVySEM7RAVaxTJ3vMAxeG%2BFPojyYBYZ1W7xKJUnEuRDuidkHP7YiodP0MuI86AQMHyFhODoCx2V5NFvbIbMIqL3HgYA3TANcl7baCSxgHOdDztjdpaBvJ5pNTahoQXyBx0JU8v8cLrtVtJlbMSdlQLdPPs%2BtfXrYbN53CRaIokpy%2B%2FG5VeGZ342qxppefrKBh9ezKNKLdxoy33Cs2o1lwF4uBESRgPHt8aHRRg7U5nBZvKEGT5QjA9GPP3o2zASP%2B1z9%2FlFJl4bhKTsPgUCQQqkADipcqU%2FMfz4X6r9DvsWX5cQvbkRZ7Ci%2FJujoCMV7pHZnSS7VK873SFXOEcKuZfva4lpVl2kkqm3f17n3%2FblBWUoK6dPUm5mGTOrlouMiwW20psupX3jUGRS3ZK57toaKwDo8bDm5iqwjr%2Bo%2Bde4w65K1zAY6pgEgKIMkZlAKnzboenLNieqw4GVWuh64kWKdfeG9SBAbd0wPsAmrpPk%2FOy9h8ogdVw5BxKDnynx72h5bM98lxzmVMEhvQfBw6CmfV3lsauoKIFevSkt8TTRIgNZFWVL4IfgS7JzxBrr2Cvro6qH72zIhP4BoBoIAPQMQzbcRPpkhMjL8mubF2Gst2U6HbcpUKM7mPiYOISc7duTXB%2BR04K%2BOKSzQ3G3B&X-Amz-Signature=843e95897c2b02078cd359bb50200432da2602936bcce5cda97356fa7cf4c5ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



