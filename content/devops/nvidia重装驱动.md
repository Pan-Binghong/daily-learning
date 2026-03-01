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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKT6J55T%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFAw4O1aCs887gGXviy5Kso3yjlmxYtZCRZX6hv%2F1eQ1AiATpHVDF2ph7dNvJveuwhneo%2BGXSoyxJalxNixoKPsdLCr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMW714QG%2BPKjFg7uhBKtwDXnaiF%2BDbWomzr4z2n4w3WxaeIiFsor3NfPifNeH%2FDtgku6ucHKma%2F2NZzusE4JTtobgcbxvWASXQc2oEccsfAZUq6DkSpx5rLq0jjhgLnI2mLS7oKH22g6MzWLQtkRDTmZA%2BGUj03Cy0eTLiHmsMV4cx%2BOm11YSAKYSUSye9EBryXmKPkde%2F60QBbGLEz235u%2FLwgd8vYz8Vpklw6%2F1nauVyJEVNnobULawsJoQQSUHJ98Wdo93t6HByXN8z9XuI%2BX0BApufd%2BZ%2FEQPZDKl8Jk0XqPRdMoFIvSv7sCCHEnu4LNEE4Q7pFDdHjTEP5sX7XSjlsZvbyuI85RPonkcbWA6hrOuIPwokpQlXzZuOmgW7UOcJ%2BfUMSqWXGBLpZ965FpyIvnqktL%2FBKracpWbLLTAma5HaOGCqT5W6JNihXbLPI3ltqoU8cdSAeFLLqiJ%2FMmD%2F8dGydI%2FDLvW45qBS%2F%2Fujb0TWhK9Ro7W7lw2KL9re8xHXFnhu%2BsWYqlIypqg4PAs6SlU4KpUMoJUWkFDd2m37CszryxC0YtGTDg1oR3AMXwsOUVUF6W%2B3ulzzlQ7tPji%2BWsywENIM%2BydRkxtHKVbDkXJe735kAt5i6ojMqlUsXliYkrUH9XnhN8wwz82OzQY6pgGIptF3vjuO8r5omwP8XHzjsMiz7Do4UY7k6vc3BnpRmT4rFVJ8xo68mgt2b9XPQMnZ3kQsOFecL4uSnuns10CNhsPl1zHgTi3kONRFICcue9CJLeAfI6jFwKbaFr%2Fj0OzD30F4SAyX5%2B6SGSo5qbYTqNVTOcG%2B%2FOFd4uFsaJAyUOCA4uZPByxN1iJRCEvJTScOZutxTypHqxX5Mxu73IgZ%2FiQqdy3B&X-Amz-Signature=c2a4c8f891fd75639f4225e8d59b4abcbcde91c9fce447b7c31efe9a28a7d5c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



