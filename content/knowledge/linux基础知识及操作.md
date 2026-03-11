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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBU25CMZ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSyaZXhmanal33mBgJtsHQxXcS%2FiFmkd%2B1asMicoSqTAIgbZAsg36mTYnfjdALcapILuqnhN%2B2vNvSpqxk7tPJWLIq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDEZb9HnnZ1s97f35nircA78RyWXFT8KJOeHOPY0VHHS9A0YG3JwtqpRfK8%2BalxikADdh4pZRvDKghCvAmUQtq3xLnNudbJr0lrRl9HndxccaZATJetkf3SgTcKCgugHANStXzgtwVeN%2FXmW3NiViKlfBMmOzYq1RrXgtHWnqdg%2BvqdZ9RtvK2anLEh7ZwJRSWnT%2BF3Pkg4q0rRuuGdD6jf0GjPnLmRBF6AqLIKxa5QtyiovxsXDoNoOESZ%2FbZJd8dRgrbjQsCK%2B9tM0NAvp%2B5%2F8rOytTjdrM%2FuRGLG89KuBZVLieL%2Baf3%2FjEFejXgrATVfO7320pW0DTTj%2B493mC5dP%2BAYAnAtMOKkyv43cKvg1TLutxQnzs21htRGJn6VVVfP0WGnWe5hr8itPWIrfQXrrY3OT59ohNKESNUoF12TN6JVJVuAe4A503X1WM3SXKaW7zrmgdltT4QFJznKOFeHk3sVoTKghWppfz26fzMF2RzHW95zQxBB3AnDTBl4lxYWSDHYJYXUailW%2FvCGlMiFEsfAqtxmczPigLbceW1R1KJY4TfrxBGf5e1zrQn2Wp3drb74gADRVdCUAdp%2FKSKEfX5muFsfFIdI8l5sWu9tcbazpbDWQSB1ho4z6IpyxoOgcrkZq3xw%2BnslE9MMjAw80GOqUByUIqnsKpFnKEF2XlYbKlqpuF5g6AKe%2BAOkqijMVJT12C9zq5NJqqKCndzH9FqUmaKtsz6G4raEPzHlvxr44GNmAJ%2BJnDdmoy28B2N8MCN8TnACW9Sl4ug6kJhgBHhQE6FKbjxDVMl7iuSI%2BFBNuAjNWJJxTCL2Mvp%2Flq7%2BDoZqJwxWWb3bDBQl21LNaZ6dl5fc3moUKwGLfOTkPCpUgd9k4o9m4G&X-Amz-Signature=db9beddb2c5f9d38b46ff30f42df251840633f4d739a282520cf3cec7aaa5129&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBU25CMZ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSyaZXhmanal33mBgJtsHQxXcS%2FiFmkd%2B1asMicoSqTAIgbZAsg36mTYnfjdALcapILuqnhN%2B2vNvSpqxk7tPJWLIq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDEZb9HnnZ1s97f35nircA78RyWXFT8KJOeHOPY0VHHS9A0YG3JwtqpRfK8%2BalxikADdh4pZRvDKghCvAmUQtq3xLnNudbJr0lrRl9HndxccaZATJetkf3SgTcKCgugHANStXzgtwVeN%2FXmW3NiViKlfBMmOzYq1RrXgtHWnqdg%2BvqdZ9RtvK2anLEh7ZwJRSWnT%2BF3Pkg4q0rRuuGdD6jf0GjPnLmRBF6AqLIKxa5QtyiovxsXDoNoOESZ%2FbZJd8dRgrbjQsCK%2B9tM0NAvp%2B5%2F8rOytTjdrM%2FuRGLG89KuBZVLieL%2Baf3%2FjEFejXgrATVfO7320pW0DTTj%2B493mC5dP%2BAYAnAtMOKkyv43cKvg1TLutxQnzs21htRGJn6VVVfP0WGnWe5hr8itPWIrfQXrrY3OT59ohNKESNUoF12TN6JVJVuAe4A503X1WM3SXKaW7zrmgdltT4QFJznKOFeHk3sVoTKghWppfz26fzMF2RzHW95zQxBB3AnDTBl4lxYWSDHYJYXUailW%2FvCGlMiFEsfAqtxmczPigLbceW1R1KJY4TfrxBGf5e1zrQn2Wp3drb74gADRVdCUAdp%2FKSKEfX5muFsfFIdI8l5sWu9tcbazpbDWQSB1ho4z6IpyxoOgcrkZq3xw%2BnslE9MMjAw80GOqUByUIqnsKpFnKEF2XlYbKlqpuF5g6AKe%2BAOkqijMVJT12C9zq5NJqqKCndzH9FqUmaKtsz6G4raEPzHlvxr44GNmAJ%2BJnDdmoy28B2N8MCN8TnACW9Sl4ug6kJhgBHhQE6FKbjxDVMl7iuSI%2BFBNuAjNWJJxTCL2Mvp%2Flq7%2BDoZqJwxWWb3bDBQl21LNaZ6dl5fc3moUKwGLfOTkPCpUgd9k4o9m4G&X-Amz-Signature=f1920576684a0f774000c91b8b56089e1573c38156838e56fbeb5b1b8cd9f357&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









