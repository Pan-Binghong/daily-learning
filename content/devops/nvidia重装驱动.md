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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJGYJWR4%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDSUnOYTuIwB6jwPn0CapnBlo3%2FzVcs964uEV%2F2CPRYdgIgBw3qwiLmDLCZAqZu%2BwUzio0JfBuXMxPvOJJyM0qGC7gq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDL%2B4CSg%2FCLTtH4A0myrcA44Vjgfv21dStpZcGe7DbJj%2FeJ7vILtD%2F8XkhnxAM5ji2jZ%2FbkhYGDehFq%2FxvK7w9OuWIubPD7mIsNVmY1QJHq2%2FbWLT1m5%2Bhkhn70MQYipq9ElFHiD3nRI%2FIwTPT0rz7HN0TAiAR%2BIrDhYvM6GoLP7JfeyPRIYBh2r3nUoN3BdGNCqHQ99djqpSdHxSleCvlPLHlxnViP6XgiT3WjQnDt3%2BVdTtzZmlDYhHxzY5o6SGacqdP01zlhyIeBlPR%2Bem2EFnyEpGr%2Bo72juAnxKxi4zcigfENN%2BtJnPLMT6Q9HNSHQLB1IN%2BsULPiXoWImqKhstYAj9nWUplg%2BLA0Xyvr6LtAex4kpZ8XXc4ETcPSXWUxbgmmvdr5JOJl%2BYe7l8faJ7rj%2FrOW8xOQg3UaGfEZgJLE4jXau1rWPWzEA%2FnWNpY6DZsrNfgcoMyKHiJKFI2C3YySf7Fe%2Br53ds4t1T3LZgZMXqVc3LmC0dcYBUC%2FMLUQ9RFR%2FR4xd5qV1dqOa4cn%2ByPuIbqTOnnhMAtDg8yfQlPVRUPF4yDOKMniIBQqynIDZ0pmoP8goroBY6GCkK9WBOl%2Fk9uzvzvbEUVTkO4ucMVEEgYeBxz5WCUGS%2B5cc30v%2Biqo7ZmzupCfdEcMLGD%2BcwGOqUBtNbwCz%2BE%2FdCuq91iYgvvPzIuMT%2FVDIKBR0ATpZHV8noQbBPnMYddvKNVV0sy2mmqc5g0uMEybVG47KarT8vr3%2B%2FDjpDvUr5XnY%2Fy40aZbQPbax65xPJ9CPP1m2CBihD4DS%2Bng1e1G%2FVfu2lw%2Fc5z9poaVEI7LSxx6jqh59N5LivmPGRksj9CqNHnBi9XEKo5kZNjCRkUgpESzKc0mL9E5vY19qyy&X-Amz-Signature=23d5a446f4b0c8170fb1af77749640d557ff83ca9f8f9939c92ed19db3b172b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



