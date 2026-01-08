---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QDDPS2W%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBN4EdH05Ba5m7fgcxdEJXcKKTKVUiRuwGcvrzIATNwbAiEAuvurfu6cyZdi9mQ098l0zrGCaXXOYV1q5SBclMTnjNIqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHb%2BM4G60HRKpciiPSrcA9TSJkcvZ%2F084Su%2FhxTuCy1Q4s6LIRF419q3vkudH1KsqL%2BUBJ7%2B3tpy6h5GQzKo6fqqd5zC3Bwc6k6%2BaIsCen6%2Be%2BQ0IT7dyYnkpTbmrw8tzKHH9wN3YyzxeuaO19J7UgE3ddTZxprmE0Zehwdk4Ak64vlrQ0Qe4iZje5aXLvL8wUq42In3ItXXfPLGeEplgG2StEtNd0lPUuc2uRnw84zVD2JbvLpaXPYRHvIIMGUiWyYNpmY32HAQoPEl5L81heiHtHqnP%2Bt5l3ayHXiWMw8FqIXapDS6awbD0Kt0QkDmbxSykPjTIMubhIj09Lz9fVc6%2FNreGePpxqzCeox7W7LxRNpSJBay6fYVdXZBg%2BKFO6na3MLdCXWTMggDpK5NCmcCAUmvw8Iv%2BycyR67hICFoBGQ782%2FSBeO8zmoKzul3ldoOhFhaKPzT3EAU1s1oDngCGyxobRkE5Fa%2FFSZXMDr7eL%2Bu1mHIUgrCzKnxvjb%2BLnNfeepygoM9j2xLf7mM%2BHKQ3iyrKua6SzcluF%2B6a4jqVsR3M0LH32Z8tqEW5Wao69RdthcZThOBsin8HlOl819An0yW8mRPbc5mmW46Btep0xDO6TzGilPtuRRRxNfI23jmxenupt5KjWAPMOio%2FMoGOqUBLKVdqWyZ1DAxFGAiBTFB6qgpQ2KEj%2F2DQLy4FD6Pf0B4Urd8QVyYh8dpWkxQPdXjcdgjf4SxFWaBhHHi3G9lv4ES5pZW2sBAV4kVWC9v8Gu0Jk8WuNrbmnnZBOooQ2lu79tcLWEyT1jdXmlkmAj43UBYTSL58l6XW%2F5xlPifrclMKT4la2XsfmV%2BMNMdWx4lMLS98srdUDIYfHs5BoJ7O%2Fusit3R&X-Amz-Signature=a3dce6d2e51dbe5f9da27bb58536037421b88b565a3adc3b171dabe0700fb582&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



