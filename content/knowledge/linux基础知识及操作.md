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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXT3XDO6%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDko5We%2Fm97ZtnzTOZL3L9tsXICd7Xkq7GjbGl%2BOU2fsAIhAIIv6viUPr98HRjGfNrEc6Z60M2edgu%2Bz0wpB7xjIN8nKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxCTD%2BhoKJQpQBWUfAq3ANZUdOlN9vTKTxgh1njXGnOhColzEW56V%2BPb8Y2IrLzVU7KGTe%2Bz2e965vJN71NA1Ruq9o2cDBe3SNzStZHz44phwFVLqMBov3ptdT9Adf5C4bJK46Kpm9psY5kH7nU5MiwhiEt3bc5t789YXFgxtGKzkMc5%2BDov5pwac85QgnCvpt8sxXdNhxeVM0WQ8PuQEAi1Hw33yMwqQVK590iDJIQD1Z%2BMlarg4HsnzZIyBZeETQxXzUMaa7ZrU41D%2BLLcUOFk%2FbHC48T7hoO1puiF4GVscq6EAqXoeqMvV69NRN2%2BcMuU0YZbyQPNji2MtqyVPtrIVL9Ii%2F3Z8MPBPixBwHPRz4OQG6QOQcG0A24QwyLz312OuxIWm0RGbEQgnctU2wa7dR%2FtAGGI40NQOXHQY4A0FmJ0BfECH0Ymhz4wY2OcUROqad0GPEU8XgV%2B4vKlXTvkwsew8DDskIOfUUwCZURO1QyuI1iMpKI%2FoG5dzpCAikF8HNEwxJSZRAfTulo79rABiTT2xogsvhGKZJKe5D%2FeKtlKf5%2BfgTawPh%2FUWS9PDow92Ri4ExrzAPi2lsZWoymnfM0Ca5N0Gvip2t6wF5mRCQGVdDjS3ZiCAV6udhHFxzSa8LHPwrHyu95%2BTDq1czKBjqkAevymO9KoaAaj2f658ZdArRs4ffY%2FUaDw1f7zg315q8CPbA99rSFFbRL2S01Hprg%2B18Iw1tUxlUfyhki9rtxMwd0Q8HsoO8ghreTviWuROwr6sXkghGZygMi6B3BJXOTPBiEYZMuCObPc0JRrx%2B4xLo%2FzNYyhYXUI7RLy2WwXfh42W9RG8gIk2zCbJ%2FIK7jEwOpZ2AaWJN2IRKo2eN8FNlyO0pVz&X-Amz-Signature=f9abf58bb662e245192d9a7369fb02d8ed48066c723dfafba54bbb254b978e47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXT3XDO6%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDko5We%2Fm97ZtnzTOZL3L9tsXICd7Xkq7GjbGl%2BOU2fsAIhAIIv6viUPr98HRjGfNrEc6Z60M2edgu%2Bz0wpB7xjIN8nKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxCTD%2BhoKJQpQBWUfAq3ANZUdOlN9vTKTxgh1njXGnOhColzEW56V%2BPb8Y2IrLzVU7KGTe%2Bz2e965vJN71NA1Ruq9o2cDBe3SNzStZHz44phwFVLqMBov3ptdT9Adf5C4bJK46Kpm9psY5kH7nU5MiwhiEt3bc5t789YXFgxtGKzkMc5%2BDov5pwac85QgnCvpt8sxXdNhxeVM0WQ8PuQEAi1Hw33yMwqQVK590iDJIQD1Z%2BMlarg4HsnzZIyBZeETQxXzUMaa7ZrU41D%2BLLcUOFk%2FbHC48T7hoO1puiF4GVscq6EAqXoeqMvV69NRN2%2BcMuU0YZbyQPNji2MtqyVPtrIVL9Ii%2F3Z8MPBPixBwHPRz4OQG6QOQcG0A24QwyLz312OuxIWm0RGbEQgnctU2wa7dR%2FtAGGI40NQOXHQY4A0FmJ0BfECH0Ymhz4wY2OcUROqad0GPEU8XgV%2B4vKlXTvkwsew8DDskIOfUUwCZURO1QyuI1iMpKI%2FoG5dzpCAikF8HNEwxJSZRAfTulo79rABiTT2xogsvhGKZJKe5D%2FeKtlKf5%2BfgTawPh%2FUWS9PDow92Ri4ExrzAPi2lsZWoymnfM0Ca5N0Gvip2t6wF5mRCQGVdDjS3ZiCAV6udhHFxzSa8LHPwrHyu95%2BTDq1czKBjqkAevymO9KoaAaj2f658ZdArRs4ffY%2FUaDw1f7zg315q8CPbA99rSFFbRL2S01Hprg%2B18Iw1tUxlUfyhki9rtxMwd0Q8HsoO8ghreTviWuROwr6sXkghGZygMi6B3BJXOTPBiEYZMuCObPc0JRrx%2B4xLo%2FzNYyhYXUI7RLy2WwXfh42W9RG8gIk2zCbJ%2FIK7jEwOpZ2AaWJN2IRKo2eN8FNlyO0pVz&X-Amz-Signature=b5a794376e63a224d29c1226d548ab0fd8c65cefed679f1b4f6a62ede5863e40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









