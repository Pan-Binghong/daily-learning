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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCBT5QOP%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxg%2BYTnx6La7w%2B21zqM5YJATFjN1EOCP5lINUYbXdCxgIgKA2SXCaJQFCioxd8PKtMeob4MBlQ1CF4ptblP573YA0qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUEI5tQ7gHoBm9u0ircA9IYp6%2FV5fAMd4N4bebOEw%2FV2TrdecNny1Blf76qrEDwyTzL2eEcmkreNTbDpcb9Vem%2BzuIpvCc3NG9M3frQ5NFJI0mASWLMYNcfG9RGurWXye9z8gU93OH6xJ0yPzThp9fLg3chn6pb%2BKFBPdJBJhDIZXOSe3gS%2BDjKR1hCzEAb3APUsfSZOD8RNrHyNxkyDwTaSGNuh1ik9tSz4ZYDrDjvWNLd43wTxd7tGPo39J2Fe82aUQshHw3Bw9SqLCq6fDsJQm0WNXQ%2FiHOsKXnpkbyY9Rpkt44oD6ZeWuYT78XsdZ61XDmxqPvncYE1iIqzwAeIcibXeM7dLWJQ9gqpvI2A1UnnwP1eXvSc1AuQ%2BD7%2Fj0WXBzQrLHfhu7Lto3Fxp4DPBWqfJyg4GXKpNHB3GofkpV%2BbQ7b9CNCYbCc%2ByBkN0GKAicmOQWSB8Bsfto3mz9doNAHvcuNBPN%2FRAObpGyoHAAxx5r3eCq%2BG71j7DCKTKRIpIzzj1qGjxsW9H7Ma4Xsw4%2BoRJPbyFwdwqdNLR2DULsrB0qVvTnaQEpQakbwHSZrZKitPpLf2aHOxgk%2Fig6oB59jzpOKNeuNMdlfFjVRNNupuGamnKawNFZ11L6RmMMdk3nMK067a2n0tMNfeo80GOqUBJmfDQQmMooq0cDoShm10npbE6mbN3yMQBWYHgLlVxQ%2FIyebokcELrF4uwspLTr5VF1sKCg49QECVVq124vY4lcbMbGZY6PWzVtl%2Bx2JZQl%2FIxiD6GZRYTwE5v1xOA%2BnZT45v%2BXwlPB7PolgbZXcXv%2BjyCppjvUkH13vYjJG6ljlRMxCRpJ53pWfVgWOJoUJERSUWCXjh0MYXbMlbrDdHa247mCI2&X-Amz-Signature=d5d290946f25cc4291b4926b0d94d66a4411f561b18525b7c5d02214a318bc93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCBT5QOP%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCxg%2BYTnx6La7w%2B21zqM5YJATFjN1EOCP5lINUYbXdCxgIgKA2SXCaJQFCioxd8PKtMeob4MBlQ1CF4ptblP573YA0qiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCUEI5tQ7gHoBm9u0ircA9IYp6%2FV5fAMd4N4bebOEw%2FV2TrdecNny1Blf76qrEDwyTzL2eEcmkreNTbDpcb9Vem%2BzuIpvCc3NG9M3frQ5NFJI0mASWLMYNcfG9RGurWXye9z8gU93OH6xJ0yPzThp9fLg3chn6pb%2BKFBPdJBJhDIZXOSe3gS%2BDjKR1hCzEAb3APUsfSZOD8RNrHyNxkyDwTaSGNuh1ik9tSz4ZYDrDjvWNLd43wTxd7tGPo39J2Fe82aUQshHw3Bw9SqLCq6fDsJQm0WNXQ%2FiHOsKXnpkbyY9Rpkt44oD6ZeWuYT78XsdZ61XDmxqPvncYE1iIqzwAeIcibXeM7dLWJQ9gqpvI2A1UnnwP1eXvSc1AuQ%2BD7%2Fj0WXBzQrLHfhu7Lto3Fxp4DPBWqfJyg4GXKpNHB3GofkpV%2BbQ7b9CNCYbCc%2ByBkN0GKAicmOQWSB8Bsfto3mz9doNAHvcuNBPN%2FRAObpGyoHAAxx5r3eCq%2BG71j7DCKTKRIpIzzj1qGjxsW9H7Ma4Xsw4%2BoRJPbyFwdwqdNLR2DULsrB0qVvTnaQEpQakbwHSZrZKitPpLf2aHOxgk%2Fig6oB59jzpOKNeuNMdlfFjVRNNupuGamnKawNFZ11L6RmMMdk3nMK067a2n0tMNfeo80GOqUBJmfDQQmMooq0cDoShm10npbE6mbN3yMQBWYHgLlVxQ%2FIyebokcELrF4uwspLTr5VF1sKCg49QECVVq124vY4lcbMbGZY6PWzVtl%2Bx2JZQl%2FIxiD6GZRYTwE5v1xOA%2BnZT45v%2BXwlPB7PolgbZXcXv%2BjyCppjvUkH13vYjJG6ljlRMxCRpJ53pWfVgWOJoUJERSUWCXjh0MYXbMlbrDdHa247mCI2&X-Amz-Signature=3a7f10efa79d026156737c51c5cebf42982d291d0ba238af1160c575121fd448&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









