---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-12-04T09:08:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VMASSRL%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYDiKtmOkskT1hupR5J48aF07VqkZVmEKVzP5wNvI3qwIhAORtbQyAxH%2BSOYw9DzxQFkuM4d2pGoTgYnCvWo8674SNKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwVwHCDOrGTS7gmoWMq3AOOHkCatP2iX8G73dYL64HihuTeXs4ts879LlktFqt8tqx1zDioPJWGw8bVYaTZhKZZyMpJnbBiHQIoMB%2B79dF8p0atMgsOytX%2FueIZp%2FrSzpj3hO2tBr0%2BeBFjqy2eMzkEnac9ytUvOytAOpTGjqckNorJH7UR%2BELCf%2Fd1YGGyGjYoZHvheZ%2BHCwpoekBqP6rU2S0VmvCOnbOCPQX5WHyZLjcGHbtiQWF9o4lp1CSbNd4PJkixVdOpjOwCAhK5cZT%2BXVD74yuICeFJ0aTPlO5NrLW0GvCC%2FsnrgEpqnZbAWJLaJtoA7ACShPAUdiELzhtF%2BTZMwTNB8fLJJTyColJgux%2FKyVEeFqCPccxRHNTGK7x7phEBUEodJlvJudkVaoxG3bPA6xpPHq%2FsyKgCe%2F%2Bqc4a5Jsg3%2B5Iqm5LUIs5ayzr7zikFkrVogG%2FPNcm%2FJcxdveZfBabYUjmvG1n9B8ErS%2FNsBr9Gs%2F4%2B7lLsYHHeziSXwSszEWhLFpTVu5%2FTMPfwVDlbjg25f1AVZQUos6D57jLX4ei7yKQ%2BlVECdsg6vOYNcBBq8tTW48D9zlchxtrsu6D9qaDXgFSlcDqLqG3U7WLLLL1J8qnTVVBLB80LOm6%2FoTBMs6sTQhrQizDnqvzKBjqkAV3SivMONURveAaWLaknlfpn0qLmSMO4nLlr3ME%2FTvmIB7swLuIdnqunNi4aVlCLoXrcSbpWHqDTAHPrGI8TglsGJafu1%2F4%2F5%2BqNB0puSPi7Egyo5wqTGMbtkuBRv8nuQ1Bk3WAjtOxv0PfmOG%2FIdHGkgemxpToB51v%2BaLzFo0y74y2Bfa2vVET5CDNTOXDUetdJLhS6iuz2%2FyFSni2%2F%2F3PiXFf9&X-Amz-Signature=7ec3c9cf514800dfc22d2f6360d6e77d2c151283595941e0fc774c088139885c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



