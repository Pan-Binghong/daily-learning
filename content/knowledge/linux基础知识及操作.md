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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPA73Q7M%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0eK%2FQiXmcb0aJgwn6%2FaRptXBhCF58i%2B%2FlR5LLkIqdjwIhAKaAJqx7xLot0Pu1jnTC8BGlNvo6rL3ZC4hBYQN7ZNDPKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe%2F2LQYuJ36SWoF0Yq3AMqpGnLtsSJljhwlY1HJTMVW4LyvLIVddWJlAKupqU%2FPP6PXhDV7hfyziHrIvVfci%2BbtC%2FyLsHWYyzIkaZCHS1HDXf0Ood7LS8YKzzayU1hWObenuaoxdMfXOFHATCQD20oDxvJhdXGQJ3jZzfHMF8oJFake21TCKR%2FR5VQgshbouOf2%2Blt3kO7YvoE%2F4UpJ8KX2gxRv9tVeqpLSBsNcCWhx9sQB0pjZGfm4dFECzjQx6ARCPjwJEBPGg96J0KA2w4RrstS0DpYq2KMG6ClwA%2BZmUX0jcomw9ucyWBVQ%2Bh97VzECgnwf3kTiiOKmFV4OJ8%2BMSfnuJ5OlOAZAYUK0QnMoi9%2BpWjrOyIGpixmESGEPNI1m2JhoDPee5UEFxGnld%2B%2BzdUsPgwVB7dGSoyMmV7GtkbGRvwK3PD4qeLbw0cW4Wzy9oN1geURg7PRXARKQADHt5QknRaYLV4fQXXpncqQvJdc%2FjmBTMZeYHX1VKYg%2FbaXhr3r1mY2l3R1FBThtyroFVNwXQUp%2FmpvDV1%2BJoVsJalSPeYS%2FAtRXSJSmCYb8J%2FJcwVjh9Eb6NpXg9ZxOg8o8xxhqz5tRXqsMlqANdBxaxFB82emLTBWN%2BgiXxIxobvNpt0ohcyCGMm8mTCG%2FdLJBjqkATjg02FEexAUfa%2FUFR5AUah64k1LhuTk%2F8OXw%2FhXrXLRaqknuxXa3rzFKyZO33SqKkhFzAQYCC8SEaJ%2BGmIZAMl5SucBtxN%2BwgipMGKDeIf44cNLxln4BNmR4MA9UHXBVnciuAajPxkyvEk4XZ4ShpUJfhntttnWBzSO3KhYpY8K7UAjwQ7ESbbmQI6zzxkMgjtaArBI2suDPTzaCTQ47rPMcy4%2F&X-Amz-Signature=2f72a740f74d8328c225cbecea7f5f347854333a7824afe9370f596aa04eb073&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPA73Q7M%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0eK%2FQiXmcb0aJgwn6%2FaRptXBhCF58i%2B%2FlR5LLkIqdjwIhAKaAJqx7xLot0Pu1jnTC8BGlNvo6rL3ZC4hBYQN7ZNDPKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe%2F2LQYuJ36SWoF0Yq3AMqpGnLtsSJljhwlY1HJTMVW4LyvLIVddWJlAKupqU%2FPP6PXhDV7hfyziHrIvVfci%2BbtC%2FyLsHWYyzIkaZCHS1HDXf0Ood7LS8YKzzayU1hWObenuaoxdMfXOFHATCQD20oDxvJhdXGQJ3jZzfHMF8oJFake21TCKR%2FR5VQgshbouOf2%2Blt3kO7YvoE%2F4UpJ8KX2gxRv9tVeqpLSBsNcCWhx9sQB0pjZGfm4dFECzjQx6ARCPjwJEBPGg96J0KA2w4RrstS0DpYq2KMG6ClwA%2BZmUX0jcomw9ucyWBVQ%2Bh97VzECgnwf3kTiiOKmFV4OJ8%2BMSfnuJ5OlOAZAYUK0QnMoi9%2BpWjrOyIGpixmESGEPNI1m2JhoDPee5UEFxGnld%2B%2BzdUsPgwVB7dGSoyMmV7GtkbGRvwK3PD4qeLbw0cW4Wzy9oN1geURg7PRXARKQADHt5QknRaYLV4fQXXpncqQvJdc%2FjmBTMZeYHX1VKYg%2FbaXhr3r1mY2l3R1FBThtyroFVNwXQUp%2FmpvDV1%2BJoVsJalSPeYS%2FAtRXSJSmCYb8J%2FJcwVjh9Eb6NpXg9ZxOg8o8xxhqz5tRXqsMlqANdBxaxFB82emLTBWN%2BgiXxIxobvNpt0ohcyCGMm8mTCG%2FdLJBjqkATjg02FEexAUfa%2FUFR5AUah64k1LhuTk%2F8OXw%2FhXrXLRaqknuxXa3rzFKyZO33SqKkhFzAQYCC8SEaJ%2BGmIZAMl5SucBtxN%2BwgipMGKDeIf44cNLxln4BNmR4MA9UHXBVnciuAajPxkyvEk4XZ4ShpUJfhntttnWBzSO3KhYpY8K7UAjwQ7ESbbmQI6zzxkMgjtaArBI2suDPTzaCTQ47rPMcy4%2F&X-Amz-Signature=e895ed9ac0e8db8d392ef8b5c04fc9743a98c344540d2f5148230b5340cfc170&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









