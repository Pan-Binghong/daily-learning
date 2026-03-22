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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUDZEHCI%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BwR5AshjQtgtHyZj%2B%2FN8tPc89MYb5XdQS%2FFPlPfK1hAiEAsUxCXOPZ6fNJaf23fNSC84xW2CnxPiDEFOZaD6NF4%2Bcq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDL5Ddho3LfVbnQqCKyrcA2CyqtrZar%2B250zIfG%2BbHy3Qjc3IX2LkaptoR3qQsLBc5kXjdUTP6YgNpKWzigeGIi4ZrW7GCY4sQr%2F0sG6W4M2mjzWGFz%2Bw0XqnQ85Llwmp2C2jB1BPXrq148uTKDIMLTNK5QoPeDJVt%2Bo60LEe%2B3XwxOun43Becs6rrzMQPI5gx0etkBBchKKdSkrVpAXTC5et851UMM6lsN%2BLXbZ2%2FKROs5vpTFFmLYBUD2wu9BUOiOlXwcNF3jX9TZX0C6DBKmSYSAiMgJOKgF%2BriykfnZxwslrxmo0LP7C9AMKt7nlm52aj6mFvy0LZltRdju%2BW8FnCEZ5ycrNGIbba%2BzWTMoS7wRa8HdugG1mB3EbKG7SvS3pXG0ojYAk1ySECqqbu08s0wnnr3rhyHGzeBf7PRLAFLIccdjhhtGftz%2FNYdj7P7UaD%2Bfbkm7HuA1YG8wMvqu%2FIRMA445MMsyf7HM2QApByBQsK006x9iOwh7GWzsd0v9s8uiQR98E%2BH6wp%2BC6QAOK%2F50k5k9thenWUI68RwgCp0Jh45ffaSYRRaeVXAfTG7f9iGFKebQOiz70A%2FkWBHKf67VWCjiuO5d88ydEs3SD1s6QfNaq5sPmNHhS2u6l2NKxwmsPO%2FVbS8OCMMO6s%2Fc0GOqUB%2BOKu9cfw6bOv9zUDZs%2FpomZnbYesE011msfKlRGW%2F%2B5ANTmfPyjalKUQphBr7KZrPJcmOzIFXArOnl42WEGhXoYw7a3GVrlBAcVg39fSGZbz%2FyYTpUOdnXqZFsi7SRDMevgDmR13KeC3BukZ1LYMeS%2BolI%2FNrSFm%2F1oDJRaVpfNXlCUv4KEapooZ%2BT19khXK2oCW1W5T6%2BO9dsiAHTDuJ09MAOsb&X-Amz-Signature=b2117301d5ae29a85e33849be27a0b29ed757615c81b0e4aee5c34d3af4e2478&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUDZEHCI%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC%2BwR5AshjQtgtHyZj%2B%2FN8tPc89MYb5XdQS%2FFPlPfK1hAiEAsUxCXOPZ6fNJaf23fNSC84xW2CnxPiDEFOZaD6NF4%2Bcq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDL5Ddho3LfVbnQqCKyrcA2CyqtrZar%2B250zIfG%2BbHy3Qjc3IX2LkaptoR3qQsLBc5kXjdUTP6YgNpKWzigeGIi4ZrW7GCY4sQr%2F0sG6W4M2mjzWGFz%2Bw0XqnQ85Llwmp2C2jB1BPXrq148uTKDIMLTNK5QoPeDJVt%2Bo60LEe%2B3XwxOun43Becs6rrzMQPI5gx0etkBBchKKdSkrVpAXTC5et851UMM6lsN%2BLXbZ2%2FKROs5vpTFFmLYBUD2wu9BUOiOlXwcNF3jX9TZX0C6DBKmSYSAiMgJOKgF%2BriykfnZxwslrxmo0LP7C9AMKt7nlm52aj6mFvy0LZltRdju%2BW8FnCEZ5ycrNGIbba%2BzWTMoS7wRa8HdugG1mB3EbKG7SvS3pXG0ojYAk1ySECqqbu08s0wnnr3rhyHGzeBf7PRLAFLIccdjhhtGftz%2FNYdj7P7UaD%2Bfbkm7HuA1YG8wMvqu%2FIRMA445MMsyf7HM2QApByBQsK006x9iOwh7GWzsd0v9s8uiQR98E%2BH6wp%2BC6QAOK%2F50k5k9thenWUI68RwgCp0Jh45ffaSYRRaeVXAfTG7f9iGFKebQOiz70A%2FkWBHKf67VWCjiuO5d88ydEs3SD1s6QfNaq5sPmNHhS2u6l2NKxwmsPO%2FVbS8OCMMO6s%2Fc0GOqUB%2BOKu9cfw6bOv9zUDZs%2FpomZnbYesE011msfKlRGW%2F%2B5ANTmfPyjalKUQphBr7KZrPJcmOzIFXArOnl42WEGhXoYw7a3GVrlBAcVg39fSGZbz%2FyYTpUOdnXqZFsi7SRDMevgDmR13KeC3BukZ1LYMeS%2BolI%2FNrSFm%2F1oDJRaVpfNXlCUv4KEapooZ%2BT19khXK2oCW1W5T6%2BO9dsiAHTDuJ09MAOsb&X-Amz-Signature=92f54ea49c9b1fbf396b8d4d5b96fa7379a8c124c130061f7936837a4cd84593&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









