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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6GDXSXQ%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQD76RmURTLBj69XFZIWVjtw4pC7%2ByqyrB7s%2BDQIySnd3QIhAPDfurcDZNOCUpYNksm%2BQtTQMuvKllIJxN28j39QT5aaKv8DCB8QABoMNjM3NDIzMTgzODA1Igxyw04YovSL1Ktkvhoq3AOrhoKXkv5WriBH5b90wYC2CSuMctHnZhPG1dM2uHxqoLY0gZpHSbvqnLdNp5u0aXN8ZK4VyE7DKMSbUx8vk73Ta8vLHEzQbLzn2Zp5geRGOkK49EejOFrA9jBBNSTSAL27ed7aGRxE1JOi31qtH1NXZ6SeXkDGL3tyUFKgF8cgt4%2BHvfLbGx0FnMEg%2BJRGNhhfFuy%2BSk1iOxKIGcpjhh8OywkVnM3XfHszdd2276WVLj1ZGZoOADB5qV72bmDOFh1hbn5qFWVN3jICtWJuqnh0WpDpzErHTjMcZsaj6fSsZobykXx%2BjsCUDY7M%2B3qEE53eAJLlm1W1bs2bWfXOlOynW%2BtHDGxiwHzFJXhjCyufA37ht5Edy80U97GBuiMp%2BbTrX5PZ3k8aR%2Fv7XA%2BBJl6ur9kdWt%2F5NvQG26wGGR84S4acD4tYr%2FKlt6LEmicqUu4DT68vnkhZafcW%2F6wASgKEVBCVbpvtyawNs1Bq1jndgzTj0k0cJUcuKQFblqCQcPkGzpwGCPwImHm9K%2BbVrJvyujA0oH47aHse15U4FZgSU5o0kvkvqLl8otl6ktvH8dy%2FfqAT9l7HHQ5UBVQuS01dSYgCgoV00yp3YcGVtyfXTS%2BA7jv9SAiqqf7daTD6k%2BbKBjqkAaLSbHlI0Tdb7YtgeaKl78r0Y7c8LO60dHH%2F3mgjwF8vo9T7gQUUoVzr5yE0KKWR2ez1f7XyRc%2BrPKEbm2GF2qbNesg9j2GDrECl%2FVofVPMN%2FYen7c1yGvyWUz%2BFvuM%2BjWPSjmgeVWV%2B2Uh61DYV4H4enbf3j7rWlwQPrDvRYbBZDT92dJrMpMQnf%2B4pFb3w9TKprdcXoF2MpqCgpyDqst0RDeBU&X-Amz-Signature=910091d54838cda51c259ee119ea40420d0135fb410714a231c618d55632ca31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6GDXSXQ%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQD76RmURTLBj69XFZIWVjtw4pC7%2ByqyrB7s%2BDQIySnd3QIhAPDfurcDZNOCUpYNksm%2BQtTQMuvKllIJxN28j39QT5aaKv8DCB8QABoMNjM3NDIzMTgzODA1Igxyw04YovSL1Ktkvhoq3AOrhoKXkv5WriBH5b90wYC2CSuMctHnZhPG1dM2uHxqoLY0gZpHSbvqnLdNp5u0aXN8ZK4VyE7DKMSbUx8vk73Ta8vLHEzQbLzn2Zp5geRGOkK49EejOFrA9jBBNSTSAL27ed7aGRxE1JOi31qtH1NXZ6SeXkDGL3tyUFKgF8cgt4%2BHvfLbGx0FnMEg%2BJRGNhhfFuy%2BSk1iOxKIGcpjhh8OywkVnM3XfHszdd2276WVLj1ZGZoOADB5qV72bmDOFh1hbn5qFWVN3jICtWJuqnh0WpDpzErHTjMcZsaj6fSsZobykXx%2BjsCUDY7M%2B3qEE53eAJLlm1W1bs2bWfXOlOynW%2BtHDGxiwHzFJXhjCyufA37ht5Edy80U97GBuiMp%2BbTrX5PZ3k8aR%2Fv7XA%2BBJl6ur9kdWt%2F5NvQG26wGGR84S4acD4tYr%2FKlt6LEmicqUu4DT68vnkhZafcW%2F6wASgKEVBCVbpvtyawNs1Bq1jndgzTj0k0cJUcuKQFblqCQcPkGzpwGCPwImHm9K%2BbVrJvyujA0oH47aHse15U4FZgSU5o0kvkvqLl8otl6ktvH8dy%2FfqAT9l7HHQ5UBVQuS01dSYgCgoV00yp3YcGVtyfXTS%2BA7jv9SAiqqf7daTD6k%2BbKBjqkAaLSbHlI0Tdb7YtgeaKl78r0Y7c8LO60dHH%2F3mgjwF8vo9T7gQUUoVzr5yE0KKWR2ez1f7XyRc%2BrPKEbm2GF2qbNesg9j2GDrECl%2FVofVPMN%2FYen7c1yGvyWUz%2BFvuM%2BjWPSjmgeVWV%2B2Uh61DYV4H4enbf3j7rWlwQPrDvRYbBZDT92dJrMpMQnf%2B4pFb3w9TKprdcXoF2MpqCgpyDqst0RDeBU&X-Amz-Signature=87feed82b453eec06353e62a75cb26f0e8001a5ef91a43988068729cbdfb2c62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



