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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4UKNYMZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIHNP5ZsFR4Lnr7ZSVCCvZjJ5F2TMhCrfAiIQA3KjH5m0AiAQ7UKWw05rAhpdNiC0Nzk8hMOtzwlroy9eOQ49IEIXHSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMeqBNabelyTKecgwHKtwDCNv7VkNoYQBQ4ozwMGZtEAx47JFdMirrPLVGRiV2GNw1yiP5YbIOCDakF0nJriAkknPtOyuJK7x13Z2uPik6moj5FBD8dWPuFxlsUk%2F82nR%2FM3uoUjSQTCgFNbetvXDoH9fy6PHVhOY9b%2B6joM%2B2LpkG2R3ahEf36E9KADFJ3T4tPake64RKCOVpFXWxnESHoIY4UYcHWytbj02wcePmLJMtj%2BNp%2F6lb8TfA6RXR%2BOjXUiIjCocFm1uYqAAPU4%2BxkxAhap0iT54rfjS%2FvrVnorOS3C9iNdSMAlvEoqjfJ1a7oFQDkOGdw45WLX%2Fu%2BzNVLll2z9mxLfVoS29qcLacak6cFJGMwYJlVU%2FPhBMNyGlPqzs8WW0AVUmvwgRUCz5xVr6IBdUdiNw6yH6K3Ad540pPFgGJWQ%2FkiYSuUIi4mR%2Fokiox5NrmPotN%2BIg8k9l7bQPurKntXsWuF5MgvDwqaTzjV5sIHbUxmyMvrSnA5xjlTiZwRU2wtr0LNvT%2Fpi%2Bte1DPwYlZjJ9cZ6Akw0ROaDiq9l635qW%2BrP8J0CczIR4f3zMKbWA4PJl2PfujGCGQhuRCr91%2FcPOY1QC5GCGOSvVDBo6Arp3YKoApNlBWQ63ZFibfUxVhKZsIt3wwjozzyQY6pgHguif5yQexI0phddhqqYdKinqI0ABot5yDcw1ccJs85RlPPCGCH4O1v%2Bp9hxEKpnFo%2Fv4pXLQrymzdR20xIfpnUShKMXhPSqcC6tmb8zkI4Vi32DRep2Jwd03W3OZbdNgJ7FcDJZgfdVeeDh02hLeC0ofle2IXo6%2BVPMkFOmy%2BcgmI49poF8cXzg0xefYNRh3S3wFXhMY4mMGYCzFCkcwYGT5I2%2BPv&X-Amz-Signature=8cc8bb705a1fe8887ab65bc4037ec5ad9ccadc65e817efc861cca0aa8b8a77b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4UKNYMZ%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIHNP5ZsFR4Lnr7ZSVCCvZjJ5F2TMhCrfAiIQA3KjH5m0AiAQ7UKWw05rAhpdNiC0Nzk8hMOtzwlroy9eOQ49IEIXHSr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMeqBNabelyTKecgwHKtwDCNv7VkNoYQBQ4ozwMGZtEAx47JFdMirrPLVGRiV2GNw1yiP5YbIOCDakF0nJriAkknPtOyuJK7x13Z2uPik6moj5FBD8dWPuFxlsUk%2F82nR%2FM3uoUjSQTCgFNbetvXDoH9fy6PHVhOY9b%2B6joM%2B2LpkG2R3ahEf36E9KADFJ3T4tPake64RKCOVpFXWxnESHoIY4UYcHWytbj02wcePmLJMtj%2BNp%2F6lb8TfA6RXR%2BOjXUiIjCocFm1uYqAAPU4%2BxkxAhap0iT54rfjS%2FvrVnorOS3C9iNdSMAlvEoqjfJ1a7oFQDkOGdw45WLX%2Fu%2BzNVLll2z9mxLfVoS29qcLacak6cFJGMwYJlVU%2FPhBMNyGlPqzs8WW0AVUmvwgRUCz5xVr6IBdUdiNw6yH6K3Ad540pPFgGJWQ%2FkiYSuUIi4mR%2Fokiox5NrmPotN%2BIg8k9l7bQPurKntXsWuF5MgvDwqaTzjV5sIHbUxmyMvrSnA5xjlTiZwRU2wtr0LNvT%2Fpi%2Bte1DPwYlZjJ9cZ6Akw0ROaDiq9l635qW%2BrP8J0CczIR4f3zMKbWA4PJl2PfujGCGQhuRCr91%2FcPOY1QC5GCGOSvVDBo6Arp3YKoApNlBWQ63ZFibfUxVhKZsIt3wwjozzyQY6pgHguif5yQexI0phddhqqYdKinqI0ABot5yDcw1ccJs85RlPPCGCH4O1v%2Bp9hxEKpnFo%2Fv4pXLQrymzdR20xIfpnUShKMXhPSqcC6tmb8zkI4Vi32DRep2Jwd03W3OZbdNgJ7FcDJZgfdVeeDh02hLeC0ofle2IXo6%2BVPMkFOmy%2BcgmI49poF8cXzg0xefYNRh3S3wFXhMY4mMGYCzFCkcwYGT5I2%2BPv&X-Amz-Signature=fb407b3483346bc5d04b442eeba1f5a9909c277843fb44998b0436dd9978cb15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

