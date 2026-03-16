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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THEELD7T%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDdpAdCBu2VGybgY4nfi6hvJuVwJs7mHpEW0I16RL6vkgIgMx2wMTobsa1iSOaVT%2BZ3Gy%2BTHykQbBLryStrWKveeKYqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIHH4sSBoR1NSot0VSrcA8eunb9VB3ofZka474qnJYRjbKVARFj%2BpjPo5aDTYn6I7Hgs1PFGhKWBag8YvxWYo0770ez04yOdS1LL9y4oRJtUbiNTE1I7h1IpJXE3NHMGFrhyZevmJ%2F0HOMLWLstnrZQlQexp0SsLIjTmZM%2Bh0eCdYU0ij5f8kEmecAr2pTssgXbasZh42ITGdr9XxU6Gd53526IAXZl%2Fy%2B%2F63vVPjvhAPrBsObLJGZ00OGOxJ9i1rw1QvHkZdJAMl1MxHDwR5YZmk60zqEIBh8qrjIygmbtq18U2tU8Gn31NLWLJLopsXGLbSg5ZrOqZ0%2FkHZzmUsFIcq%2B9svEupbW%2FOr0CVxgvSsc%2FYZ652OncV1htpb99mcf3lM3DeS3EuG0AXkdZgogvs6giBupF3fYAB0OcEZOok8rVXAQeeX33NzeZ1A0cSwfMZGT5teUjyE2W42aQPeSakI4byMF8bMtPPYFsRwoqVGuyIAYXn%2BIRuKU4RQoIwvA9TWljMVNv7aaT%2Fgs0wqtUw0MYuEo%2FnjDnSgTGf%2BCJb6EB%2F2M0O3OkNjBlLOXjzBBNKeB1nJ7aM1Te%2BVK6OEbVlWxgjR49DJTtbnfagj1oyX3k8283Jc2Ww%2BbWub3QB5HWnvdQPTOpuXY1VMNy83c0GOqUBuSGsoOi49fqXA3rwUPai7rG%2BLVjtsunR9cnC7t%2BxGfDfJbpEovMQY%2BtOx1PRcfdL7HUr%2FTIdLab9lNKWeA%2FgPP029dUs%2FqGZJrkimEUIu%2Fzno3MSu9MV0li%2FUboR00D6wztkzVVJiOM4jFm7IA2YItny74kSP8jnhe0ykVq12qmQPuZDvANnGNC9mJ%2Bek3dXnjYrAQA%2Bf3pj0IVffrMDjZGBT8AX&X-Amz-Signature=a0d4944dfc004d6403ee23d29142ac12c0940f9e1e386f0637770a34c9e93600&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



