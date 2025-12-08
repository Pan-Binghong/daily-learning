---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4XNF4FV%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGw8UzTgzlSeo25pXgHMr80uUh7I1dME2QP%2BQM2LyTWHAiEApq9HwMEA8OPlFOiWNmUf5VU%2FXN5ljy78PYaX7h2Rl8oqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPAxPXrVWH3Xz%2BPgkyrcAxuwIKa%2FsVLwrq2nzR97DBObALpqZvXbok56CJbJO6Kuz1GBEyVyGadPux7tOXzefMnHtEomZEQEy9vV0AMzD5s4Nw6pGaNn6bvWr7lb%2FBFmVJJJdGDS4BG4NZGSAbp7jmWHUM3AhFkmJmbXoYqX8H8rNJ2Xqbag%2FjnA6u1j6OSmMHHTOT%2BVmmMPsnhBc28a%2B3XMdNuXwZSiIBQpVXpZbQr2NLfnyd6ljYlSBdEJjHg5Qe0OiWUIk2Nw79%2Fs3qsmikeJpiD7p5MO4wXIhRgPQ3IS2aqOHdrFazq43eDGADhzm4FnOSDjhI3zydYWkZ4cBQb0KILIhmiW1C%2FrjSvpUQctx3eF9rCvm6ehm3t0LXKvPihypOP%2BDVWkxDX0qyuv%2BWMqlc4kFhyfQYPmAQ11h%2BGCyNNZOcyF%2FHCvnJ513SWkW0Um2JBAMy%2F6jIdYCRDe17kT%2BBO6ii2d5lYQqnqk9%2Bsg6J%2BwGCCXFRqCzN49hz%2FNJO7z0GUulbimNAKw%2B%2F6%2B5a%2BZNQ1JLj8YXnIFYW1hVD0%2Bq2VeHc6hdoITA4R8KYeth6%2BXQ8hVVMXpc3bWziOKfYLDmQ5xQ3QLUIr41v2wQP06uhkOEXhhYj9%2F39L%2FXRrcIa9B8O5Vb0J%2BgCvgMKzu2MkGOqUBS3UvZRWA56CSuqBR%2BdDB79qfCBpgduFP%2FKKeHCZUfsdDykaGLqIGeMVADwjhCwOyWscf7F4%2BMnx3Onfu5KJEGhVU4DV%2FQIzci2sdhkVdLmAfjGOBsqUgamW5iRT1%2FUXCc9WzqVJZvnvlOJZOBY9%2B9QLLhphopa6rJrleAOSIxxrEe3BzCoLeYwz0cWFbbuEaTmoN7h3HUYOj%2BDOnQf0K5unaMqOo&X-Amz-Signature=1ba9ea9309317a352017956e04ab7df60dec7841cf9bc562a168b28ed9a7cc68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

