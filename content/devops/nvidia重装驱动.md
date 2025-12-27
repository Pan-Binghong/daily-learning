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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMSVJJZJ%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTFiXluV9hp6ax9qFild4ppsqmgeNSlQI%2BFHBlW8Zh0QIhANXOI0h2883hCROauIV3DwiaLxg9J2R0YXjiqbHHJjLBKv8DCGIQABoMNjM3NDIzMTgzODA1IgxFPl4PT3FanpfkDjoq3AMnUUoEYhWvhK4zLVEdY8vrfVEMcrmcjNs16q1UrUyta%2F%2BGqFKJHXFz7ZEYZ7GoIo19ArkgOON7BiRvvcjBxV2JsAUDLB7utBn5P7rICidEZnmd67O74V0S6zjIV0B5AKfO6Z8aMz32vObCL7O18Qqn3tO%2BOiUtztdXhjdXuvAVOU20VPtqDPletjhnpUf1gHCKhihyad4dAt09yCRpKfF%2B4rc8hn9qiUG%2FsYuoBs7cbDzduQavVxl95L1acvkVLUML4kBjz4blG6x%2FyQuYHyRN1UDrrRXUGLJScuMwfaMIN3qyDGq3rVArIWEmXE1Qu2JOMhX2AwSOOzsXkqjVQugwmW47Z%2BbQUkzzN9cGb5RRCXyVR4IkeqaJSQqfIcfcRFJ8YsvX2esS74%2Bukagsz8KfauEmPmhWuFYGQdL7xOqFMSlEqcZ67iIKuKXqCl2xgrKw3x%2FfnFnTSOcGdx5J6Bw%2Bqp%2B%2Bs7mhZvXtoSPuDbH8O6cNsnad3dSUB6mdGerWpH3vFa%2FLlLQAlBXF1jxDWas10OMHCk8Yp0IwWmQ1%2BcTxopXEMYiRFlpHlXIcQGbCZCeumusAn%2FxhsyFV0WpCvMfJJQzef0BV6sFgv1agOmoi8rAfNAoNzsNUrU9r7TDF5rzKBjqkAbNWa4exL2quovhCaRr4Aa5V11JyDNGTMSdTeAdFkV%2FL1U%2FoihAkVQT1exBJ3iC%2Bc9z0y6xf83MXyfOrz%2BbEDYzjpEC%2Fz728tvzdswUrrze8iOGTcXx7aexON12CA34w6lPuqV4ifnUAIzDBYfNSC%2BUAIS6AswB5oiJASgcpG2KBWSo9Vj6RBe2D7e1aBTOcNmYRyA9JTOXQtVCb8%2FLSmZKMcngd&X-Amz-Signature=c7b2e687421aa603ef30686358c8ad25e803b0e25c70125cf28f11b3da1d546c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.

---

> https://help.aliyun.com/zh/egs/support/a-gpu-becomes-unavailable-due-to-inconsistencey-between-the-nvidia-fabricmanager-version-and-the-tesla-driver-version?spm=a2c4g.11186623.help-menu-155040.d_5_2_6.753c282erKfv7j&scm=20140722.H_2847461._.OR_help-T_cn~zh-V_1



