---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPTADCU4%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqZhs2lUefg138cXWp5UaqeCUSjJ%2FlexaxK6gOxCU%2FZAiByJlAo7uj2egK5pLe1TLFh%2BseIBqLfDi4GXJs3snNrHyqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdYMZQlOf1IoPBD9mKtwDJj75Jgd6ZlsnwtXHbpGUppKUSVZllqTRLHHL8SYgqcv1LWTT1Htn0sVOFBbXICznZ36HWP%2FXMuxgSChh0HA894SgY6ppXNX9dBEXl%2FT1S3SsXNIdKyvMDeaeHS2u3O9DTmLdn4OIQ5UnMmv3ZqkRvNFQjYYRB1hMKAIRNbT4EnYvx4vUxNxyh%2Fym9brj83I5hrBMW6fx9r0EJSf8woCn7avUzF6zkJnCMWPUC7Zjk%2Fev6LGKbn2aiPlm2DAcisdk%2F%2BbcwMTn3JdaakDyzYbxXrT28ZJS2ShsfXWkHTVlKNd1UFJiccProumIbby9hZXt3%2Fp4X8nBaxbpH8yFbWhZMSivtdBOY7j9z%2B3avvl5kpzM7Cl9muCnMTp2eJsdQShHKvzg1kwhWaqL9Aoc0hEimensOEXZq2h6ZlNq%2BdPZm745p6b4yAtLyTC%2F7ZyfGLIzXlDm8wN%2B7OrtOyv2Ea3VVTeSTfGaxHk6u%2FYn03TEkgqaaGgDeLvu5aFjdppDY%2FkzdgRZqbEjcb%2BOVsHePGFn8AUt9%2FxNFUSDhMJsEMV7NvIZQFXMrm1nEliU6PxfewCTwi1LNdZVAlZXm071qrdAV2LkKn2Lt%2FQpXVKEf0LaSgPAE90xLHQoa6GSF6cw65DfzAY6pgEBuRToZSZ1iYeE8pkINRnQsLX9Hnkl9Qn4wMI8JlVUli4j2Kw1FuW2u%2BJRO2dOkwGg22p65hSpHX0Aeg4dpi9PUWXBzyJtolm2m3JBj%2BvYKB8qfjFfhxdkjLVgZu6ijpQAekleFQC0g52zbUVp2Rp1wLvaGd3C9v1jOFzQYGiVi02XK%2BVYzp9c9lUIpQzoflWPZ14jZhdJgh5Q1iSqx7XtcA%2F8FvLV&X-Amz-Signature=fa8907403f30bb87c99d10ed2dc46fca1a4250f93223b3cde5aa7f22526233ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



