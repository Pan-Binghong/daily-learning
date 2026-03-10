---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6Z6CTWK%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCICnWqufPqcJTH5IdKmtRHlLu9vy5%2Bgh68m0B0%2BpiZpelAiAcg7NWcv0JjXh71g7YCJ2VRQuyhiyWqAmw%2FUpjD9pV%2Fyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMQaoyd5ILHi6Y8Ns6KtwDII2v2tVrkW7zkBwOOb%2F4VY%2BzEfPjnbSWYL6AqsDakYYHOPxSSufPOHaLmdNLd%2BeIJA6Va9lY9DDeWdtLzPKIJTTUvPWUKX5Zpmfvrsu9GsKrzOISxgOnhegZft1ECwf0eURe%2F%2F0Tl6blrHA29LYwdZPpiMhZ2tEnHBb32PkwHQZleD80z4ReaceKDoc%2FfL%2BVeA%2BM5YfwsA3fX8EGM2CZJw5v704Mv%2FRwzMMdt9BGTtlWi9cJewr99MS5EKe%2BSjAD6PxhBawtufXFB5JjJGxkdjEGRUoCbzTMFR9c%2B6YqaNnZELfpKcPmopYmF8tvj8XloGW7ZuF5d6wRiTrXKWkknJesC6JOqiWUjIzJ3vmQR14ND7bzwaEOgnSBaFfjxcSf6i3mGYA8ybblAcZuBNh35yHETL9KBsf5mwaQC5E7jwRk9bo0RmrC%2Fy5mH%2BLyMZ1TlrxbXuvpT3mzNHkFWOuTsk%2FdouDkfyzuvs1qVx36oTxx%2FtecUUmcdfrIEQufA2HUOMtm0RZv%2F79PvzpMwlLDNqAqdtC2OJyhwIj%2F7kWvy2uuGTUhVqmhv8phA%2BE6quTmslD3Q84QiuEPl9Pku708dvWBOYSbqRRdL9vIzDoDjQIwcTcnWOJiq%2B2MKncwg5C%2BzQY6pgElStP9v1gfMUKRSBWFsUP2DOFjmYwhDSM9iKQ3cpXV0X15F7aKoJu%2FQLDresVPMjHOELFR7las3ElV8k19R6JOihn1FcRpWmtCriLdM1rqawzF86Z%2FDW9dW67msXNYYR8EZpbhOM4UlTbyr8rwMQey9gEAjZZYx0I6Yu8VQr2Fu6Gx1jrH9vyI2WTHr11eL3rOOHihM4QPF0bj6A0PuHOtWFTZjNjA&X-Amz-Signature=bd08975785bf5a9b4ed4d33b035b8555bfe73120972022c18457fc61466eac68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



