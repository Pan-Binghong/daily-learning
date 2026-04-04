---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7SFYE5K%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB3ror6s2sxClYEbK0y4F6%2F37rHJOPbyN1ckODKCSDsIAiAS%2BVj0hLlmg7I89nPiwbFSVfqghcQihPZF%2Fh8stVvfxCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhmqPpexBmyVUUmc5KtwD1tLP3VW53vcjFcYNFdcoeX6oNPzxvpGLuS7NeSiiFcNe%2B7FgDnE%2BffHG8VproU1mf1rwk3CKL67GhTAkGMF7NvS3hm99msZjXkmKlfB9L1Z5gx3Qr144VVnAufcvC%2FHkJhcUbv4YjYHFwi%2BhUhETX1GipJs3NJoBJlBJC8we79B%2BVmbQO8B%2BO98aVcAScbtzint2tT6sVlxjgJggqMn2%2Bls6j%2FQVweLp72Gt%2FbC91HCVI1W6rLchOmb6Uxh22lPKKsVaQ5x1zvBPrahgtbB4ixb58EVp%2BEuADR1LTt8iaBQP9S4x00ukMRwp5MYKfcBcNt9UO4mDf12Pu%2BPYAqpJ16z8ekdfdqUutuTQzjqxaNkoTCZuQ13Ard6akRAqnauof3nDyRvfCiXB9CE8cQvvAYym1uv4f%2BZHwRVCj66jqNA64ytY1PBrIlV3JK3U%2B7BnR4g7eENv%2Bee3MpJTRzLKLvizvxt16lGHAxC2lreowBCVz4U8gYMr9J%2BWZDz4estWvVgitysFY64k2ZhCXMeeedGmCyr4cxsNFSPGg3jUp3S2h97yPSoS2NyS0cwDELaljjrj3zaDWS6bXyy%2F4Dotj70JISqjDLWLahmqGXu8R34SGxBFD9nRWWq4xeUw0oDCzgY6pgGSXPpVtbQyMX%2BzYwwx2A6wTcEksHZO4CnMR4YGzsAVXmE1JGJVsq1JArjzyT3CH%2FIuqwcAr1cIQErlA%2F6Rgz1GpaNHR3PsV7tb0fIFxcu%2FKhl%2BbM2aLXQa4SeqRxCrKx9G%2FuYT%2B3VFAiQv6MPCAfbs3IkL%2FdkH24K0XgTuSDPrhNJvceyBsz0kINiCu3P%2BuAUogr8DuuLXe%2B2S0QLJqzSdEH1s3HCA&X-Amz-Signature=5dacce6c7c1faa4b642cabb2e2dc7e2b46b3769d28c3332a08141a6051edec60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7SFYE5K%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB3ror6s2sxClYEbK0y4F6%2F37rHJOPbyN1ckODKCSDsIAiAS%2BVj0hLlmg7I89nPiwbFSVfqghcQihPZF%2Fh8stVvfxCqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhmqPpexBmyVUUmc5KtwD1tLP3VW53vcjFcYNFdcoeX6oNPzxvpGLuS7NeSiiFcNe%2B7FgDnE%2BffHG8VproU1mf1rwk3CKL67GhTAkGMF7NvS3hm99msZjXkmKlfB9L1Z5gx3Qr144VVnAufcvC%2FHkJhcUbv4YjYHFwi%2BhUhETX1GipJs3NJoBJlBJC8we79B%2BVmbQO8B%2BO98aVcAScbtzint2tT6sVlxjgJggqMn2%2Bls6j%2FQVweLp72Gt%2FbC91HCVI1W6rLchOmb6Uxh22lPKKsVaQ5x1zvBPrahgtbB4ixb58EVp%2BEuADR1LTt8iaBQP9S4x00ukMRwp5MYKfcBcNt9UO4mDf12Pu%2BPYAqpJ16z8ekdfdqUutuTQzjqxaNkoTCZuQ13Ard6akRAqnauof3nDyRvfCiXB9CE8cQvvAYym1uv4f%2BZHwRVCj66jqNA64ytY1PBrIlV3JK3U%2B7BnR4g7eENv%2Bee3MpJTRzLKLvizvxt16lGHAxC2lreowBCVz4U8gYMr9J%2BWZDz4estWvVgitysFY64k2ZhCXMeeedGmCyr4cxsNFSPGg3jUp3S2h97yPSoS2NyS0cwDELaljjrj3zaDWS6bXyy%2F4Dotj70JISqjDLWLahmqGXu8R34SGxBFD9nRWWq4xeUw0oDCzgY6pgGSXPpVtbQyMX%2BzYwwx2A6wTcEksHZO4CnMR4YGzsAVXmE1JGJVsq1JArjzyT3CH%2FIuqwcAr1cIQErlA%2F6Rgz1GpaNHR3PsV7tb0fIFxcu%2FKhl%2BbM2aLXQa4SeqRxCrKx9G%2FuYT%2B3VFAiQv6MPCAfbs3IkL%2FdkH24K0XgTuSDPrhNJvceyBsz0kINiCu3P%2BuAUogr8DuuLXe%2B2S0QLJqzSdEH1s3HCA&X-Amz-Signature=1d1d73bf48f02ae4a53a680095244955d0fe06cc3fcc9be0f38454a2e6f1f185&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



