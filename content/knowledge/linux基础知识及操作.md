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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7W2D4L%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeXM50CMTs8Thvh%2Bd0at08ZriNqe7dGEDmKaGWLU9IlAiEAnmALCGmq11IL5xxc420YR37xgYVOvXEvBVERnDvXrmUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFncNqpX1IJcvM0E4yrcAzlWrYweJPi2Zg7PvBcuj9v5XVyX13%2F8y7Cl5Mqr7Ylf2210pQA0W%2FJXdNRlcd%2BYP9ja%2BMjqbgVR%2BXKYzqGK7PLqIC6pLK1kfwK8xnTTXfnVWkUEMiK0H4ghAh4z3mEyc6bhNNRcHNUBuEVvsqvRvEsctsyIWIBDBuDNAjUwsr69dCNX5CDlrjjSDf6faOJo5%2F0%2BgtuXHkGT4JpiuNVHvy3dnYUCZGDbP98ELrh2nRUWPUBI6gWfK%2BjHTNHps65Hwa9daB7TT4JpPK2JG7hQz3x%2FLyASAcIok60qxbhaCxkTGJVwJa7E9IusK9EZagL%2FKFCNlfCJRlRiP7dNudtcIbdZUj6gv6OD%2B8QZXj2KnufzyuL8PAPg%2BhX3y%2FyFIK4m0aWjr0Ykao9U20OP6qL0w8Hae9jBIyXKRomDUfc5zUDioIpTXQxr%2FlWCu8pGF6g4wvu8GmMlwlHAJfJ1yPUui4sscUJgIc6oSX4XEsw1ygZfv5rKxyce6ezzwKFgEl8ctkLCNtOLgnT%2B0%2BMEHdMxRH6D%2FmbtMqwjoclB74uIri28GCRm8xagrsN4L4dj7pGgKpOX36ErEmjr3CeEtpygDOFIE%2BFmY4i99YSxUF1za2bBbdU41J48cy%2F4O8sAMIzKks4GOqUBV9ZtlIpjE7lgYMJNnfScv%2FIlMs0WWbWqqMsK8JVa%2BaA6a5ClI9uJy9L5uNSzct5QsYag%2FECW9vvuH2NdAU7kZlmM5A6oYtru%2FuCkbKUD%2FBgKm%2F6qZJ2bicDP6n0D0JtTqhlhYAOOYYs8Sk%2FBOE%2FchZbOsNtm1FJ7C6FANgDOjlC2FZcuJKtvK46224fOigiPXP6oWAGHapy3Gnv5V6l%2Fxij6nrUT&X-Amz-Signature=97b690dc4d8dedf07c7622b12c27494bb0a67eb00556565991c9adac0fc756b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Q7W2D4L%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeXM50CMTs8Thvh%2Bd0at08ZriNqe7dGEDmKaGWLU9IlAiEAnmALCGmq11IL5xxc420YR37xgYVOvXEvBVERnDvXrmUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFncNqpX1IJcvM0E4yrcAzlWrYweJPi2Zg7PvBcuj9v5XVyX13%2F8y7Cl5Mqr7Ylf2210pQA0W%2FJXdNRlcd%2BYP9ja%2BMjqbgVR%2BXKYzqGK7PLqIC6pLK1kfwK8xnTTXfnVWkUEMiK0H4ghAh4z3mEyc6bhNNRcHNUBuEVvsqvRvEsctsyIWIBDBuDNAjUwsr69dCNX5CDlrjjSDf6faOJo5%2F0%2BgtuXHkGT4JpiuNVHvy3dnYUCZGDbP98ELrh2nRUWPUBI6gWfK%2BjHTNHps65Hwa9daB7TT4JpPK2JG7hQz3x%2FLyASAcIok60qxbhaCxkTGJVwJa7E9IusK9EZagL%2FKFCNlfCJRlRiP7dNudtcIbdZUj6gv6OD%2B8QZXj2KnufzyuL8PAPg%2BhX3y%2FyFIK4m0aWjr0Ykao9U20OP6qL0w8Hae9jBIyXKRomDUfc5zUDioIpTXQxr%2FlWCu8pGF6g4wvu8GmMlwlHAJfJ1yPUui4sscUJgIc6oSX4XEsw1ygZfv5rKxyce6ezzwKFgEl8ctkLCNtOLgnT%2B0%2BMEHdMxRH6D%2FmbtMqwjoclB74uIri28GCRm8xagrsN4L4dj7pGgKpOX36ErEmjr3CeEtpygDOFIE%2BFmY4i99YSxUF1za2bBbdU41J48cy%2F4O8sAMIzKks4GOqUBV9ZtlIpjE7lgYMJNnfScv%2FIlMs0WWbWqqMsK8JVa%2BaA6a5ClI9uJy9L5uNSzct5QsYag%2FECW9vvuH2NdAU7kZlmM5A6oYtru%2FuCkbKUD%2FBgKm%2F6qZJ2bicDP6n0D0JtTqhlhYAOOYYs8Sk%2FBOE%2FchZbOsNtm1FJ7C6FANgDOjlC2FZcuJKtvK46224fOigiPXP6oWAGHapy3Gnv5V6l%2Fxij6nrUT&X-Amz-Signature=32657ed8c0eb63c8e44f946c44986d9d628a875304cc887ccc6181dbddaff37e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









