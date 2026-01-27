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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW3EZDRI%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDEADAmGfclCeU4uEsLfzyMYhCHvH8xwN3BZHoLg6bAnAiBmFz9tra6qDXjNHDHVEIWzS4%2BNhRQxbS4xJJ03Ovm0wyr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMdkDQJ0xgB5b9ozHQKtwDI7jo5kvSsefqP1ZxGjZyIcpYYx%2F%2FdmmpmbEh2sAh6gldR0OK0LAbInEDDWrgxpVPAxb4i6wQ5GalZDaJ01dX0hdSC2B4vi4hMnO7uMNthuA%2FmxiTA4g5YTL1xyDlfoVFPg%2BDQaDarRbT%2B%2Fu4UDP%2Fmaki98SMko0dE92mr3wNd4Jx60xrx2Vx4Q55OyzG4z2m6VGV6qSD2oEyBqI58sZz6gX5ce0nRM00UqqnXw%2Bs1eZFdGiuehtjafRIfiY%2BpEMjdrTl935jIt5zC0bbIyJwKU1jVucvMYVHfco2c8GzDotVY77jMRe9hU3ZWmMNzwTkjU4VEfqG%2FPvCD%2FX8HU832uIWtDcY5SEtSKE2yqw4Twexg%2BiLpwf7jFZYi7VDqZ9RBYGUSNSCc45XwehHrG0YMppOWgoOLZRRy9idsffk0FhEdRgHQkh4aldA%2FD4QuK7%2BZdUAkFmVZ4uCTErZjseXpK00UdgoUeD5VOCOjN%2FO6oTLiZ03aATXTjcEe%2FwU8AauNqlWTiIiJy7pI3d4osSFimTcj41ELuxhbM1uJ1%2BeX5PFZdCg%2BdPeRVYeLboO3JpvgQOsGTR2T0RzmlqXWDXsdrzoAMCXGHOkNeqeHPsxZe1FUF4q9cw4EOiN2yYwpdLgywY6pgF4UySfmGEVlAx84tkX1kySJn6vbYEiSY8%2FcAWeoY51nSCtMZwZsF2OyB7q2EzCtiBtoTpz48zMRa9VSqZQpQ%2BJPe3h8YcsgPH4F5dcsldGRuvPx4Bdlibr%2FDOgb%2BWARw4hXsBUW9355m%2FGaSzwrAIMiTkVclB4y2dWsy%2FfN98zsNkFVmXfzh6BpJXbnDpLeZlXVn0y%2B%2FILDzgQ4ibr0zYPU6h4uvYG&X-Amz-Signature=05cb875c3f2d8ff8391bb20f06a5add647d76efe2e736da81cdffbf8fe599a87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



