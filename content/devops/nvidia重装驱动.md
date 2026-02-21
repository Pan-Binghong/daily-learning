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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3OFATNA%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCZQ6k4Sfky4eGSktOhr1EPgHiKLBQ3vuHlNZoPE6poQIgbip6Aq%2F05RDBFfy%2FckWzj2b9yNQ8DH1KC6Yp36Ql9ZMqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEeh94fcpl4orq8zcCrcA8yOPGh2%2FcrQ%2BpEE6dZZa8RxQrstPkEh3WXwt1%2BLxCS8GMwdYxlwJFl9eErhFnnu1StImOJgrYia%2BcUbkXLusChw7EKZnKD%2F1%2FmAbF%2B3ILXZnHJHPH9FSYs55nXKq27hk2yoAMiHaugEbmacGxyQSOijUqiMMVuKn0GOIfnV7tA%2FbvGEhmt9LzUl%2FnaL9FqhpoSMLVqPzR4EC9fEgak2RGzQlra4qSp9RBnbgijN0zan%2FTOFrSKbCcG4cGAZVU2F3U2ebFiJDFkrUMkjYjGpXsZ2A9hyz7M3vS9JHAt9rqyZo2CunIlf%2FckNhYTzvLp7n2PMn7ZOZWH6FPUFG4IcSWom%2Fy%2BWDKU33jcFNYCU2mobwTxnFkkKgpCcNCmV0sXDPe8j8gloyyvILKk5ZHrIDrw9jDi0qKneUqMyymOyDkn5fDsF7vcue91DQ88wnNlplhFZB1ew1RMkMfiXeS%2FVWwrbkXlFMWSqY3nGw5g4BL543qdvQOaeOgKKIYP4yTiecKkQNmeCrkdgx3e6rvQkfh80%2Bvv3KZyq5LiNOxiuPHDgqCpiTNcdmVL9i0LdvHopiYgBUjmiX%2FMBPbYGwYUquwmmPjgAwwBgPXNxQ86Gm03gA5YPLgqhVDEOUeknMLi95MwGOqUB4HAsFGwCTOOeUV5Ui7hop%2BECn0qxWTPgGTO%2FGXHe6nbQtCgZmX65zEXmrVwHyrEopmP96Y%2BBx6kjOoF63wBrd84oQsSAGzNhRn0wYdxQsNRPsq7TFOmNE8WmEPUKRtpAaimMvWUuUYr3u%2Fc1AORDWumDQdng0jihDmEj3mPsGd2y303azNf5LdMqJnU9DTcGWGQGLz8VuzzF2xEoHOh%2BzT0gTXLA&X-Amz-Signature=96bc5427411ae2ae74a4368a20d929b370b559db97055ddf0addccffa38793d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



