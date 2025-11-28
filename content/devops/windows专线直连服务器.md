---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIUSG6CR%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPRn0wRzQQxVnyEl0i8fShEVkHrOaJAnQra3KEQDcNQIgRiF4xVpJrOlaAxeAULBTBdL9b9gHwvYBM7plsd%2B7jzYqiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHl0vqNH%2FrP9gqoNFyrcA86y2Pa1hWbyuYVK0g7WJb2z6ZWXuN59d%2BCPlv%2BYQ6gTeMfvcmPtVdeWvrJ36gPEBpiAxWZ8RUYekbno0q3weHLZlxHU3tXEpi%2Fky2LmfQCGJRzQA9vbAFw7baJDMwaCk7JX95tdd9C4mEwfzlOgseHMhZLXSLbb00Ox8SwJVD50qwXcoGZ8xRX4s2pxCA6u9F1eq0b2VMdfJH17y2Ua%2F8fgY%2Fuo7LOhDxMqRSeUvNp%2FoRQ4vVF9zTas6CBw6KFvVBkzvDEt31Qr3LBMM6WAbtMEr%2BcWt6x8rlgw3E%2FUl%2FPcFttRpQqf6sqRPCTkLjOV7QRH5waVpMSgrEUeqvN26P2M59pWcnyDSR09QDTjKcY%2BRTLtiwqVf8wMZdoifrjVlE7F2%2F%2FotoQ4DzpzUloJYZMGPqrvqFtvVQzs%2FmiaGS0TQA9GMV7eFoLlk5cAYQoGIaw3OScpMqZvqdcE4ywLkrV69CQ4uYYA9fwg89fDEutXvx79NiRF%2FVccRO9uF1QG2vKiyYHkjFKGD9rplwmGHZm98HfYC1BusMIFgQCndSkrYIDHRkGpRXVvfV1x%2BOuXbQM8G7eQgTH%2FEJQX%2Fq2EOLZdutR6M9oaIOiEt2AteHJo88KeqPuJnOT1AC8mMJmDo8kGOqUB5LXnk9ikU6GdjUhoLof8WtRG3LF2btYsT8ObhssNmB41EiTbwiZvE4Y85JSyvOM7kVbyM4N1c5PCfeTixctThOuM67VKFCnt8sWuapo5anTDsiBClxLDIEIvP%2FWQDGPEb304wOAbMThAm09JsXL0Ty8tJlMW6SWKtxKFEmcl0IUgSCLt6XZUHp7CoTe0WSFn7GMFOmnXb5Ocpw7NzoOicGp0PHaz&X-Amz-Signature=d6281e54bb3dec181a93e4fb2402026a19d04ba8f284d986117e7a0843c4a407&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

