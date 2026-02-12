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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G3MA7SV%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIDlPI5aljpwQpzqpvSsN%2BSvNCzR%2Fb92k2gPzJ7SdBwIMAiEAsEle4%2FJkwDjtn76Nfr2rbDg9JojP4FG%2BxAxMiOwLtBsqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVFidGYk3FudIfYdircAxTyQ%2ByEG81t2%2FmSc%2BQ3ofscWWNgctIXOxphZ0%2FFA7vT4QKLDJYwoQ1MyqrjVq1ponEBCSu2%2FubazfkRJR0mRwekEWsrgyDCd5rXkkpPwZNcu8Srnb196erZrDTCw5NJjAz2r1t9ic%2BwgfeCJLPcaFsGAxYKWIgWXEtrDAs1ZjOybxVhVl0ZcXAafQ%2B3E769ImVArGRtF04NYWUnxJWD3wGAEuZLmlpAER96iOgFiOeQuEMTN1606gAtPm%2BNZBGh5s9nXuPin%2FxwQuQQnLU2LZIQ8C%2FxkRPxzX9FNYmHgJ7p%2BUZsZFmVsD23DT4w%2BIZncqemql2ZBwg7DSAFvvKfK%2FBcI2WRnHtD7ubBRni%2FnxyLCOQ1wYNyijdCo1FT2q61KGldVU5EBuiavXG%2BF7KWxazjXUsEkL%2B%2F7qHp3Dp2rTLjwNJ6g%2B3xwoBNHy%2Bs2Xp9RWWA6%2F9bNiccuPWJXPrk%2BRm1M29%2F%2BiSh9%2FWznJ1lECTd98uhQ3MTiEICn8d8wCMrq%2BYhzIzwCWdev1dJ2eubU35VaS3IIeUb62B%2BfEMhSXrgJaQPzQih0%2FP5BGvEhcoq3PJ5mcFHaUY%2FZpkq6WhytL4PkdyTEzaVKlueZcMEetIU7sloSJeuTY99ObbtMKGTtcwGOqUBSZEwXkz8qq0WyrAQWXe8My9Xg0oxNL7ap7hTxGvbuUqTlj2D93lGxmvQIrENfj6xCX9pDlyWENfCJMR%2Bl53UOt%2FaXbss%2BK7PXZg1BiBh%2BVxz9U6N%2BdFrnL%2FUmRZdpt%2Fg%2BqHnfVkXIcNNG%2FAXZkvNUSEwIDIzCGzh3sZbZHTyNvsZ90pVX1fWVdYhbRQ6lybro6MW7pRVtqhvm57MXqoB%2FW5bbz8L&X-Amz-Signature=7c90c13a10ed840dae8e71103b2c7681a44e92664d910c88f17d96fbf5ef5306&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667G3MA7SV%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIDlPI5aljpwQpzqpvSsN%2BSvNCzR%2Fb92k2gPzJ7SdBwIMAiEAsEle4%2FJkwDjtn76Nfr2rbDg9JojP4FG%2BxAxMiOwLtBsqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVFidGYk3FudIfYdircAxTyQ%2ByEG81t2%2FmSc%2BQ3ofscWWNgctIXOxphZ0%2FFA7vT4QKLDJYwoQ1MyqrjVq1ponEBCSu2%2FubazfkRJR0mRwekEWsrgyDCd5rXkkpPwZNcu8Srnb196erZrDTCw5NJjAz2r1t9ic%2BwgfeCJLPcaFsGAxYKWIgWXEtrDAs1ZjOybxVhVl0ZcXAafQ%2B3E769ImVArGRtF04NYWUnxJWD3wGAEuZLmlpAER96iOgFiOeQuEMTN1606gAtPm%2BNZBGh5s9nXuPin%2FxwQuQQnLU2LZIQ8C%2FxkRPxzX9FNYmHgJ7p%2BUZsZFmVsD23DT4w%2BIZncqemql2ZBwg7DSAFvvKfK%2FBcI2WRnHtD7ubBRni%2FnxyLCOQ1wYNyijdCo1FT2q61KGldVU5EBuiavXG%2BF7KWxazjXUsEkL%2B%2F7qHp3Dp2rTLjwNJ6g%2B3xwoBNHy%2Bs2Xp9RWWA6%2F9bNiccuPWJXPrk%2BRm1M29%2F%2BiSh9%2FWznJ1lECTd98uhQ3MTiEICn8d8wCMrq%2BYhzIzwCWdev1dJ2eubU35VaS3IIeUb62B%2BfEMhSXrgJaQPzQih0%2FP5BGvEhcoq3PJ5mcFHaUY%2FZpkq6WhytL4PkdyTEzaVKlueZcMEetIU7sloSJeuTY99ObbtMKGTtcwGOqUBSZEwXkz8qq0WyrAQWXe8My9Xg0oxNL7ap7hTxGvbuUqTlj2D93lGxmvQIrENfj6xCX9pDlyWENfCJMR%2Bl53UOt%2FaXbss%2BK7PXZg1BiBh%2BVxz9U6N%2BdFrnL%2FUmRZdpt%2Fg%2BqHnfVkXIcNNG%2FAXZkvNUSEwIDIzCGzh3sZbZHTyNvsZ90pVX1fWVdYhbRQ6lybro6MW7pRVtqhvm57MXqoB%2FW5bbz8L&X-Amz-Signature=925f38e636a3efdb03bac7f4b50c74085badfe11309d004a5a229d611da7b2af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

