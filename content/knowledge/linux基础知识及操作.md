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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLF25SMP%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCJaaQ%2FZzoJqgN9B5hV3gGEa2z3mjTwWFahsWBIVgC%2F%2BQIgc9dmAalPpCy7IreAONFd%2FwX9TDq6K8oCEOLJQdubRqEq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHP%2F5ao2w7xBk8yBvyrcA4jwYcz7%2FXzEp8lOMWmeaB4xQJ391LQdfan77%2Bp6Wjo0P8bzrkwFfyn2R6UPUUn%2BUo7gRN%2Bl8Jkox%2FYB6ZoRJtULzyGMQ2vCwz8JrH%2BXVb4FpqzTabbmFgG6fDvjgNILF%2FSCscnfDQjjFOVCq9k2twJyB9KVPECr4Dit%2BAc6S53SjBxj7A1TzrgUxMNLRX%2F%2BLjSNQuw2XLcFJ7IyhLkf8YccIDudmN2%2FnzBwk1Ov7N5OvHnzqXoXKixdXn7R5jrigZNUVZiiSyUuKKVU12VXcl%2FL41Qygt4sOM%2Bn1auxBsAoJCAm%2F4%2BAU%2F3vaTKpGJ2I8AifEk2%2FTMb6hhqlFgJHMN8QS9F35T6QUFA%2BMXek5sSSdyJjEflTOy7%2B6uIu0vfGGjitaPZVp%2Fc897Z8h2sViQlKI%2BH%2F4Uz3Uy2fFRZShaiMauJ9pt4xS%2BklyQklIjegbTIM8AKn4K56h%2BYMbLqLaQbusekojcFrJxaEXwSU4FPANRqnfW0C563NCshcC1IjYc1%2BTgjbk8tao6cggLqjqe%2BavMKcbh87PTarmMUwGdFQAjOTKHNFdNTIJr178yu1d5K8XSvftfLgP4sgaRpjr69t7Sxt5mQXeD1A1pc%2FbtbLf8L0Bqeei5Md3C0WMNfeuMkGOqUB%2BXnj8NmvyAQAdBOMnlP2fT6McX9%2FI14%2Fp0FwNGpCSromd4IPHGTWJuB4BxF%2BkZfeF6fMPEMEvI6OnfE9O3AYMSyTClH9Ju5YQU0Ko5bmFErylhMAZErK9UfPsd%2Fn1HHIh05TIWXBIJj0Wp52eEiHAOLT9Cw1J4Z8WfxlnaL3ocsrJ1Bmp9Xons84%2F2wTfMCW0U3DBWnujeAQYRX9h00bRmshMjMs&X-Amz-Signature=04bdffa48afd908172f9197119bb3836806e8d6b95d857efa990dfd0f807e502&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLF25SMP%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCJaaQ%2FZzoJqgN9B5hV3gGEa2z3mjTwWFahsWBIVgC%2F%2BQIgc9dmAalPpCy7IreAONFd%2FwX9TDq6K8oCEOLJQdubRqEq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDHP%2F5ao2w7xBk8yBvyrcA4jwYcz7%2FXzEp8lOMWmeaB4xQJ391LQdfan77%2Bp6Wjo0P8bzrkwFfyn2R6UPUUn%2BUo7gRN%2Bl8Jkox%2FYB6ZoRJtULzyGMQ2vCwz8JrH%2BXVb4FpqzTabbmFgG6fDvjgNILF%2FSCscnfDQjjFOVCq9k2twJyB9KVPECr4Dit%2BAc6S53SjBxj7A1TzrgUxMNLRX%2F%2BLjSNQuw2XLcFJ7IyhLkf8YccIDudmN2%2FnzBwk1Ov7N5OvHnzqXoXKixdXn7R5jrigZNUVZiiSyUuKKVU12VXcl%2FL41Qygt4sOM%2Bn1auxBsAoJCAm%2F4%2BAU%2F3vaTKpGJ2I8AifEk2%2FTMb6hhqlFgJHMN8QS9F35T6QUFA%2BMXek5sSSdyJjEflTOy7%2B6uIu0vfGGjitaPZVp%2Fc897Z8h2sViQlKI%2BH%2F4Uz3Uy2fFRZShaiMauJ9pt4xS%2BklyQklIjegbTIM8AKn4K56h%2BYMbLqLaQbusekojcFrJxaEXwSU4FPANRqnfW0C563NCshcC1IjYc1%2BTgjbk8tao6cggLqjqe%2BavMKcbh87PTarmMUwGdFQAjOTKHNFdNTIJr178yu1d5K8XSvftfLgP4sgaRpjr69t7Sxt5mQXeD1A1pc%2FbtbLf8L0Bqeei5Md3C0WMNfeuMkGOqUB%2BXnj8NmvyAQAdBOMnlP2fT6McX9%2FI14%2Fp0FwNGpCSromd4IPHGTWJuB4BxF%2BkZfeF6fMPEMEvI6OnfE9O3AYMSyTClH9Ju5YQU0Ko5bmFErylhMAZErK9UfPsd%2Fn1HHIh05TIWXBIJj0Wp52eEiHAOLT9Cw1J4Z8WfxlnaL3ocsrJ1Bmp9Xons84%2F2wTfMCW0U3DBWnujeAQYRX9h00bRmshMjMs&X-Amz-Signature=9e166e77e53ea09ecb75270c009992f728a6c3fa18623e7b3cafe890c84c0fc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









