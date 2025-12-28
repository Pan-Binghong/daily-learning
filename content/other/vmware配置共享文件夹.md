---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4XF2ZUR%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCm4oUs3ZT1flxN8%2B7jZLYAKj3YjjZJDkV5s%2BUf%2FDS3wQIgOQ4w6Lo4CNkhrbvsUZSdEwps2Uc2NW%2BuvNGEo1faY%2B8q%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDDLfLH4NTZJIo%2B%2BiaircA9%2BhZ5B05j6rMnOVUadG4znksxIWrh3Yz5PDhLhT6JAcvnne1NYZ%2FIkWBjJaWZrAPn%2Bza%2FryKTWgtQWIOfTUfhtlRfXuevFLlIYuFn7qexB8Ki6E4qZSpyAQkjkBOoBVgaWARNU6fxFMo5WfR0VisyxnzOR97rDJubgi7YHsyUqSzkHnneV7A%2FifbQXWTBcPz9xL3ReZntjP6QQiRxMUoui9AjdOZ7Cojvbvo%2BU3iOeG5k6m8%2Bsl63cOOfJHsC3kTvspvcKz5ssLo%2BP5GaMyhpnTC8YfJz2QEFt3S%2FTRJ1Iyge6q8j65rZnEO2v7KB5%2BuuzA1h5nwxbbIDbMgL7pzxF0o%2FPqIrDJ5t6tqYxyzx0qBBx%2Bvi8iSC%2BHX0XgZWKOZROCT5GIPcRd5YfvnrZWga4Rpbyejmx0%2FXyS69u4qTQ5aUpuSDC7hTTG7tM%2BHb6LGJdMWA%2B0bSDPY%2FvM1GQppim29hW4Q1bGlYGFapLyWRIYwOGRezF5rfLe%2BWFOYMRlv20z3pRTIG%2BDeQgAOnRiFZFsHgu50QWOgnzLa7JnICfN489hXh2%2BCfGhMF9MjB3hz1PewWpsBlLmp2QnDkO%2FtAXn%2Fh%2BmKx7lcP6ah5peD7YnByif380ru%2FIaYFVlMJywwcoGOqUBq3OmoD0pVDl%2FrsmJOvjCcAO4CRZFq%2F6dqRBAwOyRcAXVFHA%2FI0N5PpG5bLrwFqol6a5VLD8H%2Fx4snzIdSZuqZhMo962mwZEuOUBi21UMfocUno%2FPOgLlqATHXpj9fuY2RTjb6LsOCupNFvE772Q1ToRwmTclAyEkTpJN6ZXR667n8aLWvcLOG9F7K5fBWf9IrYoxUZNHBgoGHgzDyRdVU0ri4%2Fx3&X-Amz-Signature=65cf6e18ffff6b3267e5c558f1730fb0e2dd1fc4e2e4dfbaa01ecb5a1bb4687e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



