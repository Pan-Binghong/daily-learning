---
title: Linux基础知识及操作
date: '2025-02-27T02:22:00.000Z'
lastmod: '2025-02-28T01:53:00.000Z'
draft: false
tags:
- Knowledge
categories:
- 知识
---

> 💡 Linux操作系统中文件与目录相关的知识。

---

## 1.Linux文件基本属性

在Linux中通常使用chown 和chmod 修改文件或者目录所属用户与权限:

- chown 修改所属用户与组。
- chmod 修改用户的权限。
上图表示，通过chown来授权用户，通过chmod为用户设置可以开门的权限。



在Linux中通常使用ll或者ls -l命令显示一个文件的属性以及文件所属的用户和组:

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6XYX2O%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4erWDZh5eKtbJabH6qx0ZAhtk0ISy3WtcKmy0vr573gIhAIOBDjAObVF2r7LJ3JjqnjL8yqPyNevGNNMgQLi6ICCeKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOee8p6iu95GxP%2FVkq3APZehSgFweRJCH4MhLyAqgeOp%2FVkqk%2F4Gl%2FatH2mXVVR5QDDIakA2%2Byy4gCTlNUgg3WVrPK4366s%2BWwAI0x1xE%2BOVLuu2L49HOcygz6BYGD40NFZ611Ne3E%2BnLG5dWZLFn4Z3wi%2BYVAGaD53UjnRg7dReY%2BFhcy4VbGTSqK3CpRlmnJNaX5ePQEx5bvd7SUvumb3Rg3rYiusqN%2BJpVkB0ICvNtDN%2FRrxyiDB1rzXdoZ1teE3SiVMkj6ISlaYqZLEzxNnN51XXDiwKVHN7VeepsfE0xkdRtSKp63CbarFKNGPEij8wmaG%2FtFIEChg%2B24YfANLtsNEdb3c8w3e1yQucriuQouqOxhpOqokhJSptJraCHL6vHeQhmu0TLTBd21EofdMBruIG411V2YKsTSXfHqAfQZQEtkpTeic6TMRh0wyfXSPrpsH4HV3JRjilCAKghq%2BqOPHBjpahqj3eYtrdcE1kGeyqlQ1It3OiR1nhCtubJVPAIkmF8Hn08Igi%2FntspLPEHbn1tlMTh1dBPTjjuBBG6Ndw4GcReQyxl8Oz5FLVA4epMGiAKjfSaNWZLqu1A6EzNtu7l8oAv%2F3RzHu2NHQkw34ArJfa3O5orjou0p9IgvvMdrBh1U5oGRTTC4mJ7NBjqkAZHo2napjtN%2BTfpChY6RcPi0oppXomcFha6gT9Vzkv%2B9xo4NtcQ9Y7jJAXUttPiYCRFCnot7WkueLZTZ%2FS2DuU1VDlPFvUY5VS1It8V4k%2FMoIwfl581iRONmWkXNwd3P7aDwMP4FodCXpCyE53rHz%2B1j2xpHYL6rugUXXExJE0H1qd%2FpAC%2F5iCJEucOYnAmsUTZABCjzzm%2Bnn2ByW1uJSPPOpwKo&X-Amz-Signature=6b5f0e28445374e48815f903a96a370b6de715d3fed9cbed9c55c989c5a8af8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN6XYX2O%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4erWDZh5eKtbJabH6qx0ZAhtk0ISy3WtcKmy0vr573gIhAIOBDjAObVF2r7LJ3JjqnjL8yqPyNevGNNMgQLi6ICCeKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwOee8p6iu95GxP%2FVkq3APZehSgFweRJCH4MhLyAqgeOp%2FVkqk%2F4Gl%2FatH2mXVVR5QDDIakA2%2Byy4gCTlNUgg3WVrPK4366s%2BWwAI0x1xE%2BOVLuu2L49HOcygz6BYGD40NFZ611Ne3E%2BnLG5dWZLFn4Z3wi%2BYVAGaD53UjnRg7dReY%2BFhcy4VbGTSqK3CpRlmnJNaX5ePQEx5bvd7SUvumb3Rg3rYiusqN%2BJpVkB0ICvNtDN%2FRrxyiDB1rzXdoZ1teE3SiVMkj6ISlaYqZLEzxNnN51XXDiwKVHN7VeepsfE0xkdRtSKp63CbarFKNGPEij8wmaG%2FtFIEChg%2B24YfANLtsNEdb3c8w3e1yQucriuQouqOxhpOqokhJSptJraCHL6vHeQhmu0TLTBd21EofdMBruIG411V2YKsTSXfHqAfQZQEtkpTeic6TMRh0wyfXSPrpsH4HV3JRjilCAKghq%2BqOPHBjpahqj3eYtrdcE1kGeyqlQ1It3OiR1nhCtubJVPAIkmF8Hn08Igi%2FntspLPEHbn1tlMTh1dBPTjjuBBG6Ndw4GcReQyxl8Oz5FLVA4epMGiAKjfSaNWZLqu1A6EzNtu7l8oAv%2F3RzHu2NHQkw34ArJfa3O5orjou0p9IgvvMdrBh1U5oGRTTC4mJ7NBjqkAZHo2napjtN%2BTfpChY6RcPi0oppXomcFha6gT9Vzkv%2B9xo4NtcQ9Y7jJAXUttPiYCRFCnot7WkueLZTZ%2FS2DuU1VDlPFvUY5VS1It8V4k%2FMoIwfl581iRONmWkXNwd3P7aDwMP4FodCXpCyE53rHz%2B1j2xpHYL6rugUXXExJE0H1qd%2FpAC%2F5iCJEucOYnAmsUTZABCjzzm%2Bnn2ByW1uJSPPOpwKo&X-Amz-Signature=a980867ca7f898daf2363c04dd1e5e86bcfdda8df62f24887cf4db04a499d50a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### Linux文件属主和属组

