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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD5ULG2Q%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQC7JKt96Fa7FO7H19oMry5FWaBU1V8Ray%2FBVR%2F16etDAAIgB0YYWFbhZAXesltwNO9FG0qZyDFkzxEmOkUV6WAyUokqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRUq4w7K8ifH3vRnircA7Ml5BreCVpOKpjgCUnb3u400aYJN43eUoxb2AKeHy8WNqSzRtO5i4kbT1pPtaJs12Q41PlaUB4G2l1aygPu%2B%2FHjnr9TsisGlUvV2uCBV50mzDz3Su%2F2KEW30%2FT%2FUtOZzf27rJVoKzO3IqyEA9KYf1p7qfbA7zz9agVIQ6vA0Ketup%2B6gArTOcrfmNtfUhiRqnaqevPX7OSTjoUHl9OZZ8WeQhjX6DGIH9jST9Nx%2BeY9BnWqyehNwIiGeqdM4308xFQylrxdrOa%2BimgR65%2BriUsz1JYnevkm%2BWoM%2F4fby3%2BgTxhJR1xvx22%2FKCfmxd2XdDyjCTIkwJ6EGlgdGQAfBV2aIKhGAP%2BhIKknB7CCmvCJaipr6kAiKYf72DFLVTmJKYOhMosh8laLp7EBhTOgZ3Td5gKA7mRfPM5duhyULQpGJz7PhXXlOnKTBJZkmMBRRREAbQAau6fCGyuf9vdzwR%2FolaSNqORuha5yoQZXPEfhEZply9LrOtYDa0Agow0ttvGXt94wEvvzJrwlmhLKQlfPF96dPjwaVOuNvGYVSBjgPaGklePrW7NzhA%2Bul9%2F%2BkQgeSfVn%2Fzp5iDtVBVwJJFQTJs6cgV0%2Bm6CeqMXn74YJF7b91hc3ObL1gqtlMJDYhcwGOqUB8w4%2BpqVqbzSsTZyXxLx1Znz0yedzXx%2FGXqRxrO%2BrlcpM9V8YOj5CLe58ar92TFBEbRq5nIld4Xx4AeMtmz3VKn22175hxtRaXfaT9JuY5XwEFuGZbpPzBc1GxCRI8yN6nbLiPXAOeN6TegfCWldQ1xM%2F5FQcRYPWypspby88%2BxJEOYPcjjJ20vpA21thob%2FyLVvJg0bKmetAbJdC1ASg0WZZ3ryt&X-Amz-Signature=acff0c0d74ae66da2c0d60c138d0c93994c35879ac4f2a3d3e9a9d1081d2f249&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



