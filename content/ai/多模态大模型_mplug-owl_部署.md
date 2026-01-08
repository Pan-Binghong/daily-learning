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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XQW6AJ7%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRl8hSKpTsJGzWfrF7CmR4xkT0%2FcVPK13Lua5WHMNXyAIgDmUKVmw41aDBbd8H8KovjiORRjCMG9FFucvdU5FpjZsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBO%2B1ecU%2FdFRxlYKxCrcA1wmajkentjzSW6aXjGfjVfLEDpbeJJo8ywHEwQn40cWFCWALDg%2Ffqney4DKdW2x4y2OC2voPgzdpys45Z%2FENCSFs1FUPbwAejJhRGC%2B4RZ7kMddex6cyFaEQJ6XKosIpSYMbHPbHkpXrrkHLGF3iY%2FELmOjR9T931dzrswx%2BSJRbFcgxqNNqYkdxIVpglLPltT%2FbOcx1Wzq%2B3szoc7plrIasgs0s9MS7SuxfmJEfoqBaBv%2FVkIF0W%2BsC2vfcyEE3GOkK1l%2FohWtskG6TKKg9Fctio4QjQtVj0HUYN8tPQTHt4iBRtC45Jhm4bBTxDB8OErYdol7of95y86Ls9eNLRUIxJGvQNkhCH7UVLCe1fu2QW9kiZz%2F5hPaukxVAGzDxQVSS0CK30rIbiG5GJWyYyohXxhgUPabpJP54CYCSIV5w%2FeQSTEJVAlZDIcQ79zlLtZmqrYcgpDbahnYKvSJPCdCASgqxIx%2FrD5eyuL0A0MkIAA3rJV%2BcgnZltM5UNL1HjacDOImhqUafklKn4QDGDqvvUv3BUUYZfaWrpFfV2%2B69LIkKf5g8%2Fnr32xqNjeAuhWu0tfTuNRuUGevMHFcXKgaUR%2B5V05TObKOTUvRG18hNJC9YsY7ejG4ijshMIap%2FMoGOqUBpiFnGbseQ09Elx9uDZGcvMIeSvYYShb8ltVMwj9pjlGhNNGAuhMLoUBImfO37NRD5OyytjWl9H1QyuFduHphnE3xhMd5RVKwqrpd9OumJno%2FMSnHy5mYFggudf%2B29N0NZvIueRoCDxHVA4VllB0%2FuKMExVdquwrMu3gWfdNEpwbt3JEAqgOq7JA4F7jVXCac70bC6dmdIUHAQUoD9inhjZRdXlgq&X-Amz-Signature=3a573173abc4884440a4ae2a4b155d5af4816fbbc175f6d2f8ce608104b53d98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XQW6AJ7%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRl8hSKpTsJGzWfrF7CmR4xkT0%2FcVPK13Lua5WHMNXyAIgDmUKVmw41aDBbd8H8KovjiORRjCMG9FFucvdU5FpjZsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBO%2B1ecU%2FdFRxlYKxCrcA1wmajkentjzSW6aXjGfjVfLEDpbeJJo8ywHEwQn40cWFCWALDg%2Ffqney4DKdW2x4y2OC2voPgzdpys45Z%2FENCSFs1FUPbwAejJhRGC%2B4RZ7kMddex6cyFaEQJ6XKosIpSYMbHPbHkpXrrkHLGF3iY%2FELmOjR9T931dzrswx%2BSJRbFcgxqNNqYkdxIVpglLPltT%2FbOcx1Wzq%2B3szoc7plrIasgs0s9MS7SuxfmJEfoqBaBv%2FVkIF0W%2BsC2vfcyEE3GOkK1l%2FohWtskG6TKKg9Fctio4QjQtVj0HUYN8tPQTHt4iBRtC45Jhm4bBTxDB8OErYdol7of95y86Ls9eNLRUIxJGvQNkhCH7UVLCe1fu2QW9kiZz%2F5hPaukxVAGzDxQVSS0CK30rIbiG5GJWyYyohXxhgUPabpJP54CYCSIV5w%2FeQSTEJVAlZDIcQ79zlLtZmqrYcgpDbahnYKvSJPCdCASgqxIx%2FrD5eyuL0A0MkIAA3rJV%2BcgnZltM5UNL1HjacDOImhqUafklKn4QDGDqvvUv3BUUYZfaWrpFfV2%2B69LIkKf5g8%2Fnr32xqNjeAuhWu0tfTuNRuUGevMHFcXKgaUR%2B5V05TObKOTUvRG18hNJC9YsY7ejG4ijshMIap%2FMoGOqUBpiFnGbseQ09Elx9uDZGcvMIeSvYYShb8ltVMwj9pjlGhNNGAuhMLoUBImfO37NRD5OyytjWl9H1QyuFduHphnE3xhMd5RVKwqrpd9OumJno%2FMSnHy5mYFggudf%2B29N0NZvIueRoCDxHVA4VllB0%2FuKMExVdquwrMu3gWfdNEpwbt3JEAqgOq7JA4F7jVXCac70bC6dmdIUHAQUoD9inhjZRdXlgq&X-Amz-Signature=d7936483fc6b4b4e7550bd3881cb05029397013d9455389e85fb9a2a9b112bc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

