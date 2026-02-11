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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKSRH2WL%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T035049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyQ3zkgu0ljl7yyDGkK8eii8wM02XeVbV9IIXMKYfGoAiBxPW2HkcT9%2B7BHAj%2F%2FFuYt%2BlGOsD6bDKkVNNHTcThI3SqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWGkhHFBnxWn%2FipuyKtwDCXvvcY6MUgDQpNXjAlx3srMHY4xlhmCzk8dDLLqk8admaoUJdwnwrMQhzKecLtqWgQ8jsxBrcY9%2FJwcEvlF8zdIJYDw74IdFxnBxGBc9yD7MP0xhh8aBDbkttSENO4VwSIq%2FISSqasa9aSeTCPwSwikXIWuPvcq9C1FvAzKLFkZrR3abfQRFl%2BFRsG2BbEP1U1eYR6PqDt5qgiJoFm6Zgob7M%2FLx22kRQ72gmoO%2FoTsjbfRZwLuV%2FHa5HSEpuGk7fPoTXP20RFOl50nklyK6MC%2FuNOo7zjQ7jcipH6lgtnUZQR%2BnADRZmusLjMYjh%2B0rO7NyK7kg1nb8N6m81aRq1xeHqde%2Fzwpl9ehwH%2B769lfLv6B6LKq6MhCmjt6iMekDjaGHfK2rUFQpv5cVNw50DJQkHgRS5vE2egNtfAusgKx6mD%2BLjmLoylddH7LibbGaiAk3pDCL9SroR8o7GXxwpztDvokpMoOY3YUeJfjardI4Gm8%2BkTK5yqlgpGOZ3rIGy0dnSUP8mtKRtAo7Q3FlqtADYiEi2Twk%2BtdL%2BiHgeLA0q3HkXv9wqL8W3oDx1yzE%2BLrD7sqjp5CfU3O%2BHi4oxAZqXSrQ37jnwuDsHX3541fIwVk1Coys8SJl%2FicwnsyvzAY6pgGiBgizwJOAP8XCBeU%2FbLjMo0bVKHmx8int3hXy47PkynjGFxY0XNVd4I5Tp43%2F9k1SrJ4X75s3xVG0ZEdJB%2Fba3b5TrjpEFoAfveFpGNjUpAdxulb4sjT3p7FwY83DLK0zCqOYkXYQaPkisOId4GacGRIDFwP7ff2xiTCKT0Pyq3TPkGMbuz1cW8ZqBkZ9CFRLRHA3L5k9%2Bf%2FtuS%2BAvh217GpuZZZB&X-Amz-Signature=3e0d09c8f1948ea267ed8416b6c0d1cdbbe1521c4fcd270ddd603dfe7d94d72e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



