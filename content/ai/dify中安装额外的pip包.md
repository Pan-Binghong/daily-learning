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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z77LV3PM%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICtQx0o%2Fr2MNhvHp3F2ZSTRcz5VmVkjXI8kqJiDUQMGHAiEAj%2FzGKf3iQWIX86M9ZjFbp2HGPVlT6PBF7sXan2UKwcQqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCiGgOn1hxj37UDbircA20DThqV9UXDYPQ4Cm%2FSSN5vlJcgXMXAcFPDDBf%2Fn8Etni%2BG2W7NQqYnuMnH5nOOD81%2FK51jWwPbSQOevZ83Q1%2BVgdJlETFEIJ5nVHau6e5aOaRvvFCvUleIbFDQ8eo0fkcP4xdp%2FrPw3U5v8lRiKoCAYigPmRo86NISkKPnmiWWKhs39cvDXCan9PVdxs3fx5BenkczkbiOwMuXm226fNOxnJfATQ1f%2FamF%2BgupFLuSBkVks5wpYU1kp%2Bgc5ljf6M7qSw2Y2pg7VbKPrBdHJlwXYeJCNHwvKI%2Bt4sVcr1BuidKHNGPhqJTEGGkzRgs%2FphjfEjZQaSchTGhCNEMc4NvjgV56%2F22rnvQUhwZjF0QNOQmz%2B7194iku33a9%2FSnxTOQMjpBj43IBNTPNwZEC%2FeDSnrvTbWcNW3ATFF7SiAO8R2DThQwHtFmQ%2Fa5mtX%2Fc4Ofh%2Bn3NccifPrH%2FhYWJUogr455bnqkA3OAp6AqCtw0ai7%2FGIKh2IRywcCByK5TgcPNp4GwiNJDdx7y2xXiEiuDR5r5TAbhxB6Y0e6eBdZXVOl18QAMVqdvqcw0SUV%2BMvbhIbrbyD2pgf%2BTNjyTMdM48FW41JBQnrK%2Fs8eEKUGDUorLK53vlzMCoPszMMISq%2FMoGOqUB3hXJdNby90DNoSzIK23TzEqm6yrI4mmDgy%2F1h6ttaN5cbHDtGcn2k1zLhEHrr6NLzxh2I8v%2FohimMedK1h9dpLycfYrlzRMC0LsQwQAvcWSsc4Izg3rETA5u2PhXcSArlOVUvVLeon1LQ4j7cnISc5sWG29wINsZLovX9F1ZduhepIGkehvCm71AM0xKoaxze5aodkW82SNLE3nNnH1WvuVGzQtF&X-Amz-Signature=c9a26e06ba7963c73d00e5cf24801e211592477c0572708b0766108bf39e5896&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

