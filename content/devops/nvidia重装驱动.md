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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7ZUE6QK%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEHjt%2B5wyjupbKarUdxzDKxTcq32Or7WjwfXyBkEWqZnAiEA4Jf2pWOozOPY%2FhuYMOOB8tmgDEF5oOA9ovs6JAuIpmkqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1UnpnEAuca7gygZircA7P3X4apRGuC53PF3Zcn7KFogOnLADk5BN%2FpZ%2BdZMVPd73goJO38jbOXBIRAk7UoM07bi5QReYCFUKHoQteGM%2B8DPnq96hTKrJRpKOzidpvTr2Cq81zK9Ba5LBRx12cUTNAUKJPoWqciqD0tfFmadUzL49Fy%2Biujid0StRqHIOZv3UPya%2FxvRbOdN1CxslL410QyJIMUqtGh8iClJlUowgOhT4tDAiWF8%2B%2BBSCXk9Fe5piwzsmBdzpyxr%2B2HE5wGDjwzJndQB1FPaQdblXsEI7OXnNEbg90oBjw8DMO1z8S6avxkFsb4%2Fm%2F%2FNJKVOLpGhmr03w4qELJ3mYEkLr3PH7mspzwS5oTzembLf2SO25bgcKgXOVuMQhUDfoMaMoHGCDn%2FLKr5Cl3k7xKTZ4%2F9mRdJ7CBpwF3aXQ18ElQI8m8wsJw0BeX%2FX0f4zF%2FpsCF1HpZBLLq2YiHwRoXGx4rYi1FT64%2FI%2FLwcAc9U4eiu1uglsG%2Bri2fyXEAjkrb7vE152ntjYmA1Eg9Jb3%2BOq%2BGtPbTEZImXSXa8Xmj2m2JfLBgNuDU%2FEWUyFwfHuRvwWxUBJBn3Texv7JrF8ZcXsoMp3P3Rri7ud31kl8%2BquTgpNDbDoXjvDIpojP01bDY7MKOW%2B8sGOqUB9LMhjihBd%2Bp4V0EiZW%2FUGVzQW5qppQGEDbbeLlGrqc9vgEpAwiFmt8cWz8NVuXOgtcvTvHPnUPyqG4ym6ydeFgomRW1jTaJxYtRz4kkU%2BqQ0ODnRbjRNcm54tDeceridfiMPdPPnquboyjeQ0JgA2KQRtpfveIdEGDEhIokDBAx3dT2bw%2B%2FemOd9Ed6Z6d3vCyf0N8DFwvwY8786qbXszJYk60r9&X-Amz-Signature=e0aee35e3f309b8a08304751abface56a53cb50b79f23acec23e5cd10bdd846f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



