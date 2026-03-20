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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEKQEUNO%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDm%2BgJoN8jRGT6B1y%2BRmVHW2HBCXGxSkVpAQ8MqY4Gm%2FgIgN4cwnBydBHrPuHNTNJQR0as%2BBwfu12yEEpOBFHANKDoq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDBrJTQZzxIewL2iXGyrcA85Bx6vA0gVaaxykE6gGjwowfbUGx5%2BTGFbILx9BzTuI6qOwoPiP1oEc6G2zJnjjiI9Dhu%2Fx0JZ4qFzwKngNyKvA%2FlGjczV%2Bani7TzjQMewXO6ngh8SCt8xRINMkGLIjlPP3ZLdCMQKR5UqrmE4AxrYFPSKGVqv0%2FBs3uPiGrQQ2BI4QRA8X2xwcsJfJeL%2Fv6W7zAEJnFjZylZGXG1hnEOJbhsZM274ZactyobdshVHL%2FwJKGHTpZQhWgXwUIZSfqgfSMOWPVnK7bY4CFbjgdzmhPb3sYdt7bn%2FrlBLy9DiXRadqF1807Ax6o72D2W6UMaYmUIeXp6kd9FYV9RSkPfJucNKMLpC%2FxYMS%2BrLekWHrZ3NDf3jw%2BkKWYAtl2evL9gyEtbfjHKTFhDkferqDAGkn3OWIFyfyuL%2F%2BZ0ZvkCccJH%2BBmuMuhePw6m0mg84XPIH%2BIwrBbqjcg13mpnySEFchOghZE2z6pp7ZXIhBAJ3HM3pB5YfXz%2FkwhVl6tB%2F2Ava5KFzEq7dySc5AKVpgXXzKNqUZI36fX%2FDG%2FjVy%2BjIV73ESbfU2eKXWfRem%2Bu0WCndmJnprwigqwfn9hL4jtsdrRj862WAekEIuKh%2Bq2L8HCrZwB7XOX1PeqkBkMNu48s0GOqUBXeve%2FDjQPj7K0iVwOimaPHfWzH%2FeWKYK%2FjBKZjDX5ElztmgzWTCEL2F0MRVzwcmVTHsb6AnvOshiCtCJmFyqwyYgxU6MXpfEW0NMnBJC30%2BRwADu7q9788eHP3HMK5Fvt0QoKErfjDe7T0vplur%2FCXK4TmcuLzua18qEGZS5VX%2Bz78SQKD19veMG6D2CYRu6GAF0dXIamixD7MWKQv3ZyYCAuVie&X-Amz-Signature=33346a4bb835e99251d045feff6a90e74161149357d0598f1911ed3be168f85b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



