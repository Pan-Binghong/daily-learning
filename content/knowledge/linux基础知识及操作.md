<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png)

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









=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTL2OYKM%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIDdNVm%2BaakYYhseXMlZJFj2v6o5z3%2BMRy4nDBM3Slst0AiBzlJhSMfKiYN5f5OwRgeEGDCpeVZCA9O39iKVEGuGOGyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMaet8jqpengl63vT5KtwDz4FeChzQodneJY%2BeJNnUjg2LcFioMnp3xXNSYBE82AYoh8c0xrzelb6YnsCS3NOukP3yPfwQInbYw40sfdgzhwUx3H2gptyNpAM28TSvLIe%2Fgk%2BJnOZgT7V3531KuEJoakJdXtF7c%2BVaHJDI2JfgvTUrK2MErNAlG9tXVkKNHpIF0lNeTBMtrUTK%2FJztuNp6u0C%2FfRxE612FdVIBpZ5oDexxDT%2F7DIXn04ljL0n4ywYFfvLw7o8ko6r9QOUayVexTaSFFksMLehwgYpuUZzxCKnIlsKzV6zFhp4BtVrPb%2BXUS5Oxjs2nyEOM04BHvnuAMoPSriwDK0CE3PqDoeYGGpLDDLJdZY2COrEEmAdsSOaxfeThG7kyd1VXgeWXas9g%2Frs9LlPvWzUT6YwOULf7AiEEUUHhr8LI6jju1rSmRMzelKwMntFg1D9TAKB6QPKN1OPvaCU%2Fq4uT%2BUJ51KfkwCa2nX2uGwANvckkWS1K8J2cMdfL8VafV2glJXgeO9nnoXtAj%2FLKU1kligqufXMVwDcBdjttB6deybBiYg5xRpn4IfEKPwrRpTuDKCTFsRE%2F0Lzk902tiXg1oGv9qhCC%2FqHPlwSLO7sIzZvsPuw18dVvaCQ14HHDCoMPOmIwsJ3MzwY6pgFK2ALZ4EZ4XEh0VbDsMbUu0wIT%2FlwgXajWeyZmT%2BqJNiiUOKec1SKPaK74NcmPOififjhiFdvx7MmjDZh0tLSozoWauqYnD8NWp7SSfQ5fAewtXu2TCubyExDaquNsykkvcIjN1KXVUdMA5o94w%2BL3bavKaMq4FHkldDOO25Zk36eHV6l%2BgRAVliUkJ1nNfMzYB0rE1T3DWG1BEfruPsJsy46%2B5y8C&X-Amz-Signature=557b781c82ffb44eda3afed8921f30d4ce6d56c11fe7205290d9c411e313bde8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTL2OYKM%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIDdNVm%2BaakYYhseXMlZJFj2v6o5z3%2BMRy4nDBM3Slst0AiBzlJhSMfKiYN5f5OwRgeEGDCpeVZCA9O39iKVEGuGOGyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMaet8jqpengl63vT5KtwDz4FeChzQodneJY%2BeJNnUjg2LcFioMnp3xXNSYBE82AYoh8c0xrzelb6YnsCS3NOukP3yPfwQInbYw40sfdgzhwUx3H2gptyNpAM28TSvLIe%2Fgk%2BJnOZgT7V3531KuEJoakJdXtF7c%2BVaHJDI2JfgvTUrK2MErNAlG9tXVkKNHpIF0lNeTBMtrUTK%2FJztuNp6u0C%2FfRxE612FdVIBpZ5oDexxDT%2F7DIXn04ljL0n4ywYFfvLw7o8ko6r9QOUayVexTaSFFksMLehwgYpuUZzxCKnIlsKzV6zFhp4BtVrPb%2BXUS5Oxjs2nyEOM04BHvnuAMoPSriwDK0CE3PqDoeYGGpLDDLJdZY2COrEEmAdsSOaxfeThG7kyd1VXgeWXas9g%2Frs9LlPvWzUT6YwOULf7AiEEUUHhr8LI6jju1rSmRMzelKwMntFg1D9TAKB6QPKN1OPvaCU%2Fq4uT%2BUJ51KfkwCa2nX2uGwANvckkWS1K8J2cMdfL8VafV2glJXgeO9nnoXtAj%2FLKU1kligqufXMVwDcBdjttB6deybBiYg5xRpn4IfEKPwrRpTuDKCTFsRE%2F0Lzk902tiXg1oGv9qhCC%2FqHPlwSLO7sIzZvsPuw18dVvaCQ14HHDCoMPOmIwsJ3MzwY6pgFK2ALZ4EZ4XEh0VbDsMbUu0wIT%2FlwgXajWeyZmT%2BqJNiiUOKec1SKPaK74NcmPOififjhiFdvx7MmjDZh0tLSozoWauqYnD8NWp7SSfQ5fAewtXu2TCubyExDaquNsykkvcIjN1KXVUdMA5o94w%2BL3bavKaMq4FHkldDOO25Zk36eHV6l%2BgRAVliUkJ1nNfMzYB0rE1T3DWG1BEfruPsJsy46%2B5y8C&X-Amz-Signature=ac8fdd99db388e8282fd51d27620af32efd39f25525441ab417807f335b77c79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
