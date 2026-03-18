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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXZSCVOO%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDF80uaykC%2FBHRGnEGTJSujoZiF9LXyu8%2Fd%2FHlyV2AY6AiAicXOQlb49hSies5fS4zRg1Jer8akdUdLXohyZZXkkLCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMen9VVeupFnwc5T4dKtwDO5czx19si1GGhO%2FIqaaotrEjwaIlAHjZ5x%2BtSPMSz6iHM15JEsPlpvZrvjuf5sWDG%2Fuf2eSOMGM5vh3oEj%2Bt3K3c8djcV7PEI%2Bf3sRZvlYJm4CNozexQz5j3dYfqxl8M%2BfXZdcs9ChJHOstnRGOla581eo9nN7VtZ06fAmYWjQtY9adedw2%2Fpcv8DajDsuugMWj%2F2qcsAlyjTlo0%2BaHtB71L63EYYKt9hQv6jehCRVclr6w2o%2FFWpNFaOk%2Fs1lcr76EesP9EMv%2FVWYVzkz5ovsCG6%2B1blgzrr3MhOu%2Fnyr5COmX1GLgPxNiH6bW0TW4l%2FvJb4S0Vig8zeC8gj5ArkaetkQPfLZsyPtXuZUGXOvgMJXRC8%2F5BE5bMj3Th%2BatElMKpoKBMNyAtUvkRDcgbUxGmAQe%2Bvw8JVJ2R3Pnumpaz7w3MKbDI5D2cWL%2BbjngKbsPWrixpYB%2Bu8XH5xZSTey54LSxKRL1wfk0Xljugt2Rgv5C7nhAtHFgvxKJaDNrutHPCQ0I4kiPR%2B4U6enzAYaxQsSh5HP80en08qR0r1%2FjAgUXieh2m22l6nWIyWZkNcZFmbvI2QFMiOAiBbrfI3AudZUxF%2BBJk2l1zbhaHvw2PxS%2BsjY6SXsYWkPMwnKfozQY6pgGcuel7F%2FLhgDkWtmTQuZCmzqGFMvTFKejgZ%2B1Az9qR44v%2FT5hVpn4QhNBNOy%2FZ84WuKTZsMas7yGKV8o%2FDPXJM3IIXOkaKWgNl8c4B%2B5l%2FdLpzfplMEAnH6ndkeOVHWDTbscFdWYmEZT%2FPI7IBgAMOvxKOAVjB6GmZPE1Z8syW5kAmSykDhdda5%2Br5ewUlsz9XHwD6MGMQcnWsMenoUcA1PGNe426k&X-Amz-Signature=087c86497bd42dd6b687ab615e1cbc1685f9224c4874db9108166ab620648c56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXZSCVOO%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIDF80uaykC%2FBHRGnEGTJSujoZiF9LXyu8%2Fd%2FHlyV2AY6AiAicXOQlb49hSies5fS4zRg1Jer8akdUdLXohyZZXkkLCqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMen9VVeupFnwc5T4dKtwDO5czx19si1GGhO%2FIqaaotrEjwaIlAHjZ5x%2BtSPMSz6iHM15JEsPlpvZrvjuf5sWDG%2Fuf2eSOMGM5vh3oEj%2Bt3K3c8djcV7PEI%2Bf3sRZvlYJm4CNozexQz5j3dYfqxl8M%2BfXZdcs9ChJHOstnRGOla581eo9nN7VtZ06fAmYWjQtY9adedw2%2Fpcv8DajDsuugMWj%2F2qcsAlyjTlo0%2BaHtB71L63EYYKt9hQv6jehCRVclr6w2o%2FFWpNFaOk%2Fs1lcr76EesP9EMv%2FVWYVzkz5ovsCG6%2B1blgzrr3MhOu%2Fnyr5COmX1GLgPxNiH6bW0TW4l%2FvJb4S0Vig8zeC8gj5ArkaetkQPfLZsyPtXuZUGXOvgMJXRC8%2F5BE5bMj3Th%2BatElMKpoKBMNyAtUvkRDcgbUxGmAQe%2Bvw8JVJ2R3Pnumpaz7w3MKbDI5D2cWL%2BbjngKbsPWrixpYB%2Bu8XH5xZSTey54LSxKRL1wfk0Xljugt2Rgv5C7nhAtHFgvxKJaDNrutHPCQ0I4kiPR%2B4U6enzAYaxQsSh5HP80en08qR0r1%2FjAgUXieh2m22l6nWIyWZkNcZFmbvI2QFMiOAiBbrfI3AudZUxF%2BBJk2l1zbhaHvw2PxS%2BsjY6SXsYWkPMwnKfozQY6pgGcuel7F%2FLhgDkWtmTQuZCmzqGFMvTFKejgZ%2B1Az9qR44v%2FT5hVpn4QhNBNOy%2FZ84WuKTZsMas7yGKV8o%2FDPXJM3IIXOkaKWgNl8c4B%2B5l%2FdLpzfplMEAnH6ndkeOVHWDTbscFdWYmEZT%2FPI7IBgAMOvxKOAVjB6GmZPE1Z8syW5kAmSykDhdda5%2Br5ewUlsz9XHwD6MGMQcnWsMenoUcA1PGNe426k&X-Amz-Signature=0ab8c073438a4b5ee24d7c4e0456cef77e141579da3ac5c66f4a721198f55765&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

