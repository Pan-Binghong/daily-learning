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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLPMCYKZ%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQC3Mhz2h9jB%2BKB7l%2BaZuz6Fck8A%2FxDlUCLL2Lep%2B1iQrQIgOLn%2Fo%2FcWuTUj%2BZAfLeu%2Bnju9NiNq1FRT9JSWo90UgScqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnPtvlmU3ML8Y63uCrcAyqWBpnRgU759Gub0csw31Iebivqtixhpqhmzv4p%2Fnu6VBVqEqHjnPmeX%2FTvvrpmiEYpJnW%2FPk%2BEt4mJb3M16GH%2BlZlnxoH8i5%2FQu1b1IkJ%2BsS7Y%2B7%2BP%2FL6C5wA6bJOMATYnPv4xj6fYDx%2F6r7TgTPDaUUEXqJAgHRzFVAJQRYs6BgvPmTSlY6CV2amXFSZx%2Fs8FT9LymFG%2FJxEm4GjHQ0iOuZReVXD6sEoKs0brEzhNo1qlQiFMotWq1l%2F%2BLkCKAa1VmYTmWrDUaaJMNbhrU6IRxbY1AXhAS8ojy%2BiWMTfzzA5T8Ri1uyTqjGn4aZN9%2F7DUkcPA0ZzmGlAOVRprdaO1WFl8wooVFD%2BGsnYXBNdTBVpBDPLbhN95D1SJ2o4qK7vCTPoumMAmy6muB60dGG31i%2B5mXdE%2BJeSDKDX13EXtyRbJMu9yFVrUpD0kejI9bD%2BpD4%2Frqv%2BdotH1E1mf%2BZksmXYW8Gew9vIcDAerHaKkoj3zRZf1GsHwjD2IiYGrp6MbkesUoLNwh2aeCmN0%2F%2B%2FY58qLRHmqQa3HdwjML%2FcQoWRMez%2Fqg1hkdQ%2BAgVLd0lUUWDqB5u98r0x9BioEJHPEzT%2BWvZmdNTrK5sdg1Lfl2T%2B77w7Nh9agHF%2B7MKvq%2BcgGOqUBHYeZZqBoy5EY%2BVZ0ungvS0AfoSOdRDMebj0V0GW4SN0T7077YQNyS%2F7FlVwTua4KUSGWc5pb4M1%2BCT%2B2xZYq9Q5R5ehBVRHHCvPhEaX4CBYVKFBMVxOchiL8DQb97dfE%2Fb6ENSntka5H9pbjiO3rfX9VpjY6BTAFvYRrAAyUjV1%2FMwCHBhaOZQs%2BK5fcI7rdKJHjJixwXsz5XCJHEN02KYPv%2FdA2&X-Amz-Signature=25d32764dca70d94782cb964e95807402a037b6b60ebf5210c8fc0ced6fe409a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLPMCYKZ%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQC3Mhz2h9jB%2BKB7l%2BaZuz6Fck8A%2FxDlUCLL2Lep%2B1iQrQIgOLn%2Fo%2FcWuTUj%2BZAfLeu%2Bnju9NiNq1FRT9JSWo90UgScqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOnPtvlmU3ML8Y63uCrcAyqWBpnRgU759Gub0csw31Iebivqtixhpqhmzv4p%2Fnu6VBVqEqHjnPmeX%2FTvvrpmiEYpJnW%2FPk%2BEt4mJb3M16GH%2BlZlnxoH8i5%2FQu1b1IkJ%2BsS7Y%2B7%2BP%2FL6C5wA6bJOMATYnPv4xj6fYDx%2F6r7TgTPDaUUEXqJAgHRzFVAJQRYs6BgvPmTSlY6CV2amXFSZx%2Fs8FT9LymFG%2FJxEm4GjHQ0iOuZReVXD6sEoKs0brEzhNo1qlQiFMotWq1l%2F%2BLkCKAa1VmYTmWrDUaaJMNbhrU6IRxbY1AXhAS8ojy%2BiWMTfzzA5T8Ri1uyTqjGn4aZN9%2F7DUkcPA0ZzmGlAOVRprdaO1WFl8wooVFD%2BGsnYXBNdTBVpBDPLbhN95D1SJ2o4qK7vCTPoumMAmy6muB60dGG31i%2B5mXdE%2BJeSDKDX13EXtyRbJMu9yFVrUpD0kejI9bD%2BpD4%2Frqv%2BdotH1E1mf%2BZksmXYW8Gew9vIcDAerHaKkoj3zRZf1GsHwjD2IiYGrp6MbkesUoLNwh2aeCmN0%2F%2B%2FY58qLRHmqQa3HdwjML%2FcQoWRMez%2Fqg1hkdQ%2BAgVLd0lUUWDqB5u98r0x9BioEJHPEzT%2BWvZmdNTrK5sdg1Lfl2T%2B77w7Nh9agHF%2B7MKvq%2BcgGOqUBHYeZZqBoy5EY%2BVZ0ungvS0AfoSOdRDMebj0V0GW4SN0T7077YQNyS%2F7FlVwTua4KUSGWc5pb4M1%2BCT%2B2xZYq9Q5R5ehBVRHHCvPhEaX4CBYVKFBMVxOchiL8DQb97dfE%2Fb6ENSntka5H9pbjiO3rfX9VpjY6BTAFvYRrAAyUjV1%2FMwCHBhaOZQs%2BK5fcI7rdKJHjJixwXsz5XCJHEN02KYPv%2FdA2&X-Amz-Signature=2c0eb7335151cdd4a375a4ab9fd264b86ebfba98f5f309433b2a188ba1827851&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









