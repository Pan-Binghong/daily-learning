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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2S4P3A%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4GB4YvLFIpQrcTs4I2pcRSf7d6%2FYt5B9xWbeb8uIYfAiAEna6eBIR6XZc0oSSRWEJdFj2QVDPTRFET%2FR41GGIQMiqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1%2FJZtG6eWjsRiEH4KtwD69qz8GVTJSFoBri66i%2BIvcAR4UhYeloijA7brZQu0xeuq8tGeie65cFnc38jbBPUMX5Dz01fCEbj7UNHGJrszMZv64rWTvzAp4Jm3jkCf1nAuI693x2LJl%2FrklrVvQ3TQRcNlRrZV0rOZOeiN6BpB9Su0dRk6Xp89mzNA2H%2F7geXU1SfHG5%2FZhrg%2BuOTdRO3bQE0sEGJxo2lVnOSyMM1nGHjbxkCZ2%2BkgZTa3hR0zvFYFI%2BI8%2FPS1Oo4nuR5fPYDRP%2BnI388FZYeCKtTmAydk6wX9q22k6WoGebt5eYqiMSp56yHtRfLr2NKE7j7gRY6yVI5Ax3Y59zTRm8Rj%2FERnUbP61OOKLZAtAZw1%2F4IAUQg6EVRnQd7RtC1UhjZm5zIO0059L5G1U1FtbdVm%2BA2gMrEDG3o2DNPgJxtDKNwREZjHRFZBWLDxJaWUua0eYQOfFUTPUfl02Th3o%2BMUpIgAXwK1ZtyQWJVxAcvTIq3sNYSPJb9knFjVIc38ZDKz59d1m8rdriWafg5Z3qwg9PdM5WDBwA30u6U5OyX9ndkeG%2ByfFmFdTMtCPQtWESiKk7WeM4ulQdPUKqfr6gpOVg9cz2sSovBQ5p4dNdlSxSSu4PKalR0dNNGos2QJX4wj5apyQY6pgFNgubL5ej%2BO3qEPTFessGudYJTnGQcKnHoRmYV6C%2FhSnCsnoIOFhQbl4wRoh%2B%2F%2FTi3%2FwtLgFCHt8olsFD%2FSPwMofAWqN4le9X5BgvC4ufC5TptjGdyXuv5aRClz8Hxnt%2BUlC6ZArdTGWzQhOpyH3TQqGhWsMMrC9PniaxokLhYzGKDYXr%2B%2BeywEBrvEakQo%2FFLkPj5dozLb5WL5NnDUjNTWy%2BBXJEC&X-Amz-Signature=2af1f671d50e76193f873286d6d01a35d22e4b51f7b99dbe652cf5a460135aa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB2S4P3A%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4GB4YvLFIpQrcTs4I2pcRSf7d6%2FYt5B9xWbeb8uIYfAiAEna6eBIR6XZc0oSSRWEJdFj2QVDPTRFET%2FR41GGIQMiqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1%2FJZtG6eWjsRiEH4KtwD69qz8GVTJSFoBri66i%2BIvcAR4UhYeloijA7brZQu0xeuq8tGeie65cFnc38jbBPUMX5Dz01fCEbj7UNHGJrszMZv64rWTvzAp4Jm3jkCf1nAuI693x2LJl%2FrklrVvQ3TQRcNlRrZV0rOZOeiN6BpB9Su0dRk6Xp89mzNA2H%2F7geXU1SfHG5%2FZhrg%2BuOTdRO3bQE0sEGJxo2lVnOSyMM1nGHjbxkCZ2%2BkgZTa3hR0zvFYFI%2BI8%2FPS1Oo4nuR5fPYDRP%2BnI388FZYeCKtTmAydk6wX9q22k6WoGebt5eYqiMSp56yHtRfLr2NKE7j7gRY6yVI5Ax3Y59zTRm8Rj%2FERnUbP61OOKLZAtAZw1%2F4IAUQg6EVRnQd7RtC1UhjZm5zIO0059L5G1U1FtbdVm%2BA2gMrEDG3o2DNPgJxtDKNwREZjHRFZBWLDxJaWUua0eYQOfFUTPUfl02Th3o%2BMUpIgAXwK1ZtyQWJVxAcvTIq3sNYSPJb9knFjVIc38ZDKz59d1m8rdriWafg5Z3qwg9PdM5WDBwA30u6U5OyX9ndkeG%2ByfFmFdTMtCPQtWESiKk7WeM4ulQdPUKqfr6gpOVg9cz2sSovBQ5p4dNdlSxSSu4PKalR0dNNGos2QJX4wj5apyQY6pgFNgubL5ej%2BO3qEPTFessGudYJTnGQcKnHoRmYV6C%2FhSnCsnoIOFhQbl4wRoh%2B%2F%2FTi3%2FwtLgFCHt8olsFD%2FSPwMofAWqN4le9X5BgvC4ufC5TptjGdyXuv5aRClz8Hxnt%2BUlC6ZArdTGWzQhOpyH3TQqGhWsMMrC9PniaxokLhYzGKDYXr%2B%2BeywEBrvEakQo%2FFLkPj5dozLb5WL5NnDUjNTWy%2BBXJEC&X-Amz-Signature=5293d14e8e6117d6f6cabcdcb80ec8a91d26dc414a1f540c78e9de9bb417ca3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

