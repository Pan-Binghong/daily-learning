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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG2AZXHZ%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICIGUYHt9MfrY6OCamnaCQgFsLoFio9E7k7ot8Rcu1PMAiEAxG5AtL2gGE%2BivkF4T7JzOqIaqz6gJNV%2FFrmC7jnfFeIqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5lRF7pjOh6nRoIWSrcA144KSelX28x3dGmV%2FEG11aewKHmLIIdilz3dGXu9riEmsJ1eBsRo8mhTHS3JT%2Ba%2Bf5%2BP4bU2QA8SBgxsD4858UarH%2BuKjoJpgsMvFOBfCk7kMeCfFSu1lUjCOax8iMUMh3%2F28PVIVU0FsShii%2BFKnL1z2ijsPqktpQ4QUL0nWRlKEhVbnvvVGpIkVr9MVwfjYB6YWSSr5AgurrBW1shvBfmHMETdSoCSQK2TKRphtPUi%2FIfp2ayfp6K8NrZm7xx1GdcCwbriJrhMysp%2F01fTYSRSMoxT9rMGWmdnfWFZRcNFRGh4CNvN8Fob1GrrqEDtaDlQQJ%2Bzk5x18egTbb9cLT1VYB%2F3STP0DViOdk5GgM%2FM96FU%2B7mmAxCrozKTMwR%2FFVBib2lDzZR2vt6A9AepwllEoh9yB5Bebn6pAVLciuql5lfhRj0ZWgQ9ekLcdUFyDHO3NTLIxz33A3enUwaCzDARPuvETlPPYlkT%2BycCKVZzBiTgu3nlogtKyvBA%2Bot5gIlpZvU8duyhb8LFGJ7uy8jsjAKG1bBz%2FfqSCMSJyH91S0vz0TMAUXaiCG0s%2Fc9X%2BoWDFc60cynU4Uvrk9ecXdG8zRabu39ID4EJT2iYsX0FSJ%2Fi%2BsrB8mdqfvZMIb0h84GOqUBCY3MgSKaLdMkG4VWBeC%2BsvSBEQO6ZoHQYRCPs6W4vd7KrouWUYoD1xM3QlRATXOsLehRWNssyqCaNSfGRXGegtIfTjrnXPE4b7G2hZXzhLlot3ZCetnlXGDVqQ2kY2ylKWQqXpWR0MJ77annyKbyaaeWe5LGUPXgDhXm%2FJ5zVt%2Fe%2B%2Bo4ZnKoMS4%2B%2FuuFHu2ALQdJVHbkW8aJcH10IgRWOEkk7aFO&X-Amz-Signature=19bc4849b099b471bdfa034e04304fed399b1304d8365d4ecabbf75ecb4e2dd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG2AZXHZ%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICIGUYHt9MfrY6OCamnaCQgFsLoFio9E7k7ot8Rcu1PMAiEAxG5AtL2gGE%2BivkF4T7JzOqIaqz6gJNV%2FFrmC7jnfFeIqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5lRF7pjOh6nRoIWSrcA144KSelX28x3dGmV%2FEG11aewKHmLIIdilz3dGXu9riEmsJ1eBsRo8mhTHS3JT%2Ba%2Bf5%2BP4bU2QA8SBgxsD4858UarH%2BuKjoJpgsMvFOBfCk7kMeCfFSu1lUjCOax8iMUMh3%2F28PVIVU0FsShii%2BFKnL1z2ijsPqktpQ4QUL0nWRlKEhVbnvvVGpIkVr9MVwfjYB6YWSSr5AgurrBW1shvBfmHMETdSoCSQK2TKRphtPUi%2FIfp2ayfp6K8NrZm7xx1GdcCwbriJrhMysp%2F01fTYSRSMoxT9rMGWmdnfWFZRcNFRGh4CNvN8Fob1GrrqEDtaDlQQJ%2Bzk5x18egTbb9cLT1VYB%2F3STP0DViOdk5GgM%2FM96FU%2B7mmAxCrozKTMwR%2FFVBib2lDzZR2vt6A9AepwllEoh9yB5Bebn6pAVLciuql5lfhRj0ZWgQ9ekLcdUFyDHO3NTLIxz33A3enUwaCzDARPuvETlPPYlkT%2BycCKVZzBiTgu3nlogtKyvBA%2Bot5gIlpZvU8duyhb8LFGJ7uy8jsjAKG1bBz%2FfqSCMSJyH91S0vz0TMAUXaiCG0s%2Fc9X%2BoWDFc60cynU4Uvrk9ecXdG8zRabu39ID4EJT2iYsX0FSJ%2Fi%2BsrB8mdqfvZMIb0h84GOqUBCY3MgSKaLdMkG4VWBeC%2BsvSBEQO6ZoHQYRCPs6W4vd7KrouWUYoD1xM3QlRATXOsLehRWNssyqCaNSfGRXGegtIfTjrnXPE4b7G2hZXzhLlot3ZCetnlXGDVqQ2kY2ylKWQqXpWR0MJ77annyKbyaaeWe5LGUPXgDhXm%2FJ5zVt%2Fe%2B%2Bo4ZnKoMS4%2B%2FuuFHu2ALQdJVHbkW8aJcH10IgRWOEkk7aFO&X-Amz-Signature=73db6055db0abb7c3a79aaaa110c77dc55480539ad6582e7dcb5f9d085155c31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









