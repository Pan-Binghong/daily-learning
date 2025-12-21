---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC5C4CQM%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCi%2BLwV8P1PQr0twNDENLM86D3OLFIyGPzsqAxf4L9zMQIgfi5xpaHILfFo1M%2BChFTfW3V%2BzQfvkkBLGz%2BTqpF3eToqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPTRkCL33EMtQcifXCrcAw6pAGz1Yeu42GK1tnTFWXyYC5MN7z0OWK7ghpNWR4%2BN1KBNFYwz2gibJ1JC8rdHVXf%2B7sp9eDQ%2B1h40%2Bp6A39eBaYoNUaLeYhFMl2bUYD3Z0Spp4SUfFmf4H2%2FN83xPFd8gLRP0lGePPcF2mwXft2%2BHLQVD847K7OLPZJWuQ%2B8A7LnBWYVu3WapOgeEZRR3rZuR6lCO45zz7GVjIQafg6K6yn81uGGTpMYjgTqNLQwbBP9QLvrhsKsQKnay%2B5ChA3Y3xFY8orGvbAklexdM0MeNB0ASElZnMXErXNngo2zfhAtyKrh5vNuod7JCQ9gpw%2BBFPRPXa2K9h8umJe0qFaVgztNd2KlpvjD3Vr%2BDJkb3wYAY8TdianSYBqOKQlgnORy%2FSqR%2BS4OonQkIHYTc5YQVBCQuhPRx3WUnqEzOevA1j5ewoUKL72cPpysJzc61UMcloCoUyoLLZ6Q9VdXNuwETL8rEA3qQSgdkijlctS2u8cvgYDVDGlzVcGvv%2FGcpABk1DhrSe93q7RIJ0ThsjlXisKmrVdndHpImPBNVf%2BxggpltMZD%2BGR2hYV0yHYW%2FinMAGtf5QzY9dV2scuAVNvMduli7KOHtcy7Zab38T%2BVwUPI11NUMDvIUFiLyMKH4nMoGOqUB8o6bupbT9ZYeZ3OpqbFuGpoQ0wXqrSA1C3PkMh%2BJXVgSs%2FsaPlXkbtPun83nV0chnWUszvcyRx67DjzyaIGfAx7hCvYsR4DfSLKaGUzaagjtuoCwpTonk7%2FRRHAr7syQeB%2BU1S1aqeqo5QwmPea8iMx9KmxqdDjQO3GHO7J3OeLiOk4vBBWlzIR9zI28Yhdbn7uTwLU1p%2BJ4SonHtz7imQ9weZAW&X-Amz-Signature=1053dcdcab64c479de5e3cccb3940ab9edbb4a7c1269093c0712c506eaa4dbe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



