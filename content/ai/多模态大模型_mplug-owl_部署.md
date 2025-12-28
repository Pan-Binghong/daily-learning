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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676E66KWM%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoozJGDFqfuKrVAUjYSHtAB1XIvheNIrtHG%2FYIPexpRwIhAPQkAQFrDKbs70fiSvazapmwR0TWNkWnkHVyjMaI3sqJKv8DCHsQABoMNjM3NDIzMTgzODA1IgwVHKVJy869fvfgD5wq3APv2nVhzZeGRg5VMGt0xVaJIX8Yu6TVrGHMJOJkoxW%2FAjndCLYWZek3AHSrMevCflgZc53tt%2BcJ5FQ5d9rQqnD9yGzhY1qrZgDDjoQIXmrTx90GJCWCC2BqjNGu2Laxp%2B10w4t51T04%2BClX2l%2BLUlngRsUb2vIeHrRsek4ij71QQt2s3YxuSSj93w5POFARHkPPzzeme141GDMcGavU%2FxKS15cGZmGHtMnQLmE%2BnKerYh2wjuPqiBwFpJPhbz6cm6BMk41uJqG0LKPo4EZ69YFc3QYyF1kxm8UE0B0ychRIHDWJLcgHr%2F3abry3zKuGlW%2Fd8V7LvPzWu8eObXFvScJljCgki9fKrzoXKqXh7T%2FnK2dnGOm3Ql3sqFKDoxLJnF4vT%2B64UvT9%2Fb1YLf%2BFDGhPBhfZEaQkMIZ1U0TaPlj8H2sjp7F%2FwkJ0r5myr2eGzRPwWNzMViGtRjJxKXyiYZdaxfmmRMyhqHDjgWfrYS94Q9MuEettJssWGD61E5dRtXpscE9YgYsFuqxqQzXyoV3hSRB1faWa4tgcHMkoVMhnsI%2F%2F3r5x2TWQoz83%2B1Xwq%2FrUrZclFRRJlZQKO875vh4MU62XN7Mk4CkLl6J6aM2fgMawvL2ifUSfCQ4fxDCOosLKBjqkAbSENXx7v6cgYjRmAiZJNN0ptAcx%2BsD%2BwlrEgopmjY5cj%2FIvf80i6Uc7QCfwxpRtg3B%2BimINz0J0jkcRzllKtWdHel3jYdCyGqVPrUCgCP8GX5PhJXwr6pdWtmmTP338LwZZBV28t%2FmFWrxZiAuWEFzuVXReBukrM5BAOtpsHWsVYAa7sJSyPNBvZFUrcRto8X5tgPPdz3DoBWGN2dos1jpp6Alu&X-Amz-Signature=01a1182aec1c1c3d46cd20cfc5085b21b538ba417eb65c1e6218f689287565cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676E66KWM%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoozJGDFqfuKrVAUjYSHtAB1XIvheNIrtHG%2FYIPexpRwIhAPQkAQFrDKbs70fiSvazapmwR0TWNkWnkHVyjMaI3sqJKv8DCHsQABoMNjM3NDIzMTgzODA1IgwVHKVJy869fvfgD5wq3APv2nVhzZeGRg5VMGt0xVaJIX8Yu6TVrGHMJOJkoxW%2FAjndCLYWZek3AHSrMevCflgZc53tt%2BcJ5FQ5d9rQqnD9yGzhY1qrZgDDjoQIXmrTx90GJCWCC2BqjNGu2Laxp%2B10w4t51T04%2BClX2l%2BLUlngRsUb2vIeHrRsek4ij71QQt2s3YxuSSj93w5POFARHkPPzzeme141GDMcGavU%2FxKS15cGZmGHtMnQLmE%2BnKerYh2wjuPqiBwFpJPhbz6cm6BMk41uJqG0LKPo4EZ69YFc3QYyF1kxm8UE0B0ychRIHDWJLcgHr%2F3abry3zKuGlW%2Fd8V7LvPzWu8eObXFvScJljCgki9fKrzoXKqXh7T%2FnK2dnGOm3Ql3sqFKDoxLJnF4vT%2B64UvT9%2Fb1YLf%2BFDGhPBhfZEaQkMIZ1U0TaPlj8H2sjp7F%2FwkJ0r5myr2eGzRPwWNzMViGtRjJxKXyiYZdaxfmmRMyhqHDjgWfrYS94Q9MuEettJssWGD61E5dRtXpscE9YgYsFuqxqQzXyoV3hSRB1faWa4tgcHMkoVMhnsI%2F%2F3r5x2TWQoz83%2B1Xwq%2FrUrZclFRRJlZQKO875vh4MU62XN7Mk4CkLl6J6aM2fgMawvL2ifUSfCQ4fxDCOosLKBjqkAbSENXx7v6cgYjRmAiZJNN0ptAcx%2BsD%2BwlrEgopmjY5cj%2FIvf80i6Uc7QCfwxpRtg3B%2BimINz0J0jkcRzllKtWdHel3jYdCyGqVPrUCgCP8GX5PhJXwr6pdWtmmTP338LwZZBV28t%2FmFWrxZiAuWEFzuVXReBukrM5BAOtpsHWsVYAa7sJSyPNBvZFUrcRto8X5tgPPdz3DoBWGN2dos1jpp6Alu&X-Amz-Signature=2ad41489a07a04d7b53af3c987bf970fff823a4a595c832958374ab5495a0da3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

