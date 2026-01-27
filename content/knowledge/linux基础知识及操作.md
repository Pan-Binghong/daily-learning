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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/685c3aa8-3f48-4d61-8042-eb0245fe07f1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXFO7IGG%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsgYrN2M9Fs2QmSCTaW3JMpH9h1j88zz0Twi50IA9AbwIhAOBx9vYVO9FK5ZqNws4MXDA6HvnESvF93P2HAoCr6GvDKv8DCEwQABoMNjM3NDIzMTgzODA1Igyb89I8DM7dQTbccZgq3AN5PmZ8TsgBmc3EdxEJi99XVVBs2gbkC9inPA0Ms6UaZKHjIW3iuaff6molakBzPaaEFDU4SqOUeJM2rDyrAXxrOxqBXJA4plcc48PKuP20LiFJQJSkfZeqNN2ujPLIevNbOJG4JBKFvyr0wJAnyq9ck%2By6FbT8%2FgaDL65lSt%2FW3cZJtLrQTrirovWqPDAnMgbGVC%2FoFs53keVxsp3uXF%2FgeK41oHP4bG4G8%2BSVHjfLuNM4GO8FNaHNV6WYYtEkXUsFy21BcfAU%2BhfrwI5P4U4Z2KY6WHzABdA7ox4kHjvFFLelwG1l9Gmxl%2FGH5V0UwHUcozyhPnVTVffKyvbh2fBHPT48BWqmTIYrhsx1cNL24jHe9yl%2BaWyRA8GVPDgsAQUJPoOyWH9mkHFZ17ilJPpc%2B2c%2FFJY%2Fk6ZZIDT6t4oGPnpqMfqDCg%2Bul9DiDOo8cAKMrGVu6%2FAZvkxHY9yu0M7ApoIoWgLLuAxY6HiTqh7RbxyLOTjtXyFkXpkjHeBNyXHWqQUj6OMWtPMnlLp%2BshICTXrNxv2HPUqmv644iKYRf%2FbXulTYAldduaK4im1E9b8WQ0bfYAM3sZh%2Fv6nXa4UoMRcp37kxnhYah5XXfw9NIQfyYKSxcX4Ofns3PDDM0%2BDLBjqkAaz4LQvykw9%2FUo9NWJSvmRnwyafiD6BCjs2vjRqsdYFSDlzKwKLJerxLHz4hltE7Ou%2FVfQBWukm1GMiiXelx3YnwWO6lRkAsROVyfXzDK07KPryY8YKq2VkS4%2FwnIBVf0Aow1x737a4mkw%2Fln7tE790ku85lPbmGVLouoOag2hJggdrCL6KcCUuzxHPebwJyN3PbvoFc2CyoawjO2aPzECo%2B0tVH&X-Amz-Signature=3671c5522ebd9463169c6a5a02ddc50129ea6a8613a3a1b8b6ab1d9b1cf8141f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

以上案例中，main.py文件的第一个属性- 表示为文件。

接下来的字符中，以3个为一组，且均为rwx的三个参数的组合。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/12d462e3-e272-4346-8b44-dc1b18f78b42/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXFO7IGG%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsgYrN2M9Fs2QmSCTaW3JMpH9h1j88zz0Twi50IA9AbwIhAOBx9vYVO9FK5ZqNws4MXDA6HvnESvF93P2HAoCr6GvDKv8DCEwQABoMNjM3NDIzMTgzODA1Igyb89I8DM7dQTbccZgq3AN5PmZ8TsgBmc3EdxEJi99XVVBs2gbkC9inPA0Ms6UaZKHjIW3iuaff6molakBzPaaEFDU4SqOUeJM2rDyrAXxrOxqBXJA4plcc48PKuP20LiFJQJSkfZeqNN2ujPLIevNbOJG4JBKFvyr0wJAnyq9ck%2By6FbT8%2FgaDL65lSt%2FW3cZJtLrQTrirovWqPDAnMgbGVC%2FoFs53keVxsp3uXF%2FgeK41oHP4bG4G8%2BSVHjfLuNM4GO8FNaHNV6WYYtEkXUsFy21BcfAU%2BhfrwI5P4U4Z2KY6WHzABdA7ox4kHjvFFLelwG1l9Gmxl%2FGH5V0UwHUcozyhPnVTVffKyvbh2fBHPT48BWqmTIYrhsx1cNL24jHe9yl%2BaWyRA8GVPDgsAQUJPoOyWH9mkHFZ17ilJPpc%2B2c%2FFJY%2Fk6ZZIDT6t4oGPnpqMfqDCg%2Bul9DiDOo8cAKMrGVu6%2FAZvkxHY9yu0M7ApoIoWgLLuAxY6HiTqh7RbxyLOTjtXyFkXpkjHeBNyXHWqQUj6OMWtPMnlLp%2BshICTXrNxv2HPUqmv644iKYRf%2FbXulTYAldduaK4im1E9b8WQ0bfYAM3sZh%2Fv6nXa4UoMRcp37kxnhYah5XXfw9NIQfyYKSxcX4Ofns3PDDM0%2BDLBjqkAaz4LQvykw9%2FUo9NWJSvmRnwyafiD6BCjs2vjRqsdYFSDlzKwKLJerxLHz4hltE7Ou%2FVfQBWukm1GMiiXelx3YnwWO6lRkAsROVyfXzDK07KPryY8YKq2VkS4%2FwnIBVf0Aow1x737a4mkw%2Fln7tE790ku85lPbmGVLouoOag2hJggdrCL6KcCUuzxHPebwJyN3PbvoFc2CyoawjO2aPzECo%2B0tVH&X-Amz-Signature=065c82e478d059ed0ca8994e9ee0ff162a510d213feaa1ed17ccb62dd7b80e9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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









