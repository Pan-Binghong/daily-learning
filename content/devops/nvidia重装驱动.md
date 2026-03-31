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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2EKZZ32%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDva6UHT5Wbp%2BGGDn4tpULfGe0Cfbl2ErKd7QSI5RcX2wIhAIdyUdsLjP3%2B300SDyPaW1RTUfLM0v9LwTsgTRLBtlPqKv8DCDQQABoMNjM3NDIzMTgzODA1IgxdM33A7aESETHQT4Iq3AMRIIJ0m9gpKztVtzuc%2F9YdvfJ9QUO%2Bwk0s%2FYCvgtCG9XrXuPXDEiU9lWkua0pe0tNJp3%2FWUimjiUm6ZPiPMeLPXkncjGQMzz0xRgJb9754xVb14FsGTxg6Jr51Co9Hb01UVwJYS%2FoqwE1e4iJnzn5IWZCsiaMhj%2BGZBEspsojV51oL44RnaK9TCRffbQH0AtLKIpYIK0zcG3YRibnYL6rH9xY9oswASplHoH0P1KMoavwsRkv7SUakiJ2pIDtU9mTfaSPTaZnuyWj18Kh8fNMwfE8Pyi5sdcKpc6y6kuR6HI7oiGx%2FYqscbxKCEfTaPdGMnWThPXjKjMIMBBat9VXcGsE9bWBpbVdj59KNeS4VG4CA0jkObNi7cpbdYL3g3FmuESmqMFMQ2pc1WBC4UCA9lQP7%2B4btwP3uLopn9qN71VOip0ogxHul%2BFe33PT1BKBSkRyE4UYfoZa4QdUzYXCJgVto7dBBzif5E8TrmLER3HA%2B1DHsgNI%2Bb641Hu%2BbX4fMZMAe9WWnchc3rTTxGY29c4EeT0IR3OOva%2B2WMhi47rgrbHHcIAXvd889LsgR6SsC92N0i2r33CL5H%2Bq9WmcRoXsJ%2BHRpCNjORGu9pBHY%2FuERt%2Bt8oQc0Iel%2FoDCO9qzOBjqkAYXqwhLACwZTpb2%2FqybDXia3rjV0w649FYpTj3UVzO4G9n9UdN%2FDntySrc0smnne6UWQF0Gv67isWGxkqObpmu6eMzI6LqZ0d0zV8oh8lhwWQ07PAR4vLMtL4SojdE3s43ePDbLZNWFnK4ldAP3JiqfSGfO%2FcZHm%2FuGbTJgiqvgIb0ZOfnzXaoFcuHALSbU%2BYK1jCF8AFOVg%2BJajtjPkeh2lw5Ox&X-Amz-Signature=9c236d89e816bb8179a7074a48bb77669f213f4a54dd2b887035206b99ea5e24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



