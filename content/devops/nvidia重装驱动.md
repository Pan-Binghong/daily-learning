---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-12-04T09:08:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XZP66AR%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDVPpN6Dn7sRmjisO9eREa3G8pWALidPCzVyLr3WGZ4WwIhANBRS4qBNyV0qgrTTSrsJXlkjPIpYb1hCsBOvPdMU86mKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwT%2BFZKa%2BxlTB1O6hAq3AMQDOivccdvZ3%2FwKU%2Bl67SkhQ3GafFG3ldk9de6Uv373rbjBmYXt6FKRri3gLE%2BXDqVFX9LJ3QXcpRivSqmBKq3uO3CQPjFq565K2e5VtkA%2FfaNvW8ltjoz8lUCou19fWDttDsqYj%2FjFdBRQlhCmqD6NnQn9wF2uNnFN6fubhJDK3KC4xuhnPVY5IvDXIfuxhjc2GtyOXIt8N1KNZbOU0Gc21c8zQvQ6Fo3xuJUvt3A%2BjmXBKZwzxyii%2F8SfrCJPYBzKAJbgq6D0lvXkIM7qECNdCDFtJdrf9e9ulVH3wVkdNhpTN3RU0aa0om4AVCnkU7cRK3ntkEANEJtkVSyyuiJpt2R0vDGDMcOqGWQzHDu8FF4yoUfwI%2Flvaw0QFCfmnVhN6rx%2BXqRd%2FIMlQGdj7HB3VBqs2V%2B5dgPhgm5O3OzOUwugjdrv%2F%2FQ6CJV5IA%2BH109IYd9na1OHzsZF%2BfBe1TV7QC3wE0b810UbRN6DITDx8Ys%2Fba5epVoaHBHhwCWzcPPqf70SV5tSsS1T56gxd1Muna5nI7p8PWArj9harO7cA1XbGj5ZLF52%2FEe5fxt8HLFjxo6ClNjMVuTN8IxyzJo6T3lfJCIFbei5fUXAFeCu4Pro0v0uAw%2Fph1MKDCe2MXLBjqkAX0pmKOCrC7xtNX9VpqJVp3g2EuL%2BAMUFsJ2FVp29kb7BUct0YCMUjRK%2F9ozHSdjEduESryBm9LaYNPgdFpqpddYEiDC%2BQsht3mkI1h4WnqHI%2B0UNFvKGcSKyaEOvXUPKoFnG8f22yBfWiDP5V0KPh8LG5C23RgrYpLomyJXCiodnmtRaB%2BUntq57qQWWMpO38%2BkddidCEmMIKJrpKNJnp49unqu&X-Amz-Signature=f0a88f175db53a983abeb69ed788ebb2fc75b8ecfadde35c72e5fa36b32b8d40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



