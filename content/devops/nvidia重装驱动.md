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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URDQ2XTJ%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnoS8fAFvDDxOf2IeZO4tF04D%2Bu1SGTCgjNdhx1kJg9AiBBYMI7Yh%2Fc5MLtulFzS7XRJxySuj2BsV2XIcM906x1wiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMsyd2N%2FUI0doVSIpKtwD%2BOdcJWB8Fc5jA8jAJifMtp9KuxYiQ4YRGGZUx6rvQQRX4%2FC0NAvrutnfQnV%2BicQ%2FqThhITKxFRhiDgfL5O9ihzRht4M%2FpH2Oowa2xvv9P4MgbUFbzeeIRCs%2FsHrG27foQ%2BOYqjpW7gkzRNpgBeoTinCznIcu55j5p2gXnMS0xKYWzoeb%2FHX%2BGTfjopqROv2%2B2DDX4k80jSEZqGQJIDVQPHhFtscWZFi5%2Fq9hH7SchbszACKrF8so4f8K9JkvCWky5EodNILcuvy38o3DqjKcWfGvf4DWhBP%2BAmppde5JC0spWgE5QtU5YNC2B4gSHq29DyIPiHXNj2Ig2KdFI4%2FD8UAsjQ%2FN47D%2BkRynIsWmSw5wH4EJCtab1MNB1jt9iifzCMQubqmj4GJpJhEKY73CQyBGbGw0N9ziuv12fhhzNgFWrbcsvYXlkikvntcMkQL8ZctaV4PMXb99wbilzV53NjgdksyXzHV9KnJ9tPzaixR59beHUGFWpmaQXKYXWaZUR0xt6450TL0vn5w99bRarphELX1aoa%2Fh92gBT2B50WHOIcqTjuwwMFWKVVAHDxRyjTUYzOzpT7%2Bs2Te00me%2B2%2BiFIy151z8KAypGcyXPMPfhg6MOCdMBsJLeuTYwydXMygY6pgFfYvWV1WhHUWC2xe9X%2FP%2FkP4PWCp3Qj0B7xHLawch4MlmeyUrqVVg%2FREY1xhTxDJJRNUoPF9ppwND%2F220%2FXwZpwShl9Pf1Y5ZJiNvUSV3HfwA%2BqVgkWsyd64JOJsZ1d7BG5igdpSkPJ2n%2Ffapx%2FolitfHYo%2FQVusATRbcqNfr6pQW6aHOf1KSungdY8wFmlbP%2BtxrLDCizFoZVaHFzd9jaIFDpw4Ie&X-Amz-Signature=65cf66fd4c2f9385bae1e09bd1f4e4df57848198e54e32bf39e485a493d78201&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



