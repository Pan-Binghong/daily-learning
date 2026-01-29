---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T6GUMXX%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0FYM5upHC%2F%2FRLRsKW8MgdtxlQoLgZksfsXkmC3kzM7AiEA83AZKH5tt0ftU2ixtZ6xN9irLNaOBX2JC3SmEbnlT%2Foq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDMW9LdO1SiSTPQOmBSrcA2w2mF8BMxLUaHpwwFePqjw6XXwxy6ucSz1jHlxR15LVkkvbULtj0C6LZ7kJBB50ReoGM0gAtzqxnOYrTrTWZB8a9EJMFVRc2MrCDkCkaHNHzNe7Q9ET5sP6FBHnyYz6hCNtoUDDzLJ%2Bfq6Cqtdmj6SiZ6FpmPjCA6Z9ZbtoNxdU%2BKcGSgpLXOrtddY%2FenucQHnZ5rHcoj0k5IpNGJCk%2Fn%2FC87Y46oawmRM2RIFzsfX5aHbHUCUGQoH%2Fo1nK%2BUIsuXCnRTJ3izIuVno0Yj5hP0xxNBt8XSCxCzv54iQU34gkTGBXcAFUIkaFWPjW4a8BSmym%2BBxfE8rfYg6J2blksnHJaJMlDjrbwVgazsjPRJPVIeuLrv3G6PHocXQ985yeerXOHuEC%2FIr7lfxDR7WsMJUKvg94bZowTXu5msT83jcmSa9mhNv9K05KbDYlaTgkPH%2BTpxibCog3L4YOTTflyK0MZKJyZCZdAVN87PWNz0%2FmfxQpFbCpAwdhffXKWwTJ7biyflCZ3MalDfyBSpDjvOge2m3WKVbCA6UGyqZbEWbPnUlKrHDgmkemiY97rWcHtPkNAuliDLR%2FGgqT8xnCV99srYMDub51llxQpXVJvyqJrtcfCrSaihnx2Y%2FHMNmh68sGOqUBtrnlV9z2OxXPQoBZm7qDUnccGATG1A0A7ErsTmSRhnpQyvE1E0xpXY4odUFOHO%2F%2FSKoXxGLczp2ce8WDeMkBR2ztCt55bgsYWpB8PRH8DNwItdIlqUPyuiOKYbuc%2BDXH8qtmcTjzuxPgiQZkNPIMlUu4l3f%2F2mewuPT1zdg5BPzrybckN0Ec8UjOJjDiU0UUOra%2BprhqJxIttYxbYgKcRoKkMfzO&X-Amz-Signature=fba066d9abfe086be5d3a27d23a7695cd3eb236aca72c0e90e92bd5127053082&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T6GUMXX%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID0FYM5upHC%2F%2FRLRsKW8MgdtxlQoLgZksfsXkmC3kzM7AiEA83AZKH5tt0ftU2ixtZ6xN9irLNaOBX2JC3SmEbnlT%2Foq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDMW9LdO1SiSTPQOmBSrcA2w2mF8BMxLUaHpwwFePqjw6XXwxy6ucSz1jHlxR15LVkkvbULtj0C6LZ7kJBB50ReoGM0gAtzqxnOYrTrTWZB8a9EJMFVRc2MrCDkCkaHNHzNe7Q9ET5sP6FBHnyYz6hCNtoUDDzLJ%2Bfq6Cqtdmj6SiZ6FpmPjCA6Z9ZbtoNxdU%2BKcGSgpLXOrtddY%2FenucQHnZ5rHcoj0k5IpNGJCk%2Fn%2FC87Y46oawmRM2RIFzsfX5aHbHUCUGQoH%2Fo1nK%2BUIsuXCnRTJ3izIuVno0Yj5hP0xxNBt8XSCxCzv54iQU34gkTGBXcAFUIkaFWPjW4a8BSmym%2BBxfE8rfYg6J2blksnHJaJMlDjrbwVgazsjPRJPVIeuLrv3G6PHocXQ985yeerXOHuEC%2FIr7lfxDR7WsMJUKvg94bZowTXu5msT83jcmSa9mhNv9K05KbDYlaTgkPH%2BTpxibCog3L4YOTTflyK0MZKJyZCZdAVN87PWNz0%2FmfxQpFbCpAwdhffXKWwTJ7biyflCZ3MalDfyBSpDjvOge2m3WKVbCA6UGyqZbEWbPnUlKrHDgmkemiY97rWcHtPkNAuliDLR%2FGgqT8xnCV99srYMDub51llxQpXVJvyqJrtcfCrSaihnx2Y%2FHMNmh68sGOqUBtrnlV9z2OxXPQoBZm7qDUnccGATG1A0A7ErsTmSRhnpQyvE1E0xpXY4odUFOHO%2F%2FSKoXxGLczp2ce8WDeMkBR2ztCt55bgsYWpB8PRH8DNwItdIlqUPyuiOKYbuc%2BDXH8qtmcTjzuxPgiQZkNPIMlUu4l3f%2F2mewuPT1zdg5BPzrybckN0Ec8UjOJjDiU0UUOra%2BprhqJxIttYxbYgKcRoKkMfzO&X-Amz-Signature=585bb919c7e841621f1aa558c8d21f37930507243e0a8731c8dff989af5f13d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



