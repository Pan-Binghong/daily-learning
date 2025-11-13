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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FTCFBIJ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDCdGvkj%2FN6wPBgcd6TM%2BLOst5HR%2BTdGDnvuZvKnaqEcQIhAOO8IxjEz2YC7M25pg2ZZ9vJkkxzjvoCJly%2FP3ePrQsBKv8DCEMQABoMNjM3NDIzMTgzODA1Igzz3oo5paa2XEnctHwq3AOj4ULKEVUUpPWCTydL7ybuInpacMgYElEgYy8GMgsam%2FDgEbOkCLCRlFnBBplTLjxaFUwV3LhFQVpRghY1%2FRBDzM6HXwu5Dxxe%2B59%2F5vV76ZyKJrY6xT6KN6kOWSyp%2BOL1NOi5Yj4rqjy%2F7dPbwz9Bnr7Ii4L7sk7AtNMI62W4jjzop%2FK%2FXHE4R%2BQhRUoAzRoBsyV8QQCMkYun8BpTSs0r2Rr19%2F2EYFpksS%2Fx0AF0uJ48vPCsqtIph9AjjkmXlRBAGY12NQceBWkveidY71TvQ1UAtheMQyleaXYMoTxmlNIZiakGxOQKnwG%2F1MVN8j7n7Q6Y6au1ZnMQc3EkTX5SG%2BTFoGbPSonRTSGF%2F9wiu00VOWpsaFz%2FIfpev%2BjOEEf1scDUxUDsY97DUsLWmBEd7DUtE%2Bu%2FJTggY3WR4ltiAl55HA9SZ9%2BCFWdjlgpf19wSxkervJplUbJ3MER9AOBRwnW3LzVi9pHAmEkbk2NrW9VkInirMVbvyrZCEajIHTGHQt0DlA42JF4qSJpraGKy86DIjyNFi0YVUAjrxY2xMvLLCQ2UsMfrRDJVOKbYqQHvOTO%2BPTyopt6iXK0MvlfqVbanhNjroKXT%2BfZ48plRp48AKVcHxm3lSnlv3DD979TIBjqkAQ6qyWWgxqmtz7mW6YfNCjxCDq3B6C3WmM%2FMeJoaCvXeyyUGibHgf9qMeYyc%2F5S3DZN%2FGNbxe%2BlkOkvkjydyXYcpfGp8RQbG5Cjqr%2BtOAKe%2FOBKcetRcrOz%2BOjcQathHrCimRUFbPGJSdy%2F7WU4KQ9ZRyvioBNP3PFpcH49zFCmdXpOhGD%2FooU7uL6NiENAukDwH%2FChkDcDiwNxmIZGMFFHeUgqp&X-Amz-Signature=9b3ff02127f5ebc95f93fecab6b2d06dcfd0b362f00abb34224c138a4d92f55c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







