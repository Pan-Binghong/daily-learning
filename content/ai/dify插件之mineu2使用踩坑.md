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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KPVH5WH%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDm3nH0TRfAFIK3fl30fuuR75VCv43t8nyubDCa9GNpiQIhAPoDAqMJH%2Bl9NuI%2ByM%2BDFpmLqh4%2Bd3eR%2Bsa3JDJFRvRBKv8DCFoQABoMNjM3NDIzMTgzODA1Igy8qDqKlI%2Fr7WQBPzAq3AMb1wbihje5B4GSDYu%2Fp6xSOHILpkTHxkVuVKydVrQoGkKV7B561j3fVq%2B3h9i0TK5D%2BQNvdBjjl0PeYXosEFw4lCOaG%2Fumsecq%2FLTg3Wij2cBd8KHSh6620NwEvs2iTObGykbzWcXp%2FY1NWmkixXU4l9Ojh9EaxIRq04t4092a0aaSKcjAoi1YM2N8efDI%2FHFsU0EuPqKmz9m04WBvJbPThaHw0uAviWnnquqOgu2YXyPhHAqZ%2B1h0uM8SAVB2M7eBY9erhXGtrs4VL8lghdwJ7UXY81WeAQXFySDm3g5SDCZKt9CI2Oal%2FqYj0ZeHzhvTvLbGzNsydaChJz%2BIAqtzb5Hn6T%2BcUcPKwQ0A3jl5TV9qYbEIxKINaQRRS2ma7xL1lNqcOnVtEmY8hSSAxMrceSbP57JhUu6tYmf89KT2s%2B2bVjcTNoyLg0976HJXU%2BihKxhK8hixZeLZklpSem4%2BLWFC3jXtcn2GTxpjI5H9SaaA%2F5LwF0Zj3JyrA6KiEyBhVyOn%2BPnaIjmgCmD7GV8bmVpVsMDvvLRcZJ1GVFwARYb7UnqTe7sPllevrAfPUwrA34Hv4ML2BF1PJJzj31sQCiHva7Q%2FxfBg9Wfr0kMQGZJ3v3GqEdG4pxCfgTCtn9TMBjqkAYRJeLFouEvLFdMaf1Nm30777hxVG8H%2FwXRl7EoJ4WBlbnj9EtKZH1cObTASU2Y5PG%2F3DdayIqqQU9SOoKrBqDyP9g3N%2BSqGSTQ0QPwgNn2WHTHEP9Zybbf9VCNobScauHgSzpFZ1HnMsUPYqQYRhFoXZeR911ApeG5UOBF4IgEFBUEnwubd7QYwx4gTaS4OKyPHVYsn4dQhFCb5%2ByA%2FsAOzr%2BkV&X-Amz-Signature=2cc9bea7a8d199f1110b9ba6dfba08fdbb1b91f72497caee80e07b22d302d687&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KPVH5WH%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDm3nH0TRfAFIK3fl30fuuR75VCv43t8nyubDCa9GNpiQIhAPoDAqMJH%2Bl9NuI%2ByM%2BDFpmLqh4%2Bd3eR%2Bsa3JDJFRvRBKv8DCFoQABoMNjM3NDIzMTgzODA1Igy8qDqKlI%2Fr7WQBPzAq3AMb1wbihje5B4GSDYu%2Fp6xSOHILpkTHxkVuVKydVrQoGkKV7B561j3fVq%2B3h9i0TK5D%2BQNvdBjjl0PeYXosEFw4lCOaG%2Fumsecq%2FLTg3Wij2cBd8KHSh6620NwEvs2iTObGykbzWcXp%2FY1NWmkixXU4l9Ojh9EaxIRq04t4092a0aaSKcjAoi1YM2N8efDI%2FHFsU0EuPqKmz9m04WBvJbPThaHw0uAviWnnquqOgu2YXyPhHAqZ%2B1h0uM8SAVB2M7eBY9erhXGtrs4VL8lghdwJ7UXY81WeAQXFySDm3g5SDCZKt9CI2Oal%2FqYj0ZeHzhvTvLbGzNsydaChJz%2BIAqtzb5Hn6T%2BcUcPKwQ0A3jl5TV9qYbEIxKINaQRRS2ma7xL1lNqcOnVtEmY8hSSAxMrceSbP57JhUu6tYmf89KT2s%2B2bVjcTNoyLg0976HJXU%2BihKxhK8hixZeLZklpSem4%2BLWFC3jXtcn2GTxpjI5H9SaaA%2F5LwF0Zj3JyrA6KiEyBhVyOn%2BPnaIjmgCmD7GV8bmVpVsMDvvLRcZJ1GVFwARYb7UnqTe7sPllevrAfPUwrA34Hv4ML2BF1PJJzj31sQCiHva7Q%2FxfBg9Wfr0kMQGZJ3v3GqEdG4pxCfgTCtn9TMBjqkAYRJeLFouEvLFdMaf1Nm30777hxVG8H%2FwXRl7EoJ4WBlbnj9EtKZH1cObTASU2Y5PG%2F3DdayIqqQU9SOoKrBqDyP9g3N%2BSqGSTQ0QPwgNn2WHTHEP9Zybbf9VCNobScauHgSzpFZ1HnMsUPYqQYRhFoXZeR911ApeG5UOBF4IgEFBUEnwubd7QYwx4gTaS4OKyPHVYsn4dQhFCb5%2ByA%2FsAOzr%2BkV&X-Amz-Signature=2fbc0ca4ba5cb37e88469a84607038b38f1b56d7054350dfd301bd20713db5ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



