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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI4KPKUW%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE46%2FArec9x5OHljChEeS1tRlqvL%2BS7EzBCjpunN3ru3AiEA7uA5gbPnsthbZACnTKys15aOH2rpQBKo1%2FwrauQv%2B%2FsqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFYtDQlIRlVknAcmCrcA5L0ugkKoUpwjgBhfBnMIsk%2B75LSvI4gPoAmattsWus2kQTeqhW7vrQUBYkYmQFILaLzstx1LCOFnBVWcSCGdHf0uiUG%2FqS1MjgAZ%2FdDoq%2FNh2TEiETlRJKkz4G5Rv0DaHn4aq8M2sm5FUsk6NmIDHciiKgWcXaoMbHie8bzCqGv7p6rZulYZNA4unN2dg216mjG4V2gITm8sk9%2FCSh2ZW1BKQ6RzX%2Bc8yEauc9wLMgtvxbNH%2BxxQVhtlwyuy25qZTxtE9wkI1LdbWsVacEVmvng4uSbaV07MwBA%2BNv1SXXMLDXpmYKo%2FQM6tdcV5ucE%2FQQ7baIPYpVgJHiX9vPQpAtYRheSNJZXuSt5T4U6cyluahjrJdPEcwsI5%2Fv4SVIiEk6ARCTWDrViNNPuaMjFNqWVsBMr%2B8qZc8uc5ZmmZ%2FgwtvFbn3hZQhesHFlfIWfK4gfDvGVweXrUoVfkT6EFzA8AShnyisCTmXj2oa%2F66k8KxKXHgrhHCUyktUwDESQm3JqlGIwqoyc2EIxorChFkpY1J2voROfEuVXFaQecSsqd3lkcafDL8KMNxBXGPjYkve1wrM2zqPYhBynJ9aA7ZHvMjSOVuzp8UaZtwFYwOoZCsXBdBykVXPOIjrlNMN7fo80GOqUBpKzf2H9G98PYBs9cOzlAmXzF0rKOqvZ1pm7fN1PwNIT0qT02N7mQej1dD6uhGVub1y6K8beLEGCiLw4tsybBVBQknyxp54g1qo7rFhAzhd225LnVRZ%2Fp48SQMHz%2BEgdFagTtOD%2FtcZilp%2BWI9zoEq2zdipYWZ5hmwBijtQZP6mFUsTABFiSruG5LgSoXOxFl2rOve%2Bsoo70cz6jGTmGym3w3VySP&X-Amz-Signature=07b24060c5b8551164afedfee26e9dcb58bea294c5eb621b02d7f650029381ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



