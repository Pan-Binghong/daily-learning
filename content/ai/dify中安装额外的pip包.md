---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ2KENFM%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICQaCMiLBCFeEsnSTXa3%2BzDRWS2g9mveiLxjieLAhT%2BUAiAjZIJcY%2Bj9fRRfpndGPkebh8zImQ0oUHEJL5oeDWSjDSr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIM8u%2BTULIZ%2FQtgoxPIKtwDF8xEiu8lAC7b30Z%2Bg0c06vbEuHkM2KzPrCPIuZm%2BNr8wbFd%2FE2oy7aqas5yZ%2F%2BIghMTkn5VQGUqE6qdV2nodzyCMXO1eWw%2BSjl49QXm7G2LoHTtlGkFGh3K4yOZrLmZ372iPaXy%2FJ%2Fv9H3Rz7Js1F4H0SgIFp0eDXFz3z4KWbZBalUCtWP4M3%2F17PUg%2B9dtpMB6b3hfTS7BMpoyMLEqADykHa2UoXmhj3WXPlLR33DdkoCuLid%2BrqN9%2B12NUw0rHPu1Ilf9umsV6DcnxlB9ULO4xR2sjU5bjDbxxLFWj7Lj8Wu%2FwI%2BGfamEIvTt8xpC4x3LDazHtTVCF47%2BHG5yh7im2NAMjWMOw5kGWAI680iQ8%2B62ronqd8TVMRobfaLo9RWm1oci1dfShMZ64TpQ0YxyeVHy%2F1xxgT9qjDTokKRJXYz3h8RMo6nXV1M6SdzUc2xqouVk%2Fwst%2Fc03CNW4wHey%2FRyDt5r6ASGA13OSX5KLy6vVB1MfUWFK3QGFGU%2BRgxoxP36pi1NU16NIMn3ot2i0z55wfleV80PpfmPMRiwYgaiEtRcSOb9zqt7NLUd8pYJI8%2BSsrTWdP3JlfH99mz5%2BdwvtDWXadPhvm7ZptZkZ%2FH1oRvDqye%2FLaMrUwks2OzQY6pgGx%2F3%2Bj019vtyTAPWpWyZJKxspuMGZHTPNb%2BzcudR9kxLRYa9R4d%2F3kDxZtQVv6XwNgxDoF7cFvIvw0y%2FCN84GD7BxewBGOlFt3qC%2Fpo%2F%2FRmmd%2FHRh5MpwMdaJvnX37c%2FZwOxz6U6jRIlANSBOwSvaFiCPZkPP4rTtOCQp6XTGJ44iscZ%2FUWfg%2BDl0%2BKcvXMPLaHeSj%2BrLkoNDtyDJ%2BDa9oBOkPMePG&X-Amz-Signature=957900787bb414de04cb55d987bc3f07082547f29db76da5d73c394ee159f8b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

