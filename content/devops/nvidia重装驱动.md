---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OQYVYKH%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T025045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGPjMGVLdr%2BfEWF2q4oB%2FZIWQUizeDpB89HR8JeZhFlgAiEAyPSAkpFZUrMPv0COIkglMItRk9NA4CexVHwT946UWHcq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDAwMd%2B2IHPea1LrZuCrcA9B36urTnEt600W25iIA7FMJZiA4vOoim181b2%2Fjj8sd2XiEml1afmPbhiCAamR4R43EASx3vRidLVkiYNkvtTZt%2B1RWzcJzNqCQ4Ri5pao8KvOUmSMVPP2HUmvT68cY0LOWMwYpfUdWpEQ4z6Rz4FMQ5UgfuGCmnP91sCCN6JYxPUbVTEJSIP0pUBqof8lv7IaE2NSduRHIsgN%2FcdbQFu%2BWiQQyMgyVrb%2FyuYMtE32SOvj2b7ul%2FLJjxCAKxBMsJK%2Brw9qgo1TZT6KWS31z4%2FHo%2FLuISsaC5s71E9LQpXFyn5jOL72dnVsdIRk87Z2uIphPpOOyya3TPEvQnzPYTIHHC5aB4Nqe15jjerFhgOiIuFmTJ4mOr1dXWMbT344rq%2BJw3SsilMhZmPZYVIb2pn1adkE5mmVP1W2Zc%2Bfoyxgupr2BHROAUndCNGuAxRf5qUQfZq%2FXPkP2Q4oBC%2BqkyNaZVYdxyE8UK6wcPUJHFv08cEFws1Vn%2FUjAE6K%2B11eJoNv65hSHWhzUk2%2FSObrOlIgKv0Iy5n%2FAqYrvlEmqGUtV1ZGf9qT5VDSzVA25N9riDPsB12bkWzFHy44OqFn5VUAwn%2BDINKQbw%2Bb18eyWk4zSIMfXHeVZyse5WmXWMP%2FmuMkGOqUBzyLPF3GHsBUlZUFHgsZyB7CyRI00P6z7L66QWwuUnrQ4ENqRnDEyofT67k8Uk2HE1mNvRavIJm2ntebARJcFrIXr0JgwKJ%2BruOydemawA29639Rab1lTTv6TW%2B4OXSnM9OrWUTt1bXjtTyziZXYIOw5eN%2FV%2FxuX4LQVb5JLJ0xIAgG8OfAc%2Bvfyt%2FKMp2lWZN3hWi3MAeotKmjdu5dgjtSFK23l3&X-Amz-Signature=09e372772a0cf0e6fd1d9a704397326fd6fa3f83982103df59c9b0f8e6f7007c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







