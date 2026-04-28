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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGBBX4ZY%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCauQtRLDVmp0dOWwwEZc8MUqJskZ7iPmuGrGigLS6avwIhAIm5HmybCZYC4OuvTwp%2FcfcihNvjhLqU8LLMf%2FS3SSv5KogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJYm2kqAPl2UQwCkwq3APs2PFciAV2lO8fuzh4DgBOQkNc%2BNmbR0dfB3lRZDuV54%2FtsKUByoeJJar5Yqs9lyGR5DAIn0RD%2B2woe8BknmEp1OJCz7y%2BS0S%2B8%2Bqi72rAnnEdDmQvCQD4w5MOwlh6rQTIpEldFBgFl3IoF3J%2BYHPc5J%2FpFYFr9iB27%2BVKtDzfaRXzMWDnrVe3Swwj%2FG16Rjm1kjjzpKZxD2rpoD1DGB4DtwkDCukHHbDvSwnUbOUffD%2F%2F9JxBD%2BOeRybldr%2BVCwEePmQ6HfQ%2BCiqxdmf5lorQ36Fwu%2FX3%2BIYrCws5Yz2XpBQ55GIjyHrRnf%2BOQylQ%2BCya%2BZQtAHRXHeUhv2vBnVtTkURoXjBXAz6k1zpW6WeAvaOPWoStykqmKMPp0WjxgFtrUYY14msK%2FrdEkVGXV7Q3mQy9xbdTJGwWEZfsB91cFs1mznfamVypMRy%2B0cbwPMl%2F%2ByNDZSzsC6yKU%2F5bxbipSoirXhWcuho%2FB81JgKZ8njr9%2B%2Fbv41QoJG8X84z1RUNgP4R4ShCbGZ3Fx5pr%2B0JfRz48irw%2FIm2mrdYYIautrVYy9sPMeHqYr%2BaFqd67Zo1IDOYBW3Y2ZFC7KmH8O66v%2Biay0zSxH74c3LXgnd6GuM%2FYFgVN4LnKqpUN4DDp7MDPBjqkAReqznm3hlMMgwv%2FZjArHqgRBjS%2FRYPfHcGt%2FJpwJtV%2FNzUS5ttt2%2FyEBSoDjqgcG4KMyCqCIAomMdU3AKhsMaWEw%2BV%2BoVuLrhPSgEpnsRZJN%2BMOe8BQRhqw4ird4Mtf%2BzjUCdTYavqJzToCeh5z864ys0ZiXKJgCF13kEFUWwBBK4Bx6LclJxCIQUlLXkh5htzMqitbspKxE6dvar2Fwn8J%2FinO&X-Amz-Signature=817837af6eb3fc6f8a6166ddb843fac3a87a0512af1b3b9bac033fcb7d919912&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGBBX4ZY%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCauQtRLDVmp0dOWwwEZc8MUqJskZ7iPmuGrGigLS6avwIhAIm5HmybCZYC4OuvTwp%2FcfcihNvjhLqU8LLMf%2FS3SSv5KogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzJYm2kqAPl2UQwCkwq3APs2PFciAV2lO8fuzh4DgBOQkNc%2BNmbR0dfB3lRZDuV54%2FtsKUByoeJJar5Yqs9lyGR5DAIn0RD%2B2woe8BknmEp1OJCz7y%2BS0S%2B8%2Bqi72rAnnEdDmQvCQD4w5MOwlh6rQTIpEldFBgFl3IoF3J%2BYHPc5J%2FpFYFr9iB27%2BVKtDzfaRXzMWDnrVe3Swwj%2FG16Rjm1kjjzpKZxD2rpoD1DGB4DtwkDCukHHbDvSwnUbOUffD%2F%2F9JxBD%2BOeRybldr%2BVCwEePmQ6HfQ%2BCiqxdmf5lorQ36Fwu%2FX3%2BIYrCws5Yz2XpBQ55GIjyHrRnf%2BOQylQ%2BCya%2BZQtAHRXHeUhv2vBnVtTkURoXjBXAz6k1zpW6WeAvaOPWoStykqmKMPp0WjxgFtrUYY14msK%2FrdEkVGXV7Q3mQy9xbdTJGwWEZfsB91cFs1mznfamVypMRy%2B0cbwPMl%2F%2ByNDZSzsC6yKU%2F5bxbipSoirXhWcuho%2FB81JgKZ8njr9%2B%2Fbv41QoJG8X84z1RUNgP4R4ShCbGZ3Fx5pr%2B0JfRz48irw%2FIm2mrdYYIautrVYy9sPMeHqYr%2BaFqd67Zo1IDOYBW3Y2ZFC7KmH8O66v%2Biay0zSxH74c3LXgnd6GuM%2FYFgVN4LnKqpUN4DDp7MDPBjqkAReqznm3hlMMgwv%2FZjArHqgRBjS%2FRYPfHcGt%2FJpwJtV%2FNzUS5ttt2%2FyEBSoDjqgcG4KMyCqCIAomMdU3AKhsMaWEw%2BV%2BoVuLrhPSgEpnsRZJN%2BMOe8BQRhqw4ird4Mtf%2BzjUCdTYavqJzToCeh5z864ys0ZiXKJgCF13kEFUWwBBK4Bx6LclJxCIQUlLXkh5htzMqitbspKxE6dvar2Fwn8J%2FinO&X-Amz-Signature=0cf3ad1663cd4aa2d6cebf6514425389c476bb8f751f9b62d89554ec99886c05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