1. 对于文件来说，它都有一个特定的所有者，也就是对该文件具有所有权的用户。
1. 文件所有者以外的用户又可以分为文件所属组的同组用户和其他用户。
---

### 更改文件属性

1. chgrp 更改文件属组
1. chown 更改文件所有者(owner)，也可以同时更改文件属组
1. chmod 更改文件9个属性
---

### Linux链接概念

Linux链接分为两种，一种被称为硬链接(Hard Link)，另一种被称为软链接(Symbolic Link)。

- 硬链接
- 软链接
- 实验
---

## 2.Linux文件与目录管理

1. 处理目录的常用命令
1. 文件内容查看
---

## 3.Linux用户和用户组管理

### 用户账号管理

1. 添加新用户账号
1. 删除账号
1. 修改账号
1. 用户密码管理
---

### 用户账号组管理以及批量创建用户

https://www.runoob.com/linux/linux-user-manage.html

---

## 4.Linux磁盘管理

### df

```bash
df [-ahikHTm] [目录或文件名]

#e.g.
df
# 将系统内所有的文件系统列出来

df -h
# 将容量结果用GB/MB格式显示

df -h /home
```

---

### du

du命令也是查看使用空间的，但是与df命令不同的是Linux du命令是对文件和目录磁盘使用的空间进行查看。

```bash
du [-ahskm] 文件或目录名称
```

---

### fdisk

fdisk是Linux磁盘分区表的操作工具。

```bash
fdisk [-l] 装置名称
```

---

### 磁盘格式化

```bash
mkfs [-t 文件系统格式] 装置文件名
```

---

### 磁盘检验

fsck（file system check）用来检查和维护不一致的文件系统。

若系统掉电或磁盘发生问题，可利用fsck命令对文件系统进行检查。

```bash
fsck [-t 文件系统] [-ACay] 装置名称
```

### 磁盘挂载与卸除

e.g.挂载移动硬盘

```bash
lsblk # 查看磁盘信息
mkdir -p /mnt/usb # 创建挂载目录
mount /dev/sdb1 /mnt/usb #挂载
df -h # 检查
```

```bash
umount /mnt/usb # 退出挂载
```

---

> Reference









