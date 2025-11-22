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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB26TIUK%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCICEEPbK2dxCykzHYsSQ90Kmsrkw4xsZMx6pS43vQ0uzwAiBsyKSaf1l8pyD5hsH7qxYDpUh7FkgjHpAO5TT5E5K2uSr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIM1hClMszf%2B52gjtbaKtwD%2BXuvdu2jPq3Lz8Yp9SxEHwWZob7kXs2bxidASsTKgL8hcQxjxjqHWx579oKXtlitbN1Ow%2FmMnze8AWw3M4yc59trMXilBsU84nibyu8GNdKTE9shUOA%2BxdNBbsPZbIarfzOP9zGdIly6BcqfIr1Jza7W19dps0bc%2BE792sUWHcWGgstcru7Y7ALALmix2GzB8mwAgObf7Jd4qD5JIvENkYUQLbATmKrqdJmLhhwyRGncgTUbYn73klWmr93TIe3i%2BMSoHATzise9d5S4LAkroIHka7kVpO893GRQK52TGNVDGD3CNyOUS0201W6QbSvbs9%2Fg5QKq73OyhyDowOQBgm8cSj5wtYFYfPq2GItGQHSUuvyJkS2lY5yk5tEObRoXwxSv7Bsr2j004fjMsAaleI4RhsYTphsIrDx%2Frfq9tsZ0924Q0%2BytsQBwqmedDynsQUBklD5kGmU951nGPFFSYIlT8QRgygL7DsUPLmTsRIlu0jJ7SmihTdPkN6RdUbL0vBiPAGbq6ADnKao5B6f6EEP9BhYnuUpBQ7RiMrD2ZCmdatu8tMn9t4R075T%2FZ5crPVqJHJW8xD4%2BHxc6bAcX%2BtL2WMGlUzL574m573Awb1jZNOH0nOlRQXIVgScwmaGEyQY6pgG%2FBk2RS%2FcsWRQQC9l241zA4E2N5kH2bZQI1rA74EzlGKsPUJDGP%2FEu8x%2BSSmD7eksmnAwlkZycR1mo2sxTRzpstyi2gN76%2BfYIrd9H09ztRcwlSzK2Xien00kRTW2YNyxe5wriTioQ%2Ff2JlfMnjgp0Yjv5kMJCggI%2Bb6Yc7GAE%2BGYXmFC9jb4EScotFCLAB34EZ2qv9QexQZyM%2FRAbm%2BNSY6TodANT&X-Amz-Signature=c4fea860ff690414228a058b06e099fb8ec8c82094d4e4986bc6fb507fdce37b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB26TIUK%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCICEEPbK2dxCykzHYsSQ90Kmsrkw4xsZMx6pS43vQ0uzwAiBsyKSaf1l8pyD5hsH7qxYDpUh7FkgjHpAO5TT5E5K2uSr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIM1hClMszf%2B52gjtbaKtwD%2BXuvdu2jPq3Lz8Yp9SxEHwWZob7kXs2bxidASsTKgL8hcQxjxjqHWx579oKXtlitbN1Ow%2FmMnze8AWw3M4yc59trMXilBsU84nibyu8GNdKTE9shUOA%2BxdNBbsPZbIarfzOP9zGdIly6BcqfIr1Jza7W19dps0bc%2BE792sUWHcWGgstcru7Y7ALALmix2GzB8mwAgObf7Jd4qD5JIvENkYUQLbATmKrqdJmLhhwyRGncgTUbYn73klWmr93TIe3i%2BMSoHATzise9d5S4LAkroIHka7kVpO893GRQK52TGNVDGD3CNyOUS0201W6QbSvbs9%2Fg5QKq73OyhyDowOQBgm8cSj5wtYFYfPq2GItGQHSUuvyJkS2lY5yk5tEObRoXwxSv7Bsr2j004fjMsAaleI4RhsYTphsIrDx%2Frfq9tsZ0924Q0%2BytsQBwqmedDynsQUBklD5kGmU951nGPFFSYIlT8QRgygL7DsUPLmTsRIlu0jJ7SmihTdPkN6RdUbL0vBiPAGbq6ADnKao5B6f6EEP9BhYnuUpBQ7RiMrD2ZCmdatu8tMn9t4R075T%2FZ5crPVqJHJW8xD4%2BHxc6bAcX%2BtL2WMGlUzL574m573Awb1jZNOH0nOlRQXIVgScwmaGEyQY6pgG%2FBk2RS%2FcsWRQQC9l241zA4E2N5kH2bZQI1rA74EzlGKsPUJDGP%2FEu8x%2BSSmD7eksmnAwlkZycR1mo2sxTRzpstyi2gN76%2BfYIrd9H09ztRcwlSzK2Xien00kRTW2YNyxe5wriTioQ%2Ff2JlfMnjgp0Yjv5kMJCggI%2Bb6Yc7GAE%2BGYXmFC9jb4EScotFCLAB34EZ2qv9QexQZyM%2FRAbm%2BNSY6TodANT&X-Amz-Signature=0b0e0ff9dd8b347a83161531c4b21c4ea03197839b98357ac5015a927591ba01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

