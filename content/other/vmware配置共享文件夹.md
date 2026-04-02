---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKWUBMHF%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEfFaj0rl0fKBzeVIEMXiyii0gtEsla1Pkm7i9ReNKA4AiEA5MgS14apeKC6vjE0FD95iywZVS%2FVRKe80crhisAO71Eq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDPlpZDgSYWS%2B%2BCLILSrcA%2BdsxWqmdrEj9dnFvzkgtGoFqlJJOxDyKgDAXkVaT8R4OLFgHovtDEdvhRYZ%2Bi9pRISbmc5fZRQygF5QdgyrEtYuBcddpGKrehULrwy4JC8TbDnPoH%2FSsqX7zQhykG2Y5Vvdkdk%2BcPBXdj7C%2FufzUv9fkBMJVm2K2sQA5DgJPVWr4myILHvlRotJJk7dupu5a0zZOFpP5pvnKOAI8BTXSs3sRVSHDkZzBuYKRdUDJ0w2x15k%2BgA46NojrDs6bIYb8RneLpBwk0szo6nw64T37iPq5tvRw%2FuFxjfJe4S2S%2BdyJksVup5irlr2WZi234fonD7965%2Bo%2Fl%2BNX4MPhkzWIE5nXwBLGzf%2Fvm01G58%2BwbDtvPuREkONgkz0wkjjyQV0wYHfHRkMItEh1a6%2Bi1CBcOJxM34Ym7YMmqv38sSrKunpqLcgKLNxl3seFQSomcRtZq69ROY8226o8a%2FFQnUdd1rTrqmNl%2FJleSz3wgx0OApcLwWrEsNpS0iL1kiSxY680fSXFEkgfIQM8tbgHJJnwXllWCvnmmia7CqXaUz4toEr%2F%2BS2PtqOjeZP6HlCyHWPsx84NZGJJovc9SrwCqf9Obtu8ASkWitP%2Fohh1c5L0tUClRD0tdUyeoSCVCPjMPutt84GOqUBGn1%2BfVhkDph7kDbYo1i1UXXV3tUyPUkCpbaefZ%2Bcsrgg56OSHis1J0me4p%2BUZCVN278Or50I3Delfswhxk05ooh%2BzRYbVpky5p8FioCW6u4JVpRmCabeoSW6AQsCTHZjCvgh67RSAUbCaNc1rRQ%2BM4B18MjFpzFQ2%2FOf%2FlfY6iGj4jluOH0Oia9lrcQnm5IdhhbtlqT1%2FWzXuARltiF4sJ3y9QCN&X-Amz-Signature=51de17ff19a0b9e634bfb1648f5defc1a09ecde80286ae424fa02afefd3e94f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



