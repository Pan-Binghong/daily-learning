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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3JG2X2E%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQClmJi9Iz1WoQzg0%2FwSeo%2Bri7wvtWGxEIGIlYyTM69zmQIhAK0PNHOFVFHKLBRUZF9djI9uue9mn71yiHRzO3xGk3PlKv8DCBwQABoMNjM3NDIzMTgzODA1IgwFc9wN8u4v27hL3xoq3AP95NSHZoMumDjtFf%2Fjv%2Bo5OcV2wJOHncSr9yQ%2F2k81AS4slSM9gacCiNdF9Em0heAMlg98oDcgPfwi5YEMEPfRlEr2tgI1tjREg7vs2617mGbf0tAm1qHX1zlcSqvO9ei9%2FxbjdkCLIVksSwkRfAwyNJzbpLlXI0ZOta%2FZB4hXMCujUEHqsK%2F4bs7TfsqYZF0JsZmoq2PNUrxUi2oVh5845%2FMh3XUcd0DFtdtDbs02rzMwy54jl1pRMio3T1OkSGP%2BxkeZyUQeECjZpCiFbV3qrbBaMYClYJc8TDOUvPIRlMrRUaAnykH0BdnrhFqqC3fsr%2B4ElBzMUVrWpFkxIgPhqbBcjp3yeJwIcFSb1fMn4eOvdSatE9yUrxObWdqV6W2o43HtRL8%2FNyCKxAEnl5WTzglPh6Sqei6BPFvaHi2c7Bd0vXQcde9%2Fl5kWoxrEbfCqXTsVI0Rj27%2F36oNUEvgdrGRzjMy1Jksb1RhucwJWeUUf0IjBN8HCRKpS2FIiT2MXVDtxQttWLTV7UcSPiosyP66ZZ7fTIul68Ik4bhn2pJlDhCNfMG3ig6%2B4dU3AcCQaee%2FDPR3Ao79E1%2FVSq%2BUWuC481yNcT6lGM1vpE%2BvX%2BH4A9irn3eQLgiLmbjDe9f7MBjqkAdRJnW5cv6xiESs%2F2vaQleE8oN2TmvZEyQ0Iw9662S%2FGQ6tu7httVNWFftFN36La0cIY2XEkw9krpD82uopuCSmvg6vepgcg82oMdEtrRq4%2BTi9M42mTkk1rBUg%2B2I8QAOiL6GWyVsOwukXRWUhFpzOsXAEU1ccshInNqB%2FjZ2NFUCl9Y3m%2F1Zr9LcB50j6K2Vq69kf0k%2FLy08hHGwrsO1OA2q8d&X-Amz-Signature=a1181554ffca2ea62a5092149450c2f8ca3f8f65e788e6fa9e25295de1d7f10a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3JG2X2E%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQClmJi9Iz1WoQzg0%2FwSeo%2Bri7wvtWGxEIGIlYyTM69zmQIhAK0PNHOFVFHKLBRUZF9djI9uue9mn71yiHRzO3xGk3PlKv8DCBwQABoMNjM3NDIzMTgzODA1IgwFc9wN8u4v27hL3xoq3AP95NSHZoMumDjtFf%2Fjv%2Bo5OcV2wJOHncSr9yQ%2F2k81AS4slSM9gacCiNdF9Em0heAMlg98oDcgPfwi5YEMEPfRlEr2tgI1tjREg7vs2617mGbf0tAm1qHX1zlcSqvO9ei9%2FxbjdkCLIVksSwkRfAwyNJzbpLlXI0ZOta%2FZB4hXMCujUEHqsK%2F4bs7TfsqYZF0JsZmoq2PNUrxUi2oVh5845%2FMh3XUcd0DFtdtDbs02rzMwy54jl1pRMio3T1OkSGP%2BxkeZyUQeECjZpCiFbV3qrbBaMYClYJc8TDOUvPIRlMrRUaAnykH0BdnrhFqqC3fsr%2B4ElBzMUVrWpFkxIgPhqbBcjp3yeJwIcFSb1fMn4eOvdSatE9yUrxObWdqV6W2o43HtRL8%2FNyCKxAEnl5WTzglPh6Sqei6BPFvaHi2c7Bd0vXQcde9%2Fl5kWoxrEbfCqXTsVI0Rj27%2F36oNUEvgdrGRzjMy1Jksb1RhucwJWeUUf0IjBN8HCRKpS2FIiT2MXVDtxQttWLTV7UcSPiosyP66ZZ7fTIul68Ik4bhn2pJlDhCNfMG3ig6%2B4dU3AcCQaee%2FDPR3Ao79E1%2FVSq%2BUWuC481yNcT6lGM1vpE%2BvX%2BH4A9irn3eQLgiLmbjDe9f7MBjqkAdRJnW5cv6xiESs%2F2vaQleE8oN2TmvZEyQ0Iw9662S%2FGQ6tu7httVNWFftFN36La0cIY2XEkw9krpD82uopuCSmvg6vepgcg82oMdEtrRq4%2BTi9M42mTkk1rBUg%2B2I8QAOiL6GWyVsOwukXRWUhFpzOsXAEU1ccshInNqB%2FjZ2NFUCl9Y3m%2F1Zr9LcB50j6K2Vq69kf0k%2FLy08hHGwrsO1OA2q8d&X-Amz-Signature=3c6f49ff5a487a4335f88acdd83a89a77dab72ca5b244ede5ae4bbd9a35f143f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

