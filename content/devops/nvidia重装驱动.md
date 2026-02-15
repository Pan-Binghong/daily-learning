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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WS6HIKQ%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQD%2BidvFCnIdO6MvWT0h4A1kMtk%2B7mE4QQMXqnoPiLkAIAIgSvKkh18frXvFXJhLkvW8DiQ6%2FF7zJNL9fqsWeKXeAbQq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDJaEFYstSvHgOdWZyyrcAzDx3xFOXkW1WDKX%2BZoHnzSfyVmZP7ZZ%2FIRoLeOAFaw%2F%2FSK69sNESHdSaE%2BjxE%2BG3sh5RxjlDdshlrq4cgI5iLnFS6UdGsYSeWrtPq7Umx88Vx82Jsa6gwLvD1LWd01sZ66k1hyGShIZvE3B%2Bjrs%2FgHNWOTG3S9eUx7Iqbs1iVCa5RhhDrrdOzNt2ieN%2Bn3ZDEWKAVz7PmtJXfHjca7rtWT%2F%2F0Ir86wemM%2FP9S%2BmVv8wYMzTmV92faFeBpJlwITFehhHsLymhgJP8F709qrHb0SGJVrwVDXAXoG2sXb%2FwM%2BXzXQV4igi4vYhs6wy12vtOXnThW4WYie8Sx9aQCvz%2FV8L%2FfII7tPMsIq2N81M5h7iXolRqjF8EdGht3wPJun092etzhmMF5vwRxC%2FYqiG1vN7hcMspLgP3uGLZU2TmFj5%2Fx2D%2FlnTR10FRH%2B6obcA57bP%2B2vQVqCNo6fWm2Gp2uUDXEtOIhrRfmW6Cf53Jb%2FCayXdfhW%2BmtfcJNx0GLSQezVI1U%2BUZ47MNwpvxBFM0NDgVBX%2BouGn9kwEJxgrpOxiD1Z9lk%2BkbDAHW6F5RdMdKFljv0AbcktdAB7O35q1tSL5XP47254r1VabSW9wOYhp9C3LOey7Zn%2FuENdfMLiexMwGOqUBVl1QInMKb0j3nXJogS%2BTwprwXHE9usd1oIcKj1VrnzRN5ua2%2Fg1Cp5b2j%2FBU8xAcHfTsPQNk59xnUVOpRKd6wM%2BlRMsqB0mYSyHW6ulwNg5HyP0pGfiWIali3OHIF6FvdeP8jvEtmG1j1geCFJu55ZtAL9ckUfWOZNnosI7kP07qtdq35zKKV%2BUSJkAt35fWnvPe7r%2FLAaeI3u8hXfITS8pikl2E&X-Amz-Signature=afaff1e523b90725f7c77fef0b65e98fdcb51fdc5dfc148c33e8c485449090e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



