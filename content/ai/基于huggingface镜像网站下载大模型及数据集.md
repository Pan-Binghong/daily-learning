---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
标签:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVN4RF4V%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlD6mEQRpTTdiH1N%2Bq%2FxGpzainpEZ4tubXqJLX3UpWTAiEA8C12Eh%2FlI49%2FirGfM1L%2B%2BxcVvXoD1tGdfdxvSFuXH70qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfMjTir8uMHIfrplyrcA6Xe9gIceKQ7SwYJR%2F9Vpj6QN9RJL2AVXbiiMebqo7k8PrAEIDLnhsqAqCU%2BfhTzcsmTF7dpaPX1%2BB%2Fq7vpSwC7kJi26FwYnJEjLTo5HGeJPfn05VRxbKRnBt1X42sO0Z%2BxKPMAOa%2FziQ5XH%2FHcer9aUf9MdGvvuiec2ZiJtUy0cSZqWmoJsxdwOBs%2FzYdjV4xfcf3ZmLj8vvdpciRbCBWPgc9beFMAIVKGbkP2YWriddY1XOQn4XfHvmAKprPGDa5PwUcgwmI7GphNNT5EOAy56lpxEtIPv8GLnvNG3V%2BlaahiRq3BD9fC%2Fyzg3JfH%2FtmavlqCRDaqtcgdwRTIklB0VHZ%2F8kkhFIlBEas7dSqIfSzACu3VKIT8EHQer5upvsvHJiRpgbwv1Y3H7V7pV94bByK8n2OBk0L7rcKPuSotBdBYke%2F7J4at3ADoHtnpKL%2FHqZVN9NsQOigUZF6E110YDvjU%2Bl%2F%2FtOnluYACkORL6%2FCLfTMhbq2WZS%2BbTd5YfeRQPAe%2Ff6%2Ftdl7e2f%2B4oYrgQntiGkdO%2BrHUdD4kA5SbOJb8ETkfq2LvYUInz%2BqcIWw8lcQT72uZGfDtKBkqRXVszGI8L6JKNKcWgL7Qr0DKqUzfADaMzW5YWXotcMPWirMgGOqUBNG0tRSpNqkiHXpVlsLWhGKdfIxqHSbVA7g3lMUoRTN6TxtMlQ0UcwWFzx3M%2F02Elpa54AxBALfHKRVyXH%2BxsMTOhAswLlpsiH%2Fd061hi6z09f5%2B0m84sBjEI6Wi8YANDvPuNg7X6ipuxkG68qWSjmDyzmyCLpnufju15Mr%2Bz1Bxv7fqe0uMoMqiugP9UeRbBRrfqyyigIM2p7oRe1mZ8FuPap58%2B&X-Amz-Signature=1bd35aa50d51f7f666355c5d9e6ce04afef0a083a8c7c4b1a83eeaccf80701e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WVN4RF4V%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAlD6mEQRpTTdiH1N%2Bq%2FxGpzainpEZ4tubXqJLX3UpWTAiEA8C12Eh%2FlI49%2FirGfM1L%2B%2BxcVvXoD1tGdfdxvSFuXH70qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGfMjTir8uMHIfrplyrcA6Xe9gIceKQ7SwYJR%2F9Vpj6QN9RJL2AVXbiiMebqo7k8PrAEIDLnhsqAqCU%2BfhTzcsmTF7dpaPX1%2BB%2Fq7vpSwC7kJi26FwYnJEjLTo5HGeJPfn05VRxbKRnBt1X42sO0Z%2BxKPMAOa%2FziQ5XH%2FHcer9aUf9MdGvvuiec2ZiJtUy0cSZqWmoJsxdwOBs%2FzYdjV4xfcf3ZmLj8vvdpciRbCBWPgc9beFMAIVKGbkP2YWriddY1XOQn4XfHvmAKprPGDa5PwUcgwmI7GphNNT5EOAy56lpxEtIPv8GLnvNG3V%2BlaahiRq3BD9fC%2Fyzg3JfH%2FtmavlqCRDaqtcgdwRTIklB0VHZ%2F8kkhFIlBEas7dSqIfSzACu3VKIT8EHQer5upvsvHJiRpgbwv1Y3H7V7pV94bByK8n2OBk0L7rcKPuSotBdBYke%2F7J4at3ADoHtnpKL%2FHqZVN9NsQOigUZF6E110YDvjU%2Bl%2F%2FtOnluYACkORL6%2FCLfTMhbq2WZS%2BbTd5YfeRQPAe%2Ff6%2Ftdl7e2f%2B4oYrgQntiGkdO%2BrHUdD4kA5SbOJb8ETkfq2LvYUInz%2BqcIWw8lcQT72uZGfDtKBkqRXVszGI8L6JKNKcWgL7Qr0DKqUzfADaMzW5YWXotcMPWirMgGOqUBNG0tRSpNqkiHXpVlsLWhGKdfIxqHSbVA7g3lMUoRTN6TxtMlQ0UcwWFzx3M%2F02Elpa54AxBALfHKRVyXH%2BxsMTOhAswLlpsiH%2Fd061hi6z09f5%2B0m84sBjEI6Wi8YANDvPuNg7X6ipuxkG68qWSjmDyzmyCLpnufju15Mr%2Bz1Bxv7fqe0uMoMqiugP9UeRbBRrfqyyigIM2p7oRe1mZ8FuPap58%2B&X-Amz-Signature=9fcacb6236d1d6831d6f81bbec2b5a0b744eaa8a0c1a27248ba39bb122a2d527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



