---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MPNAMAP%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIElfuFgF6sS5jy1fnW%2Bzhp5nVdeC7NTt9qw8dSorQ3j3AiA4fHmzntl3P32fBIpLOoy9dDKJGUIriMmUvZul4YQ4yyr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMr0WN6MmccnckB7GcKtwDRnElS1kb1i8lRubyFhNtcFaelFNXt5QLaliuN5ahh07QGOVzyMrezf16Y5fCsHyU0grPucmbzFZ1utFNU7hgP2VwAFNUpe9wrFJkcKwdvzLSbpSQhPOj3TAo4OPI8BCzcrvDwwgt8hVQl%2FdP%2BGzWykdpk28V95z5uIfZ2EczhA3AupBLG9vaB%2Boc273CJPaeO%2B4AV9%2FhGHE7yvuEhASAV87na2onfzy5MsB%2BxmbfmeY1NICP%2BdoXKLSeU7AnEwR1AEOT%2BPMFlox0llOpprUNO7qpqKSVjYDa2tyPDVvqSIIj1BkknnxTsgDZ1oyzGDk57Gkm%2F488fuVw%2B2Uc4nwQRmKQTfJX7OzCzqBxnnSCrcPqIcRbpA0G9nAmLm2DwoEcZ3LJIBxU6WfV7Lg12cTkza8%2FQ2LMU89EzPpixDZ4uy9148ieo%2FDoCddiHRLhwYiPR9Uyem0hCJRN1UFlN6wgYYLFRm0yPjjAQpBDBkljLyOM7n1w%2FVjHOXONGXo90s%2FE7GYx5Xztp2zN81qwD4acjsYL5Qi0ck%2BOQBNO8z4IkywinXhd0BcKt%2Fa48ttPBZLpJ2%2F0S1FpGFxIjJA%2BYnvZVxo0lhr1vOulrlk7D65MXfvFIcc5Xh5GhmxbWHswnvX%2BzAY6pgFDMUjL1%2FuNAJGd7F7wABcP7DiP3l%2BZcDpHv4HemhC430LYMMQH2E8TGOyDgtwc2tXwCtsp8oXORUYdphUtL7b6pCauzyCI%2BkwvHZ%2FWsApcJndYr6t4u5uQ4pOvSYHOVFvEcvNUuMoW26fAAEZjtCiCs6YoFmAQad8lrPI91ZzZlyRE8lAZGOYU4jiHgHVZhvONnGxFCLgwZz3RAnzl3dT1g%2BxHiTAx&X-Amz-Signature=3bfc40692a6b0852462ac84eb6e2ba484da44a79566f0fc9bad8e8eb691e36dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



