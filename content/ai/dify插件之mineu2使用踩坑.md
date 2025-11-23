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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTBBPTZ5%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIHLC1aKo9XQm1tsBTVO8cLzZlceOocp4Qu%2B6AXRO1VQWAiEA0QadNv8rng0F%2FEqU%2BUaA%2F%2BCAqirRUKcxiRSWbovZKowq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHBVkAnDdVkblF0mSircAyfPXiJRPipCnvpGltAK%2F1I4UZxChWbpC8gn2%2F0dfCtMkCaAVSHX%2FDrehQuXe1dDrTNEAnMiNfbYPRPCYSPN7TSbX58N6T2tTIZKESoOr6pS66bMb0C%2FOK6wMcNTrfAxpuGnDk3wSZ6Kr%2BCyetSkWy8AWXS1E%2BXZ5eThXciLEy0S9WehCuK6A9%2BcZih8rKMm1OSGF77cFoZg3E6LhyU35DY9LDSHnQRIoJT7rsBX%2ByppiHTp4MOUGnr675xmg3hYyA01BKW4Ez%2FXracl0ra9vfwsFKpVJSZLBkHC4qnqydOgeHtyhDVNCRgoitxEfMH1Vzok2ACJUhgZyuffAitwWqFW6b3mVFMVgt3cu8dGrNkyJAbcL1XztbOLJr19tOgvItK9z6oNoNUPiTUmZUNr3Fup4ZiQeJePOSTp0RCZ7NLijNHpCr3txji68befa4e5LrQTjBJ%2BL9jpuHqmGBNLRvVvBnhoCrgYTXAJWvZhfbZMaFj2KpKEv7jYv1hj28oNIxIKn%2FSiGgW5ApyyRt771v%2BzVkmgludW9ZnX2r9xF%2BmxT%2BmUkrDGTRUv%2F%2BfuFRqcxjHk2GEFHqIaUfODknDdtcu6F8jA%2Fnkgy9PqC60GyZmKu%2ByrTO4wALsGGmprMI%2BxickGOqUBKchS6oqC%2FlVM%2B5Wu0ebPnEHUA5iCd0z3LtlokoJn%2FWYsTeg%2Bvg9XdJmZaf%2BHbGJ00ExhwWvBbypRdWWTbA35BOT1ogPIM6rIwF0fAu1hUxNOWBfLE4w%2FaVwUTeQeUipun2Dm7IX4bEtlvHUlU2Rv2TcdKR8O1mnbNZHwi8yvUND%2B1M3wsMHJM%2Fu0cpaqYcyfhrCfrwByKNmjdR2fp0KdDMgXPlw4&X-Amz-Signature=31393548875b6aecde5f2fd4f3c0b5205cc85a2b539c384d950492df3fcc71bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTBBPTZ5%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIHLC1aKo9XQm1tsBTVO8cLzZlceOocp4Qu%2B6AXRO1VQWAiEA0QadNv8rng0F%2FEqU%2BUaA%2F%2BCAqirRUKcxiRSWbovZKowq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHBVkAnDdVkblF0mSircAyfPXiJRPipCnvpGltAK%2F1I4UZxChWbpC8gn2%2F0dfCtMkCaAVSHX%2FDrehQuXe1dDrTNEAnMiNfbYPRPCYSPN7TSbX58N6T2tTIZKESoOr6pS66bMb0C%2FOK6wMcNTrfAxpuGnDk3wSZ6Kr%2BCyetSkWy8AWXS1E%2BXZ5eThXciLEy0S9WehCuK6A9%2BcZih8rKMm1OSGF77cFoZg3E6LhyU35DY9LDSHnQRIoJT7rsBX%2ByppiHTp4MOUGnr675xmg3hYyA01BKW4Ez%2FXracl0ra9vfwsFKpVJSZLBkHC4qnqydOgeHtyhDVNCRgoitxEfMH1Vzok2ACJUhgZyuffAitwWqFW6b3mVFMVgt3cu8dGrNkyJAbcL1XztbOLJr19tOgvItK9z6oNoNUPiTUmZUNr3Fup4ZiQeJePOSTp0RCZ7NLijNHpCr3txji68befa4e5LrQTjBJ%2BL9jpuHqmGBNLRvVvBnhoCrgYTXAJWvZhfbZMaFj2KpKEv7jYv1hj28oNIxIKn%2FSiGgW5ApyyRt771v%2BzVkmgludW9ZnX2r9xF%2BmxT%2BmUkrDGTRUv%2F%2BfuFRqcxjHk2GEFHqIaUfODknDdtcu6F8jA%2Fnkgy9PqC60GyZmKu%2ByrTO4wALsGGmprMI%2BxickGOqUBKchS6oqC%2FlVM%2B5Wu0ebPnEHUA5iCd0z3LtlokoJn%2FWYsTeg%2Bvg9XdJmZaf%2BHbGJ00ExhwWvBbypRdWWTbA35BOT1ogPIM6rIwF0fAu1hUxNOWBfLE4w%2FaVwUTeQeUipun2Dm7IX4bEtlvHUlU2Rv2TcdKR8O1mnbNZHwi8yvUND%2B1M3wsMHJM%2Fu0cpaqYcyfhrCfrwByKNmjdR2fp0KdDMgXPlw4&X-Amz-Signature=900846c956b8714137e0b2577e5e19e800646dd2a4b4b2e4fcdef6049c090c4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



