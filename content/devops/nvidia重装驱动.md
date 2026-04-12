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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TME2GDN%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrFnetKUFVyt4bBOZz5PmpK0g76gaBCNFmPawyNM3IcQIgWQq7XD4%2FwYZcOEhBOIuuL5F98A9vrxzsRx8w%2FVhaGyEq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDAVrn0JBEisETsRhASrcA%2FPU5nbU1%2BE7Wtmk1k%2BOU0zA4Qwb6uQ0BKAm3mtGa48TDMjeXUgZD1h48uTAJ8uCh72FhMrTF25POJWUDlaNpBeWCAJZoJnBvmsiCcTiF09OFY3BIW8VD9mmgDfN%2BD6ufHG%2FL0pYs6Vw981NvZJh4Mihjs4l8hfPxJqsTY9xQwxlr5viChakxF2rKegsnuNnqUMR5VRJhrkUgFa37Cg3ICNfYNEZNItZxLjH3WpmIAek8EhzjKvuBhGoPGXIuOs2fUf8Wob6dw5vz6IMxo3b1xGhu%2Byfpw4Xyw3bdfX%2B%2FOiMC1n%2FRKoRW2mdnaKSc78fpqLZEsJvoDTRPERthr6%2B24%2BawWyPu%2B7s35wm736MpPDXhGSIONEBBPp3WaxQ9x8COwjspJxgvXe4Mk%2BGXOb%2Fh%2Fh05USpmrfDIkzRAieGzEspZ2zuDkfA4QrA8rxxqxwqhb0bXPbB5KNsr6AiBuNNDidWVJ6jAeRmFpId7cvMDEbBSgyIV9aVHla7tUwyO3VKZLGTf9mTk6LN1bf406mJqFofZIgULRBZ3mB6oizy5FOkCjsUnPDqyqYbydycH461wcs4OQk69iWts61bj8pY1238HifD%2BE86Wfka%2Bj7g4XmDJ3j2mlKds%2BUM8JQYMMeI7M4GOqUBInOABg63AxO%2BOKH%2BtuAGajS1EiIjnIQRKale0Fw00qvK%2BWVqx%2F79iqwK0DI4G8f%2FcSlzkYDHEMAWAv6FRu%2BtWRrRI%2F4dzNBBHw%2BIr7X68U%2FiAySQpBuN5hl17lLI56%2Fl11eWsmhBcoFCO8ZZ3%2BVom5DDFP%2B2AY12mznjcHX2O8MaIS15Q6RKNEJ5exJBfvFCJ3pObIwQVoYsZBPTyS8c2%2FgabIQC&X-Amz-Signature=c9a1a97af2bf9ea5423ac3efd996a3cdb21c91b5878cc3067a11b852c69d0bc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



