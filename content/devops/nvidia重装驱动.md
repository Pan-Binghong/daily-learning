---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRQ6KRT2%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGazuNy56D61k4C1uygxUV%2B6DSvfldqt1JXL1Y%2FlyaXBAiEA0INPPuB6jmQshWGto%2B2C3ZVtI1Ttf1tJq3dUHxKfN9AqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOvac4p8deLIxA45VyrcA1gOe4qCA01W8PQdzDTsSKlLhxT3I4e4OSeWMgNj13DAw8z0pf%2BRzFDPxTyyo191jJ%2F5dWdGTM5slwQqBdrq9DE3izEr7g8L52WlZlHULZuZtm36sYSZHNspXhhCYFfcbKmUeyohNX0rrKsQPUGKPzrPLzWYmE6CP4JfEopobXbTiW%2BcPQiU54uIuB8ELATMX3Zn7IFkDNSub9TQ6pIBzAPGg7P22aN6hfUiotqcs6n0CNLOb4373eakUMK3XgKPY%2B7fPnT71pd0jY2o%2F70JFhngdB2gLqxdIhUZwr%2BJ9IF4n48W5A0GBSjSQgkIJ%2Bf9mUWgIE4SEVN5pwuQ6khWT9BWE9HBQ2HPBP6Gq16RyAoZuEsFKKI4b61VyApgaCagn%2FgGR0BpPUu7j13GeJDvyUQB48WMVoH2D32i3aHvgdJ7a3kwVrN3esdwNsLPQLOZeTKD86PdaZqbfy9GU9qrNkaCk9nAdzP9qByInUSYU7Ky5WIZloaAoEkbA77oaKMwYcSvTk%2FPoOBvRwG876G532OOSuuhMvXmNca0CcfzNeyzXhgNLLEceH%2BLnCRF3xGmsNhzu14%2BFBDxaeQreWrwCpuxM%2FvN6JQbqsDemAJUvrv5hUnZ0ljH2C68ZikEMNeirMgGOqUB5iOdFrMccfHpwI8QjwKvrqbSyKAU%2B9PqYnPVNqQ5TgojWgc6vi9CkU5vBwftX%2FWvoftheePozoksmlK7OnJ8XbwHUcpGseTurOWIY%2Bg9yAE6aIYjIbcVASj0ldbvPWImIIf8k95%2FR0CHNZNfxUxrB%2By%2BDu%2FhUGXIIxt1VRXisQKVzdLJVZp0CE5VuzYuJID564wUmOEviLOH%2FhhvC0D9DTFpdt0d&X-Amz-Signature=5d2b88d5c78509ef380baa575fb45fa09eba97fe12ca761e52790c08517330e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







