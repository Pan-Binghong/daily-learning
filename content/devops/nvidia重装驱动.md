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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655OTH5WK%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBg4C9QJ5DVz75M7w%2FkB%2FeDdu%2B1Egcn7Fv0BfTSVIM2tAiEArVNPyh%2F7S5q3uMJk9ndLs9xib8fYcOIaXA%2FBaCVbjBwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh9Ewa%2FR5f8lY%2FkIircA0DDJN8eYAQPIxpfUzNR7frWfR5Y7erNTJ3zB9CbEqJmXOruB3ntR30oc0ns%2FhZcjvS00VS7Qu4S5gtTdR60KgR3ezRrDl8jsKOEZ9mS9dqL%2FrkfcrVH1pM5c3GvmFPMUrUQRMGff5V8rpTz%2FFdS9eA8ewNeax0qm9tCDxdl71jcdZ3wAiTt%2Fn8GA9JJpXSXnZkre1EfrF4HMQnWn35hWonyqfhUKmSMl06Qw0R81f4vJlvA44h2H2hv7fZYlDT7m%2B7VPmAqZFXkiNLoJR54FGCH5mKni%2B4qE5Z1ZOJ5nBXsrPf4IDdjWzmERngVnzUa0mtkvF7%2BdoDzY2xIyzMYWf2L0qHI91GFJq8NtiDmUPcnJHqoUgM7ZCDkOiJ%2Bv0jk8wSx%2BBJCrBkDP3i0nDTi4zDMgqfu2hYSwBWTrFoapqInpp436xUxtJMySrgzL%2FZvCfBjQf4%2BV5dnpGWlCy0iYdFGF%2B%2F7%2F0BfOR5jrXt9xApfTKi4DErGHkxtrrTTsu5Qcd5GzpMoq9MYw3XH0szMZOeIvwofJop7ntBi%2B%2BA%2BGCG6BVcb3ptbYvm3rzY8ql%2BwiPoVHl9INYfZsmFv2pIPeqSbDdkWMoB4MW9WCkKOIl35PHEawM8oGCqKZXh2MKLFqswGOqUBKaB5Zmc3nomaSwgRW%2Bktn08nQ1WM86oobzaOJyWXuu4c4z9NiIEuoT1BCTlBP82Ne%2F0y9fJeTgZOrm3NoToe3n%2BmtFSUEV8QePfYEO5Mudg2tOh01G1Nb22RvKGOEFjNe0n3y5mrvG8Vz4DqVj5dF2GrESO3RCiH07feMGROkE%2FxebeRfMcw566lXYmGNEB7gQ7K8tKIVYdICzLfQq8WYWFXB83P&X-Amz-Signature=a6e05e7cd97f37ef66578a3e0a6a16f761a4a5cadd7b432b5ede5e4339d4358f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



