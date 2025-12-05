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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EVCXIHI%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHEgOsAASYxUg8WXXat8Z5pw35SBAy57wFdnFRlb0AtLAiEA2Ta80rVfd3D8aeACEClPKCPcqZ%2B%2BiQuW%2BUHHVIXx8Toq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDLZkGJ7MlBTmoqeZ4SrcAxWkilV78GLR2AwZpEWGDgM1LoJ3M0SVQnC1xvv4EeGbD0HiyDe7AjvXIuS56h5BB0PrqrQ6mpVch9nI7UFvxPP7gj91eZyEZ64eT8ziEQACqQ9%2BwwueXGjSvC1EPEf2Nh9fUI4%2BCZb6pex2H8c4YkpxorjjIhCI80UAFwObh6aQXSXlS5YoqGvhFVsdmd79klVQSxcxYVq167kFfWqqmqrPd8ahq1vjdYfHAtdyB1DrrXTCoMWeha2ucAG28JdNq%2FsRivKi6k6A7hl7S3xm8aqup4JjmMLORfzJY0FqdyptnnNEaTpBn%2FFd4P7mGWyR78Bbd9C4fhhBOrfscdGfyrxSIV9HwEoXsaqSvJ%2BZtZ%2F%2FAzk6MNsRFcOYQEEywc7f0a9yPt7UIpr4mUwYKkcBXa5rUEt5zW3IhMQwZzWZtVKSxE0HOjgLNpDZUyImAk3IzPNdM2cOfbOkysHxl1ucUPrSeYW7DQI2eiePTFnNFfKNWrVlCdifPtka4srpmvTHTXatnEzgUX%2F1tvgQi1Ln1JfW3kCV7XlgoCCh7RvegROmF5tUR3P6TRBjJY1XCZcwpNNUJLM1qN%2Fly2st33F%2BlHLGomWv4jRBhOxlmr1mCtl4Nd7n%2BuejDXw3pf7eMNSMyMkGOqUBt6AHZqDEIGzW6F93F5anYGooPWw4g7TTdFy1H5HOYP0M81OnPudPuddHdNl%2BzW8Y1keMc9i4wlJgbQFvJ%2BeOuJet5BBZehlTG0wC3ND8BTlP6kgMp7zNJIOnYnEb0Q5a%2BJdbsTTCqGK06mMRnQYXEvyO33WaEB4X1u4jus9KhJIvBqnn3DG8UbiAXqujnynfiQKFxz5s61AWPwWVGCTRs9e5FaJL&X-Amz-Signature=f0f4e30b5876880711a6e85d721098eb65e29df5d111df39c1d937e6689bb929&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



