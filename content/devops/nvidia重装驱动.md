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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X532XBG2%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKmyWdH7v8ciN6jfZgt5l8SmDgflaWjJwvmPl%2FlkuY7QIgCbEtx2jLd%2F0r1qfvKAJ1jtTvGUWLUQcjFwmws4BaFQQqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM8Nbn%2FfH1C%2BlkBrqyrcA0hjixuYzDyuivo%2F6rxfQuBPw7sR1wEKTnnLu%2FvS4ZvjJ5fNCeO6%2FdQur4CIXxxPNgnTBQHi1Ylfc7MH8dftYImMsSBomPPmJXRLxF%2BJIEeBhRi5Q5%2FsZCeFfOaTgVf0CimjGdfLXlba8BDREhj8rdF433aQZuQqcVi0TJeiG%2FRAYtiljLQ6jO4LfZn4CM4OXH8Jps%2BRsSdkEaVmL90vtqm26uja2CuWDum5Dvgf5rgGoT%2FTTO9Rh2LqblWiEZMigKQppG6F9bC5fYRgT7%2BpFeJVQZLMyoFYlMsGx4LCHrdyXkzAm6tUxd9j8LjUsjPS4Gas%2BHjJqeuPoO1Cdg1PNnd6G06Ey9%2FkXMioAMvdBq2vjbPh25Au5JRBkIpK51cs527joKC3OYFEn2YsiaZ037BglB2qrS6pUlJJ%2Fe5RR7s0Ku9tyFHXroCbZAp4IPKdx%2BaKN%2F3JpXSjEjTAkAZdL1nGm%2BSiHCVgk7r1ScOeqIEHW6LB1jsXEZBHak3dGboW5IYFz%2Bqy4jsnSeQiJv%2BPK3MtVzWjvZDL5RbR4ll8NkB8%2BWGaeySW73hcQ7Y%2Bd%2BUXYexBRcoWmFThu79%2Fb8aZfW%2FyLLSD4%2BodcxR6zNXnFeB%2BD7hutVJVZihf4JECML%2BC080GOqUBvNuJ%2FFRuDZSw7n0slYLwgNlpc6rkLysitGSyPmqHQX0UPXODGu0KmhkWNENeur38XKGLaZjYtw3CU46kTmfdGErjSfqRi1x9VBcNnkCvST3xwqUh%2BNnYBTe%2FoNE7z8VfGdWNiafKbNq7hSZPqQ3JJn8sctRIMapG8kD5%2BtyU%2F1%2BdCuMaXOnoGNDaViWQj2vQcBcWAW%2Fw5%2BldiFcBn3ufcfd4ewnv&X-Amz-Signature=66f3e4d9701a7fef7bc5ae7cada55544125c78c825f8edcd5b66f78c0f05d0fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



