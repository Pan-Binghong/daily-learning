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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F46L6U7%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGvxUXKSvgmE1hYLH%2F1%2BDSYbKMM88MWBUUuy1qVpqrMjAiBv%2FEnvaojNUXsthe5vmKFejH%2Fr%2FiWH7p7MgwkfXf1MnyqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGY1ET9UQFxFQICEuKtwDAk79UOjrHOfFnLDi2tedUVoqnLAJRFFEnlEO65%2B2Rd4agX6etkd9ZOS86x6z%2BHuAmwFVHJxAkmEU%2BEXxwhFRyjPeb0keuDGs%2BxoxKLIaHwRw23zWlHF5sK2djxO0%2FFL%2B318S0ADU9iJhIYdE5z6l4iJpAUAT2V8Vk0%2FkOpjT8cTveA2KqdEQix0KU0Qtu%2FvFOPzT%2BS3GCd6vmXlRZQTErTpxPsdoYKQSkpkjFwWj%2F3LCaEPO3JZpv%2B76zPivJ7mbGniCksW3B5jYy4V0%2BuQ52xu9%2FBdAR%2BJC24FwqjpYmwOMYacChQ2xqdm3dG0ELYDJLKkopyaGcE%2FofNaEHepOJhhlC5jTHVnuM%2BNvOu4uluVa6b6cwSaRBKMRAxk6X%2B7zHdElqxQ%2Bdx%2FfJjZSEbIMrHHpU%2B%2BNuPzimZl3CC%2FhzWur9dVw0Cgm9jiry%2FCFPWDAib1LENSfcKzr9V1xixfRBOC56Mstz5SK13JBhItCD1JxGLe0Fh2NBURJapy3hFA6ujHCdvcs4IO1c7X3%2FNTR%2Bx2UOyUqQe6nW35cxy7SJ5HP6rjEwlTh0DiUrxWPTO8Xn%2FZ4jtqVre1YSMO9WVmW%2Bn3BFbgP9BuWS0jgg2WSdElYUEwn2daBZFWXS3Aw%2BPmLywY6pgHFp%2Bm7LfWr91Dhdc9LMY2%2Bu7KmoZ6h0%2BSv%2FrmVHiOXgWX6quhrMgjwJl1ozf4eOc0sceA3lDWf%2B%2Bptl2CXBSo17lyCKi%2F%2BeReGcz53heScIKrTIt5HJGdkjMJToV6YIOK4uitNNlR0qATXNb7FjCB%2BzRt%2FhWqY97NB%2FcKHvQmlwzppD8C%2BSC74RL63%2FNxQkQb%2BAY%2FmxMH2AMLLB0umo7H8lhIab%2FYt&X-Amz-Signature=986f811d5ca34c442d84b8d2a02c920f9334a1bf3a833fdc2a323d4e9111eb6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



