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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JAVDX4X%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbRVTv2VqZh0E%2BjoOodiCqfiaAWE12x0j2VUW55yVKyAiEAgaIWD%2BsFsX0CvJ689RFEaLoNtNiTJ0km9l4wQzaiGHkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDP1eSgiwku1tDUwLJyrcAwH1AlhosinJfZL4Dlthm5QX3iOvo0opwy5spGAT7rk22vFWEzLAnkfh9%2Fh5dhEQvhKULjTWCxVRl7uzorFbK1EIjzXzaS0saI2GPKUhm7qxopLthlsGUmqWXWCbZWcOSsOxT%2BfeF967WOLrY%2BBHjfQ5mLHWhz%2BPV%2FjLNTDyvd0vPI1tryjb73HrBkckd5aK%2FSWIDpF4fyISIZkNKZxcDD6TQMM%2FUXU1%2FsNu702hQZ0D1p3nXdcTaehbDfCcndBe46Jg8FLod232HfbRSa%2F7KiwouZ7qct3jUxwQ%2FKZUCQxTkeit3tdrJkLrs2JINizpl8l7Mna4rl4s9cKq3WIQ8M%2FzCBhR9JxCIQqK4Vb%2Bx5o%2FwsGnoBa4xZ%2FSigEh4faDyjDrdx1dWCvOBccU4HTDstK9vP3%2Fjs9fPIFrywrD4dDqP3UCWMosRTX%2F9AdbQV2U85dhO3KnEK%2FdoDQRI%2F1V42YlfIqQhX5CN0ufOCGEk48oDtl4kgvxAR13iba5d9vVaTMr6X9r28QuXpnC%2FpnwDr0oZmbZH9lsHFucm85X7OrfUw4KfNSi0D%2BSnpFDPCio%2BvFbF%2Ba6iOCqbIZrqTvJw6OXXm7ru5VvlTtPwKV43VCXzkOCAVLBijxtn3ZUMLWnzskGOqUBbnUVncOrZV9rlVMSJW6N%2FP4mgZeGTYskQwBE3Fx350GaO%2BtlWKGVFAWZNxldHkGIM9I0VTf1xKNwS0%2B2EVyeBgfQ9mgctZM%2BaN8ZeDv2Ih7QuupqEJkbBjaoyw%2B3Htkb4e%2FbTmc%2FcoR0qbW8tb12aXMhM7mXG0OH5gHrdi7zwQATSNfXfO4mSKQeZjaOJqwbUgcS0qvUy9GX%2Fqb%2BbOYHcyWE4vPm&X-Amz-Signature=5f2a21effc3dc1b2b98092301e512526009d0095bae04771ba0061b5418064c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JAVDX4X%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHbRVTv2VqZh0E%2BjoOodiCqfiaAWE12x0j2VUW55yVKyAiEAgaIWD%2BsFsX0CvJ689RFEaLoNtNiTJ0km9l4wQzaiGHkq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDP1eSgiwku1tDUwLJyrcAwH1AlhosinJfZL4Dlthm5QX3iOvo0opwy5spGAT7rk22vFWEzLAnkfh9%2Fh5dhEQvhKULjTWCxVRl7uzorFbK1EIjzXzaS0saI2GPKUhm7qxopLthlsGUmqWXWCbZWcOSsOxT%2BfeF967WOLrY%2BBHjfQ5mLHWhz%2BPV%2FjLNTDyvd0vPI1tryjb73HrBkckd5aK%2FSWIDpF4fyISIZkNKZxcDD6TQMM%2FUXU1%2FsNu702hQZ0D1p3nXdcTaehbDfCcndBe46Jg8FLod232HfbRSa%2F7KiwouZ7qct3jUxwQ%2FKZUCQxTkeit3tdrJkLrs2JINizpl8l7Mna4rl4s9cKq3WIQ8M%2FzCBhR9JxCIQqK4Vb%2Bx5o%2FwsGnoBa4xZ%2FSigEh4faDyjDrdx1dWCvOBccU4HTDstK9vP3%2Fjs9fPIFrywrD4dDqP3UCWMosRTX%2F9AdbQV2U85dhO3KnEK%2FdoDQRI%2F1V42YlfIqQhX5CN0ufOCGEk48oDtl4kgvxAR13iba5d9vVaTMr6X9r28QuXpnC%2FpnwDr0oZmbZH9lsHFucm85X7OrfUw4KfNSi0D%2BSnpFDPCio%2BvFbF%2Ba6iOCqbIZrqTvJw6OXXm7ru5VvlTtPwKV43VCXzkOCAVLBijxtn3ZUMLWnzskGOqUBbnUVncOrZV9rlVMSJW6N%2FP4mgZeGTYskQwBE3Fx350GaO%2BtlWKGVFAWZNxldHkGIM9I0VTf1xKNwS0%2B2EVyeBgfQ9mgctZM%2BaN8ZeDv2Ih7QuupqEJkbBjaoyw%2B3Htkb4e%2FbTmc%2FcoR0qbW8tb12aXMhM7mXG0OH5gHrdi7zwQATSNfXfO4mSKQeZjaOJqwbUgcS0qvUy9GX%2Fqb%2BbOYHcyWE4vPm&X-Amz-Signature=d4289d945a6346e3002fd41ab1dcf09b4e06f534af317d0c675bd4079ede61fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



