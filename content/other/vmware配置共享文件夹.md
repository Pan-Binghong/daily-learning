---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZCYKZVI%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIBV0%2BEn5SuAVPTzUpmALcTarHbs83bVdGFKXQlJFCnp%2BAiAFYgR%2BQ2Yb9KD7lr4YKCO470KAY7%2BQo3BZvJKWyegMjyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2swA9tmfRlNRn7PJKtwDSW6PuP%2FKNm5u%2B%2Bwbm82zwUbYyuAD%2B3JbwglDXtVmTKilgNcjQAcNb1MK7ozyE8LI53Fo2SfmEiYZAV6jMfmNrkmTSSS18CUFIEh2uLNcuLtiJ%2FIPHcgiTSzZVVR40SK6oL76ZLyUMphpqy6vXLhs%2Br7Yx9Exd1ZZzxUdy8cqOAAEH%2Fpqvk9oOcCV6yfLjGwH4JF%2Bfda0v55egLg1ATxwD4GlsIt1ph2zRLc8eYW1bJZWKf0u7WDV9ucxPnYdLTXYE52J%2FQTbsjjgPQgG9oKeGWf4eOyBlz0iR3f3XkXvUym6I%2F5vTc%2FyzHMZJqlBvuLX%2BYspA2OVlDexMPu0XIMW%2B5teNy8SoIfPPxIDQnp%2F0hsJOYMUG4o1QR1aWZcUUaejzxJaOQdmLl48aR0zgMdFaLIvGtslyEqqQrttdTtlfOJHJmTeGcChh8c4TmuuqBVxU%2FUYp98v1319zBpGPUt044HP%2BeUM8Uu1bHKIqb%2FmwQP4w8V5mRb6O9PELu6y7kVRqrv1NxWs%2FGbWvDmlLfvg4hpEIMpv%2B8g3CVjGau3X4ZgkbSZGhyy22auE1JyaL%2FhRmoXGzy%2BodijIxrTECbXfRx0%2BfNcYoDJbwTneHt72XPU6kajEKFhby4VuOvMw%2Fbe%2FyAY6pgHU3wTOLXW8fzCv8ad%2FCcPapAYSANDqVWBkWYKgHKvcHyQvJfOZhiO4CJFcmATX8uymwvavNTX57%2FEWFDBDkLT%2Bz71Z9NeWnJm6Ss6IFDy9xsw%2BvsmDDdq1x%2FhYEpkdP7v1JZjA%2BsKIAtB5zqBL%2ByDUjF6%2Bvy8l1m85bdkGSK5RbXxfTfOVxceV%2F7HLk76R1iewbe1rrlNqyjf3uFGaUYSF624kPfLE&X-Amz-Signature=bcd0e565f00b80685ddf00749d4448e24924f8a9f7294168ce04a02826482b5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



