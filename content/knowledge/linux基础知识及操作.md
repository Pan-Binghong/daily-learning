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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD6JV5KH%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIHv3UUR7i5ejTC5Z34sWj%2B6eZBlajf84TYtL4At8BsMkAiAex%2BDz7bg6kHu8hicSdqAxDYwj5FqqneiXbpPKDRsViyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM97szmDke2zHGuPhEKtwD8Lyf8j19gAG7sDYufOxz0aSNkf0qEOevIcrtv6aF%2FkW8D4frtW7w4WfPVoQbfBNHu8U6MbK9bqp7%2Bi%2F6baXkuWYewlXBl7%2FOBB6IkGt1KhdRumxDw5HpSn4%2BuBLWPpn8Y8hceupBtbraRgj6A8dJ0SW1QPlCOAnqpQc4uOUqhOUhBJ0G2uMhr%2B7UwKLgxU469ziYeOAmwRMzTPwjtwqLIfdjzM02JbOMEynUexSh2Qgxr%2BhgzK6V4ZsuaAY3pXRvv4jzjmxuHSdu5jJSksD3Aw%2BSB9kZTbUGQm7lv4UdWBcdi4D0tinXxvrX4aptj0HrPFkl8CDdpUbZQ4KoRcKuOYk0WU3Cq%2FbPAUTzYi5TCIx1Sba6IBcq4pv4a5IlzQ2IZniK9zisNsBFbDwKv2oUOH5RouwndETcuIu16MdylLirH1w7pKmAY2nwxoSmkYbFpNtmqY1ZdDovPoRvpqh1TATSOe9zuwlER6r6vBqfa6BNHUPJJDZdtLIz5oTR0f26jgB3CDHYZ2lxFQ3EEK6MFEgO2eZ3uV%2FlBfiaCnL40Mxa0N42n8aKLw8Vangq6CDlygSKD8pjPcFMzL3NN34MAJULP2NAKlxDGikEnmX%2FT0r8sywyWeqaf5WgHC4wpL3cygY6pgHrAuBH9TowVEKbPStAWpIpg9opuYBLfi3pOJ4Xu2YWa9EAY58kS6GI%2B9ii2%2Fxy7QMah8KGev6oZjL2ZYXA3nUSZ0wvi45%2FxTt93ZlPeTUZYznOFUktRp%2FyxR72xVnn0n7oLH5tjJdQWzvljr2pHs4PD1hFxdkYNWsM7mquyQT8vh3dD%2BpCU2h6jqAnwasYj16k7foFfeI%2FWWtTiajBI54Zsxun9AiF&X-Amz-Signature=c8ed454d1971412d768b7b856032bdc44da0c64ab4526c0b0bfac99c0532070f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VD6JV5KH%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIHv3UUR7i5ejTC5Z34sWj%2B6eZBlajf84TYtL4At8BsMkAiAex%2BDz7bg6kHu8hicSdqAxDYwj5FqqneiXbpPKDRsViyqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM97szmDke2zHGuPhEKtwD8Lyf8j19gAG7sDYufOxz0aSNkf0qEOevIcrtv6aF%2FkW8D4frtW7w4WfPVoQbfBNHu8U6MbK9bqp7%2Bi%2F6baXkuWYewlXBl7%2FOBB6IkGt1KhdRumxDw5HpSn4%2BuBLWPpn8Y8hceupBtbraRgj6A8dJ0SW1QPlCOAnqpQc4uOUqhOUhBJ0G2uMhr%2B7UwKLgxU469ziYeOAmwRMzTPwjtwqLIfdjzM02JbOMEynUexSh2Qgxr%2BhgzK6V4ZsuaAY3pXRvv4jzjmxuHSdu5jJSksD3Aw%2BSB9kZTbUGQm7lv4UdWBcdi4D0tinXxvrX4aptj0HrPFkl8CDdpUbZQ4KoRcKuOYk0WU3Cq%2FbPAUTzYi5TCIx1Sba6IBcq4pv4a5IlzQ2IZniK9zisNsBFbDwKv2oUOH5RouwndETcuIu16MdylLirH1w7pKmAY2nwxoSmkYbFpNtmqY1ZdDovPoRvpqh1TATSOe9zuwlER6r6vBqfa6BNHUPJJDZdtLIz5oTR0f26jgB3CDHYZ2lxFQ3EEK6MFEgO2eZ3uV%2FlBfiaCnL40Mxa0N42n8aKLw8Vangq6CDlygSKD8pjPcFMzL3NN34MAJULP2NAKlxDGikEnmX%2FT0r8sywyWeqaf5WgHC4wpL3cygY6pgHrAuBH9TowVEKbPStAWpIpg9opuYBLfi3pOJ4Xu2YWa9EAY58kS6GI%2B9ii2%2Fxy7QMah8KGev6oZjL2ZYXA3nUSZ0wvi45%2FxTt93ZlPeTUZYznOFUktRp%2FyxR72xVnn0n7oLH5tjJdQWzvljr2pHs4PD1hFxdkYNWsM7mquyQT8vh3dD%2BpCU2h6jqAnwasYj16k7foFfeI%2FWWtTiajBI54Zsxun9AiF&X-Amz-Signature=c64aaaa01ea03ee3bf9b7b8bca5240ac079a2eabd8e71ed4ddb191a217c652e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









