---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665X43ECM%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIEOyBw0zeUdNNf9brm3gpccxMe9TUWf2Qe3ZgEHpE6%2F7AiAWoSyK7ywEqfCGBMYohFTQInDjl7xs2kXibGoDezo%2BLyr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMA2g0wIdk%2B50N3KeQKtwDicMuP2sEB0NMjcFKwG%2BPBOP53bzaFB35Mh35fZBkiNIhgF6TtRRVYQtmHlW8kthwz9Jc2tc4irII3P2%2Bd5Qcn85s%2BSq7dO6SrWw1yBVdkIlOR8X7eQAERpoB9fXeXMLddAoAulteU7cRXo8MinV0xzffm%2FXrZMoJzO1iZXimJYHaKuNLObedj7EUKbjqeUOD9lXC9BTKKjGM5b1R9YNlvb39Hd1FtOHQ1ftHoEaSuHcMhF9PYSkTwgZwuElR0HtrxWCJjKkGhjFZ98QKptFDCULUGkoNc%2BgogHGdS1ey9kwTQ8PDnrwKMJEpIQtwsIB%2BxMahPELrMCohsfXfiPvCD5WvS1vsdSaoSjXwcVFcVWFGJHVeKO5wNE84Np8W6gYZ3fMdsEW4drNCw2Sqtx%2B5l6lvmdQctbyr7G7ihCWECZFGeXMvsyFKMyqdj1r34ND%2BfYJqR4w6TltjX1uXiUuGNaHlU2hb%2FQZaweF1Wq1x2V8D9asWAy2IzuKWxSVKTT9Bq55cSnCsil5Q8wjOB4JNbLjHjMMBL1PyKDI%2BQxP%2BlseMKAVlB0PnLZc8Uc3uVz34v9qOjXO1z5Rr15VRfvAEUtBSxhNInBl64LYw4cdUdi5KYzyPD4iWLnkXCBcwzcKzzQY6pgFJSmGTTz1u927t0g1OmfdemOdXHDjuH07MTQRAM9on7p0DZ2QZE4KML33%2BmSgoCmmpYkz8XXOlLaBSnrwSQULNvLEBIs%2F7lXgqioKQxvt5EuN%2FchUQnm2vi02sSZ7pEF4qK6Ilt6SMKDj9Bo62A3fY5B8M3QpghYsBLeQLsYqXUtiIAPA3BAsk5ubxlk5ABd%2B2Bda1jqPksLs3LB%2FifqjsXme8h2fD&X-Amz-Signature=1547f28721a0f13d5d5009159b8b39afaa55d4504cc4f5b0c82fbd02e95a7e87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



