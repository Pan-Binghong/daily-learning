---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFME7TZ4%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIBQSkWJp9g9n86RzgJendi9HIQFlnbKgRfDM9BjiRbLyAiB0My%2FSFuW2pJFiWATyDat9v%2FKc8xDuCisqXRWu%2FvyucSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMj49Ims6lhd9JochuKtwDJ34FqCYf7WsOMIbk61UnecfYuzizAhIs7d00g9C%2BwcV%2Bp4vROZuzMBDXF%2Bsoxyzcq%2FR6y8g04tQShosmuOKRvO0m9xdLHk1j7pOxH2FI4pqb2v9T8ayBFRyLCybb%2FNgcQE%2BiF7PcoXkgqOyRgVM%2B8b%2FbT23H6Sqtr8Be%2FVUrj%2FTEHbLTlRajDHL9qAjYR8wrujX9QTDcdewW1ZvXV5RnPzeJTwIAAtCjJhr2RLIG8VVy%2FIw2O%2FKgoTuAN1I3x0oVH4lihACehm0ZIPEUzCy%2F8tygCLiRq9bXuj4g6RAyc0LqO5TrKToc7fXprwxmifgPC3gUy9LWMEafpghFcS9wpryppwrWG9aR40QzCbmW2uW3hG8PRHwoY%2BXGVFrXRsGlvi%2Fwxuuqzo7bKK8dJBTZJDTEt7MI2o22mWLZ0jDLBX1coPwxMcnlcTlCGcXHVhuWySvO5QiyjFIp23IpHoQZTNuXaXtITccxmXM%2F4nlFZErgPlvVOrBHa4%2Ba5CtA0ecqgbwyWDOMaPVWWJTjXbHDUJbYKSYhWkCJEQgxi%2BfLJa5qm2digdC2XtHxcprAE6lZljwVa4uZrVeYugV748t4OmOF79iVxvpA%2BDv74ZlGXkaXbn%2Fii%2FMcXI6JtBYw3YXsygY6pgHOW323zVuBOOHwHJhwFWhQlKFbV7cvUhDtkvqSZMvFz%2FGCqo1pKQjbZxwtm2Amj74aof84rp6FNwm2mZ%2BXsRgbXz4A8OcsBpGgaAm9TMIcUYCQxwBUEMX%2FmynLnsb4XYc%2B74g%2FmfPd3dwNZ46PMgegZ1alsTYdzHXH3w%2F%2B4qJtvY0f08R983LyGIkzhsoX%2FzfqPKUObah4N%2F%2FPiiV0JYog4El%2BCAny&X-Amz-Signature=7fe49b56e86f72d59f757f4643333b0b03ef620fc5cc43b0136cbd4ba8018fd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



