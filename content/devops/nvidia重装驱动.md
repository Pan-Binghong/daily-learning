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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIGLPNTD%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF1rP0cp5FlbHRO85USYGrlmuBD7AZJI7WIdLTkIuzJ9AiEArcG70N1QEPI1rZtjGslsTRFF4uGlgKmxxMBng%2FlhIZwq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDPzb5u7fmjffnQ1QsyrcAxY1kdGKFLaIg9LyOs%2BUVDJiYoscx9%2BAF8hWwqYyvfVyLaaZJYd4oSf7meDs2oduGnBNRK6%2Fn4DFzSe15qfK1icGIo8FNpim2ZMAvPOWWyK4JD7w8MV4%2BQ14Vs5DL8xsXnse88On%2BNoc4MQf4Z3EwplJ0vq82dzYb2PqZ5VrEeB1bhj7uGJ0dBTQa%2FzRQ9qZ68rkpJlLLHYUkThrHOKM5Uf9kWSiTJGkOS0mYZ91NdVNfZp%2FNAR5YCf%2FnnPZQB5GalUdX7SmSwabS4qRk4Ux5evNmvcarxCleNl3k2DoS0eM4hToAtm0DoSK5y%2B4kg4Y6ZfRksqH%2Fm%2BfjEv2wXvM0Badl1%2BnP7soBA007%2BfpQsj%2FtwDqV78fmC%2BXcsUxza10yq0CnJG5YDP8Fb%2FiwjA80UnQKi01W1JNN70Uk%2BlR8MTxkVTZbzL%2FchjVm%2Bf9S7wqIVsE8os9pZwoD0%2FEIHCkSPyY9bsYwrB21GWTDSXaRSWeevqZDZMKioJp4%2FJn%2BHkUM8V3mZ6ysPJMYSPwL%2Fjs4rbK9cEsXaFJwhO7lI0%2BHJvkZ%2FXRelN90g3VARORa0tri1l%2F6fRV2px9ZUwGW2P08oGaJEHsnsGTPkO60902J8erxRcDn2NVSUIpOVF2MNuf1MwGOqUBpJrSAFmO1LLXVI4GLAVkk9XFMCaNPKifJLFU%2FBKyiYpPH5cATozdsVtgR820wnUIim4B53nshQWXsaMbv39o0%2F77nTlmDz2C1JW51TdBZWT2s8pvnrYhqlsAATtjIrexQ6sRTkOdVLqGpVUrHYTZrXzUnhhoKT%2BrvPR3o3FXm%2Buz81fnSDXkyufF237xsG4uCpRtP9D86AWCPa1QxMZ%2FnVqh61Yn&X-Amz-Signature=4f78f4220d89d2bb479082ed3b93d75d36abdd7685c2bc2e8b9e2ebbd5914b4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



