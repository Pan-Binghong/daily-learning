---
title: VMware配置共享文件夹
date: '2024-11-27T14:24:00.000Z'
lastmod: '2024-11-27T14:35:00.000Z'
draft: false
categories:
- 其他
---

> 💡 VMware 设置共享文件夹，改过一次然后文件夹消失了。很奇怪…

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2690c9e4-a7e2-46b6-ae6e-556b52a86dd0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEJIMA6H%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIFjQi9%2Fh0pqDTc77p7ekCg1A7OCDOpXXH3RVwR4nDnmZAiEAuVUdOhcRv6cPyDY91m42xelVs7WY%2BHKcrqeasfQzgLcqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAYdpKdJNfbmTAQs%2BircAwFH1%2BAM5ddfU79XkNIsXdFi84p26wQ8SQM%2FOAmcbJUDUyVzhvDrHkFCxLn2pPN8u%2F5sEjlEGVj0vRf6Pxn9J1P5Gjop2x1CxOw93erU%2BGLjun%2FfK5JhAhJiPD9BNGKJ%2FjsW%2BJQvw0lX5sFfUf38aTsiL8oimEsLDJdo2USG9q4vGT38M6GzihLqdWjAaI2wZ75GOkx%2FPekSAVGGuk49s0lULjhytN6JGwX%2BboPJleofWd6uUrOouPfXGIO4I61CBzF8w1ndnkght7e8FXEtREMSQl4rCRLHa8UQeUNei7FoT02JslHvInvx2U3nZHQaxVOtVaGT8mpkyv5IJC4gdR1HuC15QAA6EBXyIxIU%2FeG7DU6TBk%2Blb%2BqYEc%2FaYZLpTxROMs8YWgtWy2gzWDOv7qBXqln2Y6ljsYlETr2hXpyPwVJUUCDsTtLuxnjBxjebUTI9jJVQQPOqlkm1Jwj2WzlXxIOdQfPRIIc60RRHhsaTaqfATHEN49yOQGB1MW84buHA40Xw3Mxsn96adknmfGxR1fWqN4%2BaLxWVgSb6skwR7NYG33%2FWPb8aFwB7WB1RETxl2XAqdR1qMTtaGzPiK8ODlqt4ebFw0FMjq1chOS3jKVq3D%2BBZCZ0H2JQSMIGU78wGOqUB0QGIe1pLEYarm8iqBWkZ96HkHa%2FGNUWZjV6SKXZFLppeSeWaxbw3%2BCFOfeLHncOe5J1jhP3camLGHB9qlrjT1oPquqnCKyeVQq95fCV0VcFmVR%2Bzrs8laCUitU1udBSghbIHXOLeqSjQ1%2Ft0awJDyIOpBaCzmVdKQXEJFVw2Q4t4g8nBklPIYBRnDoQ8ktrfAFoL4hCuy0H5DWRcCIZ%2BHDOSDSyD&X-Amz-Signature=40237e249e3ab89e88c923f31517bc85cbbc4bc7c52216858e02497dbb4025d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



