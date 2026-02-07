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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TDHYC3J%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4cN%2B1PhHXjpiuhcL4d9d4qhV8StK1VjAZHC%2B4ddcjnQIhAIkO87O8MHFIzei6xkwshd%2FaXde%2BWpfBh247uPlGZ07rKv8DCFMQABoMNjM3NDIzMTgzODA1IgxoxrhiRAFR4kLgjRIq3AOv3OQ2bhKUnsfiLNMN2Ed8nDDA25WxAZFtc%2FRmzC7IDGXwFNYMrUEQYEnmTNz%2FFa7qAvGX%2FhpHn%2FUhIvX63zCicm7IDypf%2FbrDvtHOT0kU4Z1cAHZ2extybC4RowJ3xKdljO7D2RDhiVCqAPuX1gI95AWJNbbmxfUHpk78q5IncKhjYHTiMjgSi1wGnXjCpDOVIS2gt7gQbRMg96T%2FIUryicKg5wX4PF%2Fd2IXaSTkaQs0d%2B%2B43GOfyyuqaycybDI9cyG9q%2FbxWIjjtXbxxFNO85MQCNQC3KGwRpEG%2Bgqhz9NZiUrDJmZh3bD%2FJbckur%2F9hWsrvsd%2BvRHGmDgCYS0Y6unszvLM0%2B5jsGIuh3dyPa%2FKaVLtliette7J7X%2Fk0I%2BUcO9Kj%2BGSPCVgeQwSQdxmu266MPUVgh65rmLCqRWshrz2%2BLlz%2FezORiALPUR0784n%2BnIrEMDrNE0sCAA4ZTwCDCH%2FFXYtDh2wCTj2nkwGMgPoVyF4jkYe7lI5U0ehpLe9xAwnil%2FdFMT%2BIodLxw8FVy6CGK1CKUJMwBdrltXxiB4GlV9o58noLnjIDfUCf4Cznb%2FlQ%2Fpocn7pQKbwuY82Cs5oSBz6hgpjkJHjf3KNSWYbCMPkE3yOYSyTfTDCDxJrMBjqkAc%2BiP0oY6oiPjahp5%2FiwIAZ8Gs4J%2FKQXh6sX9AemLEnhyB3fdy0ss2hohIZTgtg6Ki7XnPBQfE7aUhx64b47cF47a2dMkkotpvcftnu4RpJYxEfG0Zb%2FyN91HvW85lnPO0KPbi08YDG5kDrbWhDPiMnJuUbyeCapLDxMHaJwMpo8HowBiUb4Lzdlsa4W7wwelh%2B1E101ei2jcq5Fo%2FTKns6D4vZf&X-Amz-Signature=90358b856026815a7814e5bd09101bb94c5c389feb019dcb1433fa4f103f3688&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TDHYC3J%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4cN%2B1PhHXjpiuhcL4d9d4qhV8StK1VjAZHC%2B4ddcjnQIhAIkO87O8MHFIzei6xkwshd%2FaXde%2BWpfBh247uPlGZ07rKv8DCFMQABoMNjM3NDIzMTgzODA1IgxoxrhiRAFR4kLgjRIq3AOv3OQ2bhKUnsfiLNMN2Ed8nDDA25WxAZFtc%2FRmzC7IDGXwFNYMrUEQYEnmTNz%2FFa7qAvGX%2FhpHn%2FUhIvX63zCicm7IDypf%2FbrDvtHOT0kU4Z1cAHZ2extybC4RowJ3xKdljO7D2RDhiVCqAPuX1gI95AWJNbbmxfUHpk78q5IncKhjYHTiMjgSi1wGnXjCpDOVIS2gt7gQbRMg96T%2FIUryicKg5wX4PF%2Fd2IXaSTkaQs0d%2B%2B43GOfyyuqaycybDI9cyG9q%2FbxWIjjtXbxxFNO85MQCNQC3KGwRpEG%2Bgqhz9NZiUrDJmZh3bD%2FJbckur%2F9hWsrvsd%2BvRHGmDgCYS0Y6unszvLM0%2B5jsGIuh3dyPa%2FKaVLtliette7J7X%2Fk0I%2BUcO9Kj%2BGSPCVgeQwSQdxmu266MPUVgh65rmLCqRWshrz2%2BLlz%2FezORiALPUR0784n%2BnIrEMDrNE0sCAA4ZTwCDCH%2FFXYtDh2wCTj2nkwGMgPoVyF4jkYe7lI5U0ehpLe9xAwnil%2FdFMT%2BIodLxw8FVy6CGK1CKUJMwBdrltXxiB4GlV9o58noLnjIDfUCf4Cznb%2FlQ%2Fpocn7pQKbwuY82Cs5oSBz6hgpjkJHjf3KNSWYbCMPkE3yOYSyTfTDCDxJrMBjqkAc%2BiP0oY6oiPjahp5%2FiwIAZ8Gs4J%2FKQXh6sX9AemLEnhyB3fdy0ss2hohIZTgtg6Ki7XnPBQfE7aUhx64b47cF47a2dMkkotpvcftnu4RpJYxEfG0Zb%2FyN91HvW85lnPO0KPbi08YDG5kDrbWhDPiMnJuUbyeCapLDxMHaJwMpo8HowBiUb4Lzdlsa4W7wwelh%2B1E101ei2jcq5Fo%2FTKns6D4vZf&X-Amz-Signature=c448929b7c98a18f0911587dda87991dd000f7ab7a6c4054c3b95663e4c8fdf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



