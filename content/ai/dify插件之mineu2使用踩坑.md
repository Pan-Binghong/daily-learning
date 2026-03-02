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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFO4X6ZL%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsjB9pbCaniGKaxLbsEeOx7IqT4yPlhQODZli2ya%2BxmAiEAhIK5DjCgG3dDLtGvc58v4qm0qX%2FFUBXOxacfNDGnZPUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDJ%2FAEvKMfdFlTO1%2FfCrcA2CdsocTv%2FIqN%2B0V2P6l6YxVZPNbM8E9cWIFVVEOu6g9ax5U545S9tCn8NJNVSWOKDTDj7M0tZ9FGNQrHNRuY8KLbkiRcuC25Amsb%2F0A8ajeWdh1lOC2kq5UbMYoH5Jffew7Jv0Tho2yE4Ybnmua5IQ3bwwtU1IsMXmxNcPgyIZQQJVK3wwgQXRLZhxqV3RYRz47%2BQeSVguRLhlMhGx%2BkaXvxfwHtczH8v1NZyw%2Btf%2FiXF%2FcownF5QhJGcx2SYI0LeXMU8u8P9dH%2BbE9Ud5%2BkPy7ROfLdhfGGzBa3WGeSS0jYDN2%2FnTNywka5UNvVIY1ebuImYqOnu4hzPZgwLOIfJgWfKxbBw63cZk1aSZQOtGn986mhVaG5dA0zlu5HXSTVJ60aU%2Bb%2BHz3GXvlpeTGdFow9cundtzFcNwj6kiKjARC69FSe4pzBUfBaUL37RJRRLtbJ7t0iGvx0qbDmUXKFc5otPwi8g1eXzDcMpVgtND35EedIglnSroAU%2F3gXdPcFmKdRwP1DknuqX9jOcMUlaOAu7ZT3AacWojHoFKSzsLLEZRD9ExB0s2rrECJ08qLTsk3pRGUqeDyqGU4UX0xfrL0xfyfzdPeTdWdHKn4QpcCbS6iUuevsPG6cqH0MKf9k80GOqUBwYBXoEf0o6ACpUqNEyvjvwwyxJbwJv7jlFS2DSZEmrw%2BvrXiTpLCqCi9xK6Q%2FJcsxLY87reCQ%2FljV16tIPoVbdDNdBp%2BYy0VgMA6cfpJIyNt4P4WSgnV9mzaXBRpJkrBlav20plORU35lzDhE4Z6nNyC5zttP1%2F0T8styULqKDMUNL3N7U83TMHMtv2wrB7tO4e00ihCoMPrK5hEgfFxv%2Bma0NvJ&X-Amz-Signature=531a01a2d427d6a1f3039823a0f544631cea1907c79a9d054a2fd6e7fb0bc1df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFO4X6ZL%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHsjB9pbCaniGKaxLbsEeOx7IqT4yPlhQODZli2ya%2BxmAiEAhIK5DjCgG3dDLtGvc58v4qm0qX%2FFUBXOxacfNDGnZPUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDJ%2FAEvKMfdFlTO1%2FfCrcA2CdsocTv%2FIqN%2B0V2P6l6YxVZPNbM8E9cWIFVVEOu6g9ax5U545S9tCn8NJNVSWOKDTDj7M0tZ9FGNQrHNRuY8KLbkiRcuC25Amsb%2F0A8ajeWdh1lOC2kq5UbMYoH5Jffew7Jv0Tho2yE4Ybnmua5IQ3bwwtU1IsMXmxNcPgyIZQQJVK3wwgQXRLZhxqV3RYRz47%2BQeSVguRLhlMhGx%2BkaXvxfwHtczH8v1NZyw%2Btf%2FiXF%2FcownF5QhJGcx2SYI0LeXMU8u8P9dH%2BbE9Ud5%2BkPy7ROfLdhfGGzBa3WGeSS0jYDN2%2FnTNywka5UNvVIY1ebuImYqOnu4hzPZgwLOIfJgWfKxbBw63cZk1aSZQOtGn986mhVaG5dA0zlu5HXSTVJ60aU%2Bb%2BHz3GXvlpeTGdFow9cundtzFcNwj6kiKjARC69FSe4pzBUfBaUL37RJRRLtbJ7t0iGvx0qbDmUXKFc5otPwi8g1eXzDcMpVgtND35EedIglnSroAU%2F3gXdPcFmKdRwP1DknuqX9jOcMUlaOAu7ZT3AacWojHoFKSzsLLEZRD9ExB0s2rrECJ08qLTsk3pRGUqeDyqGU4UX0xfrL0xfyfzdPeTdWdHKn4QpcCbS6iUuevsPG6cqH0MKf9k80GOqUBwYBXoEf0o6ACpUqNEyvjvwwyxJbwJv7jlFS2DSZEmrw%2BvrXiTpLCqCi9xK6Q%2FJcsxLY87reCQ%2FljV16tIPoVbdDNdBp%2BYy0VgMA6cfpJIyNt4P4WSgnV9mzaXBRpJkrBlav20plORU35lzDhE4Z6nNyC5zttP1%2F0T8styULqKDMUNL3N7U83TMHMtv2wrB7tO4e00ihCoMPrK5hEgfFxv%2Bma0NvJ&X-Amz-Signature=7f6b13f418cbbad9461e4cd12ff08171827be0921e0b2ded3cb5c0f7f4190788&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



