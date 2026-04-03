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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGHPT6MK%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNqmwv657EOPFVxpEBBQVWV3bH2VwonqBk4ZE6BiwS5wIhAJMgZZH6z5%2BkRpg8pI%2FLDwQtogZ0JZu4Hp5afM6lA0HbKv8DCH8QABoMNjM3NDIzMTgzODA1IgwP8KuRSHf1pYbIxPQq3AOyYXznYPsCPqGDCTAn%2B7zIEmww%2FwDbsz8DBxrmlQvZ547wWZAZByolcIPuKHz2AScFFYxn%2Boccy%2FyTigOdZOgiqG57JdZPXL3eiKLiKU%2FfFo%2FX%2FF2qmLk11UKTl31MeGPVh4VruIi%2FzMEXeeyvlNBx086EyxZ7XM0AFFWIr6MZu5pp1ZuJvPXFk2oxXAQBFFb8edMHkiUQXcONhmqxkfoL8nu4znu40C%2FsCndXUREyUFWwnzTaiD%2F67oMFoNCUhqmSur8wEM3GusCpe4QyTcHnPORMTK2zxsp8vS5ppZFqLyA9ndRJoSEyiReaPdu8Aorhga0jNeupoO3vnu6Ufh9hBD3Ji%2FEqMw0uK1qdhwNiau%2B3lE%2F8vi7%2B7OzI0o5K27qA0QsJfGq6nDgd5DsVHeKfAV4WE2lBL4Swh74dhARqVyliyMK7ONv2cOGkKefkRFmUKsJ%2FWGEhXgMfaYhtuX2LHk8IVCaj2pQyyQ43xwMYrV37tq3tP47arm%2BFzt6dqA6vinTxjCVBcbXPMzHNRd2WYIJwROqsqrFL61HtM%2FuimVwebJdEeMCjKbZdwaDM4O7rOqmGt1hKUvz25zXNfIp15uuh%2BfgMrh8ie1WihYA6EhPtKjjRA2nMvjsSmjDArb3OBjqkAbie9yEWpaZaymBwllffzcqAWR%2BZ%2FDEGgiM2ZMlKmPQdoh8pWiURyJDZshxWHQmJx1oR8oLuZp%2F28KmVeXKJBTj7O6OKiG3bG3oMcIJyM7KSDs37Ef%2BukQgobhfKcKapOR74s4a7eybwRIxlCZGkxYWyYLriouY6UCNQ8opHVJGtzXow9An%2BEcGMCxovx5WwYth8D8NW%2BI%2FRnQl58AYnG2O8Fhfx&X-Amz-Signature=5fda7657e7e46df7d7dd4428873fff57920cd9432cdb5793b0a5b55f145e3e71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



