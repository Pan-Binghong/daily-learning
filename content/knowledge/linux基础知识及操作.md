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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D5X6ZWI%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIEFlyT6ialvAwIv7Thh5T5kgsHjJ%2BQ1LR%2FIyDcK3CI8OAiEA7qPCPen8qJ2ApWyP0PrjKeCIraO5EWgNvlTkc4DsHVgqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5Iv5Jjt4eu7OoYOSrcA4rHZQGTS6hCTVzj3JJVTmYuW7PEByCyGCHVWLjJEtkJZuUZX8iqoWdq5%2BKgppA2jy9JzQXtQjd7IOFh%2Bj7m6%2FVd7f%2F0Go8cxgTKLe6dRo3FCG6tn%2FLwi%2FjvcJIdR2tz77sFIq%2BaDMuSgk9xcASiJDd3tpd4qZAebCt%2B9zN%2FHsL4wTy2BE6f6aM2%2BRaZSMqndV%2FMYnKlDG2AxulTf28ot5zrlUiEf7hHQZboNimrLlAgOQ7hu%2Bjo5RgpWTl8ZLjlIgGWfm6Sp9ke%2FDHWoVrDIPP0LsYHfLxhc3qefHepnSQvo88Ay%2BUHdwBhcJ5Urw7PfVLXWLe%2B3CbpSrS7L%2F6E63uaCuMtSzJ%2BUBD8AfvQjOESws6l6KfwmKN%2BVu84q16QzVhnmzZ9TOAWbuSqPT3D9QN6l4AtS1DU%2FMq5aBNwg2xm94wginNWar3iVOFG3lT1HIvzcTTSNJyyTQgYPG1inXg9jBtTQgmrak%2B1xr%2FhZ48XTXuSrrS9uc%2FmZgX0pTlPGgOqY6rm4Zh2xdmoAJv5pIDG3GpNlMYAJT%2BAJdTEfALsWa3kG%2F9ocX9bBOobCRlFuB3nbI79At0a4WXXde5KpZJSGl%2FETuIzfjP241tfi93IFKrrV4rN9gjLzdwtMJ3K9MgGOqUBhbet499MHzba7pvQiGZjLKGAOCWIqoL4HWh7v%2FGyqbqmEUDa7Bjpb0l1Gm1Vd35h0muWtp6ioWYPW%2FdPvExlSVyk2jVfJoy24KMJlXRz0HmDGFCguM98sFBTnhA5Y3w1IEuNiE5%2BsrvvcrWVcJEcWSDM3VxBCyBxf3u%2F4Z0Nkx0SsWd3DwGgPadlcuPtPCha9XQbjViHbLtPDaF5F%2FFBMnfsI98m&X-Amz-Signature=50084211aab324b7fedafb71ffcf7fc769ce4464688b59e057ef3670fc9b0e87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D5X6ZWI%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIEFlyT6ialvAwIv7Thh5T5kgsHjJ%2BQ1LR%2FIyDcK3CI8OAiEA7qPCPen8qJ2ApWyP0PrjKeCIraO5EWgNvlTkc4DsHVgqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5Iv5Jjt4eu7OoYOSrcA4rHZQGTS6hCTVzj3JJVTmYuW7PEByCyGCHVWLjJEtkJZuUZX8iqoWdq5%2BKgppA2jy9JzQXtQjd7IOFh%2Bj7m6%2FVd7f%2F0Go8cxgTKLe6dRo3FCG6tn%2FLwi%2FjvcJIdR2tz77sFIq%2BaDMuSgk9xcASiJDd3tpd4qZAebCt%2B9zN%2FHsL4wTy2BE6f6aM2%2BRaZSMqndV%2FMYnKlDG2AxulTf28ot5zrlUiEf7hHQZboNimrLlAgOQ7hu%2Bjo5RgpWTl8ZLjlIgGWfm6Sp9ke%2FDHWoVrDIPP0LsYHfLxhc3qefHepnSQvo88Ay%2BUHdwBhcJ5Urw7PfVLXWLe%2B3CbpSrS7L%2F6E63uaCuMtSzJ%2BUBD8AfvQjOESws6l6KfwmKN%2BVu84q16QzVhnmzZ9TOAWbuSqPT3D9QN6l4AtS1DU%2FMq5aBNwg2xm94wginNWar3iVOFG3lT1HIvzcTTSNJyyTQgYPG1inXg9jBtTQgmrak%2B1xr%2FhZ48XTXuSrrS9uc%2FmZgX0pTlPGgOqY6rm4Zh2xdmoAJv5pIDG3GpNlMYAJT%2BAJdTEfALsWa3kG%2F9ocX9bBOobCRlFuB3nbI79At0a4WXXde5KpZJSGl%2FETuIzfjP241tfi93IFKrrV4rN9gjLzdwtMJ3K9MgGOqUBhbet499MHzba7pvQiGZjLKGAOCWIqoL4HWh7v%2FGyqbqmEUDa7Bjpb0l1Gm1Vd35h0muWtp6ioWYPW%2FdPvExlSVyk2jVfJoy24KMJlXRz0HmDGFCguM98sFBTnhA5Y3w1IEuNiE5%2BsrvvcrWVcJEcWSDM3VxBCyBxf3u%2F4Z0Nkx0SsWd3DwGgPadlcuPtPCha9XQbjViHbLtPDaF5F%2FFBMnfsI98m&X-Amz-Signature=014dfb25d429f4a6227ddea7d1bbc6799e8d5545b17cdb96c64a41680bb99b4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









