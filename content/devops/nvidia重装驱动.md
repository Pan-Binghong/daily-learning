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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662TYUXGD%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCU2HRGE9SuZm5WDIVB0jsfft6Y0n8TLfp5s7LsXoDuCwIhANlOb%2FaDFW9Pv4aUhO7ww2U7jsYwa%2BA4E7bfaFSKFiFOKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7rTx1exRTgGAoGnkq3AO1Wwgk82bwpeoXpsic%2BQdIvADgaCLUqzDgw2rXUJo9q8miVtGo1o50%2FIswZ1I352ybZUyg1IzRnqKHqUGBjCM8L1RW6r2t922oW%2BwqMQ56FBIYcpKKNjj9Klz64AONOz%2FWqApeHv%2B3x8kUghqNtKOmq5VVrB8SMl0epIj6%2BBzc4zbN0k31BPD7pgDIjSnKjbA96RLIVenTzSgRKvWcvCbQ1P5pIjHsZxVdrK5xYr5lf8Owl7fiYG8wIwwgan4R%2FjMYUPz2KW8OiRv%2FR4wMM%2Bpc7HD%2BQYppBOej5KRy09RJHmjkJ34XgH2koFkB2cqlRh7o6aI%2FzsESJ4GpdDYTVjtGg%2FN39t2PCxPIXRqRm3Igl4a6t8N%2FprVpMGoxdDW3w3zPFf3%2FXTaBMJkppTuT6hmmRD25UTCkU%2BWj0tQ1jsNaOwxmlznRSiNysS6Lyx%2BYinswhMQwG4XUEkXbztfbqHdZtcNoOSWXU4skcgXsyZw9dlowiyN0G5PG8tw%2BW%2FYH0c4Q9lyNokENQFk7ujnI8yDoeJ2g9L%2B5WcnzgeBC1%2FOhXZt3NyNj6SpoWIsGcjCBxBsF5eDq4gM9slKatkgf7pLeauKAkNFnMvif8crY0EE8WvXmc8xXNYRXIIvCszDaoqzIBjqkAe8rIxXloeVpEnIEVMQcYaTx6TgFnFXca19BDhxhbBWgyvFh%2BoEMbg7djo8x0drXAzOB33qX7dLdg4K2IiXKxRTTndIGyAZv0AD%2BhH3EnDHmcvdvI2pXUixZmEja63JS1PNY%2FSqyVMUJ1UVcaVUmA2lgT%2FJcQKW60m2QAmdcz6%2FKQGS60mlElkAsWbV42oEkN9xNNYzC0uHz5xe57%2F4Z9%2BGFfbU9&X-Amz-Signature=290cc85fb3728f08e5557f424effe6ab29c96a038bc73a468368c5999e9e4559&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







