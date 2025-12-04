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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIECJN57%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCJtYJCQY7aVaaMD18Wt9CuDK7gl7OCSv23vlXUvYee9AIhAJS8x5ccR%2Fx%2FTflKybWRRv7dED8ZqiafnDx0ZxVuS6gqKv8DCDsQABoMNjM3NDIzMTgzODA1Igwaf8wvpLVsPL6bUgAq3ANPWBZMQa5dTD47heugzehg5X%2FbKn4SuSlW5t6xPJFGR9vroJ%2BL31LOHUxsMuNmduA5RMjuE0o0eKyLmwhvugx4ez677%2BqAVW7WgVKwVnlhKsKSYnsHaI1rdK05gI8t%2FjqbCx53wK1OI3O7OfMRPchjz6mVLyDiv%2FIBRh2400NeMdBnxtEB5jGuQ5UnoOfcSYgRaK4I2ykSXAWR4GaRCLqYKOmKy8DYCh5u3FTz%2BihJdyVePZNDB9CZ4jN5diq%2BVHAxS614yJPqlloyzEiptRMpCFjJ2af1MO7RLz05K%2BEp%2BnPGuc3nPdInBN4aTcQnLfrGZTrW1yyuZposjRV780%2Bt2lRTbfDqmyS%2BxA4JeK3GdfnM8OP80BV8fRMYukSoFHMpnfUjmaOL7DcbcRefQHwSIxMlChnRYmnXOWwpo6IYQfEBfYHB20dtcxuwbZz6mzPjsjIJHcflxENbHyV5R1o8K7%2BHYkZwxWWL6zSj%2FjB80CQg8DOkt1gXbNshH7t3GrPvOcvEKG5Ymhse7sHvII0zsYbyDzH%2BucL1z5tNoKIgpWPvYMCCgg6ENR%2Bifkl4NMhEFyNhThMe3m6hVB4QF%2BCvKp5IC%2Fr%2Fh1yGDZ6yHWfgKVamc4f4MHFOMNOPIzCE1cPJBjqkAT8l04PDmRJ0LQHzYbIy%2FoOe0yAmd4HdNhMrxEfTHqMmyEtrcU5mJi8VKN5g0EQdslhGeQBNohEa3VYGD6pkDGUoMJuQ50NagAnR0HqrmGFkIrIzYbriYphIDAL%2FKbfhGbuKbhh63kasMctbxshojtrMRVurlykr1UNpcKWQI4gaLsZUvSiv%2BlalP%2Faw%2FjVW51aDJZjSYPZ9%2F1imo3rnt9J0xApR&X-Amz-Signature=c87014455b198450d80a2d013faa2baffcd1d16d4cedd800ade30ee37287641f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIECJN57%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCJtYJCQY7aVaaMD18Wt9CuDK7gl7OCSv23vlXUvYee9AIhAJS8x5ccR%2Fx%2FTflKybWRRv7dED8ZqiafnDx0ZxVuS6gqKv8DCDsQABoMNjM3NDIzMTgzODA1Igwaf8wvpLVsPL6bUgAq3ANPWBZMQa5dTD47heugzehg5X%2FbKn4SuSlW5t6xPJFGR9vroJ%2BL31LOHUxsMuNmduA5RMjuE0o0eKyLmwhvugx4ez677%2BqAVW7WgVKwVnlhKsKSYnsHaI1rdK05gI8t%2FjqbCx53wK1OI3O7OfMRPchjz6mVLyDiv%2FIBRh2400NeMdBnxtEB5jGuQ5UnoOfcSYgRaK4I2ykSXAWR4GaRCLqYKOmKy8DYCh5u3FTz%2BihJdyVePZNDB9CZ4jN5diq%2BVHAxS614yJPqlloyzEiptRMpCFjJ2af1MO7RLz05K%2BEp%2BnPGuc3nPdInBN4aTcQnLfrGZTrW1yyuZposjRV780%2Bt2lRTbfDqmyS%2BxA4JeK3GdfnM8OP80BV8fRMYukSoFHMpnfUjmaOL7DcbcRefQHwSIxMlChnRYmnXOWwpo6IYQfEBfYHB20dtcxuwbZz6mzPjsjIJHcflxENbHyV5R1o8K7%2BHYkZwxWWL6zSj%2FjB80CQg8DOkt1gXbNshH7t3GrPvOcvEKG5Ymhse7sHvII0zsYbyDzH%2BucL1z5tNoKIgpWPvYMCCgg6ENR%2Bifkl4NMhEFyNhThMe3m6hVB4QF%2BCvKp5IC%2Fr%2Fh1yGDZ6yHWfgKVamc4f4MHFOMNOPIzCE1cPJBjqkAT8l04PDmRJ0LQHzYbIy%2FoOe0yAmd4HdNhMrxEfTHqMmyEtrcU5mJi8VKN5g0EQdslhGeQBNohEa3VYGD6pkDGUoMJuQ50NagAnR0HqrmGFkIrIzYbriYphIDAL%2FKbfhGbuKbhh63kasMctbxshojtrMRVurlykr1UNpcKWQI4gaLsZUvSiv%2BlalP%2Faw%2FjVW51aDJZjSYPZ9%2F1imo3rnt9J0xApR&X-Amz-Signature=279bf2205fabe12710714e592837fe3f0a3bbcbe7d81e0bee019febf9a5cb1f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



