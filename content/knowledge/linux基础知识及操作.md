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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RENCKCOD%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIA9Ty0svcQO4tw7qwfZNlcqKk3l6688JBH3%2B1f0Ehvs4AiANbRmZjHwtUDDIWsex0KaYJR4HTKniw9GWTPiniB1l2yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHq8SfCWm8%2FAvnxDxKtwDKTlJo8Q9PzPa80C8DjMn7mrEwpXuQaQTsfkmaZHd7vWQfZwNgHqFFrh7aXxdB0xeFcpC464YXATvMlbfK%2FehdaN64NbZFJgX%2B31he2ycbAKoGBdUseewCnsMO3seVcy6nO8qD0Y8r4CBr3R08scZxO9xJZQnaUks24Yqy6NdwdGV2bYcnIHD77fDRq2%2BiKQw9jO8%2BsUrtG5a2MYF138%2Fj2ONTlV5lCuF%2BP%2F4jKPmC2B4DcL1VLHeCRgDcWYM5x28%2Bosb19h8NftktckjVLzKgY23Clj%2B5UMXhI2%2FKR%2BLUiXhX70uVAD1y5lJ%2ByCigAzybuIIFgkjOws2sSwFhxHW3g%2Bm0sDS0fWiFSyT6Fns1BIuRKgHwRT2hVCG2DpAPxwtC%2FM9y5VlTkbhc1C7u7MYrhumSjTYlegvtqnyT%2FpnDUSRwBFXvu0Ta%2B8ouLcuok%2B1%2FPC8%2FbT8RO1RzmXwkch7Oxw9Ez6o0VA4Owr9evodixABzNJs%2FxXxRukxqVvKZQ6M4ycq%2BC9r1hOX1DUz0%2FsQhTwRXugeZl5I9zS%2FhtLMer78UnYzqoFWkXdbqHmJUIjI1JQT3NBf9tRmCPmPCiMYu2wW6SjaBbA%2BIzn5pJKr2xw2mgjw3DpKC6v4zqYwitWbzwY6pgGay27ghNQKrQPYSEiZSo1dTCqB3jidkAv%2BEEfow7hS1VP5OOo5ecGMKcoxubUqbgI4QgGIvBGV4nGjiXynTOhnltqOdTesKG8wFPk9IsVvSEmFJ9Zz8HHH9h9vvBOrSg2LdqJln7BUW9ge%2Fo1HGReeoro%2FdtSkd0WuuSBnBKgyNG1TmenEO5sL0OFyFoXSenxNXP3bbM1MI%2F223lKLhvIOYNpHz1uk&X-Amz-Signature=d7907b374ada952e588154a1fb540a5d7320c43162b2b22ddeb63d1f630a8ad4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RENCKCOD%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIA9Ty0svcQO4tw7qwfZNlcqKk3l6688JBH3%2B1f0Ehvs4AiANbRmZjHwtUDDIWsex0KaYJR4HTKniw9GWTPiniB1l2yr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMHq8SfCWm8%2FAvnxDxKtwDKTlJo8Q9PzPa80C8DjMn7mrEwpXuQaQTsfkmaZHd7vWQfZwNgHqFFrh7aXxdB0xeFcpC464YXATvMlbfK%2FehdaN64NbZFJgX%2B31he2ycbAKoGBdUseewCnsMO3seVcy6nO8qD0Y8r4CBr3R08scZxO9xJZQnaUks24Yqy6NdwdGV2bYcnIHD77fDRq2%2BiKQw9jO8%2BsUrtG5a2MYF138%2Fj2ONTlV5lCuF%2BP%2F4jKPmC2B4DcL1VLHeCRgDcWYM5x28%2Bosb19h8NftktckjVLzKgY23Clj%2B5UMXhI2%2FKR%2BLUiXhX70uVAD1y5lJ%2ByCigAzybuIIFgkjOws2sSwFhxHW3g%2Bm0sDS0fWiFSyT6Fns1BIuRKgHwRT2hVCG2DpAPxwtC%2FM9y5VlTkbhc1C7u7MYrhumSjTYlegvtqnyT%2FpnDUSRwBFXvu0Ta%2B8ouLcuok%2B1%2FPC8%2FbT8RO1RzmXwkch7Oxw9Ez6o0VA4Owr9evodixABzNJs%2FxXxRukxqVvKZQ6M4ycq%2BC9r1hOX1DUz0%2FsQhTwRXugeZl5I9zS%2FhtLMer78UnYzqoFWkXdbqHmJUIjI1JQT3NBf9tRmCPmPCiMYu2wW6SjaBbA%2BIzn5pJKr2xw2mgjw3DpKC6v4zqYwitWbzwY6pgGay27ghNQKrQPYSEiZSo1dTCqB3jidkAv%2BEEfow7hS1VP5OOo5ecGMKcoxubUqbgI4QgGIvBGV4nGjiXynTOhnltqOdTesKG8wFPk9IsVvSEmFJ9Zz8HHH9h9vvBOrSg2LdqJln7BUW9ge%2Fo1HGReeoro%2FdtSkd0WuuSBnBKgyNG1TmenEO5sL0OFyFoXSenxNXP3bbM1MI%2F223lKLhvIOYNpHz1uk&X-Amz-Signature=a966dfd49e6426d189b0b14b41f479ae541628aedf7bab79c102eb792ccc28c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









