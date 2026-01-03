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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEQEQUKS%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIC6y5vDxMqot9RyyL0E2OlBZHcLPMFl2fXL3ShDktfSCAiAv9katCmOFUgWvTBJwBHdyp7o9y%2BXZSL19umjQRhFYOyr%2FAwgHEAAaDDYzNzQyMzE4MzgwNSIMfkm4ETNZb%2BI3qfg8KtwDKvWG2F1Kex9FYuINENGpFMlHUEv0o8cq8PzuuyShn3Sk1Hxkib9vhzEyECbghfkgZQlTH3IEvxILAdw3Z%2B9M7EbOKFmqohKDpnfDwh2ZDJS1A1OttiKw064qr%2FAogx8gqR7hwZ1t3ODaTx82XlbRAivEgCtI9cBlCFh2ISR4dydUtmnVcljr%2Ftq7dl4FumBwnyn6fJ7V9uyegV2JRBj4W%2BbzYYxqmiHJuDG8nAy2EqmrMFjLjsQAGJV5yKOFqR2OabeX%2BZTPL1f%2FDwJEIaBwkvu%2BLBSiEF0%2B%2FXKgyB%2BLpgskch0xeQAoIF5GNmu%2Fzt9r%2BBTdzxzKQzQI4yjMoZTWw5ESRa4JUrKLqNmYLvb0Xl7CLRJfupIpyGwkuGKfDDJUPXGjy011cYB8SffizFedcfZoAniMSX4teCQ2%2BCBzEA%2FvQpkrTtCFP6UyAF0l7gHFcXO7Y%2Fw6z%2F1ipKF0Bm8D%2F11dEa4pNbIjbMq%2FN6WtTfRkJvyNt9xN%2F7ABsY4ool46qliRCWAhQpEKTxtb9PlCC7pQrnrx75QvlCrTSIdJNDV7VGi4jebvL7XxVfFvza%2FFxxf%2FjfmmO5Ru9ktlst%2BsJw%2FEojh8yUt2ScU75uLmKOyyveYDbETkLnrsNecw5P7gygY6pgFT1onbZimtmk0KlMUBSPjtaUEaZC7P2IVPdMx%2BiNy6wEnEW50F5PGq6465vKed47biDA8p2Lzs4hn1WgVPOU8gh1Wjr69akJdxZHth%2FXbAQpV8oYwyWTe8X8bYGVqahNZKH7L2Ta21YUp4q8CvL2V09fsyMhfs0WEDrvdCtCnE99gThNP8dC6pH4Xu7T9Yn5AAasaWjBKeCzMijEnkVeqV58uEnSAh&X-Amz-Signature=40e55909006ce4ed8d6119cc1b41b9264cdb0a10958964101441eeeb0880b449&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



