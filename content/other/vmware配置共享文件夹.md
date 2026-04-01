---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GTEBWBW%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBFoVdzDZXX3GB3NWQkTrr47xVqrPUzBNonfkWzz4M8VAiEAnjJ57hJJws%2FgiBvqFwp45B24omLuTNxaivjks6ugrRIq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDPsJAP2qun9WC30eVCrcA%2BxqrZboSHAUVsbWJJUr1jh8giIsug0zy%2BAsVVTCci2Z6s19Q8ihaED%2FuMyf7RN72lfM0hZHdGPIFM1sTzsl2u5B7oN5zpKVNdSTldvWDLJ5fucfiL64ZvR2mIOPXGlkHtRp0jEQkDoSYYxXjOtii6G68hek%2BSHpIGhYGUY5dEN6Xh0uqs39%2FLna5doWPviPHalRWKYX8V3mq6gFvLfS6D41dMCwfmJS9u0yjdunuq9g3n13hbaEitQVjAC3GBl%2FC117pgFP6GZw3lfwnjvc0n9lo6n472GDygVI7B0PL0hr5lY2VXcvb%2B%2Bdy%2BeAzH8cEMNmeRPzt52CHyPXxu5svWBgFyGuEtRAkmB1aWHp5EWiC7h1ArFzH5YPsab6k9XdAeWjLmwMUt8lgE2gCXBWU5mQ4ORVXnp8atl%2BltrSRulXu04vyDV7hx6Dr28fa2FvBkdsnPJUOdx1olZP%2BAQG9kGz6Jk6h0sJaPd4cgOkR54dKjggJGvE%2FQwAYx3wroUQMTpvXA7L5CWTAnhjj2VKQSwIVcR9%2BsZTFHYrpc6h3469VHl7lKiZw%2F1Oea%2Bp4RNnM1SA9fbqN2tF7CDR7nJqk055ZRmzI5QcrpnJTHezUHCeQRhO0y%2FXskwVUZp4MLmgss4GOqUBRlnVzlPW5Su2nXtdotCblyxAO5OUwiSwCeCGil6Pijzz4ZghKEgjMhEJ%2FVCfXlKnUZGz1KJWg1%2FI%2BWarxTw7lugMBMptLVlAR3HXecncWXLSHA5gsB8UCKMvmNIRj8t%2BZJszLdWBi42tUyfGnkIPHdHtFi3uXsOWvLl0MY2k%2F%2FAl3olKoMDM%2Foy3yiS2JDUsOc%2F6L5Pzmy9K%2FW4nGRatsvKAPftX&X-Amz-Signature=4bd6262d46642ed1e8b1917699bd7d4be8cd1c3b8e28e646c4998ad4f6be5779&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



