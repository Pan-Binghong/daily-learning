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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662E3FFU67%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDAnyeJwIj%2Bv5qIxFtJNXun3IRLCXjUYltygOsvHWb97wIgaK8jlGTXXxNtiBU8KkDKazdo%2FJqY2KJ%2FHR1d8bzllIUqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvbV71PNIeJEXAz6CrcA1RvfjlW6MKpqw5VnzsW1PTOer7QJ0wWtu4TwvV65LRM0zdYposNa86zT7nWZFcJdJuyKp8L34ADaq3GpQ4M1sQuJ7suFuH0UUvSwRPh2ihAiTfuPEwNNn6H6qtdhqOPbKujGbmLzBGjxInTlyi7e9xxaVRdxxn34oAt21aNwf2VZ1aA%2FNgJ%2BYFWC3r50MTdYSKWV%2Ft8b4zIPHsflFROar%2ByJT6Vh4cSE7K6i3sHajom24CuyiXbacIDBOaX%2FUQnM3afpTeg4qXBYa8okKFA3bakdbr%2FuChRdZTi1W1Oh82PBhEGdIdvR8ahBYlBTwIvuJsNEkdIRC674gXsPwiZ7dbq722sKbXVvX1TkbKaIMYddtEK5n2brV1CHn6t592zvbeGgy4WM7%2B7CFIHobByt5fxmDyEc838CSRXslLT9oOmdAsURb1EdqnyqXSC5WL1nTFapLbiGqeZ4fRk1NS%2B8%2FED2i47pIk4VmIT1A9iFDXXgr%2B5R9SnmXUdAN3Md2F3rUg%2F2hPMie7WFEoAVbJYJKiiLoK8VXKu8fv2%2BDNt5fl6QpkGLHVJW1aNw%2BFcIZpww%2BeuIoEgBtcqeT2oMPNHsTGDXiHg0Vtql8vvgbR7GgHqNJO4otfkgqDDQjyNMJrsnM4GOqUBD6oO3qaIdsJ7TRoB8CXmo1P4aGNGrBU06qWJkzB0UaaWxDFyhR9zuF0%2FikKflcQtG0B4%2BKPJPpwx4nWBngLAm9YKE3sxF10QPJVSFyu%2F5dbNOv7FrRaizdhFx6qNZgYs4vV3VOeL0qp%2BZzSqwj8scuR0OUim%2BQ%2BS%2FrlVtcsz30WgWBizZ4Io%2BMgLis%2BSffZgu5ttwQNqTnvUvz2JMx4K8661GGoB&X-Amz-Signature=2b7b54bf8fc81dad00ff3744be6c1f081285f66e6238cfaabb9ffb72ba993b65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



