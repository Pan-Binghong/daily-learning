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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V42CKZUX%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCG5pT5lBRPyBAihvh%2Bvb3JDt5kxBRVogy9Sd7V6xHgEwIhALWuhSEzuPxedezeU3%2BU154nT08osvJirto4BTfLZ79gKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxP9i5Fn7Ho%2B%2BGuJqAq3AObWJJL%2BII3WbF9jwLI784cuza5IN2s9j03L1a3TQdhuqb%2B39eEaacGH4iKeClhzxCqNc%2F%2F%2BodcIyjH4SpEe%2Fjj0leIP39xbgXygBQN7N%2FwKZWLzhiKfDxAbOmAHF90k3zlvIV5yFEbM1T4nNR08CYwlEZJLwsEsvBGitSN%2BG127YT1qKLhxACTQrLmr1dsYKNb7wxtvOJxG3YcvLgK4H8NRId69sWOCfaFFXUZM0ggyrizLz8%2B3UHU5VMSOdeJBdONUVlMNoxtc9LjIun367YAQw8Inf8pRkqVLzekpMdZ16hx6DUo%2FPA98%2F4CbppdS%2FsCvVb%2BekK7BOD39Fhs8y%2F4CTUugosNXUXufSZovUNElgZW95gE%2Bh2ngcewYycL18Hpv%2Fa0sMgf%2B8KJ9e0iNLHIUlI7bG0MAb6g%2B2OhZrLW0cYZhGfxCH6eKgf0cx62oO%2FZdCpVcxRHuFfNV7CbzC4ZTET1eeGlifkObUVIkC%2FMpj8ZUvcwjTiVpLtaJzJMJLNsrcnYd4VRO5RVlazcbGW6B7aNgvlFj5780qhWDoPzCawibQphb1F1WJ%2F1V3lL%2BJITz2gf6ujXNJoeKOjvtl3Pckz2n4FzygIXe6rwXDsDOv8bDJcWvRhFSYToPjC9kd%2FMBjqkAYOIMkbTgZgd3ZjKoKSCmrBr3bCvAfoeGN4B%2B2rJHtHCdJNhSKAJX7sps4jNksDVsdb3%2Fime835Z1yK53g3OUsIqWCQRkkDO16S87j5peGgMF54MhC5KHW4OCiDZgkYmfUnTWuimAG4GI0f%2B9sWAzoEZPGhiiAmStIjeNLhDw4mLM5RbSqWOx8xoCI3SO1afvnjM2WaYnTGsY9vq1FFCTLTa4y2H&X-Amz-Signature=9580ac72f62fa146fab06c6ffdb30173feba640136790a4d52bc75f7dffeae9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



