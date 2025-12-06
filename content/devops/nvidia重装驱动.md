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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VFTKM34%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcYgOzG6XMy%2BoGXzckw245FDl%2BAeYct5b8PmZ5uEKwXQIgM%2B1JA2wNmjzxfygCQLGTRRSvfcbkYgNS28a64KbFtBsq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDBMaWgtAQQismIbQ3ircA8xvVCPMrZd3vu%2FpkYa6X7bKsbvtJ9MFfyQJQfWj7y4LSDik%2BQprZpMyXkFEV7Ra4xTVgXN6VB4a0QuuAHCa2q%2B9cfGqLjinAkRZ%2FlksFeTVjUg48lhC9EvazUtoIFlKgn0j%2BYi1oZrZkUc3l6pVvMWmEFFMwuntHswvNjK%2BGvdb%2FVcs1vW3T9ShNvJvSpSiBqTLqyu8IlofwZ2afOzFSdxrg3Ya4ZyPnYoZAM2T9N8DXtjE5N71H6DPEWBKtzqCMvGIoYvgu4yZR%2BVsiVvjkv%2BE1517EFngldsHRvoZh6e6mnLw8rjC4fMV%2BKKFAAsGaxKmm1Q4kPJkz8%2Bf6BW1wS2puzE%2FUZ9o%2Bl1wiWUFPcAMZUAUBYQfGCquiE38L4GRAIerRsi7DYCNd6P3zvfra0IGHynI0I8wyliB%2BkS16kKuM%2BOY98tf9%2ByJGqTqoUts9vjErogomWFoKUj0z%2FCGzXNUB5Om6T4roMByXavNg4eSpcsgX%2Fy9CIemmzFwkBU98FNS9crVACxC8Tbwee8%2BwWQ8%2Fk8OU1xiZVAUZGHWXxsTn3CkP6ArQVsdSAkHt7N9TTit87FYGsP73n8wtlW67xMJO5hM%2FPAIHy8wDOwQ21g5%2F6VAj%2BJbFXQILzazMKSnzskGOqUBDEvrR5SCnaej9is2n47H%2FYdSi0XA3nWLjvAnQ91suM9q4Fv4oFUT9Dv3vYY4GeH2Q%2Fx8HPd54c8omCjeethu7dwlHMdTdBzgDJ2OZrGq2Px0ucAmSNDVIJp6SSEkejF5dpRnNYhUHiBMJoLDK5WZ8Rm5fFpRwcAHXjh9lym0v%2BXBXCygK5oXf2MtbzearjEhWezO1M2zaLA7nYBvuNitMemr1KBy&X-Amz-Signature=31c83fd0d52327035005bd104d2c611a22b2142c8003ccd19c41d0ba1dbdee29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



