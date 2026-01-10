---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632UNCZBF%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYNuSKTbsoeyHIPW5AdRa5MOz%2Fx6xoWC7s10MTMyzyzQIgCSFbhlDHeZ8tBhjEyh%2BqFgm6rcpejQRMfuBGJE5vnDcqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNWjCJ2wX1meSNPFlSrcA1zLLKZRJoxIclwyzAVXUqSBxOTh4%2FSVAaVRqIB%2FtsWHWRiiWUnimMI8ISKhXORpJoYIWwlNVfGba%2FrLWgmYVf9KbEKk0WdIo4J5%2FUBNOpsoHf3LmIAHYL4lUsxjN6HcuyFsMATYlOvinsEvyP1WfK6uMypzW7TjZMD06mLuBqpsObbRLYG0AfV73j%2FF2p0lu2BQUVgnF6tQjTuOUW9c3lBvGl40FVHTs229YMii2x2cDAXqiPp468gSLAljoc7UBq%2FmqVzGDgEzDYw8ljflpe6DIgIyCe%2FlbdAxl4X3uXN3%2BseYnzCgHsfA4WZgrlDhzO27lhkYMJhazHkSPVMkZckCKtXM9DnqUcc4X3aQgPFeBpDNtTGWvf1Jr50xJWa5ewKe2norNWOu%2BenYigBxrGdnyvrYGPpGsbxJfP%2Bw8TLDRrKJdf3dZID%2FbthYf1W7fCOjGvpIWnQGtPh2fDhHatJDXPXO0JMjxsfuDGRwJVpQjndO%2B%2BM%2F1YpLhWHEETD7FT%2BXKrGzmJkckv9Ecl1j%2Fr8MpuTm9vMCkFWtUGXT9VZiHXFit5UQIv%2F%2B87w88w9eNKutOT29igthyTuUsurhZTGDBGZwx4n5LOJe701X6B%2BynmXMNqy9EE5mTTTOMJj5hssGOqUByMDSdpsjwPGNgkWg4HX2cVt2jCqLC4Y8%2BckVq7ZE2KRry%2BxWIXN0fvZaeVh6GtXcr2mIRcrmNwAUlzDIW2eXT0l9jUqe%2FxKOepOjHVw9i%2FQJorIxoicnZ8JcWhTu2klVqmqnpLaIs3ZVxbphK8dbJxEN1IiDgtY%2FAxp%2F20PC2P6rz0x%2B5L9wi4wyGQ6O%2BT%2BbjwL7uv7k8lMGwOqZmxquK6jx1KLw&X-Amz-Signature=166922412727999bffaff91aeedfe223ab3eabd76a395b47b60cb99606630476&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



