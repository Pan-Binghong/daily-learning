---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOTOQWPN%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCICozEMmRTI6g0ciaIBcjpRJxI5M0f8SgMn9DjCxLfesoAiEA0Duuxxdb9MlGvmiYusN22472IiE1CBslqPzjIujWU7EqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJJzaK446XjoqlvRyrcAwUFDpGkG25IagmyTdyDSGhDTNmEmZpj75bKDSEZo2awLLgpbZlcNZGGs5Zkfqm7h1uKEV0ArzaKC9FYSf3a%2Bn9vnu%2FdTIkyD1un7BCoiw8Rjd3K9asdvFNnb0xONBk%2FnkEbQbo27KpafQsWNqu7oXGU4Obq60gZgt%2Fc5ojzJhDyrLwG1AdJS97Mpz2kEjkd9YAssam4Lks3PG1zVAv4xhknx9PPhVNJoMAWoJWEFBZVrzWRMHEMg8sg925j1jelk9W58oWdsX11XSTjsjinkt7CRj%2FuPHeIj9YYWXFj4gs1zKW5Fa9nKROwmDLia7I0Sqrg8gFGGsEvKS%2B1JJIE89BcbcrO9AhjeczUuiNayGR93wSHxTsGO%2B4BE0AiIY8HfI5DgTxEBb6p2dmYTwg22pwNniIQTjbCovuc58HMi6DC8QtUOAtShL25kTHUBeci4lKGsdBUJiVa9mepd8ZW%2BtYCR4Ndx%2FMlH24U7FD5Xr4MxRzwy9a700zQFBCcn2tXRxM6%2BRBsNYY8X2XaGE9kxD%2FCC%2Fr4vpfW8vwb%2BmVaOZ4KuDz2XdPBTSf71SGelWUlDIkB2aK5zSIXJmEF2y8mQQaum9n5YDqvn6R8edBsafP7zym6GKmF2jKpzdC%2BMO%2Bi18oGOqUB37Kyd%2BK6AVVImvYaIbczc4g822tGU90Ttn2sUuY1a%2B1XOpTEPwLquX3fO4INPl417XJoIonVn4e6DXcgrOEuyiMEMQBAfmh61y35AXaAJ1xBW85jAuhKC19QknEsgrRRi161%2FgDPB8%2FYE9HBToCvUVotsDQ5vKt%2BmbwxokxhLJTZGLUcYYjripOU9zt%2BaLKnHcb8mmDSsDUfvTyrT%2BKMgdJ9j0wo&X-Amz-Signature=c2f41f5f3f6b4f032c1c409c43994d02daeecb9bbf18643ec1fd68b867e35911&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



