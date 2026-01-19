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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R42LLZ4J%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH40cj8xGFwdmlrjVn00VqrEoiK%2BTSauhplf%2BpXmXIvuAiEAhek5wO44VfpIfWT43H9mNYAx8%2FTj0QgynpDt7TzvsNEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVhDa6YbIHG84D5vCrcA0xlHitVkMbs7KnkK58TTG7oZ92M6fudebsEY0mvtTFuy8ULVUDsEpBCUqkrIIr7B18mf0GZ31qYSapjDTAg43cJ4ffRV4LkPstUD3egS1C8L6bNkQ2LglA2imwrxS%2Bk7qgnjc97WoDQxep3zygSxE1X3WxVnNZCcFyQ%2B7SWev1Y6SVbO30IzcNkDGcqgilE%2Bfe%2FT747jYHLs%2BtHNye%2FfUilozehItcEZDsws8qBHtfO0DruwLXIwMUJH84c8Z7siHqKKvt6FzrfUD0wEU%2B6NeBV2wj2A5MHEAdxoZAibK0yI6Ts%2BDPfIQPRE9jixZ8xrnkzdVa1sxXVcKD6gk7OLsVmW1APVikfmHzqzsS2Ji0eu%2FiRwTrHRtmDxZyQlMwFBWM27BaKniO7njwOe%2BG%2FHkPFaNKdW7XNpBYcWd6l09hP8aoKV8Yb002ABsxjxciLSSTeWaAmExEtcorXMeRaCAnPtIOLb6FCLRbdRhqXfmIvv3ZL6hz5v%2Fz%2F8KUn3jcYIAs5i4a68Lm6DA8so5K8ZI9AqmqWxILn9C9j%2BfT9thJ3kYpWgGiTVvF6vZfqSl%2B02Qn5wWBiCzTCUMp%2BgXebySwTBog%2FiO43XjhDE8NiuPZ1BI50SGTid12zdfveMM3dtcsGOqUBrHyB5FvokFVxurdW2D%2BRsvyQZqxuMX%2FYE1MIebl5fE7v1gylR8ehIradoLX6QMIOzIzWEWJc7E8QFr%2Fnyg12rLZ598Hyl3qsqToAdqGseL6dcYsENyILR5e8Zgl8ee42UgOUMqnjpQ8e8MSyd2enpN8fCFVziVRBd5uRxK95si%2FHZj0TDPwCDmiqK8x8R2C5rSxgkZT4TvAyS6XPGaEgE%2Bkhd%2BAu&X-Amz-Signature=e647568d73452b311ca28245cd41bbe6388880f26a8a54065ac321b025c57d35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



