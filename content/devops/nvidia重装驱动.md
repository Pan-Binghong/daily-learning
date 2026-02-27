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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIUOXILP%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIGFfDP8hUMYhkwUQZX%2FYcPz8zHUOiddXQLz09aIqF2UbAiEAofn%2F%2BsFVXZMtxvUxSFGAY8xzq7Oi4mDa4XSQZp33Azcq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDGhAtv30mHZkhLYSEircA19n0PDBcVo6Rs%2BNWKC0iVx0heskBsDOLqikhu%2B8YH3%2FB6IgHsOE8fNC8%2FUMwI296%2BLh5T81FL0z5jA2cS4Sl3uUN8m8EEcwiGbpDpt5ApKpHldFM2SvLOx%2FOGHZpsz1RKZEU%2B3%2B8zCNFM6Rlu9kOEaLjeJKZHRdfWz7p8ari%2FQSsAg01xEYsIgx32S02Dbc9mOt4ZDxOlF5jE56gNfHtXFYhvGWIw21oXuSPZgNZ4JwDneAjyQl9E82hQcjfSeR0QyMQynlb6LcboqXreXGYiyCMjRXeqSoqQq3tGyThTtOL409bS2hs33OhpxmydIB2cBn3QLu2RbnYsQ5NxA2iJdpVUK48LDWrLb7ga%2BKc031dn2Bq2XetWXDvy9enC2OVnW8mP1XkmMEgDbQbs8s%2FwIBKAFtX6VgNPRcWorrWDEiWuPy4QmBeurC70vCeMUwd4F7buWSOm1ftG%2BdItIs9bwH9ZCWuvadfc98Vf4lYnnWSwhYlbVeYtB4Qjm3k%2B3r%2Bidun1uPWHUMl7bSsD0aziboMMF7V6XYBidAwBsBp2nAdm86gGW9kJBBylXuY%2FJaMr0t04z0Akpa2YLM1bfjGYvSmFERzeq%2FHOdBqEKPxgDJrX2vJ0s7MjMPR33LMJCHhM0GOqUByh4BsbpV0cQ33anYXyt86tuvjIMC%2FENFcI3VWtVnRPv%2FPabxeOXhaNYDOL7cKwnhAmEwiBAlL1pq6Q36vtIzLF3XWOwVo%2Bj%2Fg9PRoXORmDjg%2Ferkv9XkX2jx7Fg5l7a5lR9gVWlLtb%2BMYNkZ%2FIjNHCatHKwVg4NJgXfJ%2FxLoiGA%2BIHRjo9e4Q5rzsBhIbfjKbYSGAoi6fsku1%2BA11meHccLys%2FaC&X-Amz-Signature=b9bef32716abf952da98994ac47dbc15ac090c8c2528e4b09abd73bba3e4f7b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



