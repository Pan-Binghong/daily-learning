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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SENAFS7%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC%2FxAR%2FravCfeE2SDIbXkN2zaEn%2BiHjV34wM%2BQbD6SI3QIgfBb2plNhyyggd11sNwEInyL8zN5T53tk425lrUbxN6Eq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDArRnW45nlGV1ktRvyrcAwY0f7u1Tw6nHVmFcndy0C5yQ12P%2BNJIMaoHcmMPf0ru7uogyWReG63rMKQsHty29OoM1AaOdJPMg8xpjgNp2fYtRrWm%2BcvoprUdAFZcn7BByVutM0aNkr0800LKRY65%2FDTSWu8Z8FzfbXXCjQcpRLDozo7cwOVduRsNaUcgfv2vnMF80BjxjbcV8H0iEaa8m4x0cBnag3HZ1R7jSEelF%2BGM1N4Lw2DUekm02P45lJf07V%2FHtR6QWE6Zt2qRlaMlgjEQfZ8LcgytGJX34QPa3b9QzqqLEhn4lJPMDygX%2BTHjeUis2yjbXgMN0AWiIWirVjv3BfDLsEujKLM4NLvYnQ1fFsxbKs5mXSwHQWNNJF0dnvvNqmlak8o7P%2BEIhaHjkxXGGm39wCvfPEfhz7VDNa0oJ2%2FeNKNA6jMSO%2BVYWq9hHkyre%2FnFGvEMPQ1oLVn%2FXfanqN9gws%2B06bUw8SKeSgijQnWnqRTtNAV1jJnIyEVA5NWjQ1HgH9tJMXoJa1rX8Kfbx47QxBuGbmiPaRlr3FKRWqgpWVsmI1%2FsXf6sm%2F0f%2B%2F5tydx4LoqWlvSRXlthryFqPjOqvtqdxJR5KNHYl%2BM%2F9bXhsbqy3EasfdXXzjSdqlaWndHa%2FaqnTvrpMM%2BaocsGOqUBm%2B6GkSEjDg%2FHu0ckDACSPke2EdVvHbdULSWVvzKNOoYHUyDQmO%2FfAAISRvZvqDo2VdMj0d%2B9GcAeZAA66%2F1druvaQlTvHH0Ood1D3X1F40vRh1Lo%2FoZuuyGKzgQ34Parmlq9%2BSrDRDpxtWNkTOWjvcrzk08DTUiqdbvtN389fsatKSqyD8NkdrSxOxXHxzhIWjrBVmKCvExb2nYyKljwUcpIMLAL&X-Amz-Signature=764256eb66af3c8b33e139462ca44c1eb17e65664636da2148a41debe63a75cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SENAFS7%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQC%2FxAR%2FravCfeE2SDIbXkN2zaEn%2BiHjV34wM%2BQbD6SI3QIgfBb2plNhyyggd11sNwEInyL8zN5T53tk425lrUbxN6Eq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDArRnW45nlGV1ktRvyrcAwY0f7u1Tw6nHVmFcndy0C5yQ12P%2BNJIMaoHcmMPf0ru7uogyWReG63rMKQsHty29OoM1AaOdJPMg8xpjgNp2fYtRrWm%2BcvoprUdAFZcn7BByVutM0aNkr0800LKRY65%2FDTSWu8Z8FzfbXXCjQcpRLDozo7cwOVduRsNaUcgfv2vnMF80BjxjbcV8H0iEaa8m4x0cBnag3HZ1R7jSEelF%2BGM1N4Lw2DUekm02P45lJf07V%2FHtR6QWE6Zt2qRlaMlgjEQfZ8LcgytGJX34QPa3b9QzqqLEhn4lJPMDygX%2BTHjeUis2yjbXgMN0AWiIWirVjv3BfDLsEujKLM4NLvYnQ1fFsxbKs5mXSwHQWNNJF0dnvvNqmlak8o7P%2BEIhaHjkxXGGm39wCvfPEfhz7VDNa0oJ2%2FeNKNA6jMSO%2BVYWq9hHkyre%2FnFGvEMPQ1oLVn%2FXfanqN9gws%2B06bUw8SKeSgijQnWnqRTtNAV1jJnIyEVA5NWjQ1HgH9tJMXoJa1rX8Kfbx47QxBuGbmiPaRlr3FKRWqgpWVsmI1%2FsXf6sm%2F0f%2B%2F5tydx4LoqWlvSRXlthryFqPjOqvtqdxJR5KNHYl%2BM%2F9bXhsbqy3EasfdXXzjSdqlaWndHa%2FaqnTvrpMM%2BaocsGOqUBm%2B6GkSEjDg%2FHu0ckDACSPke2EdVvHbdULSWVvzKNOoYHUyDQmO%2FfAAISRvZvqDo2VdMj0d%2B9GcAeZAA66%2F1druvaQlTvHH0Ood1D3X1F40vRh1Lo%2FoZuuyGKzgQ34Parmlq9%2BSrDRDpxtWNkTOWjvcrzk08DTUiqdbvtN389fsatKSqyD8NkdrSxOxXHxzhIWjrBVmKCvExb2nYyKljwUcpIMLAL&X-Amz-Signature=fdd082d4a6755bc48cb209479183cb63a2882efa73f5252e914cbf50a87ead34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

