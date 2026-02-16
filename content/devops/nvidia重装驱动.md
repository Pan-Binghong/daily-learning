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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZDGAP46%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIHnGWOo0hJ3tQTgGyHc3EdF%2BPgd2kBsn5eks9YnpWOItAiEAsuiHTFQw57RHUH6xGgYgSSrQQ1ewRqDWrqzBfGedrUQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDK%2FG2Mun%2F3G1H4bMTCrcAzvQvFrUqHSgNT3OpqXscnEKjWPkVzCw2ntPb2ROue2SkNnzRuIjbm%2BwP3hbIytQ3iGADTo5aIIodnTOar5oDbIWN4THv3oQK8mP1O3i8wRXs2lvs7tWQmPxS3%2FPCwtKE5fXVE0qpfipws9blv6eHEqp%2BSkEmfBQIRSwC7w1qH5k4rNkfVcVDKf4u0ROPlunYZxDd0brjR%2F4IHu%2Flu2FXq3TmLNRspXwvbGEU5zboyFT3Z4GDMfDaX1xS1u2jHgJkOMZ1P8%2BMvLB3iKIBnFUXFaA50q2oETqi4LwBDCOmAFjzaklZGjPLcftHLk5kuk2E23pTR7AAiEjRecm2ZWgbWKx1NJe54X2LtN6RoGMr6xS3TrQnQsgJx%2Fejx1SY1x5HZ2VmjB%2FVomASzsRyQm80gnlvs9Jvrkt3XWIeeFvG1y2pOY%2FXgeS8x%2B93Pk9CXZvKcj2fA4tyZpExoTcdpDQs6wpR4IrSWMaUYlnXSsDU1HIhXDxX16KGXQh4qjkr0RRGIkkBsUGOqt4qfoNfJmOs5RbxH7q0kvmoTvMJK5r5WU1QiKZqCYP%2Fo2ywqNlBRxzeqrYySFHhhey2SsulSfpQceNuTh%2BWpap65LTLQtDfhVr9dfEZXPZu98g%2Baa3MIGUyswGOqUBozoaCuusLsNJjfNnhpwr2OY3cPDs3UILoKlkavL8WTQURGAvC%2BZjtLCdrfer1MG8%2FGvGNWG7SMPJ3WXUBp8ogilOkORM7T1%2FO3HFKThJxkrO0XLnsMbAkPGMhzypn5NhpXc2qAV5rN3VmuktlrOS2cRE%2Br1y9CbsrdIMdk3Ok7mlxyWc5E1chSd%2BJsRaJmai8C2hu%2Fc4W58sZwvEM0YD%2B4oWLcqj&X-Amz-Signature=e14adff3047da56bb9963018aed46bc7ea7070b362ae3310086721715ade0e62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



