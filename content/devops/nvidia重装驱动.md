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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFL7BYTI%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIGYvVIdl20lzR%2BTMtvZzCJdfLL1X91Fynjg08I61BcYkAiEAxbGlBXq%2BppURPzVkD2YJinsXJjjP1IYij%2F1qGKv6PXAq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDCNL7PI%2BgGy2gae9UircA0vIG6fTbXpwVYhABAAUGcBSl0qp7tdIZlV4WmDMMjxzuIcTHQvhTzXICBB2xbVU19dNYDpvoZv5oGk5AA5Hgj%2BzA%2BbgTIPYyrrVBGz%2B8jBlbDG7SJyLZNwDilAflCDAYDM7daBa827Cr6hTNDBXew%2BdZBLefucs1nY5VmfLKOuE3KmxAEQ%2FBNV7XawEAN2TGb6%2Bnqh%2FcVdnDGwgfF8kc157lp3wBb7VzaorJ9FQmV33PepBJFHjShBdsMp4piDJXSNSnEK5BjY9C51ryZcwxmP6XLunKQNbX3l2lTrFpKtW6GXrqMqIUzIL4mV4jqi4SUIjWjnvtJdi%2FAlFKn2iTXyYG0qpyw%2B1uhpFaLZs3%2FyBVlWbDfbLIBm0pyjRwGdiLJwFoneUgFYaFT21A6MuBolwaW2AzBEBViG%2Fk5aCY1qwv3fOxF5MP6Hzq1TsNsBVtSPycQrRmYOEEsprD91CXeE4XF%2B4Ij0qTPFs2P7oJendB213TlawbhIWtATSYyJ1o6B4SG0BeGOudq7uy%2FR1njheudOU0mkZUUJzkE%2BwDTdxRrCsgVUATKU45dHpseS%2FDy4y9m2fB9hp%2BOF8VWdXx3KBwdrYYvnMAsUzpovLObMtiN%2B0HJNg3ZuTWg04MKnpiswGOqUBDMwmfP0%2F9iikL140ML4iUUadHO9w19kxARWMObWa46jzcWK0DXNMURdNW5ogLI93rChLRx7GbbiIIz2s7ynjaQUS7ajZvwGyI6CtgB%2B8TVPcwuUGjG6FDmU6e3p2j%2BQQWeu8SzvcIsSw25bKZ1dw4bmGHYLdTnrYXwveiElygAjrOEuT3A7NZpspxeARnNr2mmtevYcyP7%2BxCVVireQHT%2FrGCt3L&X-Amz-Signature=d8ca85c79ec50e4ff1b84ca23d3298b0e2f3b07fd9b82c67ea4d40e2f033c6cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



