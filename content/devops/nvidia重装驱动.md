---
title: Nvidia重装驱动
date: '2025-07-04T04:47:00.000Z'
lastmod: '2025-07-04T06:01:00.000Z'
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TF3NRRG7%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIH1W4as%2Bu8jO1fEw9gF5V4wcMo5Zf3G3ZiNlKw2n%2F5ONAiEA1GRgl59lago3Qd9AxcnwvJfv8trGyAf0sHxE1xFejiAq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDHYML9pNVuaN15cCfircA%2FURi9Y%2FmtFf%2BoVb8r%2BU8c1vTIUsj8nNTXX3Bkl7e4r2e%2B3B9bnZj9lr%2FT%2BVomwhStPrEYaZWRhfbVgas2jgtPeLbT7J446RQTjdj64WuMhgfaC27efmx9koHzLu8BTJfvWzwjyx%2FWqvfnuoRJVQW0aYg25gArBg7vrIoKhVphvWrA62K5j3y%2BNiPW2mQERCzgYPlTbGxgbk%2BNuG9aLb81L2oYqk2ALU9JYbpqcc%2F65Rse4tXfaT%2FFqc0q66YqAa9T7twJLw4%2FA85wYGt3yy77kogy9kEV%2BJSCkoTc7q5ZvqOeRNkwzlVWcAXJvQp4WWvveM3Os0CuVP95MPnC%2FwNQxj7CYD4NAbcVi%2BwP4Btw1rQeMvz%2BHtB4qumztWIoSkAuq%2FcRrx%2Fj%2BnyhoberlJiMJ4gePgO5homH0pHgpSG1reEwurLyY0Vi8l0Uh3ph4VopoJ0FDg7szvCjQPq8tBoTdpLDvwCBXYOPMxh56dFGLu8%2FoNeWiLn%2FeI6VFBjg7IW71pihuwTKRyooCKn2zgy0%2BjHZOdl5bhlvwfQC1psQ3zalHvpI0qttsodooK846irJ3td%2FytcZOvNkkvkRe5pkNiFbl3xgYRmnr%2FbbDz%2FxmoRW64u%2F5HpvL7EBqjMP2e%2F8gGOqUBmLOPJOyxYQcKB%2BtFaxG1X9tTY7xE6LpQxy%2BSjwTy5wvceoHaMjoPUkiLjD0IbKrDGQNtZMMHrS0es8aN0cbY3KTNUKe16sfvyNy1iBtBv6jsidJ2G0%2BQcCcPh3U9xTDxTDn6VTBJ9TJ7nZHG%2FOf1C%2Bqei57%2FK1YKQLlcYs9ONNwe7U%2F8XdJvx4FmtuCks%2FonTe62plmDuTAj%2BZ20zaX8Sa7r18ZU&X-Amz-Signature=4e78d2b8c6b93d568931c33d3d56610d9a97a84d2d5e8e3b55700e4ad64cdd4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







