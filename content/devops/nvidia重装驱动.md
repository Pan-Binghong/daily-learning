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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662FSBXQU%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIEhyH6MZ0mb33ake7rSMDaIaDn8sugLB7lcBSmuCxm%2BmAiEAqhzXX1m%2FljtH5pX4RlNBa2aE8OqMF3tFS%2BAMKoYdTHwqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnENBhBfFXDvTRG9ircA8NyT%2Bf19kPfRv802yQscStjS5WFw%2BkvUnnoo3PQsx784c544qRqpUx9bLAY8vTA5JpBeqy4qyuM01HxDjeanwgOGrnyXkIODzP%2BcfAjZNWox5tCQOoil4sXmFnwLQthsjI4NRc6PpNoIWGrGP6MnY%2B%2Bc9K%2BbgpB3vaQflC7tJvPaPQee6e%2BrJyJ7KYZCxzcKwjr4n1XvMp4sUpGzMiT0F%2BADkoggC4D9Fy0%2Bp%2FJOxCJXY%2BtyW4LMJiLErwCXSj1V0%2FDdmu3JqFX3S8jcdX8zEdW7I98ct8hv2hxIQRb8pn6tsbiaF8HWMJy%2FLoUAMsn9z8kGN3QJg6AsuXNKVaw9EQKcAXRhLJLtwrE4t1vj4WiMFfRiI8GOEBcG7MBoyBi%2FgeLsDdi3jKjPr%2FVeoN7QLq8%2BOwhluFYVAYOlbcqW%2FntjJHuki%2B8CvUMdOX5MjjFuDzurrbYRAIlrADVJge6agdaHju2K1NrYquzoAk27gXVXFP1oQeXHwEM6AN0bgDJwu8kckztiUa4UDUXkMtzeMesvQJN%2FspYzd0FoePFj5q3QT1kL%2FQKrQDvXNKHLDtkvU6jIbEe1Ud3PhINdpf3uLt7XWlsEXeVfxEZJxkXcaDNkDo5ZNN6nc9sPHPxMLC6uswGOqUBJFl9ImUxnchDpmZnUJavqM4ZYZUrQQ1f65irybXc%2FrN%2BqEXlMxkeeEI0GZl2NEDGreX05b7S7DebTie2QrT12aJtnSjsWbwOBU9bcSfbYm0hYFF%2BKDwyYiHeRgE8RijNjWxmIm2DRDycW5DfYMMML%2B4tupYeSKk5ifLtjzvZOUW3LbX%2FuP6BcT8gtuuTJ43P9h9haQVjnqERe1lXQtNCPR5cc0ou&X-Amz-Signature=af778014c2053e1f0746bf7497201db4f26897fef43a465aa813bf1cc82305af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



