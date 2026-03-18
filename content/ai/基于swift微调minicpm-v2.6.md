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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPOBXJV%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDjwWEXE3zSw0I%2B32%2FNk1noQGLpmOULHwC%2B5t9xj122OAiBELyziv93i%2B0mp8r1urUV1VzG9bd%2BtXufTy58B%2FfMNLCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FA%2Fmm0e6obnk3os8KtwDCIBuamiVTpVj10vskZQ63LlZlTMhgVx9vSO%2Brt%2FIez9Sbmh8wuIchP1C4aNZ79ip3SEaVm8ORoEQy9u9yyQoTCY3aW6jZCmkO38Yhx1tWRoBdWnPNW6TfSv%2Bg5XBVrqH4MFKyeS7tU0xvbegan4y3eGki8h6wnji0weKrGTshK%2BRZD18qBxd%2FGPAktqBlORWLBlok6UQEX6ZYHQvJlKpNbjzxax1q8kUe8yxFGfUMw%2B6DFual1RKKtEBvSPv%2BSnFnQat0VieUIVfMh7ZWZ7g17U%2B3XjOzU5V5ikMc3GpYelg1f%2BIoFdJNBdXS4dT%2Ff44zZXADN7gEO5wENM773bL6QaYIaWhQVxYnZlF%2Bo94EifavJ%2Bid%2B%2BNfAxnCN8SfOA8tMOOTPLfL2sDoY2GU2wW2Cn%2F%2FhP2cxMF3nZikt%2FR0RrbcMiDCS3BQAjxE41yRjryzosIAdOfvVRgdI6xfGtr6w9hJm%2BR9eocd%2Ftw5adAyvp7XmqdMTLl9ipGz11ausN5ut9DC15AJc0P7Y6v1x%2FJJBxLP9WLexfC6t2J27pIico5xPOv8zOnoK%2BtlIWaDm6o8HcG7ejLOgCw1xT9bsX%2BYMplz5GR%2FWc82vOFeYwlpXR8JlGUhDJcu6MOWEUwj6bozQY6pgFU8qdCLRBJyZUPj5cM6Tsb7IrJ4%2FqvWZHiBLa2zN5zxrPDbTOL6SsZqnDBr5GEU8BR1HaCVLFBF3B2kFBSmyKH6gDwzc8Rz%2BEzFDh2TnNLnbYFtwWzAWKAnqfe1BWkYDa40nsmA46v5fgLCVJbDVc2QB2XLdeZOsP5GiicUIj%2BpdVy5Zx040BxivzYApgOx9Pe1hp%2FZKfygcS5cPv9hLDl8yr4afe8&X-Amz-Signature=a6b532423eb41bcdcf924c257b04e11648fdd4568509d0c4970b0ff4310bab8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPOBXJV%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDjwWEXE3zSw0I%2B32%2FNk1noQGLpmOULHwC%2B5t9xj122OAiBELyziv93i%2B0mp8r1urUV1VzG9bd%2BtXufTy58B%2FfMNLCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FA%2Fmm0e6obnk3os8KtwDCIBuamiVTpVj10vskZQ63LlZlTMhgVx9vSO%2Brt%2FIez9Sbmh8wuIchP1C4aNZ79ip3SEaVm8ORoEQy9u9yyQoTCY3aW6jZCmkO38Yhx1tWRoBdWnPNW6TfSv%2Bg5XBVrqH4MFKyeS7tU0xvbegan4y3eGki8h6wnji0weKrGTshK%2BRZD18qBxd%2FGPAktqBlORWLBlok6UQEX6ZYHQvJlKpNbjzxax1q8kUe8yxFGfUMw%2B6DFual1RKKtEBvSPv%2BSnFnQat0VieUIVfMh7ZWZ7g17U%2B3XjOzU5V5ikMc3GpYelg1f%2BIoFdJNBdXS4dT%2Ff44zZXADN7gEO5wENM773bL6QaYIaWhQVxYnZlF%2Bo94EifavJ%2Bid%2B%2BNfAxnCN8SfOA8tMOOTPLfL2sDoY2GU2wW2Cn%2F%2FhP2cxMF3nZikt%2FR0RrbcMiDCS3BQAjxE41yRjryzosIAdOfvVRgdI6xfGtr6w9hJm%2BR9eocd%2Ftw5adAyvp7XmqdMTLl9ipGz11ausN5ut9DC15AJc0P7Y6v1x%2FJJBxLP9WLexfC6t2J27pIico5xPOv8zOnoK%2BtlIWaDm6o8HcG7ejLOgCw1xT9bsX%2BYMplz5GR%2FWc82vOFeYwlpXR8JlGUhDJcu6MOWEUwj6bozQY6pgFU8qdCLRBJyZUPj5cM6Tsb7IrJ4%2FqvWZHiBLa2zN5zxrPDbTOL6SsZqnDBr5GEU8BR1HaCVLFBF3B2kFBSmyKH6gDwzc8Rz%2BEzFDh2TnNLnbYFtwWzAWKAnqfe1BWkYDa40nsmA46v5fgLCVJbDVc2QB2XLdeZOsP5GiicUIj%2BpdVy5Zx040BxivzYApgOx9Pe1hp%2FZKfygcS5cPv9hLDl8yr4afe8&X-Amz-Signature=35eef364a4d1e791fed566c7c33d87ae77c031beb022fb5e7aa775c203007084&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPOBXJV%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDjwWEXE3zSw0I%2B32%2FNk1noQGLpmOULHwC%2B5t9xj122OAiBELyziv93i%2B0mp8r1urUV1VzG9bd%2BtXufTy58B%2FfMNLCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FA%2Fmm0e6obnk3os8KtwDCIBuamiVTpVj10vskZQ63LlZlTMhgVx9vSO%2Brt%2FIez9Sbmh8wuIchP1C4aNZ79ip3SEaVm8ORoEQy9u9yyQoTCY3aW6jZCmkO38Yhx1tWRoBdWnPNW6TfSv%2Bg5XBVrqH4MFKyeS7tU0xvbegan4y3eGki8h6wnji0weKrGTshK%2BRZD18qBxd%2FGPAktqBlORWLBlok6UQEX6ZYHQvJlKpNbjzxax1q8kUe8yxFGfUMw%2B6DFual1RKKtEBvSPv%2BSnFnQat0VieUIVfMh7ZWZ7g17U%2B3XjOzU5V5ikMc3GpYelg1f%2BIoFdJNBdXS4dT%2Ff44zZXADN7gEO5wENM773bL6QaYIaWhQVxYnZlF%2Bo94EifavJ%2Bid%2B%2BNfAxnCN8SfOA8tMOOTPLfL2sDoY2GU2wW2Cn%2F%2FhP2cxMF3nZikt%2FR0RrbcMiDCS3BQAjxE41yRjryzosIAdOfvVRgdI6xfGtr6w9hJm%2BR9eocd%2Ftw5adAyvp7XmqdMTLl9ipGz11ausN5ut9DC15AJc0P7Y6v1x%2FJJBxLP9WLexfC6t2J27pIico5xPOv8zOnoK%2BtlIWaDm6o8HcG7ejLOgCw1xT9bsX%2BYMplz5GR%2FWc82vOFeYwlpXR8JlGUhDJcu6MOWEUwj6bozQY6pgFU8qdCLRBJyZUPj5cM6Tsb7IrJ4%2FqvWZHiBLa2zN5zxrPDbTOL6SsZqnDBr5GEU8BR1HaCVLFBF3B2kFBSmyKH6gDwzc8Rz%2BEzFDh2TnNLnbYFtwWzAWKAnqfe1BWkYDa40nsmA46v5fgLCVJbDVc2QB2XLdeZOsP5GiicUIj%2BpdVy5Zx040BxivzYApgOx9Pe1hp%2FZKfygcS5cPv9hLDl8yr4afe8&X-Amz-Signature=bc4a5b325ef617e4bb0cea87054d3fb59f5f9165da1b04aa853f2729b960530a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

