---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLIC3OCM%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQC4q2NYTsBI%2B3AHjboN8bYwH18G2u4nJx5I3gS5a5WeMwIhAIMZyk90SAc6ZUE7JRZTkk68s0ZHJV%2FpYI67BJc%2FoaUHKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxD5Q21lrU%2FqS39uWYq3AO0GPmLSlaJrFmY813Oeasu9CjgNPR9dkgmf7D7bsXV3R%2BdvyiEQUbg8OevPgkgdhYx%2FMvCrXHweKfET4q%2BuuBm7BJUAbCJXNeIEbuRh86elfqkR4RWHPPelsuhcQRZIDE3eMyP2N8oHgSxXmW9aaxbb1v9HlUqLzE4PzMteW4evgxayspb83JPri4vBxOofL9d%2FiUV0xIudMcvAIvLz70PTLfeBgcgtQVNGwPj69r%2Bydwg9Dp6hnHBoh5%2Fqjp7Ic787HN7IEEJF6lQH70C68TiO6OTdpCWIgpqjsoQXbBuqIguBO16t8cwpGXDYDupD5ESUXXqoz5Mt4nby154EDXiVATaVBVbFNw1ZSbZxcamlxPWwYhtEXs1UDxKxNLhIowVtBIi%2FiUfq5nqvi9gUnPPR7p8H0EwPWkCwwNpGrWRdjduES33MN1um7X0IH9pC6NgqvBqVn8GNFrSs1KDbAIrGqHko7aG%2FkxZ47sbUCCCX7ZgVyp25S4a1hCc8oWFevnRv96r3XHGbu686vw%2BGuFnFSitt%2BlypY6%2BjPapPQVclCTS1vP6l9Jolke4al%2BED%2FVGCcrqfIet7G8Az0ZP%2FHvW%2FkBjeJt0yC%2FJ1AsEKtsle2eLLrbgc5Wvo9zu9jD7iKnNBjqkAVJHN%2BgrqPKhabh%2FPHyOpKyDanM3shRML8U47q5Xl9xXOmJ169Ch1qoJDEx2iObmgVUi9tF1WPx7NAiIsahebRDHLqlKGEfOOYNuhMOO2msopvO5CjbNMN8QUjqs7yxDm0N4aNFMUpsk3imrWWb5fWE6F7LRrEU7mVQ0CTjgv2r51jQCOIrC9arKQNWMwIrzxnZXcMVlfYQGihbmLnvmyBStQHZm&X-Amz-Signature=e2bc47ca456d6e008e3fbdb970fb2560f6d825d7fab196daead92b2696bdc999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLIC3OCM%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQC4q2NYTsBI%2B3AHjboN8bYwH18G2u4nJx5I3gS5a5WeMwIhAIMZyk90SAc6ZUE7JRZTkk68s0ZHJV%2FpYI67BJc%2FoaUHKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxD5Q21lrU%2FqS39uWYq3AO0GPmLSlaJrFmY813Oeasu9CjgNPR9dkgmf7D7bsXV3R%2BdvyiEQUbg8OevPgkgdhYx%2FMvCrXHweKfET4q%2BuuBm7BJUAbCJXNeIEbuRh86elfqkR4RWHPPelsuhcQRZIDE3eMyP2N8oHgSxXmW9aaxbb1v9HlUqLzE4PzMteW4evgxayspb83JPri4vBxOofL9d%2FiUV0xIudMcvAIvLz70PTLfeBgcgtQVNGwPj69r%2Bydwg9Dp6hnHBoh5%2Fqjp7Ic787HN7IEEJF6lQH70C68TiO6OTdpCWIgpqjsoQXbBuqIguBO16t8cwpGXDYDupD5ESUXXqoz5Mt4nby154EDXiVATaVBVbFNw1ZSbZxcamlxPWwYhtEXs1UDxKxNLhIowVtBIi%2FiUfq5nqvi9gUnPPR7p8H0EwPWkCwwNpGrWRdjduES33MN1um7X0IH9pC6NgqvBqVn8GNFrSs1KDbAIrGqHko7aG%2FkxZ47sbUCCCX7ZgVyp25S4a1hCc8oWFevnRv96r3XHGbu686vw%2BGuFnFSitt%2BlypY6%2BjPapPQVclCTS1vP6l9Jolke4al%2BED%2FVGCcrqfIet7G8Az0ZP%2FHvW%2FkBjeJt0yC%2FJ1AsEKtsle2eLLrbgc5Wvo9zu9jD7iKnNBjqkAVJHN%2BgrqPKhabh%2FPHyOpKyDanM3shRML8U47q5Xl9xXOmJ169Ch1qoJDEx2iObmgVUi9tF1WPx7NAiIsahebRDHLqlKGEfOOYNuhMOO2msopvO5CjbNMN8QUjqs7yxDm0N4aNFMUpsk3imrWWb5fWE6F7LRrEU7mVQ0CTjgv2r51jQCOIrC9arKQNWMwIrzxnZXcMVlfYQGihbmLnvmyBStQHZm&X-Amz-Signature=9278b49f571fde5e2e905dd480690f677513c89f0647bfb5d642e32f12287c6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLIC3OCM%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQC4q2NYTsBI%2B3AHjboN8bYwH18G2u4nJx5I3gS5a5WeMwIhAIMZyk90SAc6ZUE7JRZTkk68s0ZHJV%2FpYI67BJc%2FoaUHKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxD5Q21lrU%2FqS39uWYq3AO0GPmLSlaJrFmY813Oeasu9CjgNPR9dkgmf7D7bsXV3R%2BdvyiEQUbg8OevPgkgdhYx%2FMvCrXHweKfET4q%2BuuBm7BJUAbCJXNeIEbuRh86elfqkR4RWHPPelsuhcQRZIDE3eMyP2N8oHgSxXmW9aaxbb1v9HlUqLzE4PzMteW4evgxayspb83JPri4vBxOofL9d%2FiUV0xIudMcvAIvLz70PTLfeBgcgtQVNGwPj69r%2Bydwg9Dp6hnHBoh5%2Fqjp7Ic787HN7IEEJF6lQH70C68TiO6OTdpCWIgpqjsoQXbBuqIguBO16t8cwpGXDYDupD5ESUXXqoz5Mt4nby154EDXiVATaVBVbFNw1ZSbZxcamlxPWwYhtEXs1UDxKxNLhIowVtBIi%2FiUfq5nqvi9gUnPPR7p8H0EwPWkCwwNpGrWRdjduES33MN1um7X0IH9pC6NgqvBqVn8GNFrSs1KDbAIrGqHko7aG%2FkxZ47sbUCCCX7ZgVyp25S4a1hCc8oWFevnRv96r3XHGbu686vw%2BGuFnFSitt%2BlypY6%2BjPapPQVclCTS1vP6l9Jolke4al%2BED%2FVGCcrqfIet7G8Az0ZP%2FHvW%2FkBjeJt0yC%2FJ1AsEKtsle2eLLrbgc5Wvo9zu9jD7iKnNBjqkAVJHN%2BgrqPKhabh%2FPHyOpKyDanM3shRML8U47q5Xl9xXOmJ169Ch1qoJDEx2iObmgVUi9tF1WPx7NAiIsahebRDHLqlKGEfOOYNuhMOO2msopvO5CjbNMN8QUjqs7yxDm0N4aNFMUpsk3imrWWb5fWE6F7LRrEU7mVQ0CTjgv2r51jQCOIrC9arKQNWMwIrzxnZXcMVlfYQGihbmLnvmyBStQHZm&X-Amz-Signature=b56d6b22722d32b3a9fad84614c89140d42e48a82f39118361520239af55a8d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

