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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LDQM6WE%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC3MT2nihELQLOfSovxAaAbcWi%2BqxZVD6bFZG4FszarKwIhAMVxamvIqtxS9Ui3mEkDKNYbLEtv4nij%2BPhkVCl5z2kZKv8DCGwQABoMNjM3NDIzMTgzODA1IgyYoLChccp4lqgXXEwq3AMMd5SK%2FM5WJ0rlPEE2GqtNpioYIKMXw7FQVT90ri%2BLf%2F3HofTVKJqqV6tzHbccW1QMFLbEdDj8bGfwDSAp8DrpLtavb6abHs4JLM08ISemd8CdaYMqEDQYl8KV7nrzbBd0n%2FXC3zRHulpbwS6YACuIkQkT8HKVe%2BQ7UMt3NVfahZXxsVZDtWTDhpZIzjHg0VtOeGx9xsIgpmdWFyai%2BEF6lgqdV3gzKEMOB5NvYYKYIV97CHjV9Np5zfVpw%2BaiaZQr1ZmUY2DQi3ST87v3rKuIZooxR3IRPhJRf7s%2FIRf%2F%2FRTZ44tcOSgvPAPL0pnJSwtk0qV%2B3FwyUfQEIcH7Zs1tB5z35XA1MxeUjqpy4KCLdhyvhGN1ovF5JvQhf1GOtr2ivIgb0YWxCsJDC3w3raqN5AtOq8iCQSFcrDlpP45VUDe4RMYuoWTpq8Z2V1xE0FmVZEuNCYrvpJDPdZMsYsgrsrXhFLlnDCaA9liJ0Ay5gBNu30qXdGtXSoTcMiV45sO%2B8fndWDghvoCJYUsmOaDvrwSuBMdhHAtBmBISSE%2FH4dBZB0MZsUsSBmd2SlhLvwhFw0sX6E8pUhojPmdAVMQWxfaoZvwpA2DX0XRM9r0I1NupT0DoWQvPn%2F6UVjCusPHOBjqkAa7mD48zcDXtoNwWg7DRtkIHt%2BERPsVsp0XJ1G%2FOlvrTgJ%2BGMF7Pzrj%2BHYnyc4jpDfkLkqD7ojxBnhs%2Flhk3owoT9OtkGaUEhC7TmNyvVu50f4Su1Mygj3hTw0szcbHaj50NNcpgzQLRO1GBq2a7EpS4XiT%2BgK78brFQ820DSqyjRpkXGldb%2Bntky0Mgt6A7KOeDd5uzJL%2FXZmww04RkFU72HJ9p&X-Amz-Signature=7e7eca03bf16218cfeaa2d337d955949fab34f9bc63826d6e27b53a27b0d3daf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



