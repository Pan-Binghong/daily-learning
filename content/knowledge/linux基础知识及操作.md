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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URH43MOO%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLv6rzqZPrWDsC4ZQS1o6ODXfCBw39ZQyNvJKFcWFsAwIhAICUQIYLcoa3E8bhECsi3n5LvtyBBAcHIP4haAdZN%2BoBKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJSaezc3A96c6c6mUq3AOk4eUKTqB%2Fljpx3XNOuSUkHT5EYXxmSyou1yWkGmHOFi3OOS12wrZZ0jp1vmmapw68KY5%2BPAMnomifbz68wfeZVpeNTmRsgbjO%2Bvr1Douuiry5jbRK6NEpDrV07y4YHjau7AApHw2VZ5I%2B1IXULikmEWXrzLVdxydXTTV8HpRzpv1rNL0Tnlf2uNRGjO0fPFgC4recQ6o%2BUpMFknVNx22i7W4mOu5tZi%2BhFrYCxbcR7W%2FCsQXw5V%2FZ6Cr77vjaMXxB66K1tYjER2nhNCLRNey2Z55w35kUxhPu%2BGA4K8AVYVZ%2BgjUbIKXpxWKzVxtMsfBvVy9RKFC3biuZN66AYfyZhryk833zLmyb4Zh4Vc2tzlllMyKPU7uUTUDKoN8rzdDGHfGekcbHJoGx9R9kdE6WnP%2Bwy7%2FjSoEfKURNOfWn7MnqfYm%2FgQQIEva1UlMZ2OfHnZbjBVfWXtzNWbXYSxtwQ%2FOg4zpOaEwdhvvkjPIf%2F2wJMfr803sKpqJLZFgHsavYfn1yIUrlS0UH%2FoKjrfON48fY97YV9vEsOyKu5%2FJ1HcHUGI%2B2PBijjRkWlB7zrRqzYuXHq9Yfd%2FHznfEZvndSoS1Gym8CEK1HH6AC%2BUV6hMgJlUDonsTTmYt4bjCJk%2FzOBjqkAUHBgB2K103MuuR37tLDvEfCGGrZVy1%2B%2BH8ONnjuQHltNSz3cGmtwEThLulcbdOlgMV0jla1f%2B7W1vgxtpLaUWiQNNbbupdhQwbL%2BRZ6WUEHtxfGrWqgxRharaxwOKHT7WH5ztugJAg7exiYdhsmOHcuXZWSt2HZeTPsySUp91cHad52u7f75dT%2FJuqQs9YpMA3VleQBLpiau7LXqsEeRAgTv%2F%2Bb&X-Amz-Signature=d4274654ba7fe94da34a880ffb2feb0b123b92b8ef3056d266a08162438acb60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URH43MOO%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLv6rzqZPrWDsC4ZQS1o6ODXfCBw39ZQyNvJKFcWFsAwIhAICUQIYLcoa3E8bhECsi3n5LvtyBBAcHIP4haAdZN%2BoBKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJSaezc3A96c6c6mUq3AOk4eUKTqB%2Fljpx3XNOuSUkHT5EYXxmSyou1yWkGmHOFi3OOS12wrZZ0jp1vmmapw68KY5%2BPAMnomifbz68wfeZVpeNTmRsgbjO%2Bvr1Douuiry5jbRK6NEpDrV07y4YHjau7AApHw2VZ5I%2B1IXULikmEWXrzLVdxydXTTV8HpRzpv1rNL0Tnlf2uNRGjO0fPFgC4recQ6o%2BUpMFknVNx22i7W4mOu5tZi%2BhFrYCxbcR7W%2FCsQXw5V%2FZ6Cr77vjaMXxB66K1tYjER2nhNCLRNey2Z55w35kUxhPu%2BGA4K8AVYVZ%2BgjUbIKXpxWKzVxtMsfBvVy9RKFC3biuZN66AYfyZhryk833zLmyb4Zh4Vc2tzlllMyKPU7uUTUDKoN8rzdDGHfGekcbHJoGx9R9kdE6WnP%2Bwy7%2FjSoEfKURNOfWn7MnqfYm%2FgQQIEva1UlMZ2OfHnZbjBVfWXtzNWbXYSxtwQ%2FOg4zpOaEwdhvvkjPIf%2F2wJMfr803sKpqJLZFgHsavYfn1yIUrlS0UH%2FoKjrfON48fY97YV9vEsOyKu5%2FJ1HcHUGI%2B2PBijjRkWlB7zrRqzYuXHq9Yfd%2FHznfEZvndSoS1Gym8CEK1HH6AC%2BUV6hMgJlUDonsTTmYt4bjCJk%2FzOBjqkAUHBgB2K103MuuR37tLDvEfCGGrZVy1%2B%2BH8ONnjuQHltNSz3cGmtwEThLulcbdOlgMV0jla1f%2B7W1vgxtpLaUWiQNNbbupdhQwbL%2BRZ6WUEHtxfGrWqgxRharaxwOKHT7WH5ztugJAg7exiYdhsmOHcuXZWSt2HZeTPsySUp91cHad52u7f75dT%2FJuqQs9YpMA3VleQBLpiau7LXqsEeRAgTv%2F%2Bb&X-Amz-Signature=8cd2779087a9f54d82b0c1aef0ffe06e3fa82e48ba7fc6631a577cccaf8c5e1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









