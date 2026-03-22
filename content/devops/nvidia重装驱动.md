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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q672C67V%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEIkyynDVVniNKtc6TIK%2FvkpmwyQMVO%2BLsYh7fj2mCUGAiB0ZWLPhzY6txAFHpXJsktXW3cSrJ4b4PxTfDO3%2BlhrMir%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMhxZpjY5kgy6%2BofnzKtwDnnRajsYMhIzbg4Bzz92ZhHrkWDjRPYtn%2BH3Bzd7Ss5ZLxE5JxABZ2Zb8q9pJwSh3QiJAdiwZvLj0Ca4VvygCWCTZzNsrA6NEEiZKI2g0QaqB11knLcxTaQNz87IKPfn8Un%2FbSpiFC%2B%2BYswjpTX%2BVa55nDCR2X434c6OnkjtOhkIbajicpl8K9qh4O1FK3y2Q9LhHI%2BnLhn4Q1MfPJUlbvPJk97%2FddLpv5mnxfzwGGlmVxvexWionayTy3UhvbIV0vCjzvjp7%2FXfO6G6dU6KrUv0dVEKWrbzoXsi%2Fak%2Fo9HC1om2n4%2FioyIn63h0%2BKlLPuvNb0wAZTR0bjm69uM39r8ubolf80FkQeBI33%2BC06rHVd%2F8q5Ac9Ve59SFummstBlmiLQ4OsEqvYVZhsMy%2BMif0nPYrz0PeRTjJcGmt%2FoR8iQ7zi7oNUoSr%2B0leLtsT9XhsijuIGizWky036YlSGrskDAhkATw718oR0WLkYkT%2BOCB2lYeZL7vaehSqulQ0xhZwDWEuo920vC07JcLiscIuy%2BQZHh%2BOJzV3RVvEHg9gon0OR5bROvG0boyfbO1YXD2f6qzgmuBqvBGeWk5tKj7JIsejAznpnaDAcr0XjTTjcRbuowBLwLNkVbsUw%2BKz9zQY6pgFoRe2jz034fwMeqZJmuaOWRze0qOyVxmOeJYq28QWLZ%2FxEdguzKZheTdeo4vdYwZwDcvptXQCSNLFNX0DIww671%2FAbcfSftqLhpzZYBjxnb9PilKMD%2F7nlr9RKobkXjt27N0DKfDElkVxedFQJqe1iir4av9TsSpXfygEk0krUyYBCRJUzZZl1BsLU6Pz4bMdTPjh7nK6gaJNgRTZoJYYlhoYKfLvI&X-Amz-Signature=5b117b553073b09e6efd9a6500b147fff54aef164af064ab7a6434fdcebce119&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



