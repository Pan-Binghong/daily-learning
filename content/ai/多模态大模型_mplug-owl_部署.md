---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHELPFSR%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIACvJeywRjKxnCKWxJB8brFLVWBQwCH5aVfUSgnqz%2FK4AiEA41AXW6oGxbgfWnkRXc9680RxBxbHXIpcS23hqJAP0Tsq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDOITAXIvLP68wZASQCrcA1Hexrt3ZSOE9QQGH2ROuOghhjnbhGdxArb%2F%2BYO8W0HoqQEM%2FtBzxcGLNHzGPmjoW4rgfrinieOKwJw5nBl%2BcYfGEo3ZGovQK9f72L0wjAOh31%2FVaaCs2psk36BEz7lwKghbRExX92MMvMuQi9c7Od2xHyIl1Z7oiU8nYf05oPUsnDo6bnMyPrw9ZRvRVBVIJWA9Xue07ah%2F5tHPAuOQVD1vaJ5uKQg4Bg%2BNu0VQyM0lb3WEs8U2EirT0TKRxNRrc9fordiBQVaYSQB%2B1TocoPTlBP5g7N3HCT0wwq3mTecHAbGtv2rmz3hCGcQjWmsWMIyc71BrWnmrePUbxJ8q9ZzII1qpuk2erxqPk3ADV1eNGI2okBoffc0PODCJfrIqHJbmavf7i4vYmsAUR3mdYg9U1W34PwkY4bmZqm6xwkK%2BBiNmAIvR3E2OYKEti1oMOQaUJIOyjcrv1y%2BTqPI%2FrGerYpSJtyVZ%2FfQBOAzBjILa%2FYuoR9GLFTUjJPP35nr1dm0RLJy2RvDOlWLihGhhJH%2FwjhDiYfrtFfTMgZL1sWojF7odV0zAj2Otz7QbsVVJYMxvmU1bgvGzgDedlCowBfx%2Benl8eN2T0%2FC5wo9IjnL6%2BTufeV%2BeDsBgvpEWMIb9p8oGOqUB0ArKOFoXi5ceje97c%2Fjuy86MmhMz%2BXZIFyKDfB%2BnJ0jAOPzepcXpdHVhK1PCwsg9p6FCWg5KV7sPWlvUXmoyUbXm1BM3wqB%2FMAZ2YFJ%2FGjDRIRMUjQ5EGT5N1dcIPQelkl770lo2pD%2BuZuNdRFHCcKfhwlCstGE1xjsXF6ophHEdFLIJJxdaWOZmdlNjuiuPdNif69g%2BrSjtLOJ3werzERwT8N0A&X-Amz-Signature=e7b9f1c986ee32e966ed3f100e9e0e0c1782686d0d1611e3918dd47b04047baa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHELPFSR%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIACvJeywRjKxnCKWxJB8brFLVWBQwCH5aVfUSgnqz%2FK4AiEA41AXW6oGxbgfWnkRXc9680RxBxbHXIpcS23hqJAP0Tsq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDOITAXIvLP68wZASQCrcA1Hexrt3ZSOE9QQGH2ROuOghhjnbhGdxArb%2F%2BYO8W0HoqQEM%2FtBzxcGLNHzGPmjoW4rgfrinieOKwJw5nBl%2BcYfGEo3ZGovQK9f72L0wjAOh31%2FVaaCs2psk36BEz7lwKghbRExX92MMvMuQi9c7Od2xHyIl1Z7oiU8nYf05oPUsnDo6bnMyPrw9ZRvRVBVIJWA9Xue07ah%2F5tHPAuOQVD1vaJ5uKQg4Bg%2BNu0VQyM0lb3WEs8U2EirT0TKRxNRrc9fordiBQVaYSQB%2B1TocoPTlBP5g7N3HCT0wwq3mTecHAbGtv2rmz3hCGcQjWmsWMIyc71BrWnmrePUbxJ8q9ZzII1qpuk2erxqPk3ADV1eNGI2okBoffc0PODCJfrIqHJbmavf7i4vYmsAUR3mdYg9U1W34PwkY4bmZqm6xwkK%2BBiNmAIvR3E2OYKEti1oMOQaUJIOyjcrv1y%2BTqPI%2FrGerYpSJtyVZ%2FfQBOAzBjILa%2FYuoR9GLFTUjJPP35nr1dm0RLJy2RvDOlWLihGhhJH%2FwjhDiYfrtFfTMgZL1sWojF7odV0zAj2Otz7QbsVVJYMxvmU1bgvGzgDedlCowBfx%2Benl8eN2T0%2FC5wo9IjnL6%2BTufeV%2BeDsBgvpEWMIb9p8oGOqUB0ArKOFoXi5ceje97c%2Fjuy86MmhMz%2BXZIFyKDfB%2BnJ0jAOPzepcXpdHVhK1PCwsg9p6FCWg5KV7sPWlvUXmoyUbXm1BM3wqB%2FMAZ2YFJ%2FGjDRIRMUjQ5EGT5N1dcIPQelkl770lo2pD%2BuZuNdRFHCcKfhwlCstGE1xjsXF6ophHEdFLIJJxdaWOZmdlNjuiuPdNif69g%2BrSjtLOJ3werzERwT8N0A&X-Amz-Signature=f3999ba7d331c154865df1f202a14bac58a92cf4c7452f9159f408d416603a70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

