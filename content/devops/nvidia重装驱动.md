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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWF7U4WY%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQCkSVK8v4PGtTG2P85BrmT1cXYyaZWI8MshlJb4LGco6AIgWnVbMx7AnwmM5T7mAEXMscDOePLHR5Pb3FzAPGoSBWUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDFBzATp7fN6PdtHibircA0ha2nlrjEAh4aFy0qH0eZHgQhggv7PCqBu678n6NlVQzteZSX%2FkJ0CXzDhHpe1GJXOyaVZD2nqOMQitYEk9li%2FxcmhWAdPL5mag3kxEW8isZaFzDe5cTwbPOnTQ5PlGoVggrJJVszsNzNSOoKX53sE70sFlJjdelCQwku499boFG0kLN21U4iwcHw0tYFJYibujXYUBe9j%2BFLlvFtPQNVhXIUKFTKF1qlcRPtBR3GOFQKpGVxff33eeuv7FzM%2F3zIwR4H8Zd1CaCojDcXserPheyeoRNhGg%2FdIkiT1evx9wd47O4s%2B28QYQXJgAKoPABj1fHt48nJRXDNx573eBAzx6WhTNRPwvhmQBQ3GbjfvNMMtzWkQG8uW%2BQZk9j4mmqmLPrncyaSJUvchLlulpd7%2FIVQAEAmkkmWfHH%2BpDzNocrNKPUsnzRurd8TXrB9voQwyl7USJJgkbkR5uYPcNXNLj9jd0%2FDhPlU%2FjS6mwAvr%2BXqWMrSivFZk%2FckaZoscwtTyLixhOiWdqvJ9%2BSsq6VDkrrUKYCTRxniG%2FERuY8aUAkwV56gF2LSOhEGP55YgIslPf66bXJgwRmRCCN%2B8%2BnC1KAPZO3OMSIJP3DDsgWEf44TVIZStlbmFzbpCwMOj8uM0GOqUBm2CTK1Wkc%2BLHUC1puqX8I0bUfM8lNyCl11lXvCQ%2BqC%2Fkl4%2Ff1t4y%2B1eszlfla6FQFutniBGxYap8X1YnyKn1ULeR6BW3jmT0etgC5PzDK937ttZRX9vXtSjPTlQT24Q13Ji71ReN%2FdzMof%2FUswS7F274epJCHs0eSXwcoMowmPG8qfFStGLvA0dKRijC1uv48cQTT4P8HmyS6%2BURhGOA%2FNxv44Jr&X-Amz-Signature=7301122b16fda1caa371dc7fcec04fe60e7a26f9bed996e835bee253fdac0fa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



