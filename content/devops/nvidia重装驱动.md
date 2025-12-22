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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666V4KJNOB%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQC1U%2BCesDmqvR%2B65vexnYKq8tKTG7xTueBqTcI2EAdZJgIgfCNhIH8XMotc5dhql8HUF3VnBkf0wnV6mZx2vicgg6MqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHokVWVwLVggoN07CrcA5xIXTJQ4O0dj6g%2BSQmFArOEefr5iUuPtPzaaV3XEwh%2FBYkKaICFum9Vd5%2BUDiZTImgKBuOmVnoEWVaJXyO18GkYzuSy1NqjFddVQUduFqDTD9S72uV1aGigsbYRmXhQ1k%2BmCZ8YmVycb7%2FgYrHK%2BZ99TtGV%2FZLQXZ90M01jAbuI29Bg%2BKa6mKkrnzQ5pgNkKmZj9gr1Atl%2FGPykeo7xWyHNL2Kvj3D%2BgyRBepC5TvNw5rcCd5RZLRrz16IsLix4FbQfFSy1WLdZRFbyneF5FXnfwe%2B0q8OWMtRawmkB843VfAMxazWBJzHTQj17MQYu2PF%2Be4qeuM0ndfPspby%2FM9YUCOOga%2FOr8XyWA409B8jFzGpw7e2NrGzUS5SpIcqpcCKuq58M40ZzqftCHsFPJtoHLxXjO%2F1C0T%2F%2FTfp28IINn6Kkll8EuDgYXxeai%2B%2FeMH65v%2B4loegsLVkfAx7V16pslHvnUz2cvaFb7hUMWLcZGBL6DI4olEiaPR9s%2BlssTvLdcmt%2FEdktMo0kmbzR%2F%2FwYWmlQjwBcsO1qroVAtFR5l6TCW9c8CGBcHr%2BG3DYriCmzntIDFULmiqnpt3oBkFPpD2wTW3UNxKG1EVbKfxwCbZTUdeFlBqn%2F8jQEMN3kosoGOqUB5LTWis1hoXoWdwXVRzhrfbIwr7AO3%2FqDo%2F%2BSZIaL99KYH8BVIUFibQJFeUKxy8m%2FBHaBEIGzcxuYLhEuRPgH%2FEbI2AKrDHD3HyfHV4QbjjBHuwRMPt3RzSOk5o7Jtw5RypkAOaeJXW83aVZcTAhYrgwAEM%2FBMz5%2F7lvYv18AjK4JhGUVrwzcQhc9oL3uzlcCbgd9eXJn7%2Fd%2FSxwhRIj786Y8%2Bd5G&X-Amz-Signature=4d0aa5bcf993ca3b794cf23ec163f1f654b17ab6fba3a66a0937da78eb4edeb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



