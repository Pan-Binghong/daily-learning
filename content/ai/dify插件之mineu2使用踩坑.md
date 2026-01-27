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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPQBPZQ%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDB14jcBRjfM3Gh7ou5%2Bl9xpja00zznKTKNtFA%2BCjUKcgIgRslK%2FDB%2FRBHC6SRUhhZ0KNw6yp4mbx2dGSEV15Kk%2BYEq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDCbzWerabx%2F8IvjQyircA0tqvNRFZxcyAUddKXdl8dMULOG6nuX4xZyIWC6R9S3tTIM6toc%2FLZ41uykG%2F93Mluhpsg7L6sTJXKagURzhmPm555epiDxWApk%2Bv9Q74iCR3j8ljQlTkx29FMkSkFo66c9I3fUaFxBIo6d%2B1ZcCCa7y3qyJwv0S%2FvOhTZg%2BOjCm5rYtqV9wDPJ7oZ4YyL%2F6441Qt1NLUzp8xEVD0dakypXBjf9Kf9jsLfNizYytv%2F1hJ6v%2B%2FNl6RbdHv1nVSZstLX286CJNn1GsH%2BdtDjK2uTwKCmHbH8FoDTbiP0%2FyTVU2hR60xtbbkxoLpkdXnbPPBDrOeoifmEd6iHdpyMadqeol8%2BArTOQPhFu0XEVRyGHgcPZdkMjuPDY5jaa3lrVl9bsPUoQ4yKXiMH0Zyw7GtFB%2FqrehLJP8%2BxB%2BGgNaTRLMTXHIXlAJ%2Ftuxunpw4n%2FmBSjRpF32ISokNF0oAjeAROA95zm9Qf4y0wDoe8LY85FV3EzQ%2FR9zJTyUn9nMZDGyc7xmbrxmGnWtc8YGOGoXyttkvPdfwvXWQZAYhEv568TvQAe90y8wv4L4UcKo%2BbFkKEvHY1aGb%2BlzJUSPfpqx3kqVEtp8REQ2QD3RHxZbfPIdFequqCJUEFpFWdrqMPfS4MsGOqUBkvEFUOWE%2FJ01ACIriGqFOvHhY1kCDnaJ9g%2BplbIWYtOPQ%2BzLWDD%2BLK0eOASRtsaU8%2FDGHK8ZNb5J4HKSYhq3uRAVz7y88t%2BhZHioa18Xe5rzBPK4sbDGHbqffCXu7xi4hKSyciNGDnvotMkNncfAMrMtxMwU7c9uP0IquAXngTY3%2BDYT9nWf6cBQ6IggoJ1layF%2BbaKwqExdBt5lmmI%2F%2BZ8h7kVf&X-Amz-Signature=5b80a942eefd1fa618a1680c3b41b2f1b4e91459bfd1402f9be4e24a953226f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FPQBPZQ%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDB14jcBRjfM3Gh7ou5%2Bl9xpja00zznKTKNtFA%2BCjUKcgIgRslK%2FDB%2FRBHC6SRUhhZ0KNw6yp4mbx2dGSEV15Kk%2BYEq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDCbzWerabx%2F8IvjQyircA0tqvNRFZxcyAUddKXdl8dMULOG6nuX4xZyIWC6R9S3tTIM6toc%2FLZ41uykG%2F93Mluhpsg7L6sTJXKagURzhmPm555epiDxWApk%2Bv9Q74iCR3j8ljQlTkx29FMkSkFo66c9I3fUaFxBIo6d%2B1ZcCCa7y3qyJwv0S%2FvOhTZg%2BOjCm5rYtqV9wDPJ7oZ4YyL%2F6441Qt1NLUzp8xEVD0dakypXBjf9Kf9jsLfNizYytv%2F1hJ6v%2B%2FNl6RbdHv1nVSZstLX286CJNn1GsH%2BdtDjK2uTwKCmHbH8FoDTbiP0%2FyTVU2hR60xtbbkxoLpkdXnbPPBDrOeoifmEd6iHdpyMadqeol8%2BArTOQPhFu0XEVRyGHgcPZdkMjuPDY5jaa3lrVl9bsPUoQ4yKXiMH0Zyw7GtFB%2FqrehLJP8%2BxB%2BGgNaTRLMTXHIXlAJ%2Ftuxunpw4n%2FmBSjRpF32ISokNF0oAjeAROA95zm9Qf4y0wDoe8LY85FV3EzQ%2FR9zJTyUn9nMZDGyc7xmbrxmGnWtc8YGOGoXyttkvPdfwvXWQZAYhEv568TvQAe90y8wv4L4UcKo%2BbFkKEvHY1aGb%2BlzJUSPfpqx3kqVEtp8REQ2QD3RHxZbfPIdFequqCJUEFpFWdrqMPfS4MsGOqUBkvEFUOWE%2FJ01ACIriGqFOvHhY1kCDnaJ9g%2BplbIWYtOPQ%2BzLWDD%2BLK0eOASRtsaU8%2FDGHK8ZNb5J4HKSYhq3uRAVz7y88t%2BhZHioa18Xe5rzBPK4sbDGHbqffCXu7xi4hKSyciNGDnvotMkNncfAMrMtxMwU7c9uP0IquAXngTY3%2BDYT9nWf6cBQ6IggoJ1layF%2BbaKwqExdBt5lmmI%2F%2BZ8h7kVf&X-Amz-Signature=507082d44e24c030e96e98f8d7135136c799abfd5837b5941c90d6d4a97aee3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



