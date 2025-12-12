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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBFQ4BDZ%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCzKj1wjiDwf5cCWbIGGsZvHmT%2Fzp%2FlN%2BKOOqov03s%2F7QIhAM4hRxYnAZdsLtGPSIPNtRd56lPLJI%2BgUWljkzpNA0wNKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDXIGXwW5ipCb3WxUq3APqCxf4ERXOQI%2Fv8T5GMLG1zlIWcVlJepozi4EuEj7jzShgP%2FqEW7jYUvGkGsjmAZhCLulqOCAeGVXMtgGIdPjmNpOBoLFMtg8uCGKjIP6za1CaB3OVwqDYH6jJyys42cDUT%2F1jexCZQH7nRUDGowNkYrEF3uzdnLWhK%2BN9QHSp2zdIufGse1CCQpNQP2L7PVH68NUs4jdp1GfSjHX9GYtIw%2BbMnuFZc76O3ucOmV%2FyTQfcwwhbUB0D05C0lH15ahlr9OrumzFDiO6U8lmTgxAhIJYAnxHpSJNRej1e74FzxMqGCgopR9jKyLyOgItnk%2BdEC3wj9izTsUaHweLD8RBtpV%2F%2BEBl1O2Q0J0jd%2F28MytvCSf%2FQiiiVzHBGzXye1B5H5GXRKEpLh5MDzqlDybdaXaSZayDI5jmkIOmbL%2BjOp5%2FtHrFA0i3x4Xq2V0gPqBFHjSupgyCq0wdUVt3Qn8m%2BAAF%2FWsjW84R0HqpMqi%2Bi4bwLGVh%2B%2FIPrgE8IQdn3w9JgYUl3pmov%2FCnV8UfJyW6DQVgIaU1JINoz50l%2FgGZ1IqYsEW97CF5qCVcJv5hVQn7e%2BPJ4lM%2BzmMPWIy1qQugEnj7Ck25mIHCIvUE5LkrRMJB6Jl%2F2ZFXRaC4OkzDk1O3JBjqkAQ6vpAQyKVwlnzShmlfDxGPgBo%2B2e%2FIWZ%2BldHmOddingTotlOoyCo07NRMcURipQ22aN2vBeSrfKwQmkkXZ5c1qzk8X%2FGkApalLmFdu7GW%2F3uKhTcmFzSQXsWjZcWvFfNt1Q2S2OfgE7n2x%2BoPW6TUJwRzMpel5cJSK9DY8JztLMyncsul8KKgePgV5vVh%2FaTqv1dVOwMQS793ZqNsUhY0SyAZZm&X-Amz-Signature=2b618e08ffc195c2067b1d4b86ae77899412ed61c5a970d0586a89fd30483e14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBFQ4BDZ%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCzKj1wjiDwf5cCWbIGGsZvHmT%2Fzp%2FlN%2BKOOqov03s%2F7QIhAM4hRxYnAZdsLtGPSIPNtRd56lPLJI%2BgUWljkzpNA0wNKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzDXIGXwW5ipCb3WxUq3APqCxf4ERXOQI%2Fv8T5GMLG1zlIWcVlJepozi4EuEj7jzShgP%2FqEW7jYUvGkGsjmAZhCLulqOCAeGVXMtgGIdPjmNpOBoLFMtg8uCGKjIP6za1CaB3OVwqDYH6jJyys42cDUT%2F1jexCZQH7nRUDGowNkYrEF3uzdnLWhK%2BN9QHSp2zdIufGse1CCQpNQP2L7PVH68NUs4jdp1GfSjHX9GYtIw%2BbMnuFZc76O3ucOmV%2FyTQfcwwhbUB0D05C0lH15ahlr9OrumzFDiO6U8lmTgxAhIJYAnxHpSJNRej1e74FzxMqGCgopR9jKyLyOgItnk%2BdEC3wj9izTsUaHweLD8RBtpV%2F%2BEBl1O2Q0J0jd%2F28MytvCSf%2FQiiiVzHBGzXye1B5H5GXRKEpLh5MDzqlDybdaXaSZayDI5jmkIOmbL%2BjOp5%2FtHrFA0i3x4Xq2V0gPqBFHjSupgyCq0wdUVt3Qn8m%2BAAF%2FWsjW84R0HqpMqi%2Bi4bwLGVh%2B%2FIPrgE8IQdn3w9JgYUl3pmov%2FCnV8UfJyW6DQVgIaU1JINoz50l%2FgGZ1IqYsEW97CF5qCVcJv5hVQn7e%2BPJ4lM%2BzmMPWIy1qQugEnj7Ck25mIHCIvUE5LkrRMJB6Jl%2F2ZFXRaC4OkzDk1O3JBjqkAQ6vpAQyKVwlnzShmlfDxGPgBo%2B2e%2FIWZ%2BldHmOddingTotlOoyCo07NRMcURipQ22aN2vBeSrfKwQmkkXZ5c1qzk8X%2FGkApalLmFdu7GW%2F3uKhTcmFzSQXsWjZcWvFfNt1Q2S2OfgE7n2x%2BoPW6TUJwRzMpel5cJSK9DY8JztLMyncsul8KKgePgV5vVh%2FaTqv1dVOwMQS793ZqNsUhY0SyAZZm&X-Amz-Signature=a9b354008d5d831aebded46621ae766c8b06b2d63ff72974c6208441e2d3c450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









