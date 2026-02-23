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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TFSECYO%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDsdFydfT%2FATP1Y3Siyj64h8UGksLCqeVvwpmgy6ElU%2FwIgXjpkSRSLjmeAjPEFstlOmd2b64%2BRf47QeFu4WcKEvmQqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDADfjXtsgJHXO5u6yrcAwa0K0U22WleE1EHE%2F225wUXqOPdnmiJp5XZ%2FE%2BTszzBpkvLUeqXYEjxCcl%2BB5vbtYYIz%2FMiYJxNg%2BwX2IaGk6k%2Fxj7jjSFmWswfUNH1GH9Cql7970iqcLWulNYQ2f7VRTHTLYEdClfVLn7YFZml4Qq%2B%2F0jHTU76pVVUxk5U0BVtusowPmQQvtRUONmGeq9vzyQilVf3YaT%2Fm0P0%2BarTu2tCkLXO8W1BD7TrO%2FnqtzKIkY0odnoCuoh34q%2BYJen38SF630103qFM5Xv2SSD%2FfHjpyJJcfcO5X5T60lnSupHHHrD%2BS3V02vTfrmQmoss6xWNEKggE6ZZYUILAnSqQV79Ds4yHYS1T8vcTXEKzeHNwF%2FZA6JsaUqImidIhHrKCcE8Xe4uvpygBnuPYH65cL1SkcOmxbi7LgEU9tBgdMeC8yvfzF%2FAg0RaoXRGS0F0PD4rplOYdKhs2US%2B9AXO7WBwpefFjhkttHfJgsrGlJaarvM0XVu1HbkjnjWW8l0XY91zmEF3x1uJrE9z5TnlzHNuhCiZqdBKXxDhoKrdXtJcIS63mEekegv1ZPbOODzleXuynuHEUIfEXoU5oVgEUs5q%2Fwve4G3LU4a3EIoLU%2Bqv6gunYUkW1pMWy1nrTMKmU78wGOqUBNYezrZzWG1AyVxrIotyHIMgVwpzMHRMChVz1CIhqf202UvQ6DTEwDESB21R3ISjgaXkYsT2d9t0hw7g7y%2BRrwMhrg3vOxQKyqiKcZS1XYvzTsvGj423qvnkECIlodwa3YiYv9BY8rc7EoODggo7AwLJrHJZshy7yl4yHgCdaJh5gkxsdt%2Fk7XPHO2xgcVU%2FKezRJpm6QUdrbdZpCCuC17rxRAZv3&X-Amz-Signature=74a891cc8efd719319660d9cdd854d966bdc3065972322e7854abda17705e923&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



