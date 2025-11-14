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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E4GMSXJ%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHT1BTaWa2I2hyFrqRF8773t3sIRT9Sbkerg3cZFi2MAiAQg7JotrIrpNeluu1tqTZIH3P0WQgkju5WFEBpktcYCCr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMfbilbLZWJgtxT74sKtwDIKUUOUZTY%2F8xoXUY23SGn%2BsWQonfT%2BHJrXjxYRQ9LGg0YvQVPYHLQkoXerlkS0c6Q2cy78gF1LRc%2BZw%2B6RZv0hJi%2FO5gAKjWCaKLeieSNXVIvWo8fbIE18zPNkyPZqS6NFsuHLlpYmTAOvXNaCrd4EQ4qlsEcBWY%2FzA0pybotJPK9rGDEBqY3IiH95ogFExsQ%2B1ajVNDUvxKYhO5aLClUhsmkTkXM%2B5XjeKlVrwlmOh2YSVJDKkjkW32YW%2BTE1v6wdhQkANJbOCOYxEEia2VDeW9PICkeS%2Bd3WbkDAH2GoBpuGNI1ypEmZdIMC95QXsZzpQG%2FkdARMdTbyEsQSVw1yc2DJFJmFr7WTchzzLQSAFO%2BfNt7GPOteufiCniRfjrtTt%2BkWr2Tx3kbSfsyjeJAeMzK2H%2FUweO9dZrZtMNnWI6YH5Dp3Wdhw19WeVAHEFFX8Wgtul6kXp%2BMrxb%2BQkhJlZaiA3KdDeiAQX4q4t4nlJcKnbC3%2BXoT8LIVJdbmocDT%2Fi5bw1GFL2ASotUfvHgA8gyOelcxoWU0ndN4vyYh4IByl4lUHxDw9TodDdIejofvKerh2ClI%2BbWmflNb5MYMwBcmGwgue0RK1WlwPxEb1QdzxgD12d3saCdbUAwsorayAY6pgFrKSMisM5Uvz0AVoDnnz9xnYaT72A6bW2VwBqYhPn1sZy6GEoclV7t0g0op5OpwiazwBd5KPkDaMPfefPk6pOXJ6%2B2HCI8TyLsVBpbav%2BOfQPDycnQCGcQ7pFqzdoz1BsJnfGGX9SWV%2B072hQqhDrdto52omRweK6Kwqm%2BHjZ9jOSfTrc5FEgX9NLGFWCdpiRvJ%2FLI%2FIMB2vs2GtieT5Oe0%2BHTkuLi&X-Amz-Signature=fcdbbff296dac0447c7f9566b432f8e842ea67348b0d5159aed93c95a1d78037&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E4GMSXJ%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024449Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICHT1BTaWa2I2hyFrqRF8773t3sIRT9Sbkerg3cZFi2MAiAQg7JotrIrpNeluu1tqTZIH3P0WQgkju5WFEBpktcYCCr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMfbilbLZWJgtxT74sKtwDIKUUOUZTY%2F8xoXUY23SGn%2BsWQonfT%2BHJrXjxYRQ9LGg0YvQVPYHLQkoXerlkS0c6Q2cy78gF1LRc%2BZw%2B6RZv0hJi%2FO5gAKjWCaKLeieSNXVIvWo8fbIE18zPNkyPZqS6NFsuHLlpYmTAOvXNaCrd4EQ4qlsEcBWY%2FzA0pybotJPK9rGDEBqY3IiH95ogFExsQ%2B1ajVNDUvxKYhO5aLClUhsmkTkXM%2B5XjeKlVrwlmOh2YSVJDKkjkW32YW%2BTE1v6wdhQkANJbOCOYxEEia2VDeW9PICkeS%2Bd3WbkDAH2GoBpuGNI1ypEmZdIMC95QXsZzpQG%2FkdARMdTbyEsQSVw1yc2DJFJmFr7WTchzzLQSAFO%2BfNt7GPOteufiCniRfjrtTt%2BkWr2Tx3kbSfsyjeJAeMzK2H%2FUweO9dZrZtMNnWI6YH5Dp3Wdhw19WeVAHEFFX8Wgtul6kXp%2BMrxb%2BQkhJlZaiA3KdDeiAQX4q4t4nlJcKnbC3%2BXoT8LIVJdbmocDT%2Fi5bw1GFL2ASotUfvHgA8gyOelcxoWU0ndN4vyYh4IByl4lUHxDw9TodDdIejofvKerh2ClI%2BbWmflNb5MYMwBcmGwgue0RK1WlwPxEb1QdzxgD12d3saCdbUAwsorayAY6pgFrKSMisM5Uvz0AVoDnnz9xnYaT72A6bW2VwBqYhPn1sZy6GEoclV7t0g0op5OpwiazwBd5KPkDaMPfefPk6pOXJ6%2B2HCI8TyLsVBpbav%2BOfQPDycnQCGcQ7pFqzdoz1BsJnfGGX9SWV%2B072hQqhDrdto52omRweK6Kwqm%2BHjZ9jOSfTrc5FEgX9NLGFWCdpiRvJ%2FLI%2FIMB2vs2GtieT5Oe0%2BHTkuLi&X-Amz-Signature=9b44b9b3d23211dafe37d14bd27006b6a306548719a4efdb6ba3a1721bb21869&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



