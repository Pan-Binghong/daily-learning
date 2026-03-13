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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/51b10173-0dab-4609-b924-ab711d4dee62/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S5PJI5L%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBII6%2Fmp9sXFA9GwiyYs%2Fk2i1Yhncper6ll2YMpXIyB3AiEAxGQPAwRVSnVlAPnfpgEf1R61NyY2Vc9jXHMIXHCy8%2BwqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGuWZoST4Wi21Tr38SrcA4JEAE1ogKlwN3hGMt3%2F4UV3QnvpeMZjlGpLGbTX7mDnkTRWAkXgfyHcPmbZjsuI%2FMT5tAA4PbDOBey3dd0o0JRvYfwOnQbGRtn21e1PVIH2YXzySXGhvUIrK9pnUvtCmY96xcWQRE5ZfqFhWRDgVtrmSZ83t4YXXFAR7kI3snrL1dPpslqvbnf%2FdqVInbD59OGkJJnkUNOs79vUh9BFgl1Gi8Y3oa%2BJTMtBweHmL44kW8GY4UD%2BAd42d2WCtmFWdtk%2FgY309pqveZq0z9b3gGyZtcv9MlLuLq554t%2BGpX6XWQjsBS1KpPXyC%2FEquvfWFtvjJg0jk5%2BidgwCf5UwAoE3%2F0oEGedQ5uahBo9q9UkCbHwQfi82zglMUNT%2Bnza2ZgO5nCZfd9wkitxREk7bNGL2XV%2FeO2SYA1H%2Bgbfa%2BhgdaHoOw3wRWMK5OVumqfQhbZ1xbUh%2F3%2F6y8jwLvKLezqIKxZ1944QvG9fHIiuDKUCaB4KfbcM%2BAmR%2FyWOxMVOyG%2F8UPygFBn7RLuBxqECCSgasdkz99WtfJvx9aaWHwxP0Ke7iaWudlKlVrg9%2B8MMkHsjYKYRBYRGn1%2FfwSwYO%2By13ulnPr0%2B7tjbN455CtB3v%2BQ1tBzyI%2Bri%2FCnj%2FMMq3zc0GOqUBTznH15jUYeD58JacqPafK2HitbDz66VCHJpkc7cVRWb7LdPoMfd783ejVAZsdB%2BsdeN%2FhW3Hbzxdq07OonF37UAxmzNhJb1kd1Gs2YYV4x2njPxWN%2ByflrFwyFNMd0qnaSfBWPfiID4LCW8gmnvUYLy2yM5FvFEXYP0EVDg%2B1cGGowiOhJgrxbZee02sZZt%2ByoW7Vz4fLtKs1lAJqeGr%2FwYnujTr&X-Amz-Signature=3c46058d18490d2f36565f389689650e25c4373c54993a8d0bd6aca564adc83a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



