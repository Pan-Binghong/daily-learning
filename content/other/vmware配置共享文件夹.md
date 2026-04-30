---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QXNTGNX%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIC1lFRlri7Cjx17ezjvqwyJ9HMo4DUQkY8dbyCSoxqPyAiBmvTQidSKc2XKNA2xF4liIaAZC70w%2Bx2VLVdb0cc0XdSr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMS0GIQ8F2wUTg2%2FSSKtwDw7Ra9DorW2j%2FffOJbTfg2%2BdLdt%2FGtFYkGnKlXMXiGzoDDa8hwoHBcnHcgJWpfWdUaWYUkS3%2BzMhJP%2FuRToEgJUgCdWy82xW11dWNGb2vuxCRMo8WdIrWYq8zNn%2F5SE63%2F8DPOzxC1GSbj6Jk2JYs8qzKOXSSE10nH036lFHaZEC5991tg1f8EgPNBv4jPrQGGe7KrPuzmm%2Fhda7VZc7oWGSW1jPUT3hih%2FYjjQ%2BpDdpwiA8iCz3qRI72%2Ff7Y1tBnrUQXsMSXCKaWLRo45a6SybJjSjaxDkT6AGUPnVfuG4zynfgSJ7cBgcV8HX6AfwRUJ7GraoItVcwlW5pRAhcjQvuVvlU%2FcruSmrbrm5iqa1ILKYvcii7wQvNMURyOV%2BRO280cWWPGG2MCCH%2FrmwHHgS9RFNtkPHhGJizeQB4Ne%2F8PRpx9w%2B1Cp%2Bc0nGWDt6hYQg%2BsptlHGvjb6ZOI3TFJJqLOsv7SUClfAvN1Ehuud3NHQzb9DudaH9qx32Mq4p9bTL%2Bt1vsWE53Vjm5i%2BWom6OLS%2B%2BMykBehuTE1%2FetlXFKqR1rHJBVImOYy5%2BkhNkd3IV%2BzyICHqyN3GUp2nnrKL0rX86kwQOKj945iqJwQ0N%2B%2BwfD9orcBHh2w1AIwu5zMzwY6pgGkiVwrI5jO5E5HpGVgoUIlaz0HX5B6V1JF%2FqnrNaYLhcMHxdRbfj7EhB80ZKvOXp8sYTTtQo0GKlVs5k75PJwBRb8MPHCVLv3qvniavW8BvQH4clT5jRRFIyhoUblUZW8Ci6fAPIjDE8%2FvdxwZdsBFClrkKDHmIZRu6pFu87gktUz6wpiDNL0YUf5Ly7E0LwNcll%2Fh3FLMDZ8fsV0niyjFbuRq9bQx&X-Amz-Signature=f6dbf06cfc70dfb5477f8a24d35fabb1333b7b3c01a16d96cecf2b89c532ddc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



