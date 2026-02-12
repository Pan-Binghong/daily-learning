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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V7O6BPA%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIAlH2wxCnQLwVWIOLvciFI%2B%2BlwTdm2ifoNLqmez%2Bjcg9AiAcx7zB3ERfml7aEcutLV0w%2FDwvuLpaKEk8tBq82JEiwCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3iwq%2F%2BbLg42O19CQKtwDl192HfXGV9vjhL3QEFGXQbN12f9O44zNCJTylQ0WVCKJNTNwf%2FB2KK2I7kKOuNvLkY3dQj8FhkCl9IAw3ZA8TZc3EE93XGIW9sgPLFVqTDDhHcoxF6vp4hPUtTRaCciVXGX2snfi5CHi970ZNUMdYuMfoBs9PHaiSK%2FNNyG2OKNJPKixt0R3xTde%2BgyT4h68oGTsZhcNZcDuqclE5naI61E5FQVfCmALkxq%2BQLpKNS6AU0EN9W6r5%2Fp1J0QKo4lM8kDKHtjQA%2FxdQ3JAjfux%2BmgHipw7MD3MoYEb3AyknJbB8mgCdh4BUvBLHvdWk1WhE7xPEu5tKmoB%2BypKIeq5zvSjnSwJz3uhXVrakZFBg5gD6VXXCNXTWH3Zahh%2FkDo2YnmhFsK6xgx4cEzSFTvv6Z%2BYM8P0PnR7m464sOa5CN7WVT4UZ4ApHwLkX7ZG%2BTtA3dKKF5ElaISZ3j%2Fvq6PTMdZHYCv6V42uxoNg73Wo9TBIXoa2bcbOgYV3MkUZiNpeFPo5XGcT32cCTA%2ByM5ascN%2FpL4wVQRq%2BC6OC%2FknuzHDEKgNto4slHlie7KaqssV2rOJhN1M7vNTuaRF8w9MQA%2F5p%2BtEmpoO4vQzQxskgc15deKm%2BGU1fQmmEbVMwzZK1zAY6pgEP6%2F2ra6mdltf7V%2FN9lDCa4aNmH5yvqJn%2Fcksw2EV45CbCAcmYIxhy2%2FFNcmKvvPhbq9wmlv25sY3c3EuZItsC6ytHZQ5qQHAgvl%2BkUtgk9wa5t8W82QTDMZmm%2FUTg3uRJ9rI12bcAtPRIOy5XF7Vwm8n6hk5lqSHo3X22QalFiFrmIUYueDZW9O9m0pgp6mkKuU4KzqI68Cln9kb4ojZ1TxRM3IL2&X-Amz-Signature=517d87dde0f19196626a387d5e8a11c80ae805f819ceb1dc0d27e70bd9a8a80a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V7O6BPA%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIAlH2wxCnQLwVWIOLvciFI%2B%2BlwTdm2ifoNLqmez%2Bjcg9AiAcx7zB3ERfml7aEcutLV0w%2FDwvuLpaKEk8tBq82JEiwCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3iwq%2F%2BbLg42O19CQKtwDl192HfXGV9vjhL3QEFGXQbN12f9O44zNCJTylQ0WVCKJNTNwf%2FB2KK2I7kKOuNvLkY3dQj8FhkCl9IAw3ZA8TZc3EE93XGIW9sgPLFVqTDDhHcoxF6vp4hPUtTRaCciVXGX2snfi5CHi970ZNUMdYuMfoBs9PHaiSK%2FNNyG2OKNJPKixt0R3xTde%2BgyT4h68oGTsZhcNZcDuqclE5naI61E5FQVfCmALkxq%2BQLpKNS6AU0EN9W6r5%2Fp1J0QKo4lM8kDKHtjQA%2FxdQ3JAjfux%2BmgHipw7MD3MoYEb3AyknJbB8mgCdh4BUvBLHvdWk1WhE7xPEu5tKmoB%2BypKIeq5zvSjnSwJz3uhXVrakZFBg5gD6VXXCNXTWH3Zahh%2FkDo2YnmhFsK6xgx4cEzSFTvv6Z%2BYM8P0PnR7m464sOa5CN7WVT4UZ4ApHwLkX7ZG%2BTtA3dKKF5ElaISZ3j%2Fvq6PTMdZHYCv6V42uxoNg73Wo9TBIXoa2bcbOgYV3MkUZiNpeFPo5XGcT32cCTA%2ByM5ascN%2FpL4wVQRq%2BC6OC%2FknuzHDEKgNto4slHlie7KaqssV2rOJhN1M7vNTuaRF8w9MQA%2F5p%2BtEmpoO4vQzQxskgc15deKm%2BGU1fQmmEbVMwzZK1zAY6pgEP6%2F2ra6mdltf7V%2FN9lDCa4aNmH5yvqJn%2Fcksw2EV45CbCAcmYIxhy2%2FFNcmKvvPhbq9wmlv25sY3c3EuZItsC6ytHZQ5qQHAgvl%2BkUtgk9wa5t8W82QTDMZmm%2FUTg3uRJ9rI12bcAtPRIOy5XF7Vwm8n6hk5lqSHo3X22QalFiFrmIUYueDZW9O9m0pgp6mkKuU4KzqI68Cln9kb4ojZ1TxRM3IL2&X-Amz-Signature=d6068b4b1d2a3ebae42a340df1b1ecd93e4217951ba32bfb5d1ff05e46b2d048&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



