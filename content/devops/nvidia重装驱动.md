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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSFVEK3S%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIEsVsFVqIiHl2pyXEswKCna6I%2Fq3isw2DMjJ4MAiS7XBAiEA9F1SfRtno1TSBwK4WY8GqkriIwSxsYzOzaVwxNfxGzcqiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNZo3LV107Fo4XnVAircA%2BK%2FenYNV4g3h6z9A%2Fo1LKThMnI1LWEq0FiO%2FvcDoAZcXTzqNU5rLLgMwtyTZvwRr9g5etL9Yp30WMr82m2mllKHALK7fvu%2BF3F16qHsc7NDo%2BKAxsE%2FOfvjmJmD2SqhsRpOaaV5cmQx4Iap%2B37dIZLxCjlbE%2FFSzNZxvT7BNQqbHLHZxbDLNxkZpaF839QflUe3E66AE4BcPUPo86X3Agk%2BklB8iVGtwKSAckEF2qMxJWZec8W4dJUGX8lPDODeQQrPRqttXZpIRwe7UK3MvqzFKPC71YVSWW61NhlO8dJT5JPfhLXatNQaIAlqN21uUS50Wc4fjwDQlfqQd7F5sp%2Fi1ScCfoOaJ6uiySQb1UXOJv6vfVRrlXpVC3HVj3YeeECzpCami9FgEKxibtDgBuHXysbjisLJ9Wqzt4ao6NeYxcqb7491TxcoEtXcz3QxYIZQiBKOxtq8u2AfqI27D1HQYwAL75RwbmxNlX4dAt2%2BnNwGeeKk8JgJGtUuvJo%2BtOl0J0R1s3lc%2FC5345%2FUq2Usj%2BwAt0UydTsTjN126oCeyYUVeEzLlFQbn9a%2FPDYOy%2BQwOuvs106GTxXGBZdHwLHdFfzKbJkpbdESMCZuOgkd4Nf7%2F94TY2SD6X30MIeTxs8GOqUBEBI9jDBp14%2FW0mDt4omjQzIg0UYBGKii4MEmK0jfJL%2BykZSAm5uTP2tgMl0ArDl9EC%2FBZOToLFEGARKvC31h1kYloCEEiIATZZNhM9Rj1qODHWO52BnGGRE%2B916bWVzJ6iCfddB4XZgrpvhF5%2BenKxvDFKaRjbDu86EAA6cAlQOJU9XVOSUooUH6KEpIZXEFlV6I6QYohFiUQVqpksev2BVEMOOh&X-Amz-Signature=ae65b461ab7f324f5485388e17e58ca6270a303298a45fecf2d1816942509788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



