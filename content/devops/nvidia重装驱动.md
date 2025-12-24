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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653S3SCBI%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQC%2FbQPtn4BOS0cq2lrK9I0yJoh1thfR8Kf12JOhpnTL6gIhAIkDQcIkc%2FXGhUG%2Fr3zY6Hf5JSUeFhO%2FEWkdFoItOuiGKv8DCBkQABoMNjM3NDIzMTgzODA1IgxJRWUuQbzZcfQXkbEq3ANuAxjAZl81MRVf6uD5e282RnGs1wFf7lxsXRDUFnL0%2BftcUH60WTBxuiM%2FModlhye4YFZng5WYBiem3zQu07benBc1goSMnvHU26Blo0BqLO847jJS55UkqVhVnz5MKaT8%2FyklJSZz9nmMjFJzFWbFbCWmSubYz4GIjSU4XWi12gBaxbu3yOnj18X%2FzhCpoG%2BlhfYVAyaD9H66hvQizWcsaVegjKH4Ad%2BDRuLRpMKG2fergzBj6NZwOqxWjnLhlyrz59RnLz55X85XB4TQbnM0H9wCTcVXD0SOFNh9vasblhUKlnmU6iUb41I8v5F9vJjEV2Aaxv%2Fulw4d491nDTq1Du3eaWxBHds11LH207JiHojmpkzOtF39Ym5KO3%2FnDuphvh2MLWxT449pg3SjVFrtf%2Flc83cLCJbSZT4uNtmj1AS03yqnG1OF5COse7uFjhDblPToIahTuw7sdts2La%2FHJSeu8eqGpHRHpOaB3NMbi8WJ%2F7q5ji72nkGl0Q5Q1lKfeRhcVJpQP%2FwX0DHj76ZCS5kkULJF2ZKjiDyB%2FuQX9r%2BbQsWuBggJZq22D5NzLyCrbTivEtp%2Fg1GwomC1Oem6RacJwvy7l7TKswNoXL%2B0EgAmlB40T3s9ZNcRpzC%2B4azKBjqkAbPH0r6tu3kPD6K9rIa1NInMdPyGtOWS4hFbseuaSrJe3tbdhYh6fE6qsCqYcd2mHmNIt8GAODYYqTu64NeFSjKupLOqo6aC3lH7YP8WJPEgNXYCOma7Hf%2FSvP9P%2Fk4ef9G2eaSlMkiUxF%2FTXJHgg%2FVh43P4UmdHK33lJjSSxff%2FLj4MFJ%2BGnb3qu0QkgvcAVFwuBiGarFscBKHy8g3Abosh%2B9Wn&X-Amz-Signature=357da2cef45778c697cc7b1639c21c0af950d41f52028095471576cd657e7839&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



