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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GFXLAWF%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNmU%2F81XMKQW7YDzEhoiDONWJ03e9QGO7uZgpVhJDWBAiAm9p7%2BsUbS2fhSAvekUnZyfcJbR5z7ChllOF%2F0tJvpXyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzO9KkZTr8ccbkpauKtwDo2KwEFS4v0tEZ6cFWsoz05Dw64eudDWMd9yfNqDJzxq3X1T7t0TTnUM8%2FFuzVQDLwhy6gTZ%2BJw5KXJwGBYjo0Og692Jsm%2FquWf10USG%2Bvx5DqTUyAVubNCQ%2FZPMrOwruZAER2n%2Ft1Wix8Qk9YRctRd1gtK%2BzaGmF%2FG0ThcwJQlwp10GoIh1r1xArxymMAlX7v794u57%2BMJ8su3fZ7%2BTMhQrDOj6rToGasInKaqo5BxtiS1Bg46WW%2BdmaxJ5deeUOaVKaaRE6TgALWKHmDA3eGOXl0rIg61tgJPyIbvpHO%2Bg53JEDYDMhimaS4nJo7QiT3dHDJwdyNlPOJ0bAK%2FIrvf09RIS8IfrdSh0m%2B09%2Br8e%2BXhyHJwAQoJm5dNJW2s3f9lykhEJlxIygILHFnXisiaKEhgTYKP1jLzv2LOCc6Io9AvCTB7ZECIbFIgVWW162q%2BBuxqwaYRGrEJthJhFi59dwDTawP4KlUAUsUP68HiCzaNgsx6ne19uqzD1d1OOrQRVBF9D3%2BDu1DJZi7Dn2RBnJ%2BKhkW75uyFok%2BSFw0RRsMLQZXeH%2BBJwvzJAyxwGUAbby%2Fh6Q9TpUKTxvGL1717pB3ssfuN9LMNPwWFmc8IxSlvbrR7HA1r0pFy8w2P3SyQY6pgGgLMywZEBmcfgtjZrGOPen9HYiyfQX49SfIWyedxCAE7hFq2Fa9%2FD%2BjiQbVFMcq9RtcnwONvd%2FJf0XuooG3%2BqolV7xAOVgKGkXhvBSOYb6MewDAQdsC9Su7etkDijPDyZmd%2B8Fft%2BC8JD2yL9Ts74GJOs%2FCMB7zbtxzb5lzusa8ovuujx47YwMqSNi1QwBo7NrnrUiZIneZGt6L34qNhytFLzsiK67&X-Amz-Signature=a2d135fb37db175ec7c991c88a66ae20cfb81cd22b96b8d321445a40ddb03423&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GFXLAWF%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICNmU%2F81XMKQW7YDzEhoiDONWJ03e9QGO7uZgpVhJDWBAiAm9p7%2BsUbS2fhSAvekUnZyfcJbR5z7ChllOF%2F0tJvpXyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzO9KkZTr8ccbkpauKtwDo2KwEFS4v0tEZ6cFWsoz05Dw64eudDWMd9yfNqDJzxq3X1T7t0TTnUM8%2FFuzVQDLwhy6gTZ%2BJw5KXJwGBYjo0Og692Jsm%2FquWf10USG%2Bvx5DqTUyAVubNCQ%2FZPMrOwruZAER2n%2Ft1Wix8Qk9YRctRd1gtK%2BzaGmF%2FG0ThcwJQlwp10GoIh1r1xArxymMAlX7v794u57%2BMJ8su3fZ7%2BTMhQrDOj6rToGasInKaqo5BxtiS1Bg46WW%2BdmaxJ5deeUOaVKaaRE6TgALWKHmDA3eGOXl0rIg61tgJPyIbvpHO%2Bg53JEDYDMhimaS4nJo7QiT3dHDJwdyNlPOJ0bAK%2FIrvf09RIS8IfrdSh0m%2B09%2Br8e%2BXhyHJwAQoJm5dNJW2s3f9lykhEJlxIygILHFnXisiaKEhgTYKP1jLzv2LOCc6Io9AvCTB7ZECIbFIgVWW162q%2BBuxqwaYRGrEJthJhFi59dwDTawP4KlUAUsUP68HiCzaNgsx6ne19uqzD1d1OOrQRVBF9D3%2BDu1DJZi7Dn2RBnJ%2BKhkW75uyFok%2BSFw0RRsMLQZXeH%2BBJwvzJAyxwGUAbby%2Fh6Q9TpUKTxvGL1717pB3ssfuN9LMNPwWFmc8IxSlvbrR7HA1r0pFy8w2P3SyQY6pgGgLMywZEBmcfgtjZrGOPen9HYiyfQX49SfIWyedxCAE7hFq2Fa9%2FD%2BjiQbVFMcq9RtcnwONvd%2FJf0XuooG3%2BqolV7xAOVgKGkXhvBSOYb6MewDAQdsC9Su7etkDijPDyZmd%2B8Fft%2BC8JD2yL9Ts74GJOs%2FCMB7zbtxzb5lzusa8ovuujx47YwMqSNi1QwBo7NrnrUiZIneZGt6L34qNhytFLzsiK67&X-Amz-Signature=1d5f2e92afdb5af953cd47f2d20502e546d8ed63edf57f3162a69dc19f880ec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

