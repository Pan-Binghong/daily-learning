---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KTUWO7N%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T033008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXxru%2BrS9zYlcd49FTFnJn1ilOYKdYTLNEixeY1M5EhQIgFpx%2Fn%2BWyNLyn3%2B7m9tBbfRorvCnAJax60zmlP%2FEkZY8q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDGaOndVEk9Wx9c3aYircA4AEbOywok4barxX6hrjMXEC8PerpGCj6r4f1vSIe7g%2FqOEGvQFjRUwCyQFGCQEe%2BGs6UeZ03od6Me%2Fmp42RsdajKfi4fr6Yj8UygPfVgpRFTdOkB7iJSF%2FUhDTQNaHNB7qzlI8RCGC9eCGUVU1NsFR7WWibAJ4LojJLAwAX%2FTfZAbe%2FruxOFTWycNRlgl6jthCEl9DgXaLsXwEJVtW%2Fywh8xYjxXhG3djwxQccXSeexZ%2BN4rxMbK%2BRY%2FFqjijJvVi3uSUWqVuxQqIgnFneSKm3itXNJvLiG4%2FQ8ei4zP4wKqO4fOVv%2FijPlk5IsVCSJn24ZjupFOwV0pPstYeF2CeW6lZy9%2FGOz4Hy9C%2FG3fF3rhCg9xnLhDv3G4fv05ujZRgR6dsHFPcA%2FXRMC0HVcBz1E2WWZvk6KC7SgJJVqobRAoT9fjyvkywCBn1HtnfQWtOv3x6nWPCPgsffDkpAT5XaKxbfvKWY6WM7DnokewGxVtgE8Lc8mE5LKi6p6Yt4y4lJDOm8eshXOPnzMpeQ2PAZK%2BBriz0zxzk5vygMUw0gnlsegEjQpaasY%2FMsu1DUYK1hWQ%2FYwaf6bH7uF4LUHxXqjFKZI8utsqggz%2FGW5YrYSHGPdZ4Gppn%2F3C9giMOei68sGOqUBJReiSJteMwMeI3jSXHP2%2FigqRUPw4973TA6%2F2QOcM04FxXVQc%2B%2FIpGsntlJMp8H%2BeJhSDvzu9guIpblUdwJbWF%2Bw9xLgSc8TGouhNo3mYNWxusr%2FEQ6%2FH8gSpwrR87pZ%2B32LABSnWozpCeA2Jg7DrS37X6s%2B2TT66v%2BogX0xiu4eL3H6oj2TuTydgvShKa0RcxLTlD0sc%2Bd6KFsWq7SoOHuOpCUc&X-Amz-Signature=c5c8455a76d89a0a918d6d5776ba3b3d4f2b85ddbabca1073d34b8ac8b681206&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



