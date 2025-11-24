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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SANLMOY%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDokk269l0sVEOGi7hU3X0iQpuy08RGW4J2I8lumhz59AIhAMym%2F6zJ77HAZVxKGj7XBN7tzHaXsQjdS9fPbp4F3NkxKv8DCEoQABoMNjM3NDIzMTgzODA1Igz55kL9twbcL86g8XIq3APcZBFlOrKJTLrVFy8fzy30un7G4gjBpBtfutuybOv3Cd6vI0aSE%2Fvc1%2FfTFDy0qOlYdvRSagH38rvxgS3jxwzXWZBLGeOHEVU2e7yesaGJTrbGW%2Bm9bhGJI1rS0C4dQlgPiTC1SK5oRT9rFXiIeRUn4BrVEw%2FzN6txr7V0JN6SllfExVgg%2BkgSXBF0EFp5%2F6RP1jxniXPbVqucMrNtuFfZsN6dHxGByiCK6YMKRxFrc6tvt7zsKWaxQB%2FV1YbzblVvPPNbbsDpAauAB7YweBNXKypephZC5jpQbJKebIFCpLmHS%2Fcgwo5QLg3VGBhT7XopQFmVbHokaVJcd%2BNo%2FDrmXUT%2BeSX3NYNj26IP6lwgyOf0OU1WLU7ycj4UUi3zYNSikEx5YlR6zmParnhn7EOE2pRniKu9HEjVcBx5LqlOhXljK2wDttsZ223Hd8ju5y%2BcV%2BsaSqk3KZD8ZASukUPVlnHE4wLKbeodFHeFt9Di3bviO2ZA6%2BMK6F83nE6b9nFTLEv9dV96zBn8a3lKqcFgigYYGyoBa23ZxQR9w9Lp5Ep4YAT%2BnCKAi5MO82iwbMTOVnu2KgVNakVtCQtrXTq16BmI2jFK0HTTEc4V6NqTcvWvFJtJV5fcwpUMozDe3I7JBjqkAYH9nSSIhEOQpmEDGhyo72qnH50%2BQnPV%2BqyM0d%2Bir3SG3HvO0adxXobRTkq4RoFWcYiOWsZTAzrWfNjE9ZKKgmEy686WvryS7DgJO9O2YM1ZhrAlY%2FhJZLXvi38ZewaCtu9WWYMLjYi857dpPB46e18Cd%2FH7AMj2NrR57ufc5iLGgzhjp9PqOcpCmkdzg5zuP%2F%2BiT4tzdnoBCSDbiAqPdHoBwsvq&X-Amz-Signature=5c75d193c343dd595bfdf4760e65e988ca0c6d5176c266d951a6c41422bbd78b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SANLMOY%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDokk269l0sVEOGi7hU3X0iQpuy08RGW4J2I8lumhz59AIhAMym%2F6zJ77HAZVxKGj7XBN7tzHaXsQjdS9fPbp4F3NkxKv8DCEoQABoMNjM3NDIzMTgzODA1Igz55kL9twbcL86g8XIq3APcZBFlOrKJTLrVFy8fzy30un7G4gjBpBtfutuybOv3Cd6vI0aSE%2Fvc1%2FfTFDy0qOlYdvRSagH38rvxgS3jxwzXWZBLGeOHEVU2e7yesaGJTrbGW%2Bm9bhGJI1rS0C4dQlgPiTC1SK5oRT9rFXiIeRUn4BrVEw%2FzN6txr7V0JN6SllfExVgg%2BkgSXBF0EFp5%2F6RP1jxniXPbVqucMrNtuFfZsN6dHxGByiCK6YMKRxFrc6tvt7zsKWaxQB%2FV1YbzblVvPPNbbsDpAauAB7YweBNXKypephZC5jpQbJKebIFCpLmHS%2Fcgwo5QLg3VGBhT7XopQFmVbHokaVJcd%2BNo%2FDrmXUT%2BeSX3NYNj26IP6lwgyOf0OU1WLU7ycj4UUi3zYNSikEx5YlR6zmParnhn7EOE2pRniKu9HEjVcBx5LqlOhXljK2wDttsZ223Hd8ju5y%2BcV%2BsaSqk3KZD8ZASukUPVlnHE4wLKbeodFHeFt9Di3bviO2ZA6%2BMK6F83nE6b9nFTLEv9dV96zBn8a3lKqcFgigYYGyoBa23ZxQR9w9Lp5Ep4YAT%2BnCKAi5MO82iwbMTOVnu2KgVNakVtCQtrXTq16BmI2jFK0HTTEc4V6NqTcvWvFJtJV5fcwpUMozDe3I7JBjqkAYH9nSSIhEOQpmEDGhyo72qnH50%2BQnPV%2BqyM0d%2Bir3SG3HvO0adxXobRTkq4RoFWcYiOWsZTAzrWfNjE9ZKKgmEy686WvryS7DgJO9O2YM1ZhrAlY%2FhJZLXvi38ZewaCtu9WWYMLjYi857dpPB46e18Cd%2FH7AMj2NrR57ufc5iLGgzhjp9PqOcpCmkdzg5zuP%2F%2BiT4tzdnoBCSDbiAqPdHoBwsvq&X-Amz-Signature=77bdc07e0aeeceb9de2e6c6f9cf9c89d62b2b42ba30ce2bc80bc46dec25ae9f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

