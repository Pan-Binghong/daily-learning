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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXNM3PEL%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICLOwbllNfi8Etm%2B7eKYOBWXVRx0RZZzSAN05QNRKiy9AiEAnEEN4dphZPv%2Bf48u8lzyRpwGhXs%2Bh8n0oYWxBoiobDUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJfDi8%2BQgV2%2FkPBRICrcA6MjGh5Gv%2BPZZyTjlG0xlJYGlvaQep%2BLd93Cf44SCOJ71wEb41EgwrEpltUGfjecvQvHULzbaEww2cqc9LyV76h8SAUdonWeFBpJe%2FFb67oU%2F3Dva5tmoms5UR7IQXtiJAhWjnq%2FClTL5%2BZ1Jz9iGyBW38Z20dTgCmZieaRgcQlxCgZO1w80bjJScTtKKNSkf8JfsPtIizLlSi8lGNario0X4Z5im0BBe9R%2Fo%2FDc8wpmwBEiAmUa75fl5nPhNzYteu0Zp6LogzYauggzZ47jUiy5UA8GTrR2t78l2n8KIHUNBoWi3bnSYP7TiaWNhMNdIrAoRfmEYDrde00psh33Wms0GmrkNuTO1%2BKNRcm2dSO2XQqWL26GoHqNz0tQAomy9Py3kR%2By6K5LjzeiD8Csd6LNQF9zhsAEYArrZow6wo5LLOSAUkCExLpYtwqukK9L9tpQGyDKAoMMu%2FwlZNCIr0B%2Fscmhg4VqwjC2aKXTYWt%2BfWTdej6aLi79HbzbN0V1i9NDWpiu0ksjkUQs80gstLfRdr4jUPi2DVHVdCxevriE7kbUojqSHpp%2B1Sd4l6p%2FPQ%2FveFw0DyEMlQ9qH%2Fyj3Tkg3%2BgXoaLqwy3u3kva1lEF53VQHuhcJTgUA%2BMuMLne9s4GOqUBh4poPQAxVrsDv42yPZmZWUASGOvZ5i8xRFjI8phuUFA2BvWLyuf6sm0wz7O%2FUZQOs5HFeejDDGlYk0Fdgb8cXCwsLE1h51ZJioimnkmZKgNKGULizUkmwUIVeyrqRPAj8d2Ln3NFr7NSSR8X69O0qAJNFGCgq0aFASoGTKHHfAjUs%2FOWkLHIA4r9sgVKYuciuyFOetrRG%2F6sn7S%2B2wpPmxC3YXIA&X-Amz-Signature=a31ef1739a8f6b4dd3b4df3ccd9ba3884014c0b207baef48eb99369237b727ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



