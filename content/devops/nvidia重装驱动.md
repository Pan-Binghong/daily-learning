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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CTRZ7KG%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeHgqVlATmTrMQ8HuzgL3xn%2FdYMKJwYvjMyBKEPdtWEAIhAOmm07JGcX6PT13E9%2BLkdInsvBGptCDQrStp%2F3R%2BzupwKv8DCFQQABoMNjM3NDIzMTgzODA1IgwXPn5DuwVp74UgXdkq3AN8NGMA2pHUD9%2BDsWhaB24yCpDhs5CA%2BP66QU0tdjuazorJarOhEameJM%2BFVKKe%2Fxhy7%2BVjAu%2FsNzdqK7lCM8KkH4iNN3j8scozQD%2FuDIWSyGyjVBYv9RQKWCIcxyNViScCw9zMkjRtaDSaT3cypkqrLl0ReaeMZFYbd8uao6XrEUCRF97ZNA8nCK9R4%2FQ9DUq8IENUZYecD9JCjamQ9RBAvS%2BGpWDKd26pseiZC39Q%2B%2BJJyrBgacmfDpKOdohRLsMNifSiyqksKj22SLFDF0d6tRB1jRw7W4tfjOD3iOwd2L1PFa0ZrOk%2BLhLxnvphY22KWHcQtpysqBIL6PQkc3M3ocQUKCCnvy27sO9jnRIoyGJftcCoo1w0hDaUymjDaZIKTGVzX5cecEsa6MvVavcipwoFdnZmcDPqP23hCWU6%2Fr06hHOI9SnmOphFMwA%2BBZfR%2F9qOPtEGeyuYQBPRFkuAwXVzVlCuu3n%2BkSZYoEcoFJ%2BDrf8UGKGuXFkQsnrPKQFExHsn2LPOWaHkjIdmbqICNjpVqPMobFcOVzJs588XQRryLZeNdQbQU6fDR7STcOQUaEH2AQiCRSe4zMPQ9M733kYByZ%2FOfu7WjF%2Bea8gXS9v8gMFt%2BiAPM5%2FOazDFwMPNBjqkAW4ZYl7mfGVDsFduPdNPUZ7grf%2BwjRDB%2F45cJVUmtqJGpALFS%2FrIVKOfC8yvelxqS7YrWd9hUrF2MKWVJ4Fgsm2VxI7qm%2BkyIKz%2FlXYe1vNpehz1viZaBj6laglWlvIKFkrKKt8QS3kJviKZPmNx9i8Z5gP2ra1HS0evn6yPQRCX9Npp5sCh15%2BqQlIA%2BIEukPRluUxmXKRTWZ8PdGe2q10vjpEz&X-Amz-Signature=eae577baf172d9f6382d3898155f91aa4c2bd6d4e29228c0162d57ebc1e06ab2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



