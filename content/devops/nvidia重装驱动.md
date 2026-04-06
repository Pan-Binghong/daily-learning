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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UYMOF5Q%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T041147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHK0v7QBabOJJJPp5ricOCuc2k6z5Mk4KzTQq8QHqmjAiAXC4GoZeTg54H3IvKk7me786Ve01QJiWqXXDirpPrFqiqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMubJ4MmZQ1YIwTc%2BHKtwDj4cX%2FlNPPjzQL20%2BKhEc%2B93A2GTQAyxThSuQSNKEpiP0shBnk%2Fp2P9bcjVWEPsu5i2xw7IzCcX7RxAoZ5UkEgYL9bc%2FxsSPyk3zfNkTsyo96R%2FHhgriWJwmNqxuVElUh9l0xBm7PEqNkoycnlZDI2FXxG7l2T6zqWCt9emY3SGjsH8TrcBl1iZ4O2dyg%2FlF3jIFwkS7Nx3Axyw028My2e4iC7JGPg3txI7guRRLSiIEv%2B9C2Wwvr%2FIXo75JXRzYRI%2BdDG5eQRX5jK1cJjwZCX3LGx23fY8JYlk%2FOVzEGRt5W9KynDhxPY7Pz2O5T8yr1ywNC1yFIrccOEvKA6Mkkm2z1lNXEKYLahbF0zZrWNIRBxpI9n%2BiK9qb%2F3C3WZmk6Qt%2BcEmLx%2FxNvw6rarrgqU%2F8l%2FYL7f8dTwA%2BnWRaIYJuO4TKp5bTeox7ULmelBXNXcloMHdNwurNi%2BR8szZQUjn1Yda6GAx31w5zRT2v3PNGOWpiHNesHwToZrGiyTUSb7iNJV1tMdU2TM6cR6C%2FL2Ee%2FJlAu0MIJvbtBi8nPkLGXDCHM3PSABdGoiRp3Y2F8K1Exdddyn0lf96flVyqnZZ436gFLdukemDgE5sqcjWXR4wQ3nbAgRpdvD48wvrHMzgY6pgESE5RmocxU0xY1CL4ZVMw%2B5UMIaghlQFCBLWF180Yas157qmQ6204%2BL%2F8hrJXSffgXxpMlLdKG2zqx0Jy2WUo5vcPx83UPZ5N5eJcntftigvQpp7vzHWIlYKzl1DPlk9Ra3aBhdGAjRnHUZxkDCOAuf%2FUfICcP4HamGAJC2kcGuqI19OGZTkx567XZHcLn88M3K6jZdxwZ7vlMgFqo2XzTIxvTWdNt&X-Amz-Signature=febab18b49d76889ebfb1a868c22728146ccd5e5b7dadbfbc6bf15f2ea81079c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



