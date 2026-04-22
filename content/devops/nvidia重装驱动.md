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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2FVBCC7%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T041024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIHHfAXtdWiKwB28%2F4HecoG7tvHN35AayC3fu1WQZedjBAiEA%2FlBehUDnEJ%2B2xTU9Yl8QLV85SfqzQ22is47V0Yl03M4q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDOeo59hgxc8kVeoxZSrcA7Kk7OveklJWJaSWF4udAO6j578j0h%2FQd2k8iuM%2B9fAReQkdZa2dmMYlS5zixn7J1Eo5Y2hv7LT6dqzvZNkBzCSQ8%2FmjC5gh3StrNqldaM7BvD2q3qUBmqq3Nzv6le42o%2FAADL2kBiJCQu%2BBHuwQuNXPLivZ288H4Vgo738E6zenqp9jsku8Uf7Si3aCEC3yiVJ7HuyjPl%2BNwJuB50%2B5IZeS7L1gOa2%2Ba663GGE5vAO%2BKTYpKGxMKwve%2FiE0ulnxJ9gYaMEc46Sxg7Qm%2Ft%2FIqUu7fJ9gyi0KlzxnyC%2F7uaBzA9NSkR0jIn%2BKn5dO3967Pp0Z1FcNtpAi8Qtk8hSrg5rbL%2FBbyCh0iu9aSvwhd2fM1Pt9xiV1BLSFlMyLM8ZaJDO7n5xttl%2F4aOrWmt4MsNX1LXQoAbqFW1li42XklB3oB0KkSzwWEvFmlMfcy8sS9DrhIwssupRnnRy%2B4qEF6NjeJJtS0cjdAWntb1VA5Mc%2FOK%2BsMXxY0Pedjmehd0p1zw8xH019TDRaYc6bnsjaDX8pXdzm5YtFTGTEEZsKF%2Bw%2FlX9OOR83F0t83o3vwFrIc7CWXEnngwaqiQ78Xawcsihw41GUXEkNmzjQq1VNeu1mXI7C54PgBvLcV4SmMK37oM8GOqUBx7G7PkLzmhSRm6ukSQcPQ%2B1l0N%2BQSKDCN6A4jjH1iolSjiecvw5yLUnpGte8X6jOhnMNVgLBGPYbzptHqXnTwvhwXtk2T7Alooln4CjRlmK3xtwHCRnh%2F6amLOQiOLontoj8P50sihwsfcgLXsUA0jj%2BlVQ5MD4%2FmzwX7ybAYJBExOGO%2FwZL9STQwrOeXHjXvotKgL1qNxbB30SSUY95PutWSqSl&X-Amz-Signature=4d17ffc4260d619c9c5aa683d15461233006c2f9459a6667bcced9a8a26de699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



