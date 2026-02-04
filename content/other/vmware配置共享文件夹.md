---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FDA4TMD%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDFbWYQNUkr0ndIMxBtWuPk0hrH0LPubKnA6U6v8pihigIgEjxSSRYdj%2Fy3kXsUeCyu%2Bx1fUpnZEZ%2B1vx6AtFJOfBkq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDA6Z1scR90zJUbn%2BtCrcA9ybXOXmoCjBSscvwgR1ULXup84PYbzdj75Ldqlozxti0j0%2B6kwp9jZkl2hdPfEt6KCbo5HmxcNLf%2FwG3XV1DDs9U7saDmcsuLAm%2FUe%2FVKwGLKeAvW3z2xFpSC0hyhWP%2BVEe25bYCO5K%2BSJJpCvfmZuUW9IqF77GSIGANv16AtZQpxZizVLnPPNEIfG5ye3Gi7pMfYtz%2F3QGs%2FP%2BWsDXaRDSCyJp%2BrEJf0TN9P8u3h5n9WiT73hGWQw5sDdUyrtjWA8Fd7XPFz8j6FGZ6qAzohM4fX3NF7QWUijHlnNkPsd1snHMQJVazUoGIv8eYwVv8IfFNto6Dl7Rss67Tjy3Vkd3QKgFK1mK2SYmHoW28GX05zLOkqvnS9Pf2A6ton4Wb1wqo%2BHtFSR2KSc55x09iK88KgFV%2FI3wCW8oEQ1l2y2qk2T2DpjTk5S%2FRySNITC1rep02T7AQ3dapglPAmBKq%2BbpAHxvL0jKEVT%2FtSTnw3oYoCT%2FsJohhID%2B8nsXgyVqXSYM7%2Bq52kMGFTs5tUadF%2FRtKhnl6ZaV1e9P8HKyXoA%2FbSzfOJHrrU3BF6BUadPd5kLXv3monA62ygJF%2BCnrdVZNo80JadBo4vbQRe9hdVfIoZZ7Xzo1YNfTmT4eMJbpiswGOqUB2yckjIHcckpWRrjhLa1smkJlXU1KX6ejJwC47WPosGAMovqllhfBm6SrDdhWIFg5hvgbxvvaBqyMy9xbPkHQL0FeUJlrJfB%2BFTEtNTwg%2BD7OaNqb%2FcYDOCeqWNFgSsBy4PCL4rOGdF%2Bk9INMhKqmWSp6PT8Ub9H80s0AOsy9Yg%2Fwo79hSHabydh%2FFp0CnwmKda5mNFtspDTF0pMBkNUer15nHWTQ&X-Amz-Signature=faf935f6807f274a2f8bdae7a9a5ffbee5517d498ae8b5ce7b8490ff76ceb7fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



