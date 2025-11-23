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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMTFVG6C%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCmPny0TiBqcnIwa3pSstnH%2B1krRHiNO1hStSIWfsrjWwIgHvki7U5WtyBJRti5L8CTZ2F4OC3ALCAUegc3A3%2FaN24q%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDNpheJRBZ4CX1%2BQIRircA2%2BefhrPFW0LvGZknO92suNp4UWFJ%2FhyZ5zpbA7i3C2zJyOfiZp97ZHfqk3pY7uzp6sOBzu7PpP0JOafrVFwefBSGs7GJdBezj0714RODXYe4K1e9BBKJKc83jgor7TEDT05YfNiQ71iiy6XAsXGcLf4GCZDPXjf5C7I4rb2S8R2%2Fno0kukgTwT8PVs9%2BRlVW3e5gCoInFrBC02%2BZ0N5IbXr%2FAU%2F30%2F1f2eXfIyW%2BvJ6wQCfhwjndmSArNMtGqx9prj0aX%2BYMlnvCUsdCZZk5Kfv6JUogcCEnsdE9vmROhkA0f%2BXq4epqrvz6yUxbcQcdDiPu5NexSI%2BUyvKthG25qiDDSOsCoHJlYckxISG2BuLzujPMDExDhEYksniadKISE361DXIXP9bBcR3VC55Z14AUEofTbCPU0OIx88bxtogrzxVgjWoW96FjuuoyPeNHO4KoglAjjM0MAEKCYi1sdQPKs7580QYVFoqTyAf%2B071FmMEMGyerU1GDyPgGxasTPIMaQwUcq%2F66qO6Cs1okoI5%2Fz5ULbXxY%2B4wfpwkFk3CGXI%2BbXp3y7iJSfIc3x0qGf3BiWTN9w3yB5qDMszIcRWb47pBTyA4M464Azg6jjcMftBnG5Mgo3yJvvw5MMiwickGOqUBckqRoZ%2FBxHI5MbHA%2FEAC52f5MIkC%2BfqzW1nFPaQ08nQKmq2EcJfe21TP3lN2sIsKi4dMN72NC3vzKR4Upd%2B0jlf8Cy%2BJNMcQwl4LqLEXw7%2FdVSwUAYw0TZe5nMmbDIPdxttfsoDNU6YT%2Fcdo583bJoXa9nw4Sql9XdW7qAhfx03OEvy2TsHyAz48uyiJld%2BiZZhEN2S57Pf6%2Bloa7U1VMeEcOZKy&X-Amz-Signature=86f9a7dad7f52ba2e6335158be3a98083c627676bf547b5607edfd9b0db46d61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







