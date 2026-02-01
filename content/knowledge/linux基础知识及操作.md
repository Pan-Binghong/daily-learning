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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMM7MXKM%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyCmqVsMh8lyJMI%2BLoPVFcVCoMxvQViqA%2BzCbrzL53PAiBaMi3Wd7TobPvIyZ5xnUXEbjYKFNS%2BsMBog8jDTY%2FfJSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6YeSVkL5N%2BO%2BiPvpKtwDbeV%2B0SW3PS1wkinnMXDdiwJpPwE5McN58k%2FxHflaYWH9oKmvize2QFI8vZVA6uoRJyT7Uk1i8DGZDcbkU4bdnscEiaWl2B7PJnpf4QFNiltwdV7UZUJz4%2BZtN7Gsk8uFax6QvIz2PwVBTcJ1%2BuzEwRhzR4%2BBvXOGEdMLi1PPSlSTYYkCieEpGtE515ESX35VXLPGhz9v%2FP%2BzCzfPB0GBMbt8NgRswenj6SmuqmATOO1lh1nXQb%2F3bkZ5L%2BRlEyGYY0hevdF%2BU%2F2mh1Bqr3F0lWDEUKBdr3Vf6JxROl8Sv1oJzBXld2tzavJ3P%2BuxIu%2BJN8sJOW%2FRaxjY52nDAhY4BqJc6B71ysO1CoYMjd7eykJohJ92li%2BhgUYMp3lRIDFv6b4ufgX5%2FD1L3IyoCtjU90o6RQF95zOh7MY6W6H4rW0fiuB2obu8zJIMUfECDd7q12NRLMGQYfJ0G%2F6Rzs0%2FvyIZ7m90GkS0rero5XXTOgBQ9Rw6pQkJPDSD%2BNzStKhtSzWu9Zel7eBVUvlePL8ZYfIdYc9cD84z9e2w%2FW87Kpl4d2C8XT3LOSjoOzaFrDf%2FHeMh%2B1udsdzZxirICOTK78IdINyU7TSEyyp3LqspK0wWSelIRlqFi%2F94Un0w5Jf7ywY6pgGhD5z0zDESZO1waiRkSHY1b%2BT10k3eYQV9pToDbJPd0vBQVMU6Cw2neOszM0Vs8Us5z1h89mZqKDCngM7VUniNpO0WS%2FO1tBodb1mZecyMry7%2FnNs2bZ8%2BS40ZWpIlCGLY%2FL81Npr5ZEYuj%2BoNtlqnu0dfgpTR3XZ8weAjhZRxoPsLZ%2FjwoN98FG5PoR9WOILE62Z6%2BekiE0brFeAjUwA%2BycB04CQg&X-Amz-Signature=cf8b5202dfc45bc067a9ababbbdaa6a55ee586e22706c5b6484ac4efd45f11c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMM7MXKM%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFyCmqVsMh8lyJMI%2BLoPVFcVCoMxvQViqA%2BzCbrzL53PAiBaMi3Wd7TobPvIyZ5xnUXEbjYKFNS%2BsMBog8jDTY%2FfJSqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6YeSVkL5N%2BO%2BiPvpKtwDbeV%2B0SW3PS1wkinnMXDdiwJpPwE5McN58k%2FxHflaYWH9oKmvize2QFI8vZVA6uoRJyT7Uk1i8DGZDcbkU4bdnscEiaWl2B7PJnpf4QFNiltwdV7UZUJz4%2BZtN7Gsk8uFax6QvIz2PwVBTcJ1%2BuzEwRhzR4%2BBvXOGEdMLi1PPSlSTYYkCieEpGtE515ESX35VXLPGhz9v%2FP%2BzCzfPB0GBMbt8NgRswenj6SmuqmATOO1lh1nXQb%2F3bkZ5L%2BRlEyGYY0hevdF%2BU%2F2mh1Bqr3F0lWDEUKBdr3Vf6JxROl8Sv1oJzBXld2tzavJ3P%2BuxIu%2BJN8sJOW%2FRaxjY52nDAhY4BqJc6B71ysO1CoYMjd7eykJohJ92li%2BhgUYMp3lRIDFv6b4ufgX5%2FD1L3IyoCtjU90o6RQF95zOh7MY6W6H4rW0fiuB2obu8zJIMUfECDd7q12NRLMGQYfJ0G%2F6Rzs0%2FvyIZ7m90GkS0rero5XXTOgBQ9Rw6pQkJPDSD%2BNzStKhtSzWu9Zel7eBVUvlePL8ZYfIdYc9cD84z9e2w%2FW87Kpl4d2C8XT3LOSjoOzaFrDf%2FHeMh%2B1udsdzZxirICOTK78IdINyU7TSEyyp3LqspK0wWSelIRlqFi%2F94Un0w5Jf7ywY6pgGhD5z0zDESZO1waiRkSHY1b%2BT10k3eYQV9pToDbJPd0vBQVMU6Cw2neOszM0Vs8Us5z1h89mZqKDCngM7VUniNpO0WS%2FO1tBodb1mZecyMry7%2FnNs2bZ8%2BS40ZWpIlCGLY%2FL81Npr5ZEYuj%2BoNtlqnu0dfgpTR3XZ8weAjhZRxoPsLZ%2FjwoN98FG5PoR9WOILE62Z6%2BekiE0brFeAjUwA%2BycB04CQg&X-Amz-Signature=72e035fc601bfed0fb04f3f4a2f8b0e8b0d4d34f917f48b8e234aa7ccc8f4bbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









