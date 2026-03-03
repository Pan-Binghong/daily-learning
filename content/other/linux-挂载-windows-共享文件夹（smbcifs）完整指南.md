---
title: Linux 挂载 Windows 共享文件夹（SMB/CIFS）完整指南
date: '2025-10-31T10:22:00.000Z'
lastmod: '2026-03-02T07:11:00.000Z'
draft: false
categories:
- 其他
---

在 Linux 中挂载 Windows 的共享文件夹，使用的是 SMB/CIFS 协议。下面是详细的操作步骤：

---

## 一、前提条件

1. Windows 端已开启文件夹共享（右键文件夹 → 属性 → 共享）
1. Linux 端需要有 root 或 sudo 权限
1. 两台机器之间网络互通（可以互相 ping 通）
1. 知道 Windows 共享的用户名和密码 [1]
---

## 二、Linux 端安装 cifs-utils

cifs-utils 是 Linux 挂载 SMB/CIFS 共享所需的工具包 [5]。

```bash
# Debian / Ubuntu 系列
sudo apt update
sudo apt install cifs-utils

# RHEL / CentOS / Rocky Linux 系列
sudo dnf install cifs-utils

# 旧版 CentOS
sudo yum install cifs-utils
```

---

## 三、临时挂载（重启后失效）

### 1. 创建挂载点目录

```bash
sudo mkdir -p /mnt/winshare
```

### 2. 执行挂载命令

```bash
sudo mount -t cifs -o username=Windows用户名,password=Windows密码 //Windows_IP/共享文件夹名 /mnt/winshare
```

实际示例（假设 Windows IP 为 192.168.1.100，共享文件夹名为 share，用户名 admin，密码 123456）：

```bash
sudo mount -t cifs -o username=admin,password=123456 //192.168.1.100/share /mnt/winshare
```

> ⚠️ 如果共享文件夹名或路径有空格，需要用引号包裹或转义。

### 3. 验证挂载

```bash
ls /mnt/winshare
df -h | grep winshare
```

### 4. 卸载

```bash
sudo umount /mnt/winshare
```

[5]

---

## 四、永久挂载（开机自动挂载）

如果希望每次开机都自动挂载，需要修改 /etc/fstab 文件 [5]。

### 方法一：直接写密码（不推荐，不安全）

```bash
sudo vi /etc/fstab
```

在文件末尾添加一行：

```plain text
//192.168.1.100/share  /mnt/winshare  cifs  username=admin,password=123456,defaults  0  0
```

### 方法二：使用凭据文件（✅ 推荐）

1）创建凭据文件：

```bash
sudo vi /root/.smbcredentials
```

写入内容：

```plain text
username=admin
password=123456
domain=WORKGROUP
```

2）设置权限（仅 root 可读）：

```bash
sudo chmod 600 /root/.smbcredentials
```

3）编辑 /etc/fstab：

```bash
sudo vi /etc/fstab
```

添加：

```plain text
//192.168.1.100/share  /mnt/winshare  cifs  credentials=/root/.smbcredentials,iocharset=utf8,file_mode=0644,dir_mode=0755  0  0
```

4）使配置生效（无需重启）：

```bash
sudo mount -a
```

[5]

---

## 五、常用挂载参数说明

---

## 六、常见问题排查

### ❌ 报错：mount error(13): Permission denied

- 检查用户名和密码是否正确
- Windows 端检查共享权限设置
### ❌ 报错：mount error(112): Host is down

- 尝试指定 SMB 版本：
### ❌ 报错：mount error(115): Operation now in progress

- 检查网络连通性：ping 192.168.1.100
- 检查 Windows 防火墙是否放行了 445 端口
### ❌ 中文文件名乱码

- 添加参数 iocharset=utf8
---

## 七、总结流程

```plain text
┌─────────────────────────────┐
│  1. Windows 端开启共享文件夹  │
│  2. Linux 安装 cifs-utils    │
│  3. 创建挂载点 mkdir          │
│  4. mount -t cifs 挂载       │
│  5. (可选) 写入 fstab 永久挂载│
└─────────────────────────────┘
```

按照以上步骤操作，你就可以在 Linux 上像访问本地目录一样访问 Windows 共享文件夹了！如果有具体的报错信息，可以贴出来帮你进一步排查。

