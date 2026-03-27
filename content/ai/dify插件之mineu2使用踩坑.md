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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3JG7QEH%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDSbz%2B8gVQ9VSdCmgUD%2F3Ra5HlxbU9WF6oGNRNqDmfksAIhAJC11PqcUAuImDbGhMLUWQjtcr3x1Bj76ibDnKIVzGf8KogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcQLPvsV%2B6cVaG6z8q3AMizxMfHy0SObMR0hoYeMaWpX0gYsXta4dawTj8CvUrggvibfCO9yMpwDqD98SCSBhkXRfCFtXk9VqvDC3W9s2tioEzQHK34NSMqQ7jTsusrytHVHYSauceupFwa1xW0VMeJ%2Bpsrj0VDsd61hRxf1RUzxopGT1vgmvaMRJrMv4Vi5cNMs5RnIzFtfN1iq3%2BLha5mpxU%2FhExAAboRVJdKXLIIAPRv2GCQghdt0peAAfj87jzbUznqj6jkEt2Eo54MZFSt%2Bpf6eu2AVyYgYwwh1wvvwxAfwlPzvWwll8q6a%2B%2FX6Dq9jWsur%2F05ZFwfTuzArZymY9M9gxDy%2BzuBM2WKhVBasu9B34Rd%2FqXdtoP99VHNPOBSkD1117bSMX83%2F2fA1Cio%2BfMj6DsAOHeIga4FJaLRPX6Fpu6eVbgnwRgG6HAIlJ338Rb9zjh5NhlVTbDtEkCRWfuTsk2DMQ1P80uye%2BgNKXekcksndMgVEGZaMZjHBkeyLTHZb5tztFv8NvXgVy7jQOBiNowLwKlV2siz1G0UKK4di71ddaxaoeu2fk3pp6ZWURBpJ6DMxsQyLahqJlsN8oeO70BFFBcXCbbq%2BJkXmGwAZulinubdLw0fVUAZHVQbqKHVw25Wy8bXDDy7pbOBjqkAb%2B6OINX9ci7AxuuITYiPx%2Fvhnbdl10NEJj0GY8jcZRUExen8jup%2BQvL5w1%2F5Q0Aak2P5D8GsrIp2zlwbz8pKsk5AUxWZN84y%2BOQqKevPZqDThTHJMjud4Iq1mUmyqLAlideBwgDSlHHc9pZQok2xJrnbfqNSKTfcGPduWrMg27dpynb8cTM7RWE6RmvOS%2B5FLtQIQZSG66W%2FYrZ0ONl5rx%2FR6s1&X-Amz-Signature=7a695249269e56585ce4fa2b815e806f361da2d70d0e60e2058b290e21525ad7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3JG7QEH%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDSbz%2B8gVQ9VSdCmgUD%2F3Ra5HlxbU9WF6oGNRNqDmfksAIhAJC11PqcUAuImDbGhMLUWQjtcr3x1Bj76ibDnKIVzGf8KogECND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcQLPvsV%2B6cVaG6z8q3AMizxMfHy0SObMR0hoYeMaWpX0gYsXta4dawTj8CvUrggvibfCO9yMpwDqD98SCSBhkXRfCFtXk9VqvDC3W9s2tioEzQHK34NSMqQ7jTsusrytHVHYSauceupFwa1xW0VMeJ%2Bpsrj0VDsd61hRxf1RUzxopGT1vgmvaMRJrMv4Vi5cNMs5RnIzFtfN1iq3%2BLha5mpxU%2FhExAAboRVJdKXLIIAPRv2GCQghdt0peAAfj87jzbUznqj6jkEt2Eo54MZFSt%2Bpf6eu2AVyYgYwwh1wvvwxAfwlPzvWwll8q6a%2B%2FX6Dq9jWsur%2F05ZFwfTuzArZymY9M9gxDy%2BzuBM2WKhVBasu9B34Rd%2FqXdtoP99VHNPOBSkD1117bSMX83%2F2fA1Cio%2BfMj6DsAOHeIga4FJaLRPX6Fpu6eVbgnwRgG6HAIlJ338Rb9zjh5NhlVTbDtEkCRWfuTsk2DMQ1P80uye%2BgNKXekcksndMgVEGZaMZjHBkeyLTHZb5tztFv8NvXgVy7jQOBiNowLwKlV2siz1G0UKK4di71ddaxaoeu2fk3pp6ZWURBpJ6DMxsQyLahqJlsN8oeO70BFFBcXCbbq%2BJkXmGwAZulinubdLw0fVUAZHVQbqKHVw25Wy8bXDDy7pbOBjqkAb%2B6OINX9ci7AxuuITYiPx%2Fvhnbdl10NEJj0GY8jcZRUExen8jup%2BQvL5w1%2F5Q0Aak2P5D8GsrIp2zlwbz8pKsk5AUxWZN84y%2BOQqKevPZqDThTHJMjud4Iq1mUmyqLAlideBwgDSlHHc9pZQok2xJrnbfqNSKTfcGPduWrMg27dpynb8cTM7RWE6RmvOS%2B5FLtQIQZSG66W%2FYrZ0ONl5rx%2FR6s1&X-Amz-Signature=ba57e6f9dbb994ac8cb15273a3984f40ee01829ddd895c04db3931ffd9d9e201&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



