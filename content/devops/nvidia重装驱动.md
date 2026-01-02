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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NIWIYIA%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJGMEQCICmEciyQ028UH8l%2F0SXuO7ugeZtK%2BbdUISG6o1cNTnbeAiADGmBce7Q8OhrUVkX06wutSl1w1fR1V%2BpZ%2BdTw%2BtgF9iqIBAjx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1fKrKZ5NOjloaYi3KtwD92W%2F7cA95MqVn4F1R76G0jkw9ront5ydx%2FEUx51M%2B%2F%2B1mByqcZ94c3r8UCWkhTBcWVp4nYlv4SeQRzhvFcsXyiJQQZIfXP6mSSoZdu6vT8iv9FCziR%2FY%2BF%2FJvkigHSA%2FY2RHnTaLJYUI%2F2p8J4sB0uqK7tuv3JqKEWa5HHsQkiMq2%2BR7AopUeTzV17exV9%2F1VIOmpwmxtU150gOB0emetLBt1hjAufSxVNHu95Q6tKSrHUR%2FfuKaRhGBlexrskOyOQc5O4P2ZnvzU7zOm%2F47i8%2BXDhzQjuiJMfxlf158tltKHGvuY5Hq92hw4A%2Fsl0P8ZOTg6KOjHeIVAVkhKxvmnOYUOrBOjsDmCGvbgpcPfbhpIp9GCe9Y3v%2FB48x5hoOUtwtpGMqCsxYI9NRsNEUL6zQaoQETrpkorXyyEOZ13j1Vn3Z6RYIWy7uUOSWSqLDVyrgLTuvNiaZT3djnFQtVGuxXcO%2Fe4D3N9%2Bi1Uv4ncBNvDiqwhr1XKNXIkj8PyrLk289Ay9Aeieoma0JuwYYV68yq0vbvWKgf37rU%2F1ycCUO70SmuwSatWu3YoTf0aY6auXBiKBxrE98iOYyjaRTnl7LTP60CUkrqcfrttVFEc3VNP%2F0zAtu%2F5KfgnYcw3ZvcygY6pgEjVPMHI3nUvoj6qBzA7vwCrQY1nIk%2Fce2g49%2FiB5laeA47ZPTidAgwqPNumsx4fRVX1x6B0Uy8rshqIrOwk%2BBpXBQlJW4dk79tv8eVpfdYuwFRGIWdeanqE%2Fwx%2B%2BmLKS3aZ2Swt0xkS6y9cLDd%2FJm5xBl3358RNhH1QrEstQwJqT3WpdvIVL35CMdWsnGQfmWIwwn20KMVQS6sFfwnwiWl3%2B2yXa%2B7&X-Amz-Signature=444468da1cc41ef00cc64add48a52c4677e13d5af3a068fc929021fa8182b1aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



