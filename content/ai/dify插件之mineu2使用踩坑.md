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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LMKRZ2A%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICMDagbJH3bEU6nSdOrQwXO%2BFEd53l5quHDfiss4Hm35AiAh2MWPFLQMZayqETRb1jDOEBcp2pEVvf7TfKmx3quJsSqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbtcYH7wDRp%2Bs7vjUKtwDYbP6mBCDieGjaGkAQM2u3D0WBHOwwHECMJf099QdU0fIC435wVjMZTZFyyo4KfOaH3RR90KhRhZoLa0NOeNbZv8kODDRrkRdCLoyACuquRsm%2Fq6fYeaOlyCWiyltzEs0XFU5r7wEGuj%2BFnqDB4UlGS9KbmxJfHlHrOtrRfCu2hW2Kp%2FQS4yfl5%2FdYvtyzQ4ukQ0XL07RVdHXrGzdWxauRBL6leqJrZ0Q%2BogmndzlXFJcBk6f6nH6xCOgO5hlp8gh1O2YYPfJj166%2FoAguvzBXKPsuscc5MBKCTSlhcBN8DhrT8CxoB6qBDMFoCFT3Zs2EDDVw5WMsoKgVl2xPH2bJYik4JYnAetrm6BQy%2Bbj14P9nBI0Bl%2B2mW1vOkZJnuEYj%2BCRIGamIVOuK4lLctIVdD0lpt%2Fo5AEQAGhVllfkzp0uyflmo9n4K9pM2HudrrORlBTF6X4mBrDP1bSlkxYWqzydOZIhAuGXWX1lRiYFiQr7QNKj%2F6ktKuRf1lpTtsof%2BU%2BdyEJx1I7ydY%2F7oloPzs3qNlrFaWBVWAI0EWqsVTicAj9QLQWtSoUJ1elt9IcdbHMmn2RGzk1sJ4qY%2FucZcBr3GuBZoIivfiGwCnN4dUZNXXGEdf3RQJcVL%2F0wgOSeyQY6pgEho%2FJQFKRryyCXTI2DLbN0e9bC8JpaB5uQE0Dn9m9HtRoTBmVLaEUHfwZt7t2m5BLWqqEH6cxeI%2BHamc%2Fbnh6qjAVKpkrjZz4QDRGqKMo5Ult0tOsz64z5oOQv8EdAzMbZBOij4cOr0vweuX9o1P8I4stgHGu4CtRVaZSEEwURcpzs89vQuaNKappzfDM%2B028%2Fp1c7PjGlCswfiTGbTpWhOiO0P75c&X-Amz-Signature=d2251e2aa82f51b495f03f8f8fd932af3d1deefa326245de70bf4b0e909fe8a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LMKRZ2A%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICMDagbJH3bEU6nSdOrQwXO%2BFEd53l5quHDfiss4Hm35AiAh2MWPFLQMZayqETRb1jDOEBcp2pEVvf7TfKmx3quJsSqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbtcYH7wDRp%2Bs7vjUKtwDYbP6mBCDieGjaGkAQM2u3D0WBHOwwHECMJf099QdU0fIC435wVjMZTZFyyo4KfOaH3RR90KhRhZoLa0NOeNbZv8kODDRrkRdCLoyACuquRsm%2Fq6fYeaOlyCWiyltzEs0XFU5r7wEGuj%2BFnqDB4UlGS9KbmxJfHlHrOtrRfCu2hW2Kp%2FQS4yfl5%2FdYvtyzQ4ukQ0XL07RVdHXrGzdWxauRBL6leqJrZ0Q%2BogmndzlXFJcBk6f6nH6xCOgO5hlp8gh1O2YYPfJj166%2FoAguvzBXKPsuscc5MBKCTSlhcBN8DhrT8CxoB6qBDMFoCFT3Zs2EDDVw5WMsoKgVl2xPH2bJYik4JYnAetrm6BQy%2Bbj14P9nBI0Bl%2B2mW1vOkZJnuEYj%2BCRIGamIVOuK4lLctIVdD0lpt%2Fo5AEQAGhVllfkzp0uyflmo9n4K9pM2HudrrORlBTF6X4mBrDP1bSlkxYWqzydOZIhAuGXWX1lRiYFiQr7QNKj%2F6ktKuRf1lpTtsof%2BU%2BdyEJx1I7ydY%2F7oloPzs3qNlrFaWBVWAI0EWqsVTicAj9QLQWtSoUJ1elt9IcdbHMmn2RGzk1sJ4qY%2FucZcBr3GuBZoIivfiGwCnN4dUZNXXGEdf3RQJcVL%2F0wgOSeyQY6pgEho%2FJQFKRryyCXTI2DLbN0e9bC8JpaB5uQE0Dn9m9HtRoTBmVLaEUHfwZt7t2m5BLWqqEH6cxeI%2BHamc%2Fbnh6qjAVKpkrjZz4QDRGqKMo5Ult0tOsz64z5oOQv8EdAzMbZBOij4cOr0vweuX9o1P8I4stgHGu4CtRVaZSEEwURcpzs89vQuaNKappzfDM%2B028%2Fp1c7PjGlCswfiTGbTpWhOiO0P75c&X-Amz-Signature=ca898f3a2a8677795ffe74dbd1b34aeb8a92002c64d388c306f18641ebd96bfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



