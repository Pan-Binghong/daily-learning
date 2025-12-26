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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R4YURBBY%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJhneKHaPSULnj9YlJWI9EXtPOAIxGugWrTwcg7YUgxwIgbO9Mm0sLAr2DbxNTEFFuSoByEwkZFivJXwoTxr5%2BBuQq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDIDT0Aha42AAqrHqZCrcA%2F1%2FfQPHz%2FNRy9pElCzSU5ULpj%2BmHPbxA%2B6JAW38Ab%2FQG6j0FfzwcbsO7ZoDtUBuHqTI6MtwKgIYDwOtHS6JmEYCrejXtfwkoLkTcT%2Bh8AuB9utrhFkJhrMVY8WVXG3qFuqYdlirGeqg28orOznE9GFedbrwOi3hesXhsYJrYsXx%2BOIP5NW%2FY1TOoICyGCHkogfXoIw72DNDJHE60aPGJligc6q1%2BHWDdZLrA4YhB7bvdPY1s7qwHl%2F5NsXI%2FtjB3elj98rgEdqCTUFmv9xkCkK1oUMCa1mSzmY%2B6AljMQCToL%2FVmsrppAfZOVcmzu8vus7f8nsiHIAaF179oE1vRpBzj3CJ5RoMOgTQTJv5nBTaj3uVCHFnrC4Wg6lH7%2BWVrW%2FrB6K9LJdDNvxEbfxmc%2BkTZhhtcT4aV0iAbmnySw%2BoEfqt5q3BuVIJ16GfAAhHxdC4ojOTBZ3tQQX6LvTQZzBUZMXmyx9mtqYkSVVjhwMYr5MekwBLCeM523YLzU9r%2FrPoFL1ipqlyYQtCwqoPYmn%2BatUCYD4ylEVJQ3r1eo6hluYq2H0Ud8kZsgzBRq3PzzDjEWhklQxs7YHTRf1n7nL%2BEbOzwtiztQ6OhCkYV1lGyIHYGWPdegzPBzrXMK3Qt8oGOqUBXhH%2BSJxFBiiaQHGw3aUSlr7jSvUkNcIYqUcE8fImEtc7FMzGpMaZ4c2A0X2pc9h244pwdWDm9bs%2F0f2aJ%2Bh0l0ctG6DfaENmEW88%2FtcDUR8BcD48OYf%2BcDGz30U7KooVddAThpx431ns1T153kYW44dVxUv1kFXeE4x4SZV%2FN%2Bc3iqFXVopeKNsoZDJW5DfhOUD6XKTPGlQ4fH9Nmwbbo6Z0pfQH&X-Amz-Signature=74e71a107447e16eb2223040482a5db08921ffff681028394102588484ae7a04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



