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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZN2H4I6M%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041201Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCID2ePnodssSW5nhqleBCHexlOw53b%2Btg7IMSOj592i0aAiBVXkA7szHExGQ7nff2vYdLgx%2FpcTdhvqFWYMvSYqn2sir%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMpYK6%2FQahE98RKi3wKtwDZAt5U1MV7bjfNsfV25dmksZzY11gjXe3OWSlmq92fKIO%2Fa0tr%2FKDIFDtJKvdCBhOKYK7S%2FwQoZTX4W0YTzVb7oxsFZoPcqqF6FIjhLgrXlOu0r8CJsltlmBDtrfjXHFOCyA2UvdTlXTUs3lHIpEEIUh1U07qrByPuAZ66KuAZ5pcQ3fIUcLInQxzKc1pHm2t7GV61COTpCkJ8qTd%2FDdbCcMYnZTarVOC2svy705XQj8AqTDNJoLl22cRVR9rj%2B3S7OyqhUMXzlb%2BbZGq21rSS5MJWfCM5UriOf%2Fqxr4oss%2BbggTbY8i9B7w6%2FcIR4nGkmdJhwK%2BX0lMwjNGLqaKeKnVPu7iVk0WRANQe6Wi%2FBEXdahW3sQ33j%2B8mKhDfipunMSXuqLsTHhDnbCV9hWGFrC7RZdZZIvXaUTPY%2FnEx1sZPNeOgLGYqDO%2Bdm1CINMP5BeyZhqzLgR3sL6azwJxBTsdq4lx3L9a8QLPp03U54XyqzCVlBMQU0H4xR2g2DYTfsZFDfkp0xMZarIg5Y%2B%2BSUkHx022GIQFPkHkAvdOjo9bCHekiiCzF4sI4zxG3ZJ5HQyALCR4r%2FpNzQhbje%2FOs167UQmgUeux8rIHsqhCZBAibttfzxkKjng%2F%2Fc5cw4senzgY6pgEwg7ij6ZhAM7Y%2BUom3ydd3hM7NJad0scIEHgHFgHAl4BL3WsmKvji9nrbO%2BwuP%2Bhe8jyJ1SB6IYTmbCOYYTVUajhmWRkcWph6UjvQwaCb4NA51jhA3yR0egJReAoedvwe27kBDA7AKAITfgBjhiivUoIE4a3UZAUJT83QOm6IlPdsUgTae9JEzXsDaoFv7cu67BYXUnFb5bZY3Tal6DTuq0lrbW6AW&X-Amz-Signature=6a2298440c0f2bb621674dfd6c246a4fd167dbc5c8cac06c23a156330d1bfb0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



