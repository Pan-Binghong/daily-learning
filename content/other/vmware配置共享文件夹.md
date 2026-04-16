---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYM42YBF%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHh5H9tl7ULfEyIODR5lpEFdGPXR5GXMIo7s%2F2erG5GdAiEA2Kw1m1zHySM2awWojZECJyE0LUtNlkFqHDpencGObjcqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4Q2sStXpKassvsNSrcA43e1cnrqjJJuIC0fyOf8ltNh9LqAHCNdmGEK%2F5ipHIO7OsDxaGHRt4WiJSF0Cg29cmHzTEb87h3eRSG1dgYsRwLOd3GjESbdlcu4%2FEiAEkn27eazOXWSpG5mXCGff23MK9ubOL8bLLD%2BwmUGug5APjnW5LerVNd1eBShEzKH7lc4IfSUmNq1V1KDftU9I0e93M86fLbmDbAcOFzcNtOo%2BYYhuB2GNzQrNwOMX8%2BesBUbQ39KDEh5%2BIAEPQyF%2FpPTqrHoBzt0EfS1epkbH60yRMNdYoNe966pA7AOhjnTMqLEif4ZKLv8c0Q5kgFhSSRPoUmf5%2FpKcpIumk%2FQUD0YvpsorKwS6BUgavZZSXB2ccmesPSMU86M9xjdNdLrmimsL%2BNeatYQPiEbFJUX0tGFx1WakyWuPTZc%2BINwOWc1H7WQ9lUjoXKRVqpgXxsP%2BGyzM4ZDem8mqv3kRPyfHEMLKaKb6kLYH8w5yJKcJKAJfILyQOofhgPcYb99sX8r95hGDLgNNZPW60Vjc%2BvyQCOrinHNyEATiPEjBsiAw7XCDBtwfLPCF0pbkUX3aZKZMwZk5jjKGdt%2BLVXLasSakz9FdlwOqu17Pbjvp3ykb6zXSDujmdXP2rzRus%2FUK4jMLW2gc8GOqUByuIda4snnatW%2FaBuTnh7gmYVqzkA02ZhlEhA20T1y3YeXqGhTpPpEDI6sA25y0abxRGtPoRT7Z7gt%2BDad0i%2F9xF5BRey1UqSkhEhCEl1Vdpe1sriTKCxwgGG8jf%2Frv3QTYrFkmGNnYfrUzpKSpGZJe3T3WOhhUMlwNIiQNwAtGb28Fl9GBxSyiDJsx%2FuGBSl0GM6A3l9%2Bs7P7T8B%2BqjXbImxB3rY&X-Amz-Signature=8fbc62882a4907b5b4c1cc687790214220b4973da44259ce991acac26ce40874&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 安装 VMware Tools

- 找到虚拟机 - 重新安装 VMware Tools | 如果是灰色就执行下一步
- 重启虚拟机
- 重启的过程中，不停的查看重新安装 VMware Tools
- 当能点击时，点击安装即可
### 配置共享文件夹

- 点击虚拟机设置
- 找到选项
- 选中共享文件夹，按照上图进行配置
### 查看共享文件夹

```bash
cd /mnt/hgfs
ls
```

## 坑

当执行完后，如果没有看见自己的共享文件夹，执行以下命令

```bash
# 如果输出文件夹的名称, 快执行下一步, 如果这个啥都没输出, 我没治了.
vmhgfs-fuse /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```



