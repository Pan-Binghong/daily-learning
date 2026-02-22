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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDKEFQCN%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLraJMFMLT0Fujv795k9mLO0XQVazM5W0%2Be4vpb054JwIhAJGBcglmML0fVeAy4o0TLmJV%2FFZG0D2Qem7ueV8IIem%2FKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz217WxolZLJfrJSh8q3ANGv%2FAldHIw1ojMUG1SIjTN7tl4%2BdwNIsFYnFEs%2FT7bv7T9isQXCuLBTSfDuEJbF5XNskPptGuezZBtOnfSxrK98uHUH5xa2iGkujFuY6dma5eZwIg4NJ33VfI%2FiYjapicr5kugFIcKZkXxzfD1YcVX6vqzfgWKi12oYYquKHNPF9%2BIafo8mtOb2MFIVr8qRHQtsgOnjlrYg45nrW%2BT3UGizZcqbh6f%2B58b9JNJScaI1Jlc23WlanlTAqU3W4hVT41fFOwZ5Wx1EioXmz%2F6Gi%2FAMvwRhgwkzLItqllfvEJ8bDWU5btl8f2wttS4s7IAexpbZB8PDpG4zEf5e7nm%2FIy7kv28kjKExvEWVEHXxQVi0GbqQ3jTA3Fq3i9q89rT%2BExaGQ7OI%2F9QzmJ2IS4KQ3iZKbQHc%2FrTz2BAZXrWevPdGj0wFCpEQDeyOcg5gxCXnWSpO0EfqyTCk28sXh24LNW9Plp4gu0XM4rKvjK8rHEx2D0gI0odGmNUg5hjhN3xgSLQGOrRVnas%2BnMqLN8YX6Iz%2BTI0xonq0uRVsVsu6Ba7snF%2Fd1VVvEG%2BM8WrGYdWNh%2Bux3kC6UMQObxaLEhafPvSoA9I03rVzt0u9f2ebhIOi93%2FWwmgpQrt3cooyzDf8%2BnMBjqkAchy8NNQrW7IFkNIYxMTSqgM1ANoTcUtBvGOQCmGmrjVJjSPdvyYSCW5mbRidZBCTNJUqSIw0PKPC1fS26gOFcmyuKto0WKfwRc9mipDCiTqnqmwKQnNQbNt%2FnyDVwD3VHKUYpuqOytBThf%2BUiz3jMsbxSt0i1l2z9nKS%2B6GAeCkUdHWaOSEbf4U73EUQ56e3pnrmru56s6PD6V1xc162ugXgrQu&X-Amz-Signature=bab1883e5463e171d8ee7491fb61c458c16cd779a29e3df99e52262f8eb32247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



