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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JWPRN46%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbQvfmExeH4B9BE1b%2BC311LG9WURgaAjrS%2FwTHdvQyfQIgP0WmrjIvrCpB%2BIyr1LIJrFwm%2BJgCqVMBg3qBQaWentgq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDH9isld7FNHXO0unUCrcAznt%2BWs2c09oHLsAq3aCL%2Fdt1HzGIhgzZsHY8IyPuuByZoUBtgnlaCF2cnyxa3DprV2HXwz3WfpnSt4sFLdutmc1dCxcbJH951caZ6WDemNeXsbyL8yIgnONb2BY6%2Ft3KdCIRAR03w2Q8IxPpmhNhlLWAcdYd%2BMKAF4I4pBx2vqoeEYE7tDLImLBVmpjSuLMzaRyniB%2FehRoZdW2BepUN63o5tb688GfnwGskiskYqIPtpVYo6rlxJq7B3WSQvD2AMKnubYpS%2BUlexEq%2BLRtINprEBMOsH7H3zkJhw3y%2Bp9UfSGlHgDSLF4Nwr9DVmEmq0OvisJDCZI%2F%2BEdNA%2BQ9X7xnW5Y5fUz9G%2F8gsscHb284hsaD7TVCkuapVhXsuhb%2FYsFzRfBTISZilV5KKEQeGN6l2lFc9YwyDL9iY08PD2Qr0y928waSWbZHYEU2e8MKOQBgFH5zFCxU09njGcoGW0wbDIAEsQ8WW775ewyOdOhiDkB7s%2FJ52MYNzafQGwpyI%2BC713iWsdR2Dya93XT7CNLMJKwlhYjT%2FeFkLQ3CkS0QE1v4KKEXqJnAA612wZc3m23TEeKQ0SyXdpEiDACsTXM172d%2Fd9FgMkTNJYRE%2FodOM7YlpV8fnLNutnOCMIzFmswGOqUBMUyXO2IxNKQlG31fAqToyLmyCsRElQQWenzFAwy4z34oq7xnXo2XZryFfiKKFNnanTJzt%2BNmkiftMdo6NrraxJXKzOXXwy8WP2623UgFDLoqBKYy6niaEeS7RiEEMZrK%2FfEYisHUBnISTVuFvXFgnBHn5%2FMqxqsRYd8KIquCiWysxNfdFwCDVn1InTMr5ptYERwA%2FNosz%2FJ7s7u9ImTiW7mvlwZ6&X-Amz-Signature=e225f49813209b7d4be1e28fdbb99c051fbae25d76c74ab9ab3ee7aa1007174b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



