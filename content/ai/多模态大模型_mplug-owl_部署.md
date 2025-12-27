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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBFJVVU3%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHO2qaJaM2ZGoMwhtR%2F859n%2FNgvmB0MWvFTbMNOnRRz%2BAiA%2F6ARMg%2FFw7XbC%2BNiC%2FIYbikBQnMS%2FIkGRDKAcUEP41Sr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMwUHnCGoKcqopEQqiKtwDDGpiw88SK219F127r1J%2BIchf9PaQrQI7njVmefNCf2SKsY93R2ajaoX18JtSyrrdxenugGThR7jF2W%2BWOxKxM0Bin8RAUTxd7xDs0nj%2F%2FflR3q2P1VTbtOI0xNGo36sgJwy0qOZKeYdq7Y9%2BEdgXMN%2BIH0vrkQAol7TW0tbSr%2FySsefVYIlO2lq6OFimUxcab3u41TRD1%2FNNcbTj9iQV0X9uEXVHYlmjnpRqicLUCNxbOxbTgOGSckFGRP07Aq%2FHMmUyKjyspKx5c%2BPgP24w6GkNga3zWJIM4nxNRmhCd4Fi1Uk%2FtB%2BfsW%2FrceXqatop5B%2FexuJFlRkCzVKtObqhjSBGFNE3uFQpg6XidyOLCNHduCwx6Vl7GLUZkB360542P9YWiB57Xs3a9nqK%2F9tLNyyXJdpSTMc73vpMekHnh0LsZoqTFGPpmBDk%2BfQe6Q9ZFVK68wFWQZwdXFBi7OLBuWACFABaw2%2FqS7K%2Bbx%2BuKHB9OOjw8f15LxPBxAZCQP%2BlU7Ry%2Bt1mIBkBCrPB4XBsgedzhdANvUY%2FJAr4TScuVkOefsly4erHvSRF%2FQlX5MTXtH5FJYiAaWqI0WLm%2FKHr%2Fa3I1wgvPDz1FhXPy2O7nk87UloCqmw3tN1YY%2FIw6t%2B8ygY6pgGsx4rzD3gPZ4H%2B0oMxd8QN1Mm0X4GSbaQ9TSAQrtB98%2FERy2qj0FibAHp8dpwW2kQj9b2WOjzL15mFtV0XLevQ7a%2FFAgP2UoXYPj7JS1h9czea1hmSsMlQKqtdQkn0BvCv%2BHlv0aQEFZEI5Oppaq16cueNcMOjmaaIylpGeEL2lsdcU2FIo6Y9RZ7u5wv2wpPBnzpFrtyp5%2BpugnPtFxTblGs2L4uu&X-Amz-Signature=70d149548118c21d6ed305c102fc66091ceed030c3c98ca0288911d28396ab62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBFJVVU3%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHO2qaJaM2ZGoMwhtR%2F859n%2FNgvmB0MWvFTbMNOnRRz%2BAiA%2F6ARMg%2FFw7XbC%2BNiC%2FIYbikBQnMS%2FIkGRDKAcUEP41Sr%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMwUHnCGoKcqopEQqiKtwDDGpiw88SK219F127r1J%2BIchf9PaQrQI7njVmefNCf2SKsY93R2ajaoX18JtSyrrdxenugGThR7jF2W%2BWOxKxM0Bin8RAUTxd7xDs0nj%2F%2FflR3q2P1VTbtOI0xNGo36sgJwy0qOZKeYdq7Y9%2BEdgXMN%2BIH0vrkQAol7TW0tbSr%2FySsefVYIlO2lq6OFimUxcab3u41TRD1%2FNNcbTj9iQV0X9uEXVHYlmjnpRqicLUCNxbOxbTgOGSckFGRP07Aq%2FHMmUyKjyspKx5c%2BPgP24w6GkNga3zWJIM4nxNRmhCd4Fi1Uk%2FtB%2BfsW%2FrceXqatop5B%2FexuJFlRkCzVKtObqhjSBGFNE3uFQpg6XidyOLCNHduCwx6Vl7GLUZkB360542P9YWiB57Xs3a9nqK%2F9tLNyyXJdpSTMc73vpMekHnh0LsZoqTFGPpmBDk%2BfQe6Q9ZFVK68wFWQZwdXFBi7OLBuWACFABaw2%2FqS7K%2Bbx%2BuKHB9OOjw8f15LxPBxAZCQP%2BlU7Ry%2Bt1mIBkBCrPB4XBsgedzhdANvUY%2FJAr4TScuVkOefsly4erHvSRF%2FQlX5MTXtH5FJYiAaWqI0WLm%2FKHr%2Fa3I1wgvPDz1FhXPy2O7nk87UloCqmw3tN1YY%2FIw6t%2B8ygY6pgGsx4rzD3gPZ4H%2B0oMxd8QN1Mm0X4GSbaQ9TSAQrtB98%2FERy2qj0FibAHp8dpwW2kQj9b2WOjzL15mFtV0XLevQ7a%2FFAgP2UoXYPj7JS1h9czea1hmSsMlQKqtdQkn0BvCv%2BHlv0aQEFZEI5Oppaq16cueNcMOjmaaIylpGeEL2lsdcU2FIo6Y9RZ7u5wv2wpPBnzpFrtyp5%2BpugnPtFxTblGs2L4uu&X-Amz-Signature=75c26c4439b30901edbbdff6a0f4fe11382b150059c55dd6ceda65ecfa09fa3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

