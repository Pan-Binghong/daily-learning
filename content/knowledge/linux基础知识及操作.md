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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTKNTID%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVWmUZ6iX09SgCi9FpHGH9cs6fq3J2jim%2FZFG%2BCjAWvQIhAKQ5fQwSLD2EAMK4udBBzyBt7%2Bfi0OpHT8lIIdaCfgnrKv8DCH8QABoMNjM3NDIzMTgzODA1IgwQU9tMRTQdNotf65Yq3AMMRMuSLqlsLSWoVO7OE%2F%2F9BOba9QkGCON8M7dZin%2FY2nsKRATWG2fDHcL6lEDAglfgi4qq7Nzjg36%2Fj1JJIzdFwhZL5BprjLILD6ZhN1vQ9VMlqroJRY9y5Mu6DGwC3gX4AcYv5seefWtQeT5aX%2F%2FA97sy1UohulitqxYqjul%2Fn4OP%2BolXMWzkFAtran2O7lGslXE7krROFaUW6TYxJLKhudCE9w7n8b3JXJR9mf6bvEwQ8cMjtwEYaAe9C3qfy7LsYFAGyUsWS9kqW3mz0jo%2FnHxYla78i7IyoG2bbGuXo3%2BwrfzQZ47QHLMUD5CykFOxL9E3sJ3tGLJC7kgfFOtfPNViXuOz4jpc0vk7xmJ%2B6H0v0VPlXi7exMLze6P3CJFFAdtpF95tpJx4wtfXJNi7Qt3VKvmRJ8jH2xnaF%2B3dh3x1%2BfjngjmXKUPr1zvi2c5y9mdYV7zNWPjE2fvT7iqizQanj5cWFphV7UYzQZvTUH59VBqoA%2FpY37M7YLfJUv%2FfXmbVJMitUWUbBjty%2Bm7A0Usq7crWDEL7vbzbzyhTX7IhJYWjn0N8lJ957bz9o0CVcxa7Z1y4vmUdF8ELWtmUmUgTmpv5S7rYd0PgVM6dBGfq1i%2BHCDqtZ94NFjChrL3OBjqkAdTBb0sozk5RnemWmCCCsQZQbxz%2FUDEt%2FxJROb6VNUmROEdUqx6Bui0O5RNtiCey1vzTWmVUoGkdv66eJqGlMFIEWU6USqBq8Dw%2FXyWgfkOTi9S3jaugaNQN0vthsjGHfw18N97RNXdmUVWK%2F7cgkHhWGJ6osFdrvtO39nhjSO7sgY2e9v%2Bqh6dtPTKlw%2BtiZ%2FTUUSVNcybxAS31D%2FXeIWEtvNpZ&X-Amz-Signature=8e73a9735917d5b260e981876cb920634f2a9d55b0619976b53e820b04ff6fa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCTKNTID%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVWmUZ6iX09SgCi9FpHGH9cs6fq3J2jim%2FZFG%2BCjAWvQIhAKQ5fQwSLD2EAMK4udBBzyBt7%2Bfi0OpHT8lIIdaCfgnrKv8DCH8QABoMNjM3NDIzMTgzODA1IgwQU9tMRTQdNotf65Yq3AMMRMuSLqlsLSWoVO7OE%2F%2F9BOba9QkGCON8M7dZin%2FY2nsKRATWG2fDHcL6lEDAglfgi4qq7Nzjg36%2Fj1JJIzdFwhZL5BprjLILD6ZhN1vQ9VMlqroJRY9y5Mu6DGwC3gX4AcYv5seefWtQeT5aX%2F%2FA97sy1UohulitqxYqjul%2Fn4OP%2BolXMWzkFAtran2O7lGslXE7krROFaUW6TYxJLKhudCE9w7n8b3JXJR9mf6bvEwQ8cMjtwEYaAe9C3qfy7LsYFAGyUsWS9kqW3mz0jo%2FnHxYla78i7IyoG2bbGuXo3%2BwrfzQZ47QHLMUD5CykFOxL9E3sJ3tGLJC7kgfFOtfPNViXuOz4jpc0vk7xmJ%2B6H0v0VPlXi7exMLze6P3CJFFAdtpF95tpJx4wtfXJNi7Qt3VKvmRJ8jH2xnaF%2B3dh3x1%2BfjngjmXKUPr1zvi2c5y9mdYV7zNWPjE2fvT7iqizQanj5cWFphV7UYzQZvTUH59VBqoA%2FpY37M7YLfJUv%2FfXmbVJMitUWUbBjty%2Bm7A0Usq7crWDEL7vbzbzyhTX7IhJYWjn0N8lJ957bz9o0CVcxa7Z1y4vmUdF8ELWtmUmUgTmpv5S7rYd0PgVM6dBGfq1i%2BHCDqtZ94NFjChrL3OBjqkAdTBb0sozk5RnemWmCCCsQZQbxz%2FUDEt%2FxJROb6VNUmROEdUqx6Bui0O5RNtiCey1vzTWmVUoGkdv66eJqGlMFIEWU6USqBq8Dw%2FXyWgfkOTi9S3jaugaNQN0vthsjGHfw18N97RNXdmUVWK%2F7cgkHhWGJ6osFdrvtO39nhjSO7sgY2e9v%2Bqh6dtPTKlw%2BtiZ%2FTUUSVNcybxAS31D%2FXeIWEtvNpZ&X-Amz-Signature=77232c4bd61f8bf04436f1bf92ddfd4e301f13295b40f9d2cf7258e29b2da6fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









