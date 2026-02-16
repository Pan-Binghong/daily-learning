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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZMAQA6I%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCd2dkrH86i90LBFaoyEkdZOxs49MTn1rUiqnEqYsTLCQIhAPpoZghUsrTlAX7gOcODHz20nVNGM2KGcgEXu8eV9b9pKv8DCCwQABoMNjM3NDIzMTgzODA1IgyJPkjLg1YWAcNUZYsq3ANMqi6xficyjPDJlOAT%2BOSZ6zS2tt2OWIyKYk98xjeTfKsJQe2i6yTr67RC46xkhZfgobvDe2ZkwOvnrnUQDIQ%2FVrPb1K1aK18qLqvDimrlJpxUOKbISCZEQlHxWELBwIFxT1Ul0vdidPg6Wni3dGGeJ%2FWsanGmm5iXCGmXDWzGzvAEHeOZY9RF46i1HOHSE8u6DmbZdvmDAwcgKOsTRWNhjjeBHnINcbsS3UDyyRvyKyymI7cJrw6ikSxwFTUgyeF%2F9pPlhKwUMxTkbUKQ3HS0YSyhCygyfgAMxtqQzPPr47SNwfGpysM%2BOvvhIs17SYlwZDtr%2BKQMrkPOi6YK7dp8gBzi%2FKc%2B1hs2yTWx60xHxZ1Ols5xoK69fKSMLMVBa9rfItgPhVwhkd0UxifDbRIj5C%2B82M1u%2FGHSaO61vM500zKd%2BShz4daX3dNi%2BTFHC8HhLa%2BFrJwZUVxmgTOsioY0fSQXgpdMcXeEgHOvcrfk8wekeGamdolrwY2%2B71KumfTM39JlibtZ%2B8lxQ83cLel%2FjAkh0UV%2BJ%2F3ITgP3sFJhO5sCqtc7wirULD9I6er8NXN%2FN144Hkhc%2FLlNC04b2iPXZIrVvpzZeUINVM5D%2B0yqWxeMr5DZNSjPVkv0mDDAlMrMBjqkAfABGCht2fuZ7AfqWOY6NUoHR6681c%2B%2BkPZHuCfkl6fzPSQJe2%2F2cp7U3cEiZuMj6%2B1nus%2BOx6ZEsLDscj3YeljWGHA51lo1Vu%2Bry3Xx2L5Ih7rWX91lCDIsJXhuk5EUBQufQaDXfxwD0f0piisAhTX%2FfXGjb95YLKjbl%2FdF4CCuaLYmkx6iRM7TjNbZSa5SWEksauaayeDkrqRICMzcE9Wr2gXj&X-Amz-Signature=df513a1ae3e9595f4fc33b5aa40f9d3e902df267de49c01e40fb7f98782f16f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZMAQA6I%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCd2dkrH86i90LBFaoyEkdZOxs49MTn1rUiqnEqYsTLCQIhAPpoZghUsrTlAX7gOcODHz20nVNGM2KGcgEXu8eV9b9pKv8DCCwQABoMNjM3NDIzMTgzODA1IgyJPkjLg1YWAcNUZYsq3ANMqi6xficyjPDJlOAT%2BOSZ6zS2tt2OWIyKYk98xjeTfKsJQe2i6yTr67RC46xkhZfgobvDe2ZkwOvnrnUQDIQ%2FVrPb1K1aK18qLqvDimrlJpxUOKbISCZEQlHxWELBwIFxT1Ul0vdidPg6Wni3dGGeJ%2FWsanGmm5iXCGmXDWzGzvAEHeOZY9RF46i1HOHSE8u6DmbZdvmDAwcgKOsTRWNhjjeBHnINcbsS3UDyyRvyKyymI7cJrw6ikSxwFTUgyeF%2F9pPlhKwUMxTkbUKQ3HS0YSyhCygyfgAMxtqQzPPr47SNwfGpysM%2BOvvhIs17SYlwZDtr%2BKQMrkPOi6YK7dp8gBzi%2FKc%2B1hs2yTWx60xHxZ1Ols5xoK69fKSMLMVBa9rfItgPhVwhkd0UxifDbRIj5C%2B82M1u%2FGHSaO61vM500zKd%2BShz4daX3dNi%2BTFHC8HhLa%2BFrJwZUVxmgTOsioY0fSQXgpdMcXeEgHOvcrfk8wekeGamdolrwY2%2B71KumfTM39JlibtZ%2B8lxQ83cLel%2FjAkh0UV%2BJ%2F3ITgP3sFJhO5sCqtc7wirULD9I6er8NXN%2FN144Hkhc%2FLlNC04b2iPXZIrVvpzZeUINVM5D%2B0yqWxeMr5DZNSjPVkv0mDDAlMrMBjqkAfABGCht2fuZ7AfqWOY6NUoHR6681c%2B%2BkPZHuCfkl6fzPSQJe2%2F2cp7U3cEiZuMj6%2B1nus%2BOx6ZEsLDscj3YeljWGHA51lo1Vu%2Bry3Xx2L5Ih7rWX91lCDIsJXhuk5EUBQufQaDXfxwD0f0piisAhTX%2FfXGjb95YLKjbl%2FdF4CCuaLYmkx6iRM7TjNbZSa5SWEksauaayeDkrqRICMzcE9Wr2gXj&X-Amz-Signature=9fe5ced2d1966c8eefa8e3fb852b049f639513aba3c31c7e393830903e1c049c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

