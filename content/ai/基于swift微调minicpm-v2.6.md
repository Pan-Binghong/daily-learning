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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJBUBECE%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOu3%2F6Gt%2FcYmwFuVkZYbxSBRuzoxklzKH2%2FUSHS0A%2B2AiEA7aGosdEvD3lyfF6mIqAYGv0gST8%2FgVhvX%2FEQIAJsK5Mq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDHzJmE3oTuwGyNhv2CrcA03i7ETW5ki5x%2FfryCQTtnxD5xxfWPisfHRfi840QTINXuFMkisaSS9ka7YqM6EEiXXcjQtV2wksajU27hI1ZHkIIzCMKI7FLEmsj67HRaRSqyR3rbU0aHxUsrVNxD3IuO45grrRtf3qq5qUjq9MLmJPFfs3VVPdnj5wMzE2dS0sR48Oblk7aA4rx3zJdD3vsbMxugYuqeno39PEJH%2BAydYZGYwTYoL52xEOt92qTS2xWi5FbHG30SulyeXUKO2lknpcmA3KdzeAm6v1XOPzNpgh2K82N%2BHbdoKSVpSa1fmvmcyzSH4ViUoYyI6FJ5mjxj3iSwXgvYoh73OoN%2B9LNQm%2FRD%2FybizlKs1eHLAMzJgcZRxM6XeLd5HjekV1yztuxMELfWluyyD%2F3GVOK8J5crspbJ85tMC9izBa5ZQyeVj1N7HXLJ%2BUhXOcYa1tQj%2FybBtuDmMNrHVMKOiS4Lxq7IBD5bJnnIDKVrlMKOIJQo5XpQ3emTr0EDkKx61gV33tceXCtZ7NukGQoiuDMN6jl%2BRffuUs5ZV5QwOTMP0J8u8t9hGRLXb%2FjoWJfe%2FnJpI3AKcDIsGFyxLpp9fFkRxnEZ9kAPImC00esgEODElnCMjHW9xvFg4AN8HSK71uMIWy8c4GOqUBn3j4U%2FwADlPeTkUmSDOY1xcedkRAdDQbL3wB01GfMaCWLqfVBjJ7ZymAXr6V4tZqIYYoQ0G4I7A0ulBqxC3ULyim2a8PNnyotFYKQlzYU%2B8f1ARt5FCFzxsSAUYi2BbxxmMNV9rDfj5ZBoE%2BRFHiQyBcgRzomyksKBoRSxgq23ckYxFs8zz8scaPaJphEZYxpzbF2C051eEPEHKILxhOuWHz1cxU&X-Amz-Signature=2df130a86851bfcf9d225a4133efd494eca5951c2bae6105dd36301268301d78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJBUBECE%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOu3%2F6Gt%2FcYmwFuVkZYbxSBRuzoxklzKH2%2FUSHS0A%2B2AiEA7aGosdEvD3lyfF6mIqAYGv0gST8%2FgVhvX%2FEQIAJsK5Mq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDHzJmE3oTuwGyNhv2CrcA03i7ETW5ki5x%2FfryCQTtnxD5xxfWPisfHRfi840QTINXuFMkisaSS9ka7YqM6EEiXXcjQtV2wksajU27hI1ZHkIIzCMKI7FLEmsj67HRaRSqyR3rbU0aHxUsrVNxD3IuO45grrRtf3qq5qUjq9MLmJPFfs3VVPdnj5wMzE2dS0sR48Oblk7aA4rx3zJdD3vsbMxugYuqeno39PEJH%2BAydYZGYwTYoL52xEOt92qTS2xWi5FbHG30SulyeXUKO2lknpcmA3KdzeAm6v1XOPzNpgh2K82N%2BHbdoKSVpSa1fmvmcyzSH4ViUoYyI6FJ5mjxj3iSwXgvYoh73OoN%2B9LNQm%2FRD%2FybizlKs1eHLAMzJgcZRxM6XeLd5HjekV1yztuxMELfWluyyD%2F3GVOK8J5crspbJ85tMC9izBa5ZQyeVj1N7HXLJ%2BUhXOcYa1tQj%2FybBtuDmMNrHVMKOiS4Lxq7IBD5bJnnIDKVrlMKOIJQo5XpQ3emTr0EDkKx61gV33tceXCtZ7NukGQoiuDMN6jl%2BRffuUs5ZV5QwOTMP0J8u8t9hGRLXb%2FjoWJfe%2FnJpI3AKcDIsGFyxLpp9fFkRxnEZ9kAPImC00esgEODElnCMjHW9xvFg4AN8HSK71uMIWy8c4GOqUBn3j4U%2FwADlPeTkUmSDOY1xcedkRAdDQbL3wB01GfMaCWLqfVBjJ7ZymAXr6V4tZqIYYoQ0G4I7A0ulBqxC3ULyim2a8PNnyotFYKQlzYU%2B8f1ARt5FCFzxsSAUYi2BbxxmMNV9rDfj5ZBoE%2BRFHiQyBcgRzomyksKBoRSxgq23ckYxFs8zz8scaPaJphEZYxpzbF2C051eEPEHKILxhOuWHz1cxU&X-Amz-Signature=8362592be80a9f8563178be76fbf4d2a9246b5d69ae9b78a0ca0b30801cfd13e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJBUBECE%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOu3%2F6Gt%2FcYmwFuVkZYbxSBRuzoxklzKH2%2FUSHS0A%2B2AiEA7aGosdEvD3lyfF6mIqAYGv0gST8%2FgVhvX%2FEQIAJsK5Mq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDHzJmE3oTuwGyNhv2CrcA03i7ETW5ki5x%2FfryCQTtnxD5xxfWPisfHRfi840QTINXuFMkisaSS9ka7YqM6EEiXXcjQtV2wksajU27hI1ZHkIIzCMKI7FLEmsj67HRaRSqyR3rbU0aHxUsrVNxD3IuO45grrRtf3qq5qUjq9MLmJPFfs3VVPdnj5wMzE2dS0sR48Oblk7aA4rx3zJdD3vsbMxugYuqeno39PEJH%2BAydYZGYwTYoL52xEOt92qTS2xWi5FbHG30SulyeXUKO2lknpcmA3KdzeAm6v1XOPzNpgh2K82N%2BHbdoKSVpSa1fmvmcyzSH4ViUoYyI6FJ5mjxj3iSwXgvYoh73OoN%2B9LNQm%2FRD%2FybizlKs1eHLAMzJgcZRxM6XeLd5HjekV1yztuxMELfWluyyD%2F3GVOK8J5crspbJ85tMC9izBa5ZQyeVj1N7HXLJ%2BUhXOcYa1tQj%2FybBtuDmMNrHVMKOiS4Lxq7IBD5bJnnIDKVrlMKOIJQo5XpQ3emTr0EDkKx61gV33tceXCtZ7NukGQoiuDMN6jl%2BRffuUs5ZV5QwOTMP0J8u8t9hGRLXb%2FjoWJfe%2FnJpI3AKcDIsGFyxLpp9fFkRxnEZ9kAPImC00esgEODElnCMjHW9xvFg4AN8HSK71uMIWy8c4GOqUBn3j4U%2FwADlPeTkUmSDOY1xcedkRAdDQbL3wB01GfMaCWLqfVBjJ7ZymAXr6V4tZqIYYoQ0G4I7A0ulBqxC3ULyim2a8PNnyotFYKQlzYU%2B8f1ARt5FCFzxsSAUYi2BbxxmMNV9rDfj5ZBoE%2BRFHiQyBcgRzomyksKBoRSxgq23ckYxFs8zz8scaPaJphEZYxpzbF2C051eEPEHKILxhOuWHz1cxU&X-Amz-Signature=4e93aca0b4d044b0402c76c823aaa016d892ec27de237b07679af24598af930c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

