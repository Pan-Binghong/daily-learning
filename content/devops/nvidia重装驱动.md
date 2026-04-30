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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6UYICLE%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCPL952f01yS383OFqvxP%2FcVePdvzmQqZpo4CWTKFyQTAIgPrfeyylHeLvBDGj%2F%2FRdBab%2FWtrwOM2taJlL0NuX1jcQq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDMh2c1uE2JpBuOpQ4yrcA47qiwClPlg9QAiyBo6dF%2FpjJXHqP5S5LgTo75EkD9VgQXq6BOXPI68VGsXXknnemBvGwJkshvCBIOPPpjSkFkotO8Or1DS6fnMAv4UZva1RuTBe13y1TIqV5SVHS7qij5RlACNho39sVPilXA959wi6msz1xyNbmQ2Vq7ZjeFzq0L4O2runRxq6WyIdj7SFm0jAFtldlXjEGk5Qo76tYwofQ1BW3LgnhpCNgu%2FsMTwGJSedqvgj04BdaVLm3jqQzHEwZcN3sNJ8%2BvwsUeBQJKnmCYYiZkXJj7bznIArG8KSFuLSO%2BPY%2BQ8mv8FI4KC%2BVjy4uiXvL9zxoqgGB3FRHhuXQHv7nGkgLGonpGRp8jnUnPYyZdAlktAnQzPMGsTVKTX1gLSxOgQGLCiY3Mnz7pifoF7h4VRCiIIh4k3mjXhBzW7Ek51%2BMW6ieoOP8SAipfi6oFPHnuyhUH82AkWQHJyr7h06czyXV6uigmuDUVBRCF6%2FHaP46yVMjEjvzAv0cFgFmOL42pTsbfTV1kdjDXK%2BwJhi6lNiPVHfCKMNfLUHgGTBA2VmBqaN3A0vSdR%2FNTfXE%2FrLwqCM%2FF6mqt0us%2Fc9NS%2FLDuM3MGSTAtfp09seBIaKNWzifwgH8zPVMJibzM8GOqUBfj5%2FreUUdmUoCuvEbZQN9Ml4y3qXKMzu9IezcFDwEIbpwR%2FKAV1vwYr0uqjY11WHNFj%2BxSfY%2B0d0hKtuihtFvLsjT7M%2FUJ7vM%2BWSL1WVfDOC2dVvQO7ADC3iVGVWKj2VyMdHD8gFxAolY%2FuTrpokL1RNPZLQnsRWcJ8GdyIZ3tF99s4ccIuBZFQrdKMDLNKXDHh6FWV%2BtltVTo2yU7qFFtGY0OYq&X-Amz-Signature=07ab14bf7d083ecb769eb57e9cb0897e6231d8c6fad186c01936ebbfb379facd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



