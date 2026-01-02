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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2J3V73I%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDMWiG2YSHLJnWQVx9TnJZY29Et0Mge1ux2J2EBMyflZwIhAOIqfP7KCoKDr8%2BB5viqs%2BZKeZE3aTYheJ9yu91SMwoQKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZkRkK%2FxiE9Gl8X%2Bsq3ANwDqa2zCCIrFKvabPl2vr8FZwU9awq8Ep0VG0nvfPXrtTfipaOkGTcQp%2Bx8D6mv0P7CZVX3qRZ23jEh%2FidpnJfnLdfa5nvCfNDwGNXk2%2B4aP2v5v019Ar4MCSN1z2EYFxRqny0cum5fLDm9Kprac66h8lzmXv%2BjRL0emevxh0rwjqwPno7lbbrAcOY4kzTLF4jHrftvRHGGqCdf0MwD9RLlJpelk2LKc0%2Fuoa6HqR0UC8m%2Fl5vJIpEMqBB7omFTT3UQ%2BNvs0WYACl6%2BpWwEneVANK3SOcaAmz8K4Fu7uGSbwikAiLEONEHsmW2Y2mSS1tW83z6XOfQl0TAoKLVUQ0d15Mxp6tYAHMqIx%2BRVTrzhJjfttn7A58Jxr5F7QlNRMa4CMkD%2BHqPI2wUFHLxFifkYkbnD0Y2Rxv7LMnaW52frLRjH5euO5QWvdX5O9s6HBt8FTdq0KYoLjMzaL313BlyfsGU844oWSrN6rbTsCJWXgTVUNJYwnSBGixl4S%2BbryeM1ynqbbxjTY6NH2%2Bijiw4p%2BUa39VRFbnyXaUIVZJbIEyAWIFLilyCIwOo68JJ1%2BH3KozZwSjEvgwXuOZyIQ1hMInx2EN1f8%2B55QqsUlGmXgbooxX7E%2FQqBHKgeDDyuNzKBjqkAWBPMeMWehLE%2FlRcgi%2B6%2BDUpHJmGG3VWTzcVjMPGIel1p7v3Cd%2F5JmC9KdUrMjRvaYVnnoOiuZ72fEbp%2FexaNcpK2PL%2Bp%2BjBI6vtlXVGfONvLGk8Fb9FaATS5G%2Fs0ESDQ9ymWH%2FGoOVAgJFNY9vsq%2ByodwZcRUYWkVjVh6c7sUBYEmcU4hLqQYjGoOnRpB4JURSFmv2naVi7cHUXQxmN2S85c3Wb&X-Amz-Signature=7ac0443a2b66de75b7f8dd77e50cfed48937a56f9eed5a7210d87bb3955479eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2J3V73I%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJIMEYCIQDMWiG2YSHLJnWQVx9TnJZY29Et0Mge1ux2J2EBMyflZwIhAOIqfP7KCoKDr8%2BB5viqs%2BZKeZE3aTYheJ9yu91SMwoQKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZkRkK%2FxiE9Gl8X%2Bsq3ANwDqa2zCCIrFKvabPl2vr8FZwU9awq8Ep0VG0nvfPXrtTfipaOkGTcQp%2Bx8D6mv0P7CZVX3qRZ23jEh%2FidpnJfnLdfa5nvCfNDwGNXk2%2B4aP2v5v019Ar4MCSN1z2EYFxRqny0cum5fLDm9Kprac66h8lzmXv%2BjRL0emevxh0rwjqwPno7lbbrAcOY4kzTLF4jHrftvRHGGqCdf0MwD9RLlJpelk2LKc0%2Fuoa6HqR0UC8m%2Fl5vJIpEMqBB7omFTT3UQ%2BNvs0WYACl6%2BpWwEneVANK3SOcaAmz8K4Fu7uGSbwikAiLEONEHsmW2Y2mSS1tW83z6XOfQl0TAoKLVUQ0d15Mxp6tYAHMqIx%2BRVTrzhJjfttn7A58Jxr5F7QlNRMa4CMkD%2BHqPI2wUFHLxFifkYkbnD0Y2Rxv7LMnaW52frLRjH5euO5QWvdX5O9s6HBt8FTdq0KYoLjMzaL313BlyfsGU844oWSrN6rbTsCJWXgTVUNJYwnSBGixl4S%2BbryeM1ynqbbxjTY6NH2%2Bijiw4p%2BUa39VRFbnyXaUIVZJbIEyAWIFLilyCIwOo68JJ1%2BH3KozZwSjEvgwXuOZyIQ1hMInx2EN1f8%2B55QqsUlGmXgbooxX7E%2FQqBHKgeDDyuNzKBjqkAWBPMeMWehLE%2FlRcgi%2B6%2BDUpHJmGG3VWTzcVjMPGIel1p7v3Cd%2F5JmC9KdUrMjRvaYVnnoOiuZ72fEbp%2FexaNcpK2PL%2Bp%2BjBI6vtlXVGfONvLGk8Fb9FaATS5G%2Fs0ESDQ9ymWH%2FGoOVAgJFNY9vsq%2ByodwZcRUYWkVjVh6c7sUBYEmcU4hLqQYjGoOnRpB4JURSFmv2naVi7cHUXQxmN2S85c3Wb&X-Amz-Signature=17bcf7ad03b190b7cc5edfae3f9f429258307e9a02222048bff776a947aa30cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

