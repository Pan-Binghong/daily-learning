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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZGXRZVM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVEaTr8bBDAA0695NX1ZJP4PpZ3pCpk2QDpxcVdEQ1cQIhAIB%2FTisql4obIRaTnUCbDbIE2szUbcNQn8JD5xwLluIxKv8DCH8QABoMNjM3NDIzMTgzODA1Igy%2Boh6tUear7q%2FhPvsq3AP%2Fds1UYTf7q%2F8BH97Pp9ntigiJokPMWeIjOlZQa6cF%2FxrjUeYWQXxcw5C9KpdmchGJgaM4xwia8r1pZ8Lk1bdLDa5LXW5U%2FSwq1RmJanf4o5LW7EzBxtjYbGmQjkKMGttw%2FzlUlMOUS58JpCGStD2ITwAZ6GXmV980c9FXUn6%2Bs6ZArMBAFozR4KxyKlCKHwtKDfH8qcxveBmdt%2BpN4dTwQL0MR43Vf%2FSYHjj4%2BFv7HYfp8OJopnYa8H%2BihzFPxT2ylizbRKsPrHwaHAYut%2F%2B%2FtXK5fl%2Bq8mUPu0CVjS6KSwysuABP2wgz6hTMBD16E535dQe%2FGLUIt%2FZHSk567PBSqVAeuP%2FpJoHyiToCNVqNL%2BXD4y5oVDR2aWMqtKYsbPj%2B9EeNi%2FCDBzEDbY1DtGo9yQ73weEbkBrQHQalOreJw2CpDxXPnTAqeq36KZFYvB2300wJWN9sueSXsngE6vnvKk5uXfP6bSCVP%2Biyb6Bshrs8YGWWooDVOtveP5a8suzNn4AX%2FVVOkBp9YkenKXwzAnd9tgmMwUUV2UhtYqQm%2FWQEsiQeZzvPZlLuqfKS%2Ff1DzOds0CC3Qa1wvUhZ2qriJ1UFOxDT5fm4LXyOULNzldAsMsJTxEYLMjppejC%2Br73OBjqkAUbxx%2FlYPKKamaJhkde3RTWX3FmT%2BIoEm0xcNiq1W17oJMhcBkEgEvW5LFP3T05O4i4DbqCk5639Z85KLZwZVe85oDJCdehf6C1XhQGG0MgYNbEmp%2BCyXCq8eV6%2BWuSFgrv58YeNpaRhobBqV5mjbYhthX5Q%2FSDf9VB%2FYLrDCO1x%2Bm64eZpcKaA9t937WE0%2FuQGMiTTGptN9t2FGox4E6kHS2v%2Fj&X-Amz-Signature=3a4b910d3b5cf18e65d992ab220f049ef5b2f71b6bf87dbe1ba2ebb0b91cd38e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZGXRZVM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVEaTr8bBDAA0695NX1ZJP4PpZ3pCpk2QDpxcVdEQ1cQIhAIB%2FTisql4obIRaTnUCbDbIE2szUbcNQn8JD5xwLluIxKv8DCH8QABoMNjM3NDIzMTgzODA1Igy%2Boh6tUear7q%2FhPvsq3AP%2Fds1UYTf7q%2F8BH97Pp9ntigiJokPMWeIjOlZQa6cF%2FxrjUeYWQXxcw5C9KpdmchGJgaM4xwia8r1pZ8Lk1bdLDa5LXW5U%2FSwq1RmJanf4o5LW7EzBxtjYbGmQjkKMGttw%2FzlUlMOUS58JpCGStD2ITwAZ6GXmV980c9FXUn6%2Bs6ZArMBAFozR4KxyKlCKHwtKDfH8qcxveBmdt%2BpN4dTwQL0MR43Vf%2FSYHjj4%2BFv7HYfp8OJopnYa8H%2BihzFPxT2ylizbRKsPrHwaHAYut%2F%2B%2FtXK5fl%2Bq8mUPu0CVjS6KSwysuABP2wgz6hTMBD16E535dQe%2FGLUIt%2FZHSk567PBSqVAeuP%2FpJoHyiToCNVqNL%2BXD4y5oVDR2aWMqtKYsbPj%2B9EeNi%2FCDBzEDbY1DtGo9yQ73weEbkBrQHQalOreJw2CpDxXPnTAqeq36KZFYvB2300wJWN9sueSXsngE6vnvKk5uXfP6bSCVP%2Biyb6Bshrs8YGWWooDVOtveP5a8suzNn4AX%2FVVOkBp9YkenKXwzAnd9tgmMwUUV2UhtYqQm%2FWQEsiQeZzvPZlLuqfKS%2Ff1DzOds0CC3Qa1wvUhZ2qriJ1UFOxDT5fm4LXyOULNzldAsMsJTxEYLMjppejC%2Br73OBjqkAUbxx%2FlYPKKamaJhkde3RTWX3FmT%2BIoEm0xcNiq1W17oJMhcBkEgEvW5LFP3T05O4i4DbqCk5639Z85KLZwZVe85oDJCdehf6C1XhQGG0MgYNbEmp%2BCyXCq8eV6%2BWuSFgrv58YeNpaRhobBqV5mjbYhthX5Q%2FSDf9VB%2FYLrDCO1x%2Bm64eZpcKaA9t937WE0%2FuQGMiTTGptN9t2FGox4E6kHS2v%2Fj&X-Amz-Signature=495204ebba735a7c1ee6f6d4e2f3c6c94e37a101b8a81af91fe6b6d385d53ca4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









