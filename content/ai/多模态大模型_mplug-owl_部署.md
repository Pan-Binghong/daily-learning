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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CX6BUWC%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICVJaKB9EBemekG0f91SjJe%2BpzOnqNuAGdOBe632jHZUAiBAitnxJnBMGYvr2NMDywl9n5WD4bbq%2BnGX1LfzODcIkCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0lr%2BQENhsCMqi0QKtwDZzdy0EyHAbOW%2BSaDgJG9GXHwn7Caby3xAFpaiWxQY5cSPaF61dWi%2FgdfXZS%2BSCrKfK2ku4LCuACHX4aR4goxEe2sW7KRzcRjJoPa1uMchEoTxwaaTemwVf6bmf%2BW76NM0TzyPeSXDlIkQfZexMcAnv9l39L7OpVtSvQh6tlKJa7iKs5VEPMUtz3mTqQC0Tdd%2FgB8aG2blGtQCjGIP47hZeLBz5Cx54MPJ6OHDBWIX01WWW6wxnjKl15%2BnX7%2Btza3Pp9TZz1hjbXOcM5Dyt2woRrdTi7aV4pwvvKoOmybHi5p%2Bree%2Bu7RYbj0BxmMHNi6XuiOfz9ipf0dHRl9eO4QqPbQkcA3CJxhMRkNN19gnXFNKH%2FFjLOJUhg32Mm6qLCSaol%2Ft23z2Uu6DO9qdipa%2BXeXZl2562iRtQMYBL3HYP0PZHAJVVneaSHk1Lz0VAngxM1zwzKH8f7I%2FEveok3HVcV5sy8B48LhnPKOG4SDSsV%2BH6B2TC1%2BlckDXKflX3nWGGHsb5aZCurh0KHzX0F1TIfyQCulnNw6OwvAfVYaroUZb2AM8ImGlDmS%2FaGHcoLitQeT5mmJs0vZMCxUpaKwv0kXLgaDZx929PMsouWUYezdxk56p3ZoWOyMhqcw29jAywY6pgFPtfbEPKY7P0BwCArVswtIJOGQn2MeDASW149vKtqCz3Fq01sq%2BgMoZ0ohVjoc5XUhgpFKv%2BuNX%2BcyQlYCFRCKzYMRvYAtDE9HLRmU5mmK8KEJ981C2sNeVMHBbvgv8afw8LJkwsbieQ8rZ3j5J7Y5mcTm9nc1znCZSZRjGYQ4JKAl7%2BHtZAYEzc003BJcTOUKCrK5jhHm4gtaZspJOOAd9tvS3ObZ&X-Amz-Signature=c9c920f062439dc41e35c437c4f7b078b17f16577318149b1f642cc4bdc3829f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CX6BUWC%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICVJaKB9EBemekG0f91SjJe%2BpzOnqNuAGdOBe632jHZUAiBAitnxJnBMGYvr2NMDywl9n5WD4bbq%2BnGX1LfzODcIkCqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMy0lr%2BQENhsCMqi0QKtwDZzdy0EyHAbOW%2BSaDgJG9GXHwn7Caby3xAFpaiWxQY5cSPaF61dWi%2FgdfXZS%2BSCrKfK2ku4LCuACHX4aR4goxEe2sW7KRzcRjJoPa1uMchEoTxwaaTemwVf6bmf%2BW76NM0TzyPeSXDlIkQfZexMcAnv9l39L7OpVtSvQh6tlKJa7iKs5VEPMUtz3mTqQC0Tdd%2FgB8aG2blGtQCjGIP47hZeLBz5Cx54MPJ6OHDBWIX01WWW6wxnjKl15%2BnX7%2Btza3Pp9TZz1hjbXOcM5Dyt2woRrdTi7aV4pwvvKoOmybHi5p%2Bree%2Bu7RYbj0BxmMHNi6XuiOfz9ipf0dHRl9eO4QqPbQkcA3CJxhMRkNN19gnXFNKH%2FFjLOJUhg32Mm6qLCSaol%2Ft23z2Uu6DO9qdipa%2BXeXZl2562iRtQMYBL3HYP0PZHAJVVneaSHk1Lz0VAngxM1zwzKH8f7I%2FEveok3HVcV5sy8B48LhnPKOG4SDSsV%2BH6B2TC1%2BlckDXKflX3nWGGHsb5aZCurh0KHzX0F1TIfyQCulnNw6OwvAfVYaroUZb2AM8ImGlDmS%2FaGHcoLitQeT5mmJs0vZMCxUpaKwv0kXLgaDZx929PMsouWUYezdxk56p3ZoWOyMhqcw29jAywY6pgFPtfbEPKY7P0BwCArVswtIJOGQn2MeDASW149vKtqCz3Fq01sq%2BgMoZ0ohVjoc5XUhgpFKv%2BuNX%2BcyQlYCFRCKzYMRvYAtDE9HLRmU5mmK8KEJ981C2sNeVMHBbvgv8afw8LJkwsbieQ8rZ3j5J7Y5mcTm9nc1znCZSZRjGYQ4JKAl7%2BHtZAYEzc003BJcTOUKCrK5jhHm4gtaZspJOOAd9tvS3ObZ&X-Amz-Signature=5e75a639f349d7d2680530da8431c3c54375490d9850ce989081468200efcf8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

