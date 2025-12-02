---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZLX223L%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCLly33GDVnDyQTdTNzAm%2FyKve7QQ1kLi5F3wD9EED0agIhAJrJjsCApWEURTiHPRXmmSi4VRRdE4o%2FzxyFkM2TR2HGKv8DCAoQABoMNjM3NDIzMTgzODA1IgyAMIEai867O%2FV7Digq3AOZIAe8KUexrjAX1CVxHqBRBoe5wBwh4iavuSesuWNQ738XCiqVJ8lVqa7FSDs8rJFyl9hhOP09JbzRpkvDZbjr4O4W8iiUAImeV06MF%2BEBhwzVmVFElVE4p94V5musDiidmiMR1%2B6taf%2FH5LJeDHBGCZCsuenYp%2Fq0vbO5GR0AkcDD281HCIOWJWwEcJlMSVZkCGnnby3nONyEoBsWtD0LepizO9tLmW8J8995kw03RVvPeVBiqoBZWaxaBWeQeSYmf4zsl8fEzSenLBYW2%2B28Jesi4zRQ0QpHg9bFowrGtbzSRbKGk%2BWzHC3T1fo7MGXTU%2Fpm866p%2BfMLnxUCOsI7ioFvN1avXYph7CakHbV2Ls%2FkQnW49FE0uxUXfBliyAYlxJFxmNZIQvqxr%2FcyJPQp0FJ4DL7BbWSKr8Z%2FElEPmWB7gEuInxvghbfo%2B9vPTpwKzPlXoGN74RRNmXQ4BSJSAHYJh7yUZ5rcJEs0J4NaKdfu3wkUOGdfbmE%2BnpGHL9GuviMHbLiYB8tgyMPb%2BacFH8ti639mZQQ6Jkqgs%2BEslUFn1QjADYS3Ozl2cMV%2BPlZXbb%2FirOVQURfTyrKnyGwy6XMBbALNfgWoNUiVJ8jZI%2FMsJUHx32NK8hHIdjC66LjJBjqkAWlIjCt2bXfLGWuCDg4K%2FrBKiHj%2B6or7LIoj00vjRYz%2Bmc00mLamZt2whZSkEJyTscTQSKxAoD%2B8i2VvXIMHOQ401oIzP84vTVx%2B30NzwT1xQFWSs4T354%2F0OJarfDYJajK5mpBO6VGDCNZ%2BjHmp3Mzw4a8mJeL9zBJqxjtr0F8SkPr09y%2BEXK%2B8gKbshGYONVEt2Z%2FGqNnAW4lzuVDPyLe5%2Bz9Y&X-Amz-Signature=e27c1e0862444c0b6d183f5d4163a381ea0ae1c559b55d89eefc869afe864719&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZLX223L%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCLly33GDVnDyQTdTNzAm%2FyKve7QQ1kLi5F3wD9EED0agIhAJrJjsCApWEURTiHPRXmmSi4VRRdE4o%2FzxyFkM2TR2HGKv8DCAoQABoMNjM3NDIzMTgzODA1IgyAMIEai867O%2FV7Digq3AOZIAe8KUexrjAX1CVxHqBRBoe5wBwh4iavuSesuWNQ738XCiqVJ8lVqa7FSDs8rJFyl9hhOP09JbzRpkvDZbjr4O4W8iiUAImeV06MF%2BEBhwzVmVFElVE4p94V5musDiidmiMR1%2B6taf%2FH5LJeDHBGCZCsuenYp%2Fq0vbO5GR0AkcDD281HCIOWJWwEcJlMSVZkCGnnby3nONyEoBsWtD0LepizO9tLmW8J8995kw03RVvPeVBiqoBZWaxaBWeQeSYmf4zsl8fEzSenLBYW2%2B28Jesi4zRQ0QpHg9bFowrGtbzSRbKGk%2BWzHC3T1fo7MGXTU%2Fpm866p%2BfMLnxUCOsI7ioFvN1avXYph7CakHbV2Ls%2FkQnW49FE0uxUXfBliyAYlxJFxmNZIQvqxr%2FcyJPQp0FJ4DL7BbWSKr8Z%2FElEPmWB7gEuInxvghbfo%2B9vPTpwKzPlXoGN74RRNmXQ4BSJSAHYJh7yUZ5rcJEs0J4NaKdfu3wkUOGdfbmE%2BnpGHL9GuviMHbLiYB8tgyMPb%2BacFH8ti639mZQQ6Jkqgs%2BEslUFn1QjADYS3Ozl2cMV%2BPlZXbb%2FirOVQURfTyrKnyGwy6XMBbALNfgWoNUiVJ8jZI%2FMsJUHx32NK8hHIdjC66LjJBjqkAWlIjCt2bXfLGWuCDg4K%2FrBKiHj%2B6or7LIoj00vjRYz%2Bmc00mLamZt2whZSkEJyTscTQSKxAoD%2B8i2VvXIMHOQ401oIzP84vTVx%2B30NzwT1xQFWSs4T354%2F0OJarfDYJajK5mpBO6VGDCNZ%2BjHmp3Mzw4a8mJeL9zBJqxjtr0F8SkPr09y%2BEXK%2B8gKbshGYONVEt2Z%2FGqNnAW4lzuVDPyLe5%2Bz9Y&X-Amz-Signature=0f6527c478f0715fb9d414e69559fe3c642e1dc2464522536e7f17f2ae8726c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZLX223L%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCLly33GDVnDyQTdTNzAm%2FyKve7QQ1kLi5F3wD9EED0agIhAJrJjsCApWEURTiHPRXmmSi4VRRdE4o%2FzxyFkM2TR2HGKv8DCAoQABoMNjM3NDIzMTgzODA1IgyAMIEai867O%2FV7Digq3AOZIAe8KUexrjAX1CVxHqBRBoe5wBwh4iavuSesuWNQ738XCiqVJ8lVqa7FSDs8rJFyl9hhOP09JbzRpkvDZbjr4O4W8iiUAImeV06MF%2BEBhwzVmVFElVE4p94V5musDiidmiMR1%2B6taf%2FH5LJeDHBGCZCsuenYp%2Fq0vbO5GR0AkcDD281HCIOWJWwEcJlMSVZkCGnnby3nONyEoBsWtD0LepizO9tLmW8J8995kw03RVvPeVBiqoBZWaxaBWeQeSYmf4zsl8fEzSenLBYW2%2B28Jesi4zRQ0QpHg9bFowrGtbzSRbKGk%2BWzHC3T1fo7MGXTU%2Fpm866p%2BfMLnxUCOsI7ioFvN1avXYph7CakHbV2Ls%2FkQnW49FE0uxUXfBliyAYlxJFxmNZIQvqxr%2FcyJPQp0FJ4DL7BbWSKr8Z%2FElEPmWB7gEuInxvghbfo%2B9vPTpwKzPlXoGN74RRNmXQ4BSJSAHYJh7yUZ5rcJEs0J4NaKdfu3wkUOGdfbmE%2BnpGHL9GuviMHbLiYB8tgyMPb%2BacFH8ti639mZQQ6Jkqgs%2BEslUFn1QjADYS3Ozl2cMV%2BPlZXbb%2FirOVQURfTyrKnyGwy6XMBbALNfgWoNUiVJ8jZI%2FMsJUHx32NK8hHIdjC66LjJBjqkAWlIjCt2bXfLGWuCDg4K%2FrBKiHj%2B6or7LIoj00vjRYz%2Bmc00mLamZt2whZSkEJyTscTQSKxAoD%2B8i2VvXIMHOQ401oIzP84vTVx%2B30NzwT1xQFWSs4T354%2F0OJarfDYJajK5mpBO6VGDCNZ%2BjHmp3Mzw4a8mJeL9zBJqxjtr0F8SkPr09y%2BEXK%2B8gKbshGYONVEt2Z%2FGqNnAW4lzuVDPyLe5%2Bz9Y&X-Amz-Signature=6c94e7deba1c5faab7d48572fde49557ae1a988b9d8f91416b07393d5f670132&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

