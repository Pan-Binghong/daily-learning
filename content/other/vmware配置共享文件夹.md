---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CM3UK4O%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCR5nD2UbJnt5b3CX1S7YbsBHsTxNclk8TmQZqJmHykjwIgDVqbB5hQfGU4V8nbUyTv1HuJP9SOHj%2BMkfb4U5xejkUqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZh9cqLdg0dP4wIuyrcAw6Gws8A4RaY8eHOYih1VrYoDdiTANuW8uCMwYdmZa4QhAgRFlAkSSms7Fa6vbP%2B5%2BF9ptdgBI2zdBAgr3IvGP0%2B3oUGPl3CsVVAk%2B7%2FH2BmFdn7BD2FHnKwUk4X%2Br385jSf7wTBoheE1htxJj38uz3uXqK9%2F9jL5fximthZ4is9vkroKmYru%2F%2BrlM4lDbZdZXSQ5xJRYMcjhZUVtg3I70Vnnn7qEzYF10Bkg8mqmHd7beLknUJxn4dTW3GbFnLBd8WGLSKPJcx1lt0PWu%2BT6Bk6%2FwTWnn801PDu%2FHGrk6tw93ZjPKFCgAOm%2B1z8mXrAUYHZOX5OzltN6EsvoR31QBPAVnwcUVB5X1%2FYKZmNpHD83cftV5oTo5jTGad5AoU%2FJOmZHZEgTIZ0bdDplYZqtBwXDg30o5VExII82%2FyMMAmHPT400hbgTQD4aJXrijK8DR7ed4KAGr9pp9oaww7PsRtu2WHNByL3VSy2N%2FQrVfZbpqpjQqrwCSsxn6mTp6WKLy9jigv4xoXKH1gW5TuW4wQIkgxue0O56Ii2tNr7puvo7oXYPaZadqAVvGoQ2aO5xleUAUSjY19BY015f4uyw0PAhGUy8a0Uiok6YmoTQ%2FLG5WGpFPMetj53NS16MPfctcsGOqUBcXjSh8fX%2FKg%2BlDBOpVkoFseHS1A%2FJQGDFRX3%2B9BNyrSEx%2FiMc8lNRFvwOVWVn5ZLkAfW02hekrxFkhQehFmCHd%2BQhcBXEO%2F366%2F1DbzzgSALheGMDCABn%2BW3dqsPStaIefHEQis5inVDMYwoMty%2FXKlxTNMy27is5iFWmv98vr00RCQU3CxK5MxmqvocQ2M%2BEbn7Et%2BPpdpO%2B%2BUCggJ50uLk6Ihn&X-Amz-Signature=a3ea409ef2bc14500608e0dcf4e077cca7ebf137bf392ba5e0e7f226b063b2c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



