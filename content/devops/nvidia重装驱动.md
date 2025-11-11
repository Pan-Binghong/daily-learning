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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677XH22GD%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQD1sPb5GB8%2BSGPZ3niatZR5RTzZhYb5oU20zShO29f9dwIgC%2BB1svACAEP81%2FGiVoJMNOpwKEu0wCO9%2BlRFpYFhcd8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDBS60uFwqH%2BL2N5JfircA2SaFfjQNwbBtdVR79f7fzdiEZr2GSSN2CJaQyzuxnzPRUs4rDHWWg%2FzG8oWmPzhibzhJ%2Fa5JYhz8s031iorhplWYnHAyWcyu%2FhazzMMO%2FL4CLf7kaBjysgl85e6UItqnrIg6TZXvL5p2t6EopIgFLCmmcmOYFq0LgrFjFAGEDXpM%2Fmg0b700P3Gz4TxDJztt%2FNX1IxTpqNJhUliLRoFPdZ4YkKsxEqD7%2B02uC2u0%2FHNSrQB60NNIK2Cw3R%2FnF998p4c4Vdhtjh63iMi6EgeZcHOkDJ96oQrMjYliM2NoqKKC2%2BWJlg0C%2Fungh93%2BOTMEE7L0Qf5SzbL8yNm4qUH%2FKstaO25CNpbwgAmk6rZICW48Gur7Csq3zGOHg40z5xVT0JpLi4IDCGCc8879VZsSljssm8EcXWE9rgFh3VtG92C%2BLzt6ovbi39S5MlV3QQowSVyD5YYJ3xTR6jbKwmnWtoEtwZ4KR1r%2B0B8YRYd1fl2995G%2BN5B16YU0PpdTiYZ%2BeKX6BAdPNz3is5kfNUpOddJ7tTx9zJfuabeoSaRAEabWOKnk388u9BCqYY3PWh2CYs%2F524tRZtt4%2F1gpumYX7qHjkO0jv2k4tQdneHO3nUn%2FHsAcqBvwJ%2FkY8mPMKW9ysgGOqUBTIoNptomtZk1jer%2FqV%2FIxTz8wokbICiSICdVTGV9QnycJ%2FVI40Y5o4NLMftxa0leaSyv3U0xVXD8sOkAUs%2Bz8I0TeoRe8IulYOrP%2Fk2hE2Qz46tSHnE37jxreBkUFNeZAbSxqOBtS5DO9cnfVPvQQv56itBaDveFF%2FY8bHlMsSNNYTjIAt5Ic7AzRUD6F1enusdm2Ea5O6cEEOR40ErIapsLFL%2Fp&X-Amz-Signature=afe648ee718b1c09057f174f1437d0c21ba8640903cfd8badbbf53ce40f50bd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







