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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJPCLRCF%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIER6RKNfHiOEQJk1Lu7%2BzXuy6L387eYIcCgyML8jOgcMAiEAiMWu8trmDDZVe1I6B32GY%2BcJ53Z39tBDATfxZ1AV%2Fpwq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDJ4ZzM5TNoV%2B9ohM0ircAzCjtMcDxlUyoIgjvXAknYlyZZ0ohZEDhGT28xYPeSFFed7jZNMQCw1h9lvffb7lY1gfu3bUPiYRjuXN%2F0dmvqI849%2F%2FYkSN4ZuCsmgDr%2BSw1lyXBRMsZ5xUHcBx19%2B1WlHXkWxnmZHuGj2fawVkM2ihWG1u3kcD9C4PW63AQO6%2B9%2BMh8VzzlCba9fFUWuTbpqpxtQVY7RJ3ticc4UNzFrlFmynPqVWKPPmGgzk%2FEkgrRP2GmRicPw0Xe2j0cDZq6y3mXadQyhzZxb98AxtaYfXOCQJWhuBP8MkpV7teJxqDnyt6g6rrS0xztNjoMWAmP4M83K4zVYcmsqX0dtSEC5ZmneVICsysL5D1wybSImt5dDIoB1mY0mYYXN1o58fyUpfMHp%2FRTUNMcXK1CTxGULbuJrVGtNFgqA0xeostjK9IDDyP0FbTwZS8OFkDCseFC3g9VxeRcgx7HddPCBgIoJPRNWle35JiDdEOD6Ggb73qEVO3jCS%2BkDb6EiNP745V45C4%2FrwCoIu%2BMZIuRVGsxSqmBWiRpI%2Bj5OEaRj3moTFK28wWEm9244fREFC2PdTxI0z%2BKyztm4c3zq3%2F9SbTjVwL9zGpiqTLej3eB592Fa0KvinvPTUzmnIZbqr4MOrjwcoGOqUBiRyovjgqW23ijxCumXbka9BY7xpMktCam3vFljHJ1oRp8iLIXnr9CJUV3IyQKSDifqgYcztpAODfjd4rz1%2B9Vy5RkC8FRJmIwcomiBDkux3xCUD2YjL6FfGk%2BA5n3K7uWM34J9St1rx823Wh5ZZSImwraFY%2FDGt%2FDVYybsCRcdeThI0D3F1OsyZyC1cIy3CMi3Y90DrpvmODH6TA5q9csrU8eT2x&X-Amz-Signature=31027f664e079c228a116a8078c47c302fc5de89c7a95a877179c1d0a08733db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJPCLRCF%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIER6RKNfHiOEQJk1Lu7%2BzXuy6L387eYIcCgyML8jOgcMAiEAiMWu8trmDDZVe1I6B32GY%2BcJ53Z39tBDATfxZ1AV%2Fpwq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDJ4ZzM5TNoV%2B9ohM0ircAzCjtMcDxlUyoIgjvXAknYlyZZ0ohZEDhGT28xYPeSFFed7jZNMQCw1h9lvffb7lY1gfu3bUPiYRjuXN%2F0dmvqI849%2F%2FYkSN4ZuCsmgDr%2BSw1lyXBRMsZ5xUHcBx19%2B1WlHXkWxnmZHuGj2fawVkM2ihWG1u3kcD9C4PW63AQO6%2B9%2BMh8VzzlCba9fFUWuTbpqpxtQVY7RJ3ticc4UNzFrlFmynPqVWKPPmGgzk%2FEkgrRP2GmRicPw0Xe2j0cDZq6y3mXadQyhzZxb98AxtaYfXOCQJWhuBP8MkpV7teJxqDnyt6g6rrS0xztNjoMWAmP4M83K4zVYcmsqX0dtSEC5ZmneVICsysL5D1wybSImt5dDIoB1mY0mYYXN1o58fyUpfMHp%2FRTUNMcXK1CTxGULbuJrVGtNFgqA0xeostjK9IDDyP0FbTwZS8OFkDCseFC3g9VxeRcgx7HddPCBgIoJPRNWle35JiDdEOD6Ggb73qEVO3jCS%2BkDb6EiNP745V45C4%2FrwCoIu%2BMZIuRVGsxSqmBWiRpI%2Bj5OEaRj3moTFK28wWEm9244fREFC2PdTxI0z%2BKyztm4c3zq3%2F9SbTjVwL9zGpiqTLej3eB592Fa0KvinvPTUzmnIZbqr4MOrjwcoGOqUBiRyovjgqW23ijxCumXbka9BY7xpMktCam3vFljHJ1oRp8iLIXnr9CJUV3IyQKSDifqgYcztpAODfjd4rz1%2B9Vy5RkC8FRJmIwcomiBDkux3xCUD2YjL6FfGk%2BA5n3K7uWM34J9St1rx823Wh5ZZSImwraFY%2FDGt%2FDVYybsCRcdeThI0D3F1OsyZyC1cIy3CMi3Y90DrpvmODH6TA5q9csrU8eT2x&X-Amz-Signature=0f32a06ef65aa12f1dcd8e0b479654cc38aa65d0c1759d1000fe9b90ad1b108d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



