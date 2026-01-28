---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4C326ZH%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLzHPXldb0mlKItNlfUjmRGYkoqCNpOJOHBQIidK%2F5SgIgLI6jDqhBGwLVOIYQbNDrdUoEcluMsHTyMVuqyXSPjjIq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDOLUvxVvfMG%2BYZLIjyrcA7Rqty4X9xMiENvz%2FI%2BU0gyLMoFN8LiW5lTH2DpyyOHsAYTVBWAjwAM4T4xnNpVU9hmWkrH60nX2qkvhqQof9XGDLZC8XfjCkUl1klyqV3X2ULj6%2FhCkNGu7XHxn80lxe82nVsrBV9hfX9pxd3xJD7a3c%2BjyrVWbEnlJSWBrNP0JCzmKs9OnUs0vH53H8cN1EqUQRkf12tiwiZLDvM35J0DLhbuNCXrF58eVEG2koOZo9qRaQjMntS4dANlA4Q0VOw0SCrv2uF%2BKpehwXvGyf7IEIyYq%2FD3fQlNQJOqgfo%2FI%2BKSrSJu6B2gvYEEPqw4zQWY8pnLAmzuq2XxM6V5RgJobyoOnPUW1mGRkmBDGdlSIhbNdcoMSYBpXF6jaCm3GsecQoEjJY%2FecG6K5y9NjG%2BLkpv1bKAmapyfZGu4VV3buULnvRNuDbwyNHqvQmk1z2o7lqod9KDZFZoB%2FKkaS2Y5W4KN1Wgm4BmYlSfpAOKUXQROJtxtUmZjLOvq9VgDap%2BLMFwREr3NQgsxj%2FIp2gnzMgR4K1hr98e6oXPo76d4jEgKfNEY7R6o39KVji%2F4dMCjS7rNMpepTQ0qacIPiElJE5PYNTFiOxrMb3WeyiORYEz%2FZerdSa5JMpgHzMOWW5csGOqUB724Xz8cwub4gJeMy3Y87b22OIDnIn2j7b32VRGNOoePdi3Bq09NePiQ7tjFIiiYDn0%2BgWHRHpeiptx8Hop%2BxIqfe2Ldhjq3sQZTQYFSGz6HySFinX422O%2B5p9ullRnN03fTC4iKFosyX2SseZYeezxhO9WL4mIAuGOuoubh2cdZudAe6ckcf6eQClI66xXVlNwFZhiL7Hwf4jkL%2BWQr1Xm6nJ0Fd&X-Amz-Signature=ed3b0ef63da3454588d71ef883a666191c1f465f5b9c766f190b835cf4f4903c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



