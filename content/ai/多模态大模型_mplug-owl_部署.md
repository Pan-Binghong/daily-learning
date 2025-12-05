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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GCFGP7A%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCU3CHzEkEv4po%2BM1Ko2eYaKHUPumQsm8%2B3d%2FkfLZ17qAIgO6dy6Dt30wPo7rAEB4qHfdV%2BK6vp1j8i8td9AYbD1U4q%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDNf3rI9zmrbW2RhnfSrcA%2BeY%2BRN2Ggzk6DCGArDSaVdp6sXdm%2FEMHGhpmw5I5j3YlXfuvKIJXwaCKRYd9WbYR0lmldhktGjjSl4ixZ0q5pyLhs9fDuUv3E7Fbec51wF2ozLcljKXmhlC%2B7q6Ka3BXIoZZ%2BO8KEG0XLOeXRLTFlkbqFI6K99P4c9QU9n%2B1CEtC6hU5uc0JpPlZoQDjkn94V4Rhl9i3OMCNj1s9izF8jI6JmSVZYOTwjhqogOZAPKdpYJewQ4b9zdb%2BRJF8xk7jmmdZ0tM2K6N7ogdiF69SW0wpFShgIAWx1LPHpzuzCP2jQBEnPwLlNoGC1qIC8Lm4g3rZb0q73g6DYNa%2BFt8RFtPgmSECsRbvvFBtL2W3vMKpz0eIRNB1Ow1entu7H9abuFz9yoxRj8O7MdUJUJ3hS%2BTi9UwIJH60yhdrMNflIZ3lmyM9inxWmwXK5xflZcopj2Q%2Bu0AfviQwvX1c7RY61aCMvfeW3cAM4luH1R%2Bal%2Bi3nGRnUl7VtxUJpdLv9Q27vcptn%2FPfoU7o5JiyZMey8QW%2B09WAW4IqrGJ20Acb7tQJ0cPKWz0RU5pmcTNN%2FI13U3L4H43S6CtiVVQbFhL3cgn5E%2B5yfNgHsBhf8iKknqiSxDN6G4Gq2VJJFD%2BMPiLyMkGOqUB1%2BgpTRTfTd%2FP3WI2qU1rqI%2FpwtselaUSL3KMbv9UUcYLBUzH6TE1VbV7sraAjhbpXcKl6vutUqesM2i%2F38maDhPluCgfsNudlr9P2D51U7toQokzBUhSLnlSe9UpX0QFz6qUTlHDOKFO31TTX0TWGZyaarYk0FcB%2FidaVXzRqW3aXW0Ys%2Bn3ePgyy%2FPBc%2BbsGcuPjO8e92OrxSqzBAeurPe8j1u8&X-Amz-Signature=0bc4a34a474e2db36797d1c4265ed0a9645a16ced6d151f09255afc3a0a13c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GCFGP7A%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCU3CHzEkEv4po%2BM1Ko2eYaKHUPumQsm8%2B3d%2FkfLZ17qAIgO6dy6Dt30wPo7rAEB4qHfdV%2BK6vp1j8i8td9AYbD1U4q%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDNf3rI9zmrbW2RhnfSrcA%2BeY%2BRN2Ggzk6DCGArDSaVdp6sXdm%2FEMHGhpmw5I5j3YlXfuvKIJXwaCKRYd9WbYR0lmldhktGjjSl4ixZ0q5pyLhs9fDuUv3E7Fbec51wF2ozLcljKXmhlC%2B7q6Ka3BXIoZZ%2BO8KEG0XLOeXRLTFlkbqFI6K99P4c9QU9n%2B1CEtC6hU5uc0JpPlZoQDjkn94V4Rhl9i3OMCNj1s9izF8jI6JmSVZYOTwjhqogOZAPKdpYJewQ4b9zdb%2BRJF8xk7jmmdZ0tM2K6N7ogdiF69SW0wpFShgIAWx1LPHpzuzCP2jQBEnPwLlNoGC1qIC8Lm4g3rZb0q73g6DYNa%2BFt8RFtPgmSECsRbvvFBtL2W3vMKpz0eIRNB1Ow1entu7H9abuFz9yoxRj8O7MdUJUJ3hS%2BTi9UwIJH60yhdrMNflIZ3lmyM9inxWmwXK5xflZcopj2Q%2Bu0AfviQwvX1c7RY61aCMvfeW3cAM4luH1R%2Bal%2Bi3nGRnUl7VtxUJpdLv9Q27vcptn%2FPfoU7o5JiyZMey8QW%2B09WAW4IqrGJ20Acb7tQJ0cPKWz0RU5pmcTNN%2FI13U3L4H43S6CtiVVQbFhL3cgn5E%2B5yfNgHsBhf8iKknqiSxDN6G4Gq2VJJFD%2BMPiLyMkGOqUB1%2BgpTRTfTd%2FP3WI2qU1rqI%2FpwtselaUSL3KMbv9UUcYLBUzH6TE1VbV7sraAjhbpXcKl6vutUqesM2i%2F38maDhPluCgfsNudlr9P2D51U7toQokzBUhSLnlSe9UpX0QFz6qUTlHDOKFO31TTX0TWGZyaarYk0FcB%2FidaVXzRqW3aXW0Ys%2Bn3ePgyy%2FPBc%2BbsGcuPjO8e92OrxSqzBAeurPe8j1u8&X-Amz-Signature=8e42c1239ae3c4e8db54ae340f6944db69d3b10ee3cf271c4cfe1694b572c2e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

