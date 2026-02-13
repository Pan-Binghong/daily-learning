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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAG5S4P2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGT92VRKKwW2kir2%2F4jMIM5h%2BZz0kFLt2Z9XiMZkq2ebAiEAw2UvCg5csu2CEHeuheKoYDB3ALxruN4O7hwHR1aaaeYqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNR9HW8dQuJGJuLd3CrcAxVW%2FW1nL1uu%2Ftx0wKfhnmzO3Og2TOkKDxiJEaiSjekNpgODmhsOlA24ObuMFcy9hdTNExOtyCNoNJCvyPdXOOnwZnFEO98GoXv%2FvFj3Ta5nzUISIQ%2FYWTvD5iDYoaNLSNoLK0uUx3%2Bo1W2as4FHGEDQSdGuTMbPBmbrYnAnmA4wdH2%2BvQ1egy93quJvW1G4DtkYk5OYIFoYs4c9%2FEmXH1k7duJVvAzH6vMlvhQbnSLnZwuael%2BaqRDGUu6OTQ%2FUQQJX%2F14ct9bS47iPqhN%2B6X25JKtFvWS3FmmfHf3FIujkImXcAKW7t7G0TcsIWfpftARyVBMijvgsDFSSIrBpMkCjG2EkYMYzlTx%2BDEatXdl8w28fu0xDPF9NKnA4BIKDlBBC%2BGSB6X0C1I6L6YFLsHyX2ViZsJuS%2B4yPPWkATSkT676VbSjTkU6RZwQ08D0%2FRFAzzN3fAT6jaYyMywf0meUu9c%2Bpz61zHNHAOfFNT7Nx5htBlDMqZtz1EF%2BPD1AyKkBS9rmpMEc066%2FXYHbNiHlH9r7nacOU89Bv0k5du5uUCYq9PoBbaVWSOKOetrlAGrm0cvkFTZ4p0zYidRx5x4tYQt0BLZxU4mnUtAzdQ%2BzJVRkvBy19C6Od6nOPMP65uswGOqUBcN4Tg9AglvJnLQ6zJOSxbctw0jbArrAfj3zE3V6bqP46w53LvGvOb5AkE7GTnlSk2VTKFgVEOjf6fJQPFmjBhqRgsU%2FU4MkBMke%2BAWdLdnX08HzUnvMNXVWGy2Jqjt7joQy7RTJpgdP3tI%2FRgg%2FLpB9Cqzmv6PtnFxuyQXJTW6ppwi1N484xFXznR2pKgWYdEfkcup74%2BGJrBvjKcaMSDEeoqvkj&X-Amz-Signature=7685938c9582a9f98f814340b884ba576aff07aa7bf5a47cc49ed9cd4fe1fd24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAG5S4P2%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIGT92VRKKwW2kir2%2F4jMIM5h%2BZz0kFLt2Z9XiMZkq2ebAiEAw2UvCg5csu2CEHeuheKoYDB3ALxruN4O7hwHR1aaaeYqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNR9HW8dQuJGJuLd3CrcAxVW%2FW1nL1uu%2Ftx0wKfhnmzO3Og2TOkKDxiJEaiSjekNpgODmhsOlA24ObuMFcy9hdTNExOtyCNoNJCvyPdXOOnwZnFEO98GoXv%2FvFj3Ta5nzUISIQ%2FYWTvD5iDYoaNLSNoLK0uUx3%2Bo1W2as4FHGEDQSdGuTMbPBmbrYnAnmA4wdH2%2BvQ1egy93quJvW1G4DtkYk5OYIFoYs4c9%2FEmXH1k7duJVvAzH6vMlvhQbnSLnZwuael%2BaqRDGUu6OTQ%2FUQQJX%2F14ct9bS47iPqhN%2B6X25JKtFvWS3FmmfHf3FIujkImXcAKW7t7G0TcsIWfpftARyVBMijvgsDFSSIrBpMkCjG2EkYMYzlTx%2BDEatXdl8w28fu0xDPF9NKnA4BIKDlBBC%2BGSB6X0C1I6L6YFLsHyX2ViZsJuS%2B4yPPWkATSkT676VbSjTkU6RZwQ08D0%2FRFAzzN3fAT6jaYyMywf0meUu9c%2Bpz61zHNHAOfFNT7Nx5htBlDMqZtz1EF%2BPD1AyKkBS9rmpMEc066%2FXYHbNiHlH9r7nacOU89Bv0k5du5uUCYq9PoBbaVWSOKOetrlAGrm0cvkFTZ4p0zYidRx5x4tYQt0BLZxU4mnUtAzdQ%2BzJVRkvBy19C6Od6nOPMP65uswGOqUBcN4Tg9AglvJnLQ6zJOSxbctw0jbArrAfj3zE3V6bqP46w53LvGvOb5AkE7GTnlSk2VTKFgVEOjf6fJQPFmjBhqRgsU%2FU4MkBMke%2BAWdLdnX08HzUnvMNXVWGy2Jqjt7joQy7RTJpgdP3tI%2FRgg%2FLpB9Cqzmv6PtnFxuyQXJTW6ppwi1N484xFXznR2pKgWYdEfkcup74%2BGJrBvjKcaMSDEeoqvkj&X-Amz-Signature=ce748c224b39632a6f0044b84331c3409d479d1f9f89278ae319f78b85494b83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

