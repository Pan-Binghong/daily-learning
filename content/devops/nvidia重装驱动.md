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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIEY22VM%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQDxrjLDnroALiS1o5vvg6yv%2Bs23qTFzd1rjDM3aLwMr3AIgBugPbW7MeYrc8CBPnj3CeOZTnEYg%2BHwIiAAtKY2wxk0q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDELWZ%2BH5NwDD5vxMUircAzyDxz7zpAGLxyHEqUCk%2BqzgolU6%2BBOf9OIBzBB%2FMVOidCG9TaxZS8zsNVGjDpRTPu65r4s1%2BBDTuGNpMJJ3RESbhXbEUSxPECLJc442%2Fw7gXq9y5N5QxrnBQGJR9KbvAT6VXlTUkds2XMpLK6ApMH1Nw4RDf%2Fg8hYRlS%2FkuRoQm6jMn6VMUUnqCA0pHx0ql9JfeDLt25IJ8kmy8qiM6erq%2Fub2xdZerp%2BmSJjvd9s9bhrv8QwTNcK2aBlymXXXiptWQC%2BvQdBgn8nCZTZHKZoj7xXRYH8oEdeyg1LU2bnswyCyKxGzf2rmHejJRx4RhL1dzFRRtrnDttXgRVHw%2BssN0jUFn5YstsqB97y2EuM0NsqtfQvZ8r0xUV1wkkROxGjjP780vc6tr8Qz5U69ABUwN2vfNJLNmSZY3PcPmiTIFO2EFRnI2m3ai4rEngyvOYlcgIMIyUm47I%2Bx9XS8%2F0UJqCDWvZWo9OgC%2BwvEvZRTJJy8JJ7j3mecIcHtfn2CpV%2F6ZqoNOyhjFA%2FdmM0%2BKVhCoXjb6MltB0zbg17OU3tKzczSnHQK1NJGq7ub%2BTOf8c%2B7LT3LpOy%2F6nUe0FROdKME1a8UDLrxs1GJlxzPTHFt5CcXfH%2BxZrGGBU0t5MKrE4c4GOqUBBOG48DwBGB61RTG9TBi%2FbCibP7z08lU02iM05wnHYtBz0mYSnd6HNh8TwWkoBAcLHOLNEFlK49MBeR7X1VVBK8B%2BtPcRyXmNr1AZAT95%2Bamtrc0BMiq%2BrhxrN4W1fvC5dCoR26d9rewnjKT048kZh2NfRAx548li%2BXepSEgykP45LUOgMZYw37X3Z%2BbcB49VBDteJ9JNA24PDjv4VDg8JMxPW%2BRe&X-Amz-Signature=7df14f8e36ac6f1669f5b0da8f47cbd06b4accb7b9ee2e496da73390170c04ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



