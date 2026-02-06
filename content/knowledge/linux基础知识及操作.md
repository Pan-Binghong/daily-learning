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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMGQUJD%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCICCZRZSCSogrS5QR6YcR7HOFj%2Fn75%2BJdJzE67YRZtDEsAiBCRI4AhNxLJGjicBfQgLz9r669eCUN2%2Bj4d0F0io9%2FlCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIM4DH2OuRgVEhWEMO%2BKtwDk9%2B1quWPZk%2FUUEK3VWz%2FsrRFPF1uYI2FGGIlsh1hoMGMDoZzYAlcoKKDFIpbPTvYIad5vk1ohwpqeC%2BjqWoB27hySIZvJ%2FptEAp0cUDEspQvLjcYtoaHSBiytXPYQiX4JvlPvPM5vpM21qQOkytRxWSu53R%2FsApwxBO9U%2B04JDDa%2B7oqhEzCqxGVWmiLRiWWEeAEzbnH%2BQcd%2BL%2Feo8I2EtBEdUeuKCBym5f6c8OBv1ja9h5HDwI2vYLa9Qlh57Z6PzUVHyokrjpk54krVd4xTtJr2F1UVHxRTy8Q1%2Fz4pxHJjgVKK5fuLx1Nqqd8A%2BVSyNyt6UBu5mpIJlEImn47WGBj62UagkNRuULFXz%2B9cn1%2BI%2BIoaTOrfd1vkS9puGqSUiSf4GiYQ%2BLoL9RZyJWWMuzlnTm5A8fN%2FXGPT%2B4WOLRAyEpzDSH5StYP36YaaVbhd0Ilzwg83hE3qfGyIVHIpf4MXlibf%2BgXXcrvBfkw%2BEHI%2BkTy9dDBGR5Y1kfC4EPEgZAGQ7W08JxKb8nSjBE49ezHRlj%2B4NL9grUwUVCE4FTrl%2F1PSc%2FvuDTudBenipnQ4i1Pf4PJkWMez7j81ixe8goZYXcgXkC%2BQFtKUKV9t0WB7wY4pXX1BqYhcMYw%2B7mVzAY6pgHB1VwEQFWClj4GiHae4UBLwlIJ36rYfxzywJkVS0w4hbJmO0rBI0NmQQ2hgqJFc2adioyOuHzCy2BheIo8dQwUUhi6Ftxx%2BQ%2F%2Bil8ELJbZDwLseUDHgad7tk6idD23zPly61gfjzcTxRh7yOFT%2BHVq1dqbpwn%2BfhThJu4LltMzzZJx9z97hR2KFXPtfJiyjcV%2BijaTOMHY4wKytYV%2FLLKU7bm7JkVR&X-Amz-Signature=8bb5673610024f74a7a66b7563a1839fc9e7e269de5d79948c267710122d4d7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMMGQUJD%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCICCZRZSCSogrS5QR6YcR7HOFj%2Fn75%2BJdJzE67YRZtDEsAiBCRI4AhNxLJGjicBfQgLz9r669eCUN2%2Bj4d0F0io9%2FlCr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIM4DH2OuRgVEhWEMO%2BKtwDk9%2B1quWPZk%2FUUEK3VWz%2FsrRFPF1uYI2FGGIlsh1hoMGMDoZzYAlcoKKDFIpbPTvYIad5vk1ohwpqeC%2BjqWoB27hySIZvJ%2FptEAp0cUDEspQvLjcYtoaHSBiytXPYQiX4JvlPvPM5vpM21qQOkytRxWSu53R%2FsApwxBO9U%2B04JDDa%2B7oqhEzCqxGVWmiLRiWWEeAEzbnH%2BQcd%2BL%2Feo8I2EtBEdUeuKCBym5f6c8OBv1ja9h5HDwI2vYLa9Qlh57Z6PzUVHyokrjpk54krVd4xTtJr2F1UVHxRTy8Q1%2Fz4pxHJjgVKK5fuLx1Nqqd8A%2BVSyNyt6UBu5mpIJlEImn47WGBj62UagkNRuULFXz%2B9cn1%2BI%2BIoaTOrfd1vkS9puGqSUiSf4GiYQ%2BLoL9RZyJWWMuzlnTm5A8fN%2FXGPT%2B4WOLRAyEpzDSH5StYP36YaaVbhd0Ilzwg83hE3qfGyIVHIpf4MXlibf%2BgXXcrvBfkw%2BEHI%2BkTy9dDBGR5Y1kfC4EPEgZAGQ7W08JxKb8nSjBE49ezHRlj%2B4NL9grUwUVCE4FTrl%2F1PSc%2FvuDTudBenipnQ4i1Pf4PJkWMez7j81ixe8goZYXcgXkC%2BQFtKUKV9t0WB7wY4pXX1BqYhcMYw%2B7mVzAY6pgHB1VwEQFWClj4GiHae4UBLwlIJ36rYfxzywJkVS0w4hbJmO0rBI0NmQQ2hgqJFc2adioyOuHzCy2BheIo8dQwUUhi6Ftxx%2BQ%2F%2Bil8ELJbZDwLseUDHgad7tk6idD23zPly61gfjzcTxRh7yOFT%2BHVq1dqbpwn%2BfhThJu4LltMzzZJx9z97hR2KFXPtfJiyjcV%2BijaTOMHY4wKytYV%2FLLKU7bm7JkVR&X-Amz-Signature=4ce3f24bb80e725ed098f9e5824f25e7e492174ddcf801571c80d5296140c349&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









