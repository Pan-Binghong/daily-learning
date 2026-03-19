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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HMKKLAP%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA8%2FJeltgQeQ0xQxUNBi1yggEwt7xWek3T459ttmkulwAiEAhaKmfnUW%2BT%2B2w%2B0MsZS90z6l3JTwBK6CP2SDrZCPU4Iq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDETVtSXh3XhXctsC4CrcA%2FnT6G08JeqVa7zXPC80R7jOxxRWal24lK1Z55my67OssXQRq2hkJNx9vEiLlnpNR51yS7M5Yb0igxGV8VHx08AB1v8QyDVlgTqpztXw4C4wTseoUm7cJ0Lh3pgaETOoKehhoyQL8jMD3ptrjfvIyb0ORu5yBLaih5oACs3ddI1G7vY8YqBk72uGfOIRKN3ovSvl7%2BAUd8%2BclQEAU9tfNIt0Hw4hUh3Mb0%2B9gNz1yTh%2F%2BJ%2BNVW3wDIgMlBXhgkeFpxUylnsItBmHC8mvt1VoWgJIGWqN7kUi5jZFcKoRVaRyK2B6dKIugLHtXdNBVxeipUkOvOR5P7BkgrZO4A2rhJDyyYRrISHmTv2EAlkjYvL5PI2agNcdFlXTObOviY%2BsV3BejRmNDYlmHTWtagUdVkI6y9CB8aSDuuJ922NQZXgzW2EuVUF1Iic0vXSGZSzTFDwCyCI0LQ4WqGaNpgqs0AZQJ0k4Zn%2FRqDxKn%2BOEXjq8MuW4Kn6g1vc8mBqPSJdGnJ5ph0QIY229c2wu1XakaLihzLI7ahMhVTDbryWvnq%2B6d2HsKDjFeRH4SoY7xOlvMpkFrNvPYvoGuKuSlCupIhSvt9I7t7FcB4OgixfX0rdL0CCphC3Hwxm%2BnICHMJLI7c0GOqUBa3ERpBFb6l4cTYaRHtaPYMe9D1xsTYN6qaP3vVx7TYA6B%2FUNuoW2nGRSLDtb6V1pJg6oitwJ9EW8M0lE1q%2FMJ4yTWqrwHcO8l6Gwrf0NvJ9cOOHopHHlY1C0%2BSYYwAcxTAOaTFQDLuktwRkiTb30qyqBpV5nihjW6NrJ0XjW8QSLPIwSAknaKq2gvquRpcs9X7cyLzeP%2BAkwiHDeN2bk6ieRHQhO&X-Amz-Signature=a01d795259414aed07ba33b4294d8359b6c968878b162831fdca124524419bb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HMKKLAP%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIA8%2FJeltgQeQ0xQxUNBi1yggEwt7xWek3T459ttmkulwAiEAhaKmfnUW%2BT%2B2w%2B0MsZS90z6l3JTwBK6CP2SDrZCPU4Iq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDETVtSXh3XhXctsC4CrcA%2FnT6G08JeqVa7zXPC80R7jOxxRWal24lK1Z55my67OssXQRq2hkJNx9vEiLlnpNR51yS7M5Yb0igxGV8VHx08AB1v8QyDVlgTqpztXw4C4wTseoUm7cJ0Lh3pgaETOoKehhoyQL8jMD3ptrjfvIyb0ORu5yBLaih5oACs3ddI1G7vY8YqBk72uGfOIRKN3ovSvl7%2BAUd8%2BclQEAU9tfNIt0Hw4hUh3Mb0%2B9gNz1yTh%2F%2BJ%2BNVW3wDIgMlBXhgkeFpxUylnsItBmHC8mvt1VoWgJIGWqN7kUi5jZFcKoRVaRyK2B6dKIugLHtXdNBVxeipUkOvOR5P7BkgrZO4A2rhJDyyYRrISHmTv2EAlkjYvL5PI2agNcdFlXTObOviY%2BsV3BejRmNDYlmHTWtagUdVkI6y9CB8aSDuuJ922NQZXgzW2EuVUF1Iic0vXSGZSzTFDwCyCI0LQ4WqGaNpgqs0AZQJ0k4Zn%2FRqDxKn%2BOEXjq8MuW4Kn6g1vc8mBqPSJdGnJ5ph0QIY229c2wu1XakaLihzLI7ahMhVTDbryWvnq%2B6d2HsKDjFeRH4SoY7xOlvMpkFrNvPYvoGuKuSlCupIhSvt9I7t7FcB4OgixfX0rdL0CCphC3Hwxm%2BnICHMJLI7c0GOqUBa3ERpBFb6l4cTYaRHtaPYMe9D1xsTYN6qaP3vVx7TYA6B%2FUNuoW2nGRSLDtb6V1pJg6oitwJ9EW8M0lE1q%2FMJ4yTWqrwHcO8l6Gwrf0NvJ9cOOHopHHlY1C0%2BSYYwAcxTAOaTFQDLuktwRkiTb30qyqBpV5nihjW6NrJ0XjW8QSLPIwSAknaKq2gvquRpcs9X7cyLzeP%2BAkwiHDeN2bk6ieRHQhO&X-Amz-Signature=3d006de0bb762a04cf3625e008bc0e9a9ca0078fb39d49574c860cb9b14c0371&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









