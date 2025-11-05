---
title: 将Windows的文件夹设置为共享文件夹（设置SMB共享）
date: '2025-10-31T10:22:00.000Z'
lastmod: '2025-10-31T10:27:00.000Z'
draft: false
categories:
- 其他
---

### 步骤一

1.  打开「控制面板」→「网络和共享中心」→「更改高级共享设置」
1.  启用：
   - 网络发现
   - 文件和打印机共享
### 步骤二


1.  选择需要共享的目录
1. 右键 → 属性 → 共享 → 高级共享 → 勾选“共享此文件夹” → 设置共享名

### 步骤三


在ubuntu服务器中运行:

```docker
sudo apt install -y cifs-utils
```













## 0. 打开tmux, 切换双终端进行操作
```bash
# 创建tmux会话
tmux
# 创建分屏显示
$ctrl + b 再按 %
$ctrl + b 再按 ⬅️ or 👉
```

## 1. 运行监控脚本

```python
/home/ai-dev/pan/myscript/myenv/bin/python3.12  monitor_mirror_v2.py -s ~/pan -b haohong/pan
```

- -s表示本地目录
- -b表示bucket桶的位置

## 2. 运行上传命令

```bash
mc mirror /home/ai-dev/pan myminio/haohong/pan --overwrite --retry --ship--errors
```


---



```markdown
# 批量上传文件到MiniO

## 一、将Windows的文件夹设置为共享文件夹（设置SMB共享）

### 步骤一
1. 打开「控制面板」→「网络和共享中心」→「更改高级共享设置」
2. 启用：
   - 网络发现
   - 文件和打印机共享

### 步骤二
1. 选择需要共享的目录
2. 右键 → 属性 → 共享 → 高级共享 → 勾选“共享此文件夹” → 设置共享名

### 步骤三
在ubuntu服务器中运行:
```bash
sudo apt install -y cifs-utils

# 创建挂载点
sudo mkdir -p /mnt/TestWindowsShare

# 临时手动挂载测试（替换 IP 和路径）
sudo mount -t cifs \
  "//10.36.67.49/qc_data" \
  /mnt/TestWindowsShare \
  -o username=Administrator,password=123,dom=WORKGROUP,vers=2.0,iocharset=utf8
```
检查是否挂载成功: `ls -la /mnt/TestWindowsShare`

---


## 0. 打开tmux, 切换双终端进行操作
```bash
# 创建tmux会话
tmux
# 创建分屏显示
$ctrl + b 再按 %
$ctrl + b 再按 ⬅️ or 👉
```

## 1. 运行监控脚本

```python
/home/ai-dev/pan/myscript/myenv/bin/python3.12  monitor_mirror_v2.py -s ~/pan -b haohong/pan
```

- -s表示本地目录
- -b表示bucket桶的位置

## 2. 运行上传命令

```bash
mc mirror /home/ai-dev/pan myminio/haohong/pan --overwrite --retry --ship--errors
```


```

