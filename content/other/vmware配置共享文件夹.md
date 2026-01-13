---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPREEHGT%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T030016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIHfjBDWLG36%2Fo%2FKu5UgPRw2dIT3013aMkY0hFH3gpVTzAiB0tewspupgg%2FqAKc6ClLOM8iCiz7m0Ih%2F3DVzRgh84GSqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1zxks%2Fj51hAFyPe4KtwDZ9jRZ8S5DcEGpWoqc%2BVSFCnOLfDCBSpOasG07xnksPgZ0bpCvufgYqObM3ie919yrdMogA4OYC57t9MhWdt%2FICCBMcT1WtHTcshJKC2rzDNrVHpNi9fc83CBBbpHTHMfMxuXt2DnMF26xsdSBveuoTVOAOyj4g5ZI3NWpWYv0o%2BUH9YidQOyIzKZtSn07UMh7GQyfyuKid7X6XS22l3DDv%2FTG%2BHs%2FZYoYk6U4I9RkyksOhYdU8%2BueAWXNio3UlgUyB1y9ojzzFsPxij8UEyw18B4k2AIVoBifH%2BufaSN4UW13Aocz%2BV5NC4clquSe837wkxT8cuiEg1ijPHK9fepcLBgwuNa7MEpxYRysGAnQQjVgcqvhQWcvHIDn5yvqAPn%2B0arAYpmegn7cFPwp7VuiQ0c8vYA%2FzV3HWgfuS7Uv%2Bm8pSM62C1fmg3kqAPN%2BhCi1hdQvJdp4w2VmoS4johH%2BuVd9iGriPMZeT%2BQrby4fTVax0khU4ZiuaaZQwaMYr9H9XH4BB1NNVaJafYkEs3tv%2BV41jVUAg6%2Fmq7Rwryt%2Fw9%2FihXVnM3zEWBaetrlT74FFj3COVvUJJKQsc3m5Um2XADrNxeu4hDNK3haCjIH%2BLZFOnVmtnuQLBH3ZNEw5OaWywY6pgHNg2xymVtJkWoX7NeLFiVBWcy7h5bXc%2B3BFeFApsMXjzGXKnMOSSn8tsGmUow8guUjeJFvHKoAXUc%2FP13%2FUWoIAUAEh7VlxYnsYC920rKG3mZ9pzeSCUc2Tf4VlSKVxcc4YpppRhEz1tnF5CkpgNS9P8bqDynj2HoIi0zXjElckN6DnxxP9gK357s5HSP%2FSWm9c8ukFmUBVYNLDWyraXFRfvM1Ey8I&X-Amz-Signature=114e2078b768572a2e8b849c748f98be292b605f31eed83604801a341d546ec4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



