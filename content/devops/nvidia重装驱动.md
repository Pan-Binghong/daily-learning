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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRG4Y2CB%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCICmvhFfIiAEbHRcKQHfPIm%2Fnhce1rCs%2BA9yTieQouRi8AiEAz0Efcb1i2%2BWeNp0RbE14gjwIu2bO3bqZldSRvjpfNMwqiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPqCcaUCswrN7M3tXSrcA5ZBjaCC%2FP64Y5MHHjl0ZtQjh%2BvvHEgWhUqVM32NCZGwXohshVZsZeyb3TyIXwiO6HfJqwiZqpa8787Eq23RaHMF%2B8jEvHlov0tbyBlMH%2Fg3wk00FuC7J32MSq9hRSDNFHN3xxAD47Ji%2BSCb4CueCsa6lUZHFc%2FttPXPX6eoOAVP7mY29za6VsioFi2XdXGFdT1RyZvDbxZoQKehshLmh2A%2F2%2BkwtI24imZ80h%2Bkn1VBJcR33MflQUdV8m1kV%2FQNV2xRA%2B07ykzGe4gf5Vw01iRXIYOIx0nC8Qa3Xsu9mK697h1xObCa2u2e%2BcqowNtpFoJArVtCFeICSIrhtx0%2B%2BZ0nwjj9IW9ba8tau9WCPteMlkEUhhLnrAu1DCdKfHqKsDzLkgRxfLW6jdO4qmxpJoBfNzsuOlGkNq0Rl%2FZ4WfvtFiHwpYIMSc7HXSFgXJq4WN%2BNXgLXceFN6ihHjOaVXfRjsEF%2Fjx2TbhqNi5hbTXba%2F0DK9tOmftuyAGNbnrIAMaKFr0u2jmFDNob287CbQUXiaGZhXIzyU5g%2BAqBMo44coWZ12RAROoWOPHcMoUNEbEmPhHjPOOQ2AVvMdKkxw4OUGqOu0Zs1P9PCe411YOtQpQnR3TU33s3hg2PYMIj10c4GOqUBBTct5p1amgPeVOh3k8HMihJHxkBU7yiIcM7d21TG2HsLR9GI64b3RWKBXhqF8uP%2FlXKdxxEYItgjhzqom4mPPyH68StWugpn2YM0WESqyT41R%2FArPcDhq4zojlFhjx80XpdYjyu4LbwNc8pRTgXqPEEfvshYdsNhL6Nz63UB82CWA9l8cF9wzL8imH2R74KF5U4629v12hxI0vrq%2FBLzNctMFt5N&X-Amz-Signature=b838bbf64111462ea30cdf77ce0e8e3fe48dcaf1fbecc655b782a0179f1e6cfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



