---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626BHT4FF%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICY16auCMsNOzao%2FvTIG%2F3gHvs6R6gssk103sJR0nPPBAiB5%2BBBQdsi%2Fvn5eSPkjXxymAWBm94YHc4bq2tRAsv7dLyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLDEfd7JEnTVjnrWzKtwDSnF8Xzuovi5N8P31USOCwO7UApmizoefFqbkJtySuwiwYhoxZ%2B%2B0r1BLRgre5lgywRP2HtKr0tm6tRUOSuVDVMhhGkOjqDx9yEq9cxlAFyb3gmQ8EpII3U3tFUAM6z77yNLEkHncluRgETLehgs04q4jc8oAPpnacBnndpG3WNpMzZ1PGPqnX9QXqCnuj6fHNJrZnFBIUKey%2FUgxQ4Gqo90JWZ4DdT6XI9zHiHmzkHwVPTk23CY7hkxZ4sJ7Z0q6734JWeT%2Fgt9NmBYkxYcg0hD%2FFM74%2FC3hsJRKSjRXCyi3oRgVYcEFgGwzQENiBc7Y0nKubY0vgcM9Wz5pSIURX6gNnK%2FIgRv3oK%2F3x33MCup%2BelrTskZdQcpmF8B9rhziYkOby0AgeyCSMsR%2BKRKIU2uwH9RqunY%2FaZunaStuJeZkiaGgR9OrR03zRdNiMXDOTA1WrrDPq5qS8YF3WXyoYMTt6VdGGI4%2BdmPxMp%2Bzh8lZIPHhQdmS2X8w%2BdyeAVsSR8ZmTrF%2FpQ5NOdOz2hNkA%2BSoSkqKNkaTN5Zmf3GAdsC%2BsuIfNI6w34261Kakrwe3zfLyAoyz238kSoFJ4qQ%2F5PdXgnJPMQT9C9AH8vo8zi1ymNXg9nm3jF23e18wn7CZyQY6pgHQhQjcu6cPs%2FGgayU4hXIWdBhu3tCm7eCV3jeiyOc82pDUatB7dHp55TN592vjPgDG4hbZPd9VISeHzECfPG6VIAi7%2FORFOcqrO1Wr5%2B87KBiaIsDfLG0t7ZMYkNiNI8MhIDy%2B%2B8wIiFfEoCyM5ObUXpPPXSrw2Dar64gstrn381SmmBzp8LLA0U3XXuJ%2BkghY17i9gEsetD97PEwzFIkamRwByt%2B4&X-Amz-Signature=9a28dd216a7fd1762b577ee361b6fede51d6cb75c448cb5faa29f8b673337d91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







