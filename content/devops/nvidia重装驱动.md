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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMDH7SMJ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9fxdyW32IU5ps4lQjpYvNqyp%2FO%2FEeWLy%2BUFYFOi1c6wIgZKzwKuL0J0B8bMGJtVqH5jvOU9ughmvwRlNkiTyoqUcqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI0Sf9kyOWtT%2Bp0DdyrcA%2BMCJrQzqDf8z5XVTST4J2Gj86gU%2FnX8zzGrlpahFD%2But0Oqf2JcUy1Gy10Okckw0fxJIqoed%2F417UqGD5qRmB4D6pKkoPIylTO6NJrZAKOns3D8i6govWL5E3QDZsAaxrIKdxV2I35QXEtMxS%2Bv6asAT%2FCuxFxHKZuWrKqf8ACXaR%2BllYj9oes%2FvFT3qDiTTzKE9o6OpHZUgEdiPvtCBt9UPTpjnYoO%2BHNXW%2Bvlshb6sU748jJQoJumbOD3xHGFcuuNz196oNiMXE8l8p3OUdPwmNmm23M1Fqm5NlopN0e8PIlSvLMXZYAvDNA%2F8ijWSwaub8QzOsCiFONONbFouRaoPMdZ1Z2yf4IZCdv0LcApZVAtjYMNPHG4hJ%2F6vXsVgVMXKogoOBSmJq1JqKCDud3sX18WvOkcinehR3W8WzsO%2FGGo%2FfOkPnY%2FuSmFJIaKsZkhsKWQF2tOwyCfDruTyjPt0GA9DPpnWviNEPOMt%2B1gh9YPoMOU6VH7QwZKfiikkSQ7Y4x5aQFvUn0IAwLnmAH6heI%2FrG%2BQ%2FeqoCey1EBsMhMcijdtxNMeDCPqGO3zG8iiIVZ2856tVi7QLC14XfbNuMluqIH0HE01Rl16BBv8n6mj%2FzJp%2BywhsFjcNMPaOts8GOqUBkQup%2FIEWD4dH5RkK985Zj8JL9wqqYanoIhXroEKFWJp3L0gQqMx3jUQ2FPcHXjm4dKMJyW65tOPHdPiu07tWpYXuIXcE0uKbefc31p112VXNQ8l7MBfExA9Yyy6gdLt07xxqOPspzdfVIM%2BPguUKyifC66VUOiUpPHUIBe9Lwxk3tb6M90pQoyFekvIRk9eb7Uun182UOMelp%2B1z27M2%2FiJ%2FjuHq&X-Amz-Signature=9e548fa701b715ea30956633ee3ed627afa94bd3edc8c4220e9f94fadd64f904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



