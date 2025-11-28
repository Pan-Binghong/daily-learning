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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Y4XJG62%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5PpnIN6tZE57R6ECPPLT8kjSC5racVdUZTaT4NdwNbwIhAKhTUa6NMJoPoZAlzN0V0ePn2mhSNYp7DPpyeFxp01HiKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWQpOxWCV1iJSvVdEq3APiE18L2asLS7m%2F76XC%2FVK2XAwqLmofChKx1NfM3TOOGbTsgkpIZzfYP7YF5ojCDsw6TrHJGixOGi5pAsYHy5CB8wsRTfcPDeuZ2v0Ay36gHmessVecJSUrk%2FtYS%2BhNwr0Pz7R8WOTpEiR62foSagvvpe9UzOnX2VBBFaD2AktsOnF%2FjwPL0CmCiah7iai%2FlrH2wjeKwNX8QZoNEInBOAtXiue008MtMuFCz6NH1SMjWiWYjbTLHQqLqHWYvFXNjC6uSSIPb93BVHaQYcg47qUkl%2FFZcVy3JArF05xN%2B2hg6apOfbZ1RoR%2BE8l%2BVwJR995r0s76FjVIi7Hv3Jn0ZZqXjqIL2BghENmEPXOfA8%2BMG9AxkOTz0zu3XNB05kPSq2WiLIy%2B34JTtusqggx%2FR8Bp7jrRcm19hxZdI6vhGpRrluKwWMSn6EXhPnp5aOZMoUerkB8m1N3hBU6TtYFazYWttQpK1IUrxT8tK8MkPlGkV%2FH4PONCB5oKNeGmRngr4cgDJ8LYVohTd%2BElpiFJ%2FOQBb7ritC0qjk2wTb6Ndw9DyIsjdrWFWIDL%2Bzh7kpoFGhJ8hEUoA2cYMYIo70KGTf2c7Q6eW1wHOtOqKaBFM68RvalPwHfnnHe4lRJD9zCT%2BKPJBjqkAW4RM5F0LqLwwNTaHo1muVycs%2BLBhnXWcKDc0y6AzcGki38CYv%2BlMjm67LgWhepzqIInr9yO7j1sNcVS%2BQtVngKcJkUJxLf%2B6g%2BVT%2BL4%2F2xF0R4s3tctjfpW99EepPFqAHKTNc16iTRK98Lqln7CtUkHuOg8b65HXvxhHMsWxyN1lBcb3b1MQGU1vHqhgQF%2FMvSAgcLQAo1TfFlEFYleRQ8tmAWL&X-Amz-Signature=4ed54113502ef6347a6fdaafa9cb50a66caa61cb48e4077a9e18857300f66714&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







