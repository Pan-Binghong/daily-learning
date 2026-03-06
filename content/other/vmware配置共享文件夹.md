---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WH24IUWB%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T033030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCrX855modJqWiHAdAh42Xucq0%2BzBpPxDPGSB0dR3e78AIgXr8MwU8UkaFzd8rILlq3pd6mpXtdJeoQi2Nxj4%2BhiRAqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2FvaHSggmCnUdktSyrcA9FAsMt%2F9746F39yAL6FGKEh7TxqB%2FWYWvCuQRXzBYo0nQIk2FFqO15Y8dzR%2BiqEslhICUdLpBuSYrXYLIZzYudVJGUNoZDR8PhPnWOCn1nTnuHoNxCDohBqy2PfA8IEiiyLtXB3AJqHKAumjgHOpoIWcVvbCHhDGChFUhTfY2uqBsgQ9whBfsR61oeoFbocVcapQVsCdioSaDidTntHiXG8bCyTneEKg6Ez9nKpyTgSskapdMYM0LC2KLbAR46ZLA4iXh0lqRMmCIvK21bSNsyCAcqnJ9lTUp3wP%2FS98xovM%2B1Tx3SDxOwgoJjaRJsqJs26s%2B33g3crbi7B0F4o1poSp467bG2dEHvc0doDF59PcrzS5GcWzTCO7yJAqizvQD5Bkd%2BxQyLQyPP2wxFpIDmbW6vnDVLGeDKejlfT2yS0tVvi9VtyEizyX0bJRywNiQnE8EHNR9LtXKYHgqETiNX7zQ%2F1gArV%2BBcGlXPPEM6tQEUXu%2FTOvfaOlxF2w5knTfiZoY72COSTW%2Bz11ocNnx3yNLtTTdoRoU%2B5FGPtKDHXN4JJU3Q10I6JHcaM%2BBL92enKixTtK%2Bye%2F0F8GVDabd6F0TTg7cN2%2FNjs43gWQj%2BOoNx6Dp9acoBPaYBAMOfOqM0GOqUB%2FdoMoGYOuvA1%2FP7Q6SjFV13sBXF5NHGHK1jQfYiQmrmNpzuxHGLTnfLABb%2BrsckIiOeXBFHHGovCGvRUFmIAua%2FHfjj7eT0nOet56J37hobqVaSNiqDpSH%2B3k8kOBOoQXGALxsqgBU897M3D24X7nQgC5%2FxzANAp1ClWmuLam33FEBvtr%2Fsu%2BFhRSAb%2Fez2N2h7zisSvUz9R5oiNFKcJ7YYAwgR5&X-Amz-Signature=691571aff0dc344a3c06cb4a064f801e8cfa0ad6b235b61a38fda33fa713bfff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



