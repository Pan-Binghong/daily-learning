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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WL5IKM4U%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQD3xBBeJm1OXXBRq6cE5KyBgnyey1Zb4R93tzGa%2B8ferQIhAP9MwCck%2Bot0CBKKIec5J8AnNctYCO%2BrfJdyv14qAFuEKv8DCCwQABoMNjM3NDIzMTgzODA1IgzABFact21CW2Bq4Qsq3APOUpkDKz2b9LzUzO27Yp8ZEt9aSOFU2AtGAl7HY6fKf2Ted6MaRtz7h8lsl2Wds5CrwLk8O%2FQqXlDLLphEC3VG4wU7f1rH2KuezqQfbRmlGpaN3TrLmhfh0N9F%2FSt4gDZy80ZHRN1STupNdderjNB4C7QuB%2BNwMXOJdK%2B0x3Ohorc13TPZ3AmwKPXbTbAHNCmFSEDAZ7QD%2BUXhpc0Z766lES2LwXelq0pb%2FpOstI1iH%2FK4nbCdnOz1kY6LGk7fBIOaDEhNaPy5GKPes0%2BXhNj163biWH3qxTk0Im40RKNVMjdyfqZmUHarwQ59%2FuEWKHY4INRUI7QkcQSSt0qi31kV7D9U%2FGChulV8pjW6zB91ouIqCMIO0gA6TI3U9TM2eDTDCYPgHjwWnwSRIeQ6kiBGtFWhB8EJ2i%2BDODBERlWNT4hFqCSbGGBx7NbKbcIee0Du6xw98C1Wn4kQMVMDFN8brQy%2B480lmsu%2BldAzEOrzAV4GdzQlDgf9QlXpAMosEFI%2FH9XVXJ8p%2BVUlL%2BuJ47IPL4RbURKXeQamHJilnDIsJaLJcusoX%2FmAY64DNqur1qGb4mi1XvEViGsSsLeOIee%2BLKuosW7YVS0aldhbfyJUXwEdVQfMNYflzLlHCTCt1JvPBjqkAdkyXMZdUbvUgCQYDNN7AFTCOQn%2Bfdaa%2Fz3rFgDd0OQnFq9iF2mhMMmZ3JFJD4LfirJ5HiBP1m0mS7bmA7EjmCooe0lc9EOtd2YWvBK9le%2F67F4305aOETSbrk%2Fi%2BYyNCaHsfFzSXbCNjbjIdBVd%2FSpuhTz4p29lsrXEuCluyHfjlu4aEab4QINXSLfdFx7RMdarx5JA9d0xGUX3S4oJ7wDmP8hf&X-Amz-Signature=039deeb34a91edec39a9a9eadfd44e24dbd2125811e1cbfb20ceb1da6017d7f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



