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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDFSB3UK%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIAwGFD6v8%2Fzkt86k16hKfodzKCUApU8G7Jz4noorTaRWAiEAkTU8EWbKE3D72ihoE2K00OMsiNW1740VVYUkw75xdwEqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfKQWt10MMM1UJ%2FPyrcA8GFQ36G6rv%2BX6ezrHjKW1PBlnlpacUU6wO7Y2NtmkRM%2BPWQB6lRs9eykssWo%2B6PgXAcLPoMr5Oc3y0ZRPKuYkltdaNO4IY2rMKnO2kMIy78cDFTTdu7S3jKH2qCkPoboEHtkqiVXuQKysNRzPF0P%2FfziPIKqknZfewMMKy5vp9YbZBW1xcOfwEMWCOae3OEIh%2Ftrj4NGKS347lXNF15TMjCON%2BjGtUqiIhmdfll4yJ9tdrGHmQGa8f%2B7FBf7oRZFSqRnwn3n1y64RDOsBXEMDti5ACF2WRK32TG%2Fq%2BdB8r4WcgmR0X93LhyR2GQueLy09knGl48L%2FrIcrMB%2F22TX6m7YkXkcV8ME6Vk1pCqPcEPCA7dSyBqi%2FZ%2Bp1eXC8kVw75hBNDzsVRd%2Fkt11fCyCQF00eB1YNIB65RmzfVvLX7DD%2BF%2B4rOqiDo7fzrwemVwmlzVd%2Bcjh4q37X5JMgld4%2Fng9P2s%2BZPngB224uujPmgRlvH8mYEdRouQ2fwmUMM7W6qpNSuB3v1ePvRkoQQRgnMNzJ9qPSP7OcRdp%2FLf8Oum3x768%2BqDJzfDYHPqt7twQmf1TJC2ORvnRLxBnldUjqvjJLs9t5pICH%2BoVrkfyrv0ucQ0XFsLIxxgZY0oMNu0xMgGOqUBXl8QWgFwwJ%2F%2Ffry3wLWewRhCjtSoG9Z2FRe6GRkwcBnfjIzodPKyLVHfVgNygmph3gUoWfOQP8rQAM2%2FWK7mZZSOvYIQoIX1V0oSqH8NLULsVA0H3%2FodwFuIojYYqhNfhosLcaqORupYZX%2BThAg6YQh0mct8TPgPONzX0Yfys5C2RtLZ2TswJFuYaQp6ie94HzJxDxrkbzqcqNNbrU%2BZt3Xe2jO9&X-Amz-Signature=8471a11af6bda7b5ad7ba6ffde1c71fd0fa658f6b8ef9f011111c08e8f7031b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







