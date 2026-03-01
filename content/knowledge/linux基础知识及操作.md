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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXSJHOYX%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FHi9WJzWkqAuORRwEhEmORkUJ0ujBWvwztlRwiS5i9gIhAPlrsQiGQDY%2BEpJHQyTrx%2FZqAxenga33MX%2B4NiwVEH9rKv8DCGQQABoMNjM3NDIzMTgzODA1IgxhHWbJHPtRyH%2FaNAgq3ANA7xK4zxlT4V4lg9Iqbb50HpKNTwFK39bvEIHe9wvUOTgHxpux9L%2B%2F%2FAdzAYNE1JxZylHgrDfKBTXsXE6q3rObh8nJGTSF2UCQUOrhBphm8cgg0v5UjHnzsi4fYiztTxfsxEQ63aLuZduHQG1ecUaFhaDfuLyVWxAdlo3Oet58xm0XzEn5%2BILCscRks5qY1XmGJdndgU9rg%2Bra5gup3M9miaFQ9wSeUL6e9eX1odH9XKUXHMSaZXohX%2B6YIvuVV77yU5D%2BPEfLOeQPbvaZiKYtfpZRHI78IHAbZqeGoN%2BaAlnmx58icvUoeqVFGSA5ugiaQAA%2BGwXMrzj7xnYK%2FcaJKcjj2iZHEFS%2FI%2BW0PvPUH3rfqZ07cXntnAnBQjLeiweqUXQFlY4WiL%2BGPnZsjNA3Ne12Z%2BAuB2r7uqbpChHf0elWH0J0SJ%2FM9i7J33X90WE6IecIva2gRzqzp5fPtG4FpohT%2FfZ7I%2BkO0F55hiV7VAg%2Bvaa9aDaNJkbq3MAxM16nDz0zFRYpXu9bSmlOZNUiCsC3ucWHISEtA4A4g6CcDqhkqsJE7xN5Qe%2B00XYW%2B8U2UAw1BkKjjSmU0bIBAjVYUrRG4YlTw1w%2F%2Fg7yAgR8RJ0n02OaCw6sD7n02zCTzY7NBjqkARespnRp2m2dB%2FMdO9cZrG6THFAzBnumLJFGiWOgbv8Mc4fObEYoY1aHl09atSG%2FyOdMZGLcuoIfR6L9ThbWlT2SaVmRMR%2FIUxpg8Pzm9Z9S9NfVCkBRDfqZoP8D40ZuAuKaC0H9daVL6mIS4ORTPP39pg5NvvBGP7bH3tL1nld57BHYa1%2B6b88gxa8YXCrskxhhC1NG0p0%2B%2Bgpf7%2Fy8DbFWXG2O&X-Amz-Signature=d4314e2bf495b550ca2a77a1c65cdb6f0702cf9935d432a6e67925cf19d3fff0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXSJHOYX%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2FHi9WJzWkqAuORRwEhEmORkUJ0ujBWvwztlRwiS5i9gIhAPlrsQiGQDY%2BEpJHQyTrx%2FZqAxenga33MX%2B4NiwVEH9rKv8DCGQQABoMNjM3NDIzMTgzODA1IgxhHWbJHPtRyH%2FaNAgq3ANA7xK4zxlT4V4lg9Iqbb50HpKNTwFK39bvEIHe9wvUOTgHxpux9L%2B%2F%2FAdzAYNE1JxZylHgrDfKBTXsXE6q3rObh8nJGTSF2UCQUOrhBphm8cgg0v5UjHnzsi4fYiztTxfsxEQ63aLuZduHQG1ecUaFhaDfuLyVWxAdlo3Oet58xm0XzEn5%2BILCscRks5qY1XmGJdndgU9rg%2Bra5gup3M9miaFQ9wSeUL6e9eX1odH9XKUXHMSaZXohX%2B6YIvuVV77yU5D%2BPEfLOeQPbvaZiKYtfpZRHI78IHAbZqeGoN%2BaAlnmx58icvUoeqVFGSA5ugiaQAA%2BGwXMrzj7xnYK%2FcaJKcjj2iZHEFS%2FI%2BW0PvPUH3rfqZ07cXntnAnBQjLeiweqUXQFlY4WiL%2BGPnZsjNA3Ne12Z%2BAuB2r7uqbpChHf0elWH0J0SJ%2FM9i7J33X90WE6IecIva2gRzqzp5fPtG4FpohT%2FfZ7I%2BkO0F55hiV7VAg%2Bvaa9aDaNJkbq3MAxM16nDz0zFRYpXu9bSmlOZNUiCsC3ucWHISEtA4A4g6CcDqhkqsJE7xN5Qe%2B00XYW%2B8U2UAw1BkKjjSmU0bIBAjVYUrRG4YlTw1w%2F%2Fg7yAgR8RJ0n02OaCw6sD7n02zCTzY7NBjqkARespnRp2m2dB%2FMdO9cZrG6THFAzBnumLJFGiWOgbv8Mc4fObEYoY1aHl09atSG%2FyOdMZGLcuoIfR6L9ThbWlT2SaVmRMR%2FIUxpg8Pzm9Z9S9NfVCkBRDfqZoP8D40ZuAuKaC0H9daVL6mIS4ORTPP39pg5NvvBGP7bH3tL1nld57BHYa1%2B6b88gxa8YXCrskxhhC1NG0p0%2B%2Bgpf7%2Fy8DbFWXG2O&X-Amz-Signature=1b2b3ba90e41546e13db9a04194e5140dc22ec040024e0a234763250fe145137&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









