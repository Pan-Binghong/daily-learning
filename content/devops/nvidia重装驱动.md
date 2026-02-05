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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUP2266F%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQDuX%2BcLANkAu6r9jQWmX2IgYdMJ5SUYPbyRl9Lvh0kqHgIgTpLUPlBuQOCB2954Fv4bUWucFIsHkRxQO0Q2JbAPBMUq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDNPMkt1R3hz77GOh6ircA1kKcD0Mif%2FOcvyoj986P%2B0gRolnmWTTglKIXFbWCyWThFF1iIhZdhtPvoVf%2Fhu73iT80o6oXQ%2FX7pDOkOwYyA1yt%2BZe3XHzpEZ5BFetfToj675I5QtNWjLHdR2OHSic3NgTR%2B3LntBXoeFOu3%2FfRXwIOPknY8deb68lq0OU5bmdYoZUJaZG%2BDY5zN%2FB4AM8cCHQ4mFnf17fOB90gOtRVZC721S6%2FDrS%2B3qMQWZCh3QGVmn%2Fm8D48aiQwBbmnLT2NRh2l0t0W%2BJ%2FWpMsR6eARsF%2FDWzxBjFLrDX6Oo43hPNV%2FCtJzGQaQVMZzTvR%2FEkiAAIvztR9onOhL%2BNCnAE5QGI7jH3Usi%2Fm0mhu%2BydvtTdRtNi8dLhKG%2B0R8k%2Fbul8kTHMGqOq6MTjpWxJmx4KcAfUGpsymkpnnlqYCZicXpdRdmW0kVRvMiPyHPAuzYPVkUq%2BF6iXlqnE6kvifj6TBwWnskOJQRn9IW9hm1n%2FoDKQwfkSGiutUJvLtjqBfeYD%2FUtfF8R1ltZzW%2FG%2BjfFTFEGf5ykq4t0zxvO%2FU%2FGQys2UCrIsBfxbTr71d4RxKr%2FmCTM8W%2FaqNB4Nts%2Fpjv5Qj5WkStuwRhjGfHbdJa5tQbD6DVpeXhr1B1SGdyPPpMMOTkMwGOqUB3Jz1Qe7RammsnweySDz1bYIqhlt1YugKsGj4rw2%2BtpmHXiy922WpoBfkaSuWqbj4uqx8f8o1uDBxrBct%2FTAzq9%2B4k9ruN29eH1aiDdB66sdIDjvDgjAbYSUhimGWAbUk%2FWGsQ6pER%2FO1ZXZnAI55uoUl8KyI7XSlprAHIHx%2Br3iw1oNeI0CmhtdrMoYt2lJGh17HVm1fA8LK%2FrRSyP%2Bgtk2Cy0yz&X-Amz-Signature=212124f2c5060558fd1cab3282d1ec863af4edbfba24a2bf2a4a8d19446651d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



