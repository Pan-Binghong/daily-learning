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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDGEGU4T%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNrok8n4dDWI%2Bw9Pfq7vgYdp4YkFtUkyfFPggi7M6jqgIgFj5Sh1gLGXB6LGid59Oz5yMGn98o7DTOOUOiiAflGfUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMgm4Rz1F82zv25P2yrcA4%2BqyjYlM9lqM7bZGvijXe%2B%2FmokfSKIU%2FUCzF%2BK%2FXz9ss1nN63VJPY%2Bg3xq0q%2BeZjLsF3QnsW%2FPlHwUW67i%2F0S%2B3Vj1TIzajskCCOhMDAztrsiKpD0Cz4mZMfw1tI3O3U%2FP8D0HvN%2B9UH6ADjFu6TW6xFJ%2F9XKUz%2B2NkBF6B4geaEEAqFr3Ws9Qe7qRxukViCsm80RpWZhJ8wa6UWa6K8ck%2FoPdSdZVUgGERZhWv%2BOhd5o4pmvvYndBvu8ScEBuqAWRAlrKFV34l8PrYZcdikXPwM7HEpW49oDeYgU91GobzUgbCEPcT%2B00lxRseTTTHkP5xx%2B98Nq8UlmqJ%2BDIY%2F0Q%2FYf8HurxfdBIT4abHrW12TlP4iWqv%2FBjAPaiMynvVFsepD6CFcB9bbrcpqlzxa1%2Fyz%2BaWDj7gn7B1k8iTqWTGOfS%2FML2X%2BoD8EiV5A%2FZ%2Fl2C1zbwlNuxnH6Zc%2FjihaKQsO4x9WlZF%2FpY56E2gYBHxUYKDUDJazE7F7JLLZVwpz27zAa8wVb0y1IVT3c4oUkVuTK41Qdq6ZXPyC6FNPTc9%2FcxB6ZSeYHsawUAlEtdfjCEhMJ3z%2FNFCRum9rsI6gytXFxqu8b1MktCMcaQSQRyBpCA1a9mL3iI0c4rUMOry2cwGOqUBWX6i4XF%2FzyflFatR%2FD5mafZJNGPfDwPTSNZdBKbwa%2BAPaEcnrSyQUq1vxhYQ0qHKRMpa8rwIWAf6Hm0sHMFXJU8ddhoYvOustNTSju9ykHaBL1v4E9tvfyVP6xOa6k14FstLBhY2splyM6DT11CE4oHWlqgaXUIuS3pudyuTtQIitX3tXikC5ZCYZCgbHDuAcbMdx87al3FjkWAC4oBFnDv4Yypf&X-Amz-Signature=f0f94a6b28603ee832f89384f8f89a2e71ff73faf293795d8443d8596a905950&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDGEGU4T%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T034012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNrok8n4dDWI%2Bw9Pfq7vgYdp4YkFtUkyfFPggi7M6jqgIgFj5Sh1gLGXB6LGid59Oz5yMGn98o7DTOOUOiiAflGfUq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMgm4Rz1F82zv25P2yrcA4%2BqyjYlM9lqM7bZGvijXe%2B%2FmokfSKIU%2FUCzF%2BK%2FXz9ss1nN63VJPY%2Bg3xq0q%2BeZjLsF3QnsW%2FPlHwUW67i%2F0S%2B3Vj1TIzajskCCOhMDAztrsiKpD0Cz4mZMfw1tI3O3U%2FP8D0HvN%2B9UH6ADjFu6TW6xFJ%2F9XKUz%2B2NkBF6B4geaEEAqFr3Ws9Qe7qRxukViCsm80RpWZhJ8wa6UWa6K8ck%2FoPdSdZVUgGERZhWv%2BOhd5o4pmvvYndBvu8ScEBuqAWRAlrKFV34l8PrYZcdikXPwM7HEpW49oDeYgU91GobzUgbCEPcT%2B00lxRseTTTHkP5xx%2B98Nq8UlmqJ%2BDIY%2F0Q%2FYf8HurxfdBIT4abHrW12TlP4iWqv%2FBjAPaiMynvVFsepD6CFcB9bbrcpqlzxa1%2Fyz%2BaWDj7gn7B1k8iTqWTGOfS%2FML2X%2BoD8EiV5A%2FZ%2Fl2C1zbwlNuxnH6Zc%2FjihaKQsO4x9WlZF%2FpY56E2gYBHxUYKDUDJazE7F7JLLZVwpz27zAa8wVb0y1IVT3c4oUkVuTK41Qdq6ZXPyC6FNPTc9%2FcxB6ZSeYHsawUAlEtdfjCEhMJ3z%2FNFCRum9rsI6gytXFxqu8b1MktCMcaQSQRyBpCA1a9mL3iI0c4rUMOry2cwGOqUBWX6i4XF%2FzyflFatR%2FD5mafZJNGPfDwPTSNZdBKbwa%2BAPaEcnrSyQUq1vxhYQ0qHKRMpa8rwIWAf6Hm0sHMFXJU8ddhoYvOustNTSju9ykHaBL1v4E9tvfyVP6xOa6k14FstLBhY2splyM6DT11CE4oHWlqgaXUIuS3pudyuTtQIitX3tXikC5ZCYZCgbHDuAcbMdx87al3FjkWAC4oBFnDv4Yypf&X-Amz-Signature=c5afe5e61c37aed0e00556be123b773cb747a5c756bad7c49a36042e9362efd2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









