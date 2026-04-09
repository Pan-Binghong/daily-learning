---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4MQPAZT%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIClScHOQGTo95TEmKcrQPjWEy8pbY5cgDBY7aMXqhQSqAiAui%2BCdEyiAl1QEyVgq9d5hYfQtk9yaoa1BWNjn9MtBnir%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMbnce9zvQ8xgZAh%2BPKtwDv3YdMYs9dviKMKjsHTXJhVghFi9s%2BBwIC3i%2FUzVWr8Fe9qZKT92Xt66n%2B4Mt3pvD30BgleC6AQnmrj4y1hcqBjz76qXDUbKHvBcoYblYDyxGIXi1VBuBuxvtm9P6sLnGS4tWYoJscluTAl%2B0H06UFnjY03FTcvj%2FtFeHzGm1dzMEd1Z0kXbEvZLCRtcpeLMJnaDsUknth38dmT8Ta%2Ftgv3c5ZpPV9Njz4IFqFEJRH7jd3aM3GOnxccC3Rtj7duMueAGI9mP%2BNUoweJJfbKte9Gz0Ao1oOhWQdP5aW%2Bt9ITkeRSrKGBClVn%2BLmsPbLhXKJtGRUIKKgSB3kDoht%2B%2BA9gZt9BuIYKFJFHpIITL2dFih%2BtUuSjuG%2BQN3BKGG8i3ttlFz1YtSQJ4Euuvmv7Vs6CCMXOtJG125aCqDK4X7JsucGqXwMf3XMxFNY9IGIJibviI3bSvpz2f9AYnyYuFX%2Fpz1JHLqG00aKyoqIkCjphZW6khnvpQJLDEwXMdX5pa%2BM%2B8LM%2BWGH6rLH46ij29NRh378BTcY6K1hZWaN3Qvx%2F%2Bm6rzOJWqotmsbrjnYW%2Fi3Mndis2f6yvTWWBs8UjO6%2BnQk7FIpZrlg3SQGNY5a3zfKe6sczKYDvaknMUows7LczgY6pgG3zSlO%2FLnjvh8sz1Bbpp0cqqNPD%2B5uhWh8uF5CBmd8OhktKxoUlQ496mXBS2On6P3NoQ5EbpyYaj5eHIGQmUCHQQz2FHw5gamvXYZOlOfi9DCl30Y5tza9T85JGJfkEyNZ%2B4Saa08PswABprWFzd2k0dLg69whPo57E%2BgOEV79JFce2KIeAsBdElRtRQxcNEOxSNlYfnvAONj8dkKOtJVLGBwxHeTt&X-Amz-Signature=ca4b85086f6a73d168af4185f53bdc1d994c2e576dfceec57b7bbbbcf3761f84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



