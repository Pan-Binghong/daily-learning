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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC737EZM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDb9QlULPMnzs3ZUilA8xsPNK5AQrhI0l%2FnAaWPXlbg6gIgHAZpwsxYrGMFOncHZYvP1me4%2FGtieEM%2B6wH59PmJEGIq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPkIT7VrfMkFwWLmKCrcA5duWRQdEs%2F6Pi%2BvrBaPufwaep2T6EZQArL8syFNeLyPyMPY%2FzNFoyBGL%2FxZ12vqKbOZOsE6ZB%2BwxoRyDlL3aNnPmNuDMzBjqq0Dq%2FIQdgSGRM3mdH6KXs0iJGsisrbiPjPhdQUYsozMARHth8LP9rKeWbBlfakKVFB5unH6OTuM2hpcBzbZV3C%2Bowgg5YrMSxe%2BkeD8kT2ZLON%2B7DnnCQ6p85I2YgSBBrMbHTrS7w406NXdJVmcOOAkXEWqYcY%2FAdJeL57LRcWpG4VlZFbkbK0ejvhkLhFdAOOYcZVDzvRuPR2uSElc3vql8F1CFzcS1I1oF4f%2BdZnTltqsom0seP%2FRkrCi%2BWfUaRhHQZ9a1OcRQ4tU709eyFrFGm1H0arNZojy64q%2FreFWz6qrSFcv%2BqtF3B3l9Fq8YUZA9M%2F%2Fa8Sxj%2F5wux30eMjhajCCxWvuhsCikYX3sqq4%2BDMHcdz2gBa0SC60hw1sPZenA2OJlbbsYRbHJPzXkR6UqoJp9cU5lDs5makxBtQ2OVOG1MXgA%2B0mmnQaUgeG22F7Qtc35DBlv0hTk7oUuomivlSlVWwjgqV3BevlrNwNWqGrBPbE3nc%2BE8v8XVyPyLl%2BiFt1fWJUV%2FVJ6wlEJx4u2JBGMKew%2BMkGOqUBSzJ9UZYvRr7S3M0H14fKv%2FiBJh0Sl%2B7Kx9p0FdG0lc%2BE2OtKN5h8hIcUZexVKmBRlunWUdcUOBzgbccpa7vZwXGawewg1ChybRu7KLMJysquRfbOGfDPh4rttkJfsM%2BzptqgFayURl1rMmEkSbuCAnnNe8qupJIPJLa5dt2hn8f%2FM9fCUQCR8paTZvdVGT9DDrVdLBDOP45DSauUJgSisHBT6bbh&X-Amz-Signature=da5e521ee8daaac332a9ee062cb74b105471820bd5f446e95a5f6d97c5517bed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZC737EZM%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDb9QlULPMnzs3ZUilA8xsPNK5AQrhI0l%2FnAaWPXlbg6gIgHAZpwsxYrGMFOncHZYvP1me4%2FGtieEM%2B6wH59PmJEGIq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPkIT7VrfMkFwWLmKCrcA5duWRQdEs%2F6Pi%2BvrBaPufwaep2T6EZQArL8syFNeLyPyMPY%2FzNFoyBGL%2FxZ12vqKbOZOsE6ZB%2BwxoRyDlL3aNnPmNuDMzBjqq0Dq%2FIQdgSGRM3mdH6KXs0iJGsisrbiPjPhdQUYsozMARHth8LP9rKeWbBlfakKVFB5unH6OTuM2hpcBzbZV3C%2Bowgg5YrMSxe%2BkeD8kT2ZLON%2B7DnnCQ6p85I2YgSBBrMbHTrS7w406NXdJVmcOOAkXEWqYcY%2FAdJeL57LRcWpG4VlZFbkbK0ejvhkLhFdAOOYcZVDzvRuPR2uSElc3vql8F1CFzcS1I1oF4f%2BdZnTltqsom0seP%2FRkrCi%2BWfUaRhHQZ9a1OcRQ4tU709eyFrFGm1H0arNZojy64q%2FreFWz6qrSFcv%2BqtF3B3l9Fq8YUZA9M%2F%2Fa8Sxj%2F5wux30eMjhajCCxWvuhsCikYX3sqq4%2BDMHcdz2gBa0SC60hw1sPZenA2OJlbbsYRbHJPzXkR6UqoJp9cU5lDs5makxBtQ2OVOG1MXgA%2B0mmnQaUgeG22F7Qtc35DBlv0hTk7oUuomivlSlVWwjgqV3BevlrNwNWqGrBPbE3nc%2BE8v8XVyPyLl%2BiFt1fWJUV%2FVJ6wlEJx4u2JBGMKew%2BMkGOqUBSzJ9UZYvRr7S3M0H14fKv%2FiBJh0Sl%2B7Kx9p0FdG0lc%2BE2OtKN5h8hIcUZexVKmBRlunWUdcUOBzgbccpa7vZwXGawewg1ChybRu7KLMJysquRfbOGfDPh4rttkJfsM%2BzptqgFayURl1rMmEkSbuCAnnNe8qupJIPJLa5dt2hn8f%2FM9fCUQCR8paTZvdVGT9DDrVdLBDOP45DSauUJgSisHBT6bbh&X-Amz-Signature=223babc3e033032c2f40a05d1548e6e6ec71be14fd4aed170f94486201b51c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

