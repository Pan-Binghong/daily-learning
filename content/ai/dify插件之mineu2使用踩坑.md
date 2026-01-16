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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYRA3OCF%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCmv963Oor1ytKDv86ecl51u1y%2FTNfiXYufRu0cXn7IlgIhAJppiFXMQBDdLrZ4YyXiYS10EY3yrqw6BXPUvOgu1GX%2FKv8DCEMQABoMNjM3NDIzMTgzODA1IgxlK7MePvbYfAzQieMq3AOCLOm63ePtW3HK15P%2BFWnYrgHj9qgTHHr87H7%2FXkMY9XzxZeJB2vrLvQ5JpCIDDU1gQHyLRjep6QDPqyWR51GLjbTWcyvRZsG7j42YI6HpclsUEhwd9e2CDTZ8QZf%2F54wq8%2F8pPQxxSgzYaMB2VCHDD%2BFhBU4cSYItkDdY19cJExQSpMial94NyFltv4o%2BAAZCMD1p5Huhh%2BWm6%2Fbp9taW3DVx1x62UTq6cUPcJ5h%2BoT%2FC0dqkGPgnq4aPgiCE5PzrVj8TIotlZXD3oE4odp%2FzP41wS6dCvzJyYC3%2BY%2F8%2Fad2RSmBd7ySWZAU42HIfAsPUjOXRDO%2FEJ%2B5b9gPIm1KZrRfg0OppDQyZluQRqGfZc3EOAQ8h1M2OGya9c5nz9nDDqVvuPX05fbaSwjI%2BKwXaNpaQ6qSZN70IUYorhDFUw334zJ5pMZ9aVtwNqkouSyWaUXJhEjDEaiQl4ZCS8cqzNdA2hUWHHZZiZ6w2VS0xV5Jy2pEsQgMZsXG%2FCZFW8Ek6F7W8kv9NfIHu8c8MP8w9rKf49C8UK91aPpLWfJ86J0i3uGmNYICc37Wlo%2Bw%2F1iUJtiZ%2FMgBHHJmxECDEwKi4xLrBCllCvC07dQJ62TtfF3kjK5E%2Fgo0m6w47mTCVwKbLBjqkAdS4nridK8fGSgSG8e%2BK7Hiajo3%2FbvcSItrv989UTj0Ffjkmzxq28hczpB5yewjsBnvw25zCLxxtrMi%2F5DrkUBVX0A7YSD5FFH2JQ8K6mOtj%2FesoezG9ag26WW4qZMkua3CGFD66I69yxZ77rCpz3WyAbmyg%2F1rAkglga0aLdlwvNk%2B%2BQzp0834kksAeUWNmwmMjxFTXsr7jZRAYf7I0TvXGzXMR&X-Amz-Signature=b70a80a762c987abb09dbe1f31fbf2db9849730db9cc92cdce7b03e948cc1080&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYRA3OCF%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCmv963Oor1ytKDv86ecl51u1y%2FTNfiXYufRu0cXn7IlgIhAJppiFXMQBDdLrZ4YyXiYS10EY3yrqw6BXPUvOgu1GX%2FKv8DCEMQABoMNjM3NDIzMTgzODA1IgxlK7MePvbYfAzQieMq3AOCLOm63ePtW3HK15P%2BFWnYrgHj9qgTHHr87H7%2FXkMY9XzxZeJB2vrLvQ5JpCIDDU1gQHyLRjep6QDPqyWR51GLjbTWcyvRZsG7j42YI6HpclsUEhwd9e2CDTZ8QZf%2F54wq8%2F8pPQxxSgzYaMB2VCHDD%2BFhBU4cSYItkDdY19cJExQSpMial94NyFltv4o%2BAAZCMD1p5Huhh%2BWm6%2Fbp9taW3DVx1x62UTq6cUPcJ5h%2BoT%2FC0dqkGPgnq4aPgiCE5PzrVj8TIotlZXD3oE4odp%2FzP41wS6dCvzJyYC3%2BY%2F8%2Fad2RSmBd7ySWZAU42HIfAsPUjOXRDO%2FEJ%2B5b9gPIm1KZrRfg0OppDQyZluQRqGfZc3EOAQ8h1M2OGya9c5nz9nDDqVvuPX05fbaSwjI%2BKwXaNpaQ6qSZN70IUYorhDFUw334zJ5pMZ9aVtwNqkouSyWaUXJhEjDEaiQl4ZCS8cqzNdA2hUWHHZZiZ6w2VS0xV5Jy2pEsQgMZsXG%2FCZFW8Ek6F7W8kv9NfIHu8c8MP8w9rKf49C8UK91aPpLWfJ86J0i3uGmNYICc37Wlo%2Bw%2F1iUJtiZ%2FMgBHHJmxECDEwKi4xLrBCllCvC07dQJ62TtfF3kjK5E%2Fgo0m6w47mTCVwKbLBjqkAdS4nridK8fGSgSG8e%2BK7Hiajo3%2FbvcSItrv989UTj0Ffjkmzxq28hczpB5yewjsBnvw25zCLxxtrMi%2F5DrkUBVX0A7YSD5FFH2JQ8K6mOtj%2FesoezG9ag26WW4qZMkua3CGFD66I69yxZ77rCpz3WyAbmyg%2F1rAkglga0aLdlwvNk%2B%2BQzp0834kksAeUWNmwmMjxFTXsr7jZRAYf7I0TvXGzXMR&X-Amz-Signature=f75ddd9479b067e1342a9c0ca8999a357af9931bd39d957ce86163adf40e5a5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



