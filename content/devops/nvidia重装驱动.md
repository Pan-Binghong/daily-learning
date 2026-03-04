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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XZYZM23%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2b1P7b5hsBKVmUx%2FupqwWe9mSIwzmEPXQOMjBLGdviAIgXT78EqPdNGRSOjo78fvCJXK0RYoIajf9tOV%2FUnx07QcqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFGln3985GYUq73rGircAzjaRBfGnXITq8NxxtPeASDK6SiJA9BMBrcLn4eq98xHBpr3YsDOi5lUyBZZJrn7HrL4H1HJit42%2F0NIqI9vVvxJoCf4jgUF559ofNcZmugNd1N2745Hdu0ZLcjsNb7FoIgVaxRhSB1BEXPVgBPz6M%2Bn4pFKDzmoXiwyf%2B4o%2BWCv%2BnSIzP8IjHbpUmHASzbejNN7VBct0wiqh%2BZTOfN3KMyBFJiK9IgWuXuhCkMaf3bTANtRM4yio3F9qtm1qBoruhpdZw1LIpH8uMS2Y%2FVYlW91qKoT8fYmSFnppl%2Bwmkr5FfkmXN3dvAkx%2BdB33kv56%2B1ocg6%2F0OMxdIX%2FULqeqZeqpDvVKH4WG8lz88BomHUjoBRnrWkUDEfkauelssKgwiTMcKwmUYob0igGePQuUaQ8ViYwULM2UuiQw48NgXdH7pd%2BqMgEX6mivkc4%2BDMEqXZosBV9kirMBKhfMkE8koDpUVyNwCyr4FEvMkRWAzYxSEj%2B8dXU4ob9Ji%2FoTv56jkqhQzamZezrzWOl17WXZCqmcV7aUmbYYigQynEA1mAyf4n5bIT0OM8SjnKO2bfdN40jzdbIyKCDa6OD8aQHYk%2BtJsMRlMfzOUsXYPFtuG55fST0f73rGi1oiuwpMKCYns0GOqUBwyb2qlefArWdVtEiGaoeAsjnhj0uoFBsd92wTsp70zFap0M8GmZYb76aHCkZ9yuFBJMUCCMtFDRWElfC6MCwNlcQXeweE8NF7V3F5MznKcP76PjrYIAeWvq2ZYnqoccItgZwm%2F8my6ejbl3SMMXNKZwMVEG3ruSGwT%2BXBiTO2g4e%2FJZCcgllLTG25gO%2Fs4fnX3a9ETFLBrJ200daVjjhPiGr6Pjs&X-Amz-Signature=a84b9d0390f07b018d2971c58d658c5e21d3e16bc8e732bf755e81755696dab1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



