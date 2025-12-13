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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PI54MZP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDMxCjqNcH%2BnLjMbrD%2FdpU%2FrvcmorzSrlhrVNJXJVeCMgIgTiUGeCdB1zstFhHgC%2Fqmr6TY5guUdTzFOJ7Z61qlHHIq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIFlkB5r1WW4kgE2eircA6FJyIp4VV6sPdcPNcHG2ODsaulnXVwQYRiLqhbwCGQRW%2FgkWvBRF%2FRgPZj0EOolXBi%2FlfKuik6y1U69wOeWKTBfsJ09FFMzr54rMjlY0yQH9QUxUlC6EE92lEyHkPxQbJgrRq4EFR%2B3Q1%2FwzTYwq%2FyE2u3BSD4JPRl%2BjsO9Af2z0BU8FNbcr0pPNIP9MEjY1WfXbLrnCJKeQbWdSC7OILF4NI2B1dES06%2FxieWUBdJ9njP0qk04glr2ZQDBF2i3J5QnI3HqeK6dJFz9k43vj2COkeWnFEaSe%2Fm7Q5bM9gNeN7lfSJHrVF1yBcaR5PhNdDN9%2BiN0sSiRDGHY%2FYKDxNyQqT4OFHdCJPXs7uvrajWZsIpjZLjt0DDz94Yo7MDAMytV2ExjNXZjb7TUmq8L%2FmLdXgJL2RTmb2FYMr50ntn233qdM38a4E2amPuG6WNF39G%2BbesgPnUnFSefcuGWu5g63dU0gkAnnIsFV2DkOGrIxwaqF0rwivsDhgmMTRmci67APp9CCTC3026mvmKs9qc8sA9kraAi6YeKzUoYh60QguS%2FQ8itijcxn4vARzBpUfQaS5Ahh1qTB3QaFFrOfzJNjpTBUhwP5fsFMgSEtwebDwLUePV47u7nlcuEMLaM88kGOqUBcWGvEEgSY0aPnKnn6wHkZ%2FNQaLOe3Te2r2BzHEguSDiV2gdiuYC2E2HfmoCF1WIJEIwRdzxkbwi%2FugDujXft22a%2FEHvoVy2qSplqqwD4GyOqOb6yMGLjc3TddSqG%2BWE08bSEEljmTDi5T7kArotHpIjwwNMmqgHzpaLvy8ZLjsDwcrJ1Q8sQY0jtlCnzwgZpuSaRx%2Fx0bUcsmss5jeBkxFJY2oIG&X-Amz-Signature=3035118e9f96511b80a64d3db2bda0b9b675e39a1eae9609bba1988a67ddea79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PI54MZP%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDMxCjqNcH%2BnLjMbrD%2FdpU%2FrvcmorzSrlhrVNJXJVeCMgIgTiUGeCdB1zstFhHgC%2Fqmr6TY5guUdTzFOJ7Z61qlHHIq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDIFlkB5r1WW4kgE2eircA6FJyIp4VV6sPdcPNcHG2ODsaulnXVwQYRiLqhbwCGQRW%2FgkWvBRF%2FRgPZj0EOolXBi%2FlfKuik6y1U69wOeWKTBfsJ09FFMzr54rMjlY0yQH9QUxUlC6EE92lEyHkPxQbJgrRq4EFR%2B3Q1%2FwzTYwq%2FyE2u3BSD4JPRl%2BjsO9Af2z0BU8FNbcr0pPNIP9MEjY1WfXbLrnCJKeQbWdSC7OILF4NI2B1dES06%2FxieWUBdJ9njP0qk04glr2ZQDBF2i3J5QnI3HqeK6dJFz9k43vj2COkeWnFEaSe%2Fm7Q5bM9gNeN7lfSJHrVF1yBcaR5PhNdDN9%2BiN0sSiRDGHY%2FYKDxNyQqT4OFHdCJPXs7uvrajWZsIpjZLjt0DDz94Yo7MDAMytV2ExjNXZjb7TUmq8L%2FmLdXgJL2RTmb2FYMr50ntn233qdM38a4E2amPuG6WNF39G%2BbesgPnUnFSefcuGWu5g63dU0gkAnnIsFV2DkOGrIxwaqF0rwivsDhgmMTRmci67APp9CCTC3026mvmKs9qc8sA9kraAi6YeKzUoYh60QguS%2FQ8itijcxn4vARzBpUfQaS5Ahh1qTB3QaFFrOfzJNjpTBUhwP5fsFMgSEtwebDwLUePV47u7nlcuEMLaM88kGOqUBcWGvEEgSY0aPnKnn6wHkZ%2FNQaLOe3Te2r2BzHEguSDiV2gdiuYC2E2HfmoCF1WIJEIwRdzxkbwi%2FugDujXft22a%2FEHvoVy2qSplqqwD4GyOqOb6yMGLjc3TddSqG%2BWE08bSEEljmTDi5T7kArotHpIjwwNMmqgHzpaLvy8ZLjsDwcrJ1Q8sQY0jtlCnzwgZpuSaRx%2Fx0bUcsmss5jeBkxFJY2oIG&X-Amz-Signature=adcc91682077723569fb0b6ce4bcc46b4e5895ca1ce8a63053f20d470c84bdf8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



