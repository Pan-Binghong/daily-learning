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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TM5MPKH%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIBelAbXqFunS530e1yaLCpPtBUJJ%2BphC4U%2Boo8q4VpTnAiEAhrb6zFvmTqifkTV48YKHHGCwJWY8sy8ROpiTyTC2OIkqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOasy7fJmuZug8onwircA%2FoVBLqBSwSRGhHfo9Jw4FhtL1RuyMEybs2%2FsKzVkc1t2zMlrP429RKhaYYlQ0alZTRGEnNcUGoS6p0SwIyL%2FmgxzzLLQW2x68lNm%2FfgIY0OQHDVe4NeHGp8FYGLRzmYasSBGTCXjHdiaHBb3uF59B8jfs66r7rn%2BwPt4Sq9WssyVRPqL%2Bfy5MXY%2B3XBw76sJYBLIkj1xt0Qx%2Fk8Vh2GV0e9cMd5c2Z2%2BTG7hB3c5016r%2FDjNf8enL83VXoHgb2z8Su4S9HmGLcdGwlXPu6jsJ3yyUid6wJBnTLsS7OqHbtPQpbteXx6oKdCiSv2BGNXwwSLvX2FV6pU2Zf222FWIU%2FI0rwozKjxLq9Aj7OekYwFVWrLSQpXDl%2FEcl29alWZWQfR4j3%2Bc2ZL3a6NUosDF98v76zE0PkFHOaJJyr7qrEfyUJXPQYIm%2BYK8ahkDRlAwRCSJG57pPyuLtlSuBWPz6HGbq4hNB9xitYRQASvSe2njrL%2FbQjdma1abdM3E31hnzxfXC5AVONYbk8vA13nUg1v3KD8Y8zbsIsSjPl1Hz7gNTpcvfoUH2%2BAZ%2BBCAdJqR8kiEx0HxDgjmOuMQLY3kZgHTglBpj%2BZFQV8WkqOyIlEsORYjGDisBzyO3uQMKfQusgGOqUBXWvf1CzKYsAL5MFDHTnQ3M6AnaL7hsonS%2BRsfxShsVO95k0PvOY3HEi0tck%2BBmmAgMD7ykDUpNmDQa4f%2F%2BXDEV87J900%2BzYPU8lIVMSeNngTYyl3sFzoK0XGDL%2FG9rjvZwspcILeOiCI%2BrtPfo3q6zwx21FsmWhOCTeJuK0%2FgFFNirMU1FHkAV134r9hx2RUeq5OnMhn7jpm48F59tovTl%2Ftc5CG&X-Amz-Signature=1c934a555553d99e1de371a62d3c2409644ea60420daf8d0fde33ba147007d5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

重新下载对应驱动, https://cn.download.nvidia.com/tesla/550.144.03/NVIDIA-Linux-x86_64-550.144.03.run 将这个链接中的驱动版本替换为报错中匹配的版本,下载即可.







