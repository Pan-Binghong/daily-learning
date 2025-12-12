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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KYCIEGI%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQC0jrUmWJ%2FYlWCyPaiWbqRmny9lnGsFX7QEbolci708zQIhAL6nT%2BBnCQkbmD6MNAM711rYp1EYZC6kq%2FhPg4JafdEdKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwIMj6CS3aVCuujYu0q3AOu2QiDfnoBAGaX0efV57P6DbUzPeUkvNsSvDlkmjaghk3TcAJntSiJLdPgPAm2NFSr%2B2DZIyO83o0YeuuhcOEiJ3%2BSlTDxmA97iu5M7ymeqeyUiJ6y4XGYv490m3nOtSUKXl94l6xiNpOji5MV2huKrcLooj3zZ1nBCKzQVZT3bUI18aWtd8ilxRdFhzVSTeNsUaNKEHs1XiazNrkwBu%2Fs1L4eYgw0dkDFYWW%2BACb2O96a8Z8H%2BJLX%2FMPo2x1U7vISSE0%2F8YVCeekgRL4P%2FvSzfkBwCgX%2BlpU4GQHbMxZSfNHpyJb6mEi%2FsdR2z2acMRrPBMiz68XxD%2FdonE%2FTO%2FpA4geb1h9VOeDnfPCQZIRXs1tVzuT8S4BzDcDV69oZ4UaOAY87ZNwyXgZD5rQNbuPuUgD%2BzpSzfUy96cRTHletIeepN%2Fp%2BA3LC7O9DLJtLe0A1E%2BHAkyD%2BgrK7AomV1D6LBPKsX%2Fh0vRoPCluKeQgshvrfDpLWtxfnuTuKb%2BRlsDtLsG0VhM2xvuzOlwrTtkfCqupYUat35LP2bzNZbONfw3d2duKfPH%2BS8F7ZCqOuwdwSs3610s6WdO97fDmPKCpGSvtqk1esaialXOyVm86NVU3zqVrCjDCE00RLxzD01O3JBjqkAd5PUPKwrm3tWz0LZeRVF8C%2FFCt7Mymod08eBERExSlsdsjR4bEmYvUY5MPHujvKzVSsDQsWnHmpPeSUfDr1MaUVvHdeez1M7eF%2BJo2XYPpMJxFzYUhp4MOJWC60KkN2LxAj46gf5x6gkvzv3bbXdn8jnDn19K2%2BKOe900m%2Bf%2F2vASqicAzt9abu0%2FGdbdOYEe5MSwNRr4h3YzMvDuXPdx0%2FFWtn&X-Amz-Signature=4d363026198cdb3688fbfd868290abf30a61fed62f0f59d740399710923376fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



