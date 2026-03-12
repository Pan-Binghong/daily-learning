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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z5REHSP%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIASkhONNV8ZZaGHvj5ijmsbUEbkBbAMOUzgEAXt6r3IVAiEAyvilCu7GiTN9fiNGXSiTOZB%2Bb%2Bz6ylUhCvOSscFKgPYq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDH5WGfT%2FqJ8Aks5xUSrcA1ogkdsQkUSmhzk7TXXjXj3SZ0P7ikAvWhkHuk9B%2Bq6ezas8nAYdclvpUnr4Z3gqacVlgYxQA5W%2BavVqtEE4m6ECw%2FlFLDcba0KY5D8IWJ4AlYQNj%2FFVLfM1RqruiZdvSOQ3BpTO1b0R19CGA9mMPHfMctIut9%2FehAFVxztrOmILOJLq08Upk2nNImbjNPPFxxJqHf7dp73YPioaIdyphUJVcO5b%2BWxP75RsS%2BjYRpKmXvaQ5c1Wgk75riDgzXSEjFb9GyPAisMudt97Ygo%2FO%2BBhTf%2B6IMdnK%2BzCY2WvIGn64lvSxWO%2BldgXMgIDP1U0UEyO1fKnLQJO3OYiiGzHT6w8tG0zO5qvCnFdhXaKMb6zuUsOfPP1N2fnfNLqN5d%2FfnfFGfO1AxeXe9xsrR3ywSo3eZi7YXUZUz6VKc5ii5O8kri2l4kaCf%2FfECzZ6NmdRAMntdUBsTuEk5oSAmcYzcAlW%2BVG8w%2FQU7kl%2BAfRfP%2F7Vn4C9Ob5LdtolgboLtV0Kic4VxcL5Cqdm8NiekNJ%2FMDiuwYFtwCd0dWiiJBiZ%2FXTilRIb357%2FIHnEgqfCHXFM3rP2dtNbxSid93qhAqP4SR363nLMdpLA78PoSr1yO3pSKMJ%2FF6CzoHFMU3cMKiyyM0GOqUBmF6LM%2FXXdm%2FdSDzEvP8ryzvSRNgt8C4gwFIhYt90WP5mc9YAp36MLrF0awDXCuQCfpDNZk65i%2F9gSyaZWKfeY%2BD9OYiyqJoEs%2Bf2E7%2BMYyjder8tX%2BTX2lb4AQdDoNNC4SMaOV8kBFVSAtuFCDrV7ii1zR9MOa2FV2njCOLUKuZKP9npwen83RTwXbJbKV6%2B8gB6TAMwnx00X0Hz0KnUToDe3Huc&X-Amz-Signature=ba8ce68e71e18ff9a605959da253ffef9207fb786d9ae1e8276d9df3a6547cdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z5REHSP%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIASkhONNV8ZZaGHvj5ijmsbUEbkBbAMOUzgEAXt6r3IVAiEAyvilCu7GiTN9fiNGXSiTOZB%2Bb%2Bz6ylUhCvOSscFKgPYq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDH5WGfT%2FqJ8Aks5xUSrcA1ogkdsQkUSmhzk7TXXjXj3SZ0P7ikAvWhkHuk9B%2Bq6ezas8nAYdclvpUnr4Z3gqacVlgYxQA5W%2BavVqtEE4m6ECw%2FlFLDcba0KY5D8IWJ4AlYQNj%2FFVLfM1RqruiZdvSOQ3BpTO1b0R19CGA9mMPHfMctIut9%2FehAFVxztrOmILOJLq08Upk2nNImbjNPPFxxJqHf7dp73YPioaIdyphUJVcO5b%2BWxP75RsS%2BjYRpKmXvaQ5c1Wgk75riDgzXSEjFb9GyPAisMudt97Ygo%2FO%2BBhTf%2B6IMdnK%2BzCY2WvIGn64lvSxWO%2BldgXMgIDP1U0UEyO1fKnLQJO3OYiiGzHT6w8tG0zO5qvCnFdhXaKMb6zuUsOfPP1N2fnfNLqN5d%2FfnfFGfO1AxeXe9xsrR3ywSo3eZi7YXUZUz6VKc5ii5O8kri2l4kaCf%2FfECzZ6NmdRAMntdUBsTuEk5oSAmcYzcAlW%2BVG8w%2FQU7kl%2BAfRfP%2F7Vn4C9Ob5LdtolgboLtV0Kic4VxcL5Cqdm8NiekNJ%2FMDiuwYFtwCd0dWiiJBiZ%2FXTilRIb357%2FIHnEgqfCHXFM3rP2dtNbxSid93qhAqP4SR363nLMdpLA78PoSr1yO3pSKMJ%2FF6CzoHFMU3cMKiyyM0GOqUBmF6LM%2FXXdm%2FdSDzEvP8ryzvSRNgt8C4gwFIhYt90WP5mc9YAp36MLrF0awDXCuQCfpDNZk65i%2F9gSyaZWKfeY%2BD9OYiyqJoEs%2Bf2E7%2BMYyjder8tX%2BTX2lb4AQdDoNNC4SMaOV8kBFVSAtuFCDrV7ii1zR9MOa2FV2njCOLUKuZKP9npwen83RTwXbJbKV6%2B8gB6TAMwnx00X0Hz0KnUToDe3Huc&X-Amz-Signature=a6e807f2cdf87f19b53a42d331c8ba3d6e225130a7aeb42c181c9d1a58fe7925&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

