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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657HAOP3Q%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfZqZDxtFkVaZgJb1acT6cntANOq3GoPTG2S%2BFc4SzPAIhAIPsQRL143GYMRzWtm%2B5OPxaeqPGKFWg0I%2BHjurrClOQKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyOvgxGd7FCRNFkMdUq3AM%2BsWBTe1tjKqIKPG5aJywJPdL1qN%2BnjqInOs0ANvHy0afDSHP5JolHSEFVOaZvNdN6dQ0N3%2BDZ6%2Bc7rDYA77DrJjXR9ti4Idrs98C4p6Y63goBO2PO23I5z32kNvgKV%2B7IpZbV5xnsnvMI0Q5P9guI3WDpCgt6cIboRQf27G2zpcv8kPKmjRbp5sT1EYupmiFV6Gh5DutvfGym%2Fp2KNVPDsIQuwX%2B8bxe4UCl0pmbPskxPZp44oEJIHpfg4kHunQUgMdRgYABx%2BWSBxJcbcHdsLQmiWvgrWwP8YjFkLkx9kcif2uTcgc3zgQbLiFUnPz88Hm9Qa2AjvWkDKLFWtF6j4cLRJnhwDoIYSCLaz3C%2BP7NKPEELIWtrKpaetckbHfTxnWhSQHc5YrFYyonj6eVe9hQsB2Y7mzvzmDauRh1SVWN46tCWrNBzxlKCZYMTI%2BBTKtbZzWOzBKrtdIzA0Pit877lfJnYZS%2BFcf70Rr6J%2BL%2BQuKl0B%2B9ElH1zeJv%2BnT2mN%2BP9Q3rRcylURnQtt%2BOEZtK7f8Fw%2BfrcZkB2%2Bl7S1gXT%2BSyS5zMxcGU990%2FBrj3Czeavmb6hf42Wj7eta6zWbG5egxB01UBZPhdRy2Vk5jB%2FZgcY4yAza32wBDCFyZLOBjqkAVqhn6%2B9NLiaxytbMFErMtnCg%2FN2hoQk%2BjzUAgGnIJfifEDIt0dTpCmxa3GC8tzeMQGxOhjcGzmdNZs6kHWrD2eVmFmMQlIPtliAqXfZDtjX8eLq9iLjWH%2B2%2BaMEtmA%2Fl8kXIKMEYISWPtglslHVMbLYT0JTEhkt7%2Bpq85ffP%2BCX5GF4cMjHTjC3P44ncyQDkHTlnSP6SAZ0quhzUlDHpDS0KjyC&X-Amz-Signature=552ebf3d952da686535403141a937443159c5329b3004856194ac2fd2e9486e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



