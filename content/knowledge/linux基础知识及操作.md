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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMIOIXB4%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCYIJOV3RCZIlCPQbUn8EUQ0du31RpIQHTMixbp7990BQIgNGveZUov2AxTAC%2FoBkxjcg%2BewAlpq7d2xRbUbPfticoqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcmeh7%2F%2FsRyC5vgOCrcA4dFVNveQDZmkpBI9jWnup3TDLcQPJcUkKXT89OIY4ndoKSVVUHmrvVXa8%2BYmbytuvgqo4VETtmVtGNBITcU42mSRI0XXi58IPCc6RiFf3XP94xaPMyE3XpmegepuMbHAGe5i53Pkn5q%2BG%2F6Csu6ymy720vqQGG2IY0yVjl2ahm0xebtqoYOXF1oG6n2hTYOm8PyJffhKc95CBjIetjKOy%2FXOedkRf6eIyFAtHfCNyGZnvyL%2FiyQuDnJuDpa8db63U5XFzstxNPCcTLUuLEFMUvnOs6iT47e5VZDJtyYLrYRgLwk9z14YWPQkOauOLF0p9pGFS0aEXalJ7wAVkk4lwdZpcTAmg7Yb%2B%2FCEAM1Lk0hmy3uww4BYFq8GphOItSXIcVa5YDArBwbSvH5z%2BykMjeAl2o02q1iDQ49eoY%2BMJVZAietlateixycDtG5FpOgYfyodLxz1%2BwkcABB9Ze8GV0ZlfpYuNMJIK6gmlc8tExwHA7O2jINzRsSV8yBZYqcpuNTn4HXcAkEE1d55B5HzhtYYdaIEHQYgaNkhZM9Mllc4KR4GnPPVg0TWqtS3%2F41gD%2F5X4m6WT1kBmaskN%2FJRzY6UYTz9ZM1%2BvBdGgw6Fnb7ny4jUawZjKzKMO2SMIKIgMwGOqUBM%2BV7soqzI0U0mMHKh7ucAn%2BWyqFfCDr8aImPenJsR0V%2BAGTGA4uUCc0hgRfnixbKuwgIrWxh6mtluZ1Yoz8beHccrNDmttfA228nfAPGChSabqaJSYvkNdw9w6nn3HP8%2FK8XYfLpPO0T6gZTm8DQKEG8AY4USMeKAuRmvPLWMQtS9l9yFZ7czfRHmzeA5VoOWRrzPcr8CI8tbQ5%2BrSoOcl%2BK0DPb&X-Amz-Signature=6dddaf9942b8626755ca9810e85e77f777e07065275ef75a61cad3614605eb2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMIOIXB4%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCYIJOV3RCZIlCPQbUn8EUQ0du31RpIQHTMixbp7990BQIgNGveZUov2AxTAC%2FoBkxjcg%2BewAlpq7d2xRbUbPfticoqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFcmeh7%2F%2FsRyC5vgOCrcA4dFVNveQDZmkpBI9jWnup3TDLcQPJcUkKXT89OIY4ndoKSVVUHmrvVXa8%2BYmbytuvgqo4VETtmVtGNBITcU42mSRI0XXi58IPCc6RiFf3XP94xaPMyE3XpmegepuMbHAGe5i53Pkn5q%2BG%2F6Csu6ymy720vqQGG2IY0yVjl2ahm0xebtqoYOXF1oG6n2hTYOm8PyJffhKc95CBjIetjKOy%2FXOedkRf6eIyFAtHfCNyGZnvyL%2FiyQuDnJuDpa8db63U5XFzstxNPCcTLUuLEFMUvnOs6iT47e5VZDJtyYLrYRgLwk9z14YWPQkOauOLF0p9pGFS0aEXalJ7wAVkk4lwdZpcTAmg7Yb%2B%2FCEAM1Lk0hmy3uww4BYFq8GphOItSXIcVa5YDArBwbSvH5z%2BykMjeAl2o02q1iDQ49eoY%2BMJVZAietlateixycDtG5FpOgYfyodLxz1%2BwkcABB9Ze8GV0ZlfpYuNMJIK6gmlc8tExwHA7O2jINzRsSV8yBZYqcpuNTn4HXcAkEE1d55B5HzhtYYdaIEHQYgaNkhZM9Mllc4KR4GnPPVg0TWqtS3%2F41gD%2F5X4m6WT1kBmaskN%2FJRzY6UYTz9ZM1%2BvBdGgw6Fnb7ny4jUawZjKzKMO2SMIKIgMwGOqUBM%2BV7soqzI0U0mMHKh7ucAn%2BWyqFfCDr8aImPenJsR0V%2BAGTGA4uUCc0hgRfnixbKuwgIrWxh6mtluZ1Yoz8beHccrNDmttfA228nfAPGChSabqaJSYvkNdw9w6nn3HP8%2FK8XYfLpPO0T6gZTm8DQKEG8AY4USMeKAuRmvPLWMQtS9l9yFZ7czfRHmzeA5VoOWRrzPcr8CI8tbQ5%2BrSoOcl%2BK0DPb&X-Amz-Signature=d8d4da293246cbe6f23fda33f47d8a31bb20f5f7e26d4ae8d06273722859b02a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









