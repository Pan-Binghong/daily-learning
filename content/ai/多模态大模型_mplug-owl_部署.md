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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QKHJJBI%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk7qSGdVBP5ucwZdWzcQAHYUxdBYFzzYEFw2Sss8FRiAiEAtABOrYUqKnTKBY1O%2BebKd4OJ5d0Is8hY2D6Jl5rgW1Aq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDPz4MUnx8uCi6D3H7CrcAzhETGdBPPEV2RxYie0w%2BH9%2FP4ug9WYUJyaugpcWy2CdFPt4ymGzKM4E6fL6K%2Fw6iXk0AUZ06r8mFkATmLVHhqRjT2qnZXyX1xHfld3%2BZy4c%2Bv%2Bb%2B9%2BxVLi2Ei6ddMYujxQd2TI753JX9%2F2cjKuOpMruMCRADbFa93ioEF%2BB%2BAOCy5%2B0euds%2BAobpABZYYA9gP4TAcQT0UTnsji%2B9RKVSARKcJt%2FF54t6pXSsrqDmCA3mh26UiMS1iwmCs1UPJ3dJpnJhEvYpEXG4X1O%2B7PSE5hKF%2Bz9jk8V988CiElHNzw0vn1kbJHktLvq0BFC8BsgExHeGVjuA5EzmLSrtAQgjcn717g5rwMXG47hgFcRWR4u%2BqFKDik2VucTRlMTzznoBzreGODpdcmFtnMl3mk0RAlym4oponWJUJC8ToBz9RdTNQzjqtCjEiNd%2BPsAWSWDsTHtJkUxG%2BSBX8ZSW0StY1bl0NTdGYoIvVnlAbAzp3jMK9P41CillfLKuxk%2FqY4aFvg16i7mndIsO7Ls%2FAL%2F7%2FUbR2TowqwMpjPTml9IJLcV9X%2FRNO5f0cfnFFxz7yvW5v8RQUnvInSZDLA7oodcDGVUWvMB2Lz4lmMdtvEivZvXNEEVB4yaW4SErfROMISozskGOqUBsiefv6jcLuL9WACbaEe559o2WXHFjhyP5yLMfPlMqepQoXUD%2B5%2BSkVkw1fZwYaMGTohzkfs1yv%2Ba9bq%2FOHiG87YEp4HUBhGgsSMuJDtl66OaO89Niyeab5FMc6KQIM%2F3tFGoK%2BspV%2Fv5Sf%2FDReP8zqNTXmZ4CSylL2ZaaDipw3oeTDUP%2FdSbeb0cp9g6M7CL88RiFJW08THRgaQt%2FU7ZHor01uRJ&X-Amz-Signature=dacd089b9cee4ab73eccc5e13d486d30f81a5ba1a21dbc8496aa4dab08f6fcc0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QKHJJBI%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEk7qSGdVBP5ucwZdWzcQAHYUxdBYFzzYEFw2Sss8FRiAiEAtABOrYUqKnTKBY1O%2BebKd4OJ5d0Is8hY2D6Jl5rgW1Aq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDPz4MUnx8uCi6D3H7CrcAzhETGdBPPEV2RxYie0w%2BH9%2FP4ug9WYUJyaugpcWy2CdFPt4ymGzKM4E6fL6K%2Fw6iXk0AUZ06r8mFkATmLVHhqRjT2qnZXyX1xHfld3%2BZy4c%2Bv%2Bb%2B9%2BxVLi2Ei6ddMYujxQd2TI753JX9%2F2cjKuOpMruMCRADbFa93ioEF%2BB%2BAOCy5%2B0euds%2BAobpABZYYA9gP4TAcQT0UTnsji%2B9RKVSARKcJt%2FF54t6pXSsrqDmCA3mh26UiMS1iwmCs1UPJ3dJpnJhEvYpEXG4X1O%2B7PSE5hKF%2Bz9jk8V988CiElHNzw0vn1kbJHktLvq0BFC8BsgExHeGVjuA5EzmLSrtAQgjcn717g5rwMXG47hgFcRWR4u%2BqFKDik2VucTRlMTzznoBzreGODpdcmFtnMl3mk0RAlym4oponWJUJC8ToBz9RdTNQzjqtCjEiNd%2BPsAWSWDsTHtJkUxG%2BSBX8ZSW0StY1bl0NTdGYoIvVnlAbAzp3jMK9P41CillfLKuxk%2FqY4aFvg16i7mndIsO7Ls%2FAL%2F7%2FUbR2TowqwMpjPTml9IJLcV9X%2FRNO5f0cfnFFxz7yvW5v8RQUnvInSZDLA7oodcDGVUWvMB2Lz4lmMdtvEivZvXNEEVB4yaW4SErfROMISozskGOqUBsiefv6jcLuL9WACbaEe559o2WXHFjhyP5yLMfPlMqepQoXUD%2B5%2BSkVkw1fZwYaMGTohzkfs1yv%2Ba9bq%2FOHiG87YEp4HUBhGgsSMuJDtl66OaO89Niyeab5FMc6KQIM%2F3tFGoK%2BspV%2Fv5Sf%2FDReP8zqNTXmZ4CSylL2ZaaDipw3oeTDUP%2FdSbeb0cp9g6M7CL88RiFJW08THRgaQt%2FU7ZHor01uRJ&X-Amz-Signature=87c4c263a9bae3cc04402de38d623f3cf376f5716d974f749626e1fd10f1d1c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

