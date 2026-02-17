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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMDRT2ZK%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDJehuc%2B%2BVePYjuaNLlEYCVY92UkAEXSpgn3f9FVYCMwQIhAN33dIiKULX%2FSQxKRnzS0lgJaVpF88AKaDdsBoevAEswKv8DCEQQABoMNjM3NDIzMTgzODA1IgygKxpcQjgVmcJ0coQq3AOMFF0UTF09DV5BcBqmUEn9td6W2a5loWbSdhJ%2Fs6sbHU54gao6Vr152GgpVMXJui0b%2Bw9l3qL14NOGDY2tlVG4aO5RhMt%2BJj1PNxtxfn6AJrAi1oa2WMf6EMTXOBl1LgCf5pZeUo5sH8MWyz6Tzj1V7jVRKg7z011mAs%2Bd0cZm2mw0SpNc4fY5Ihz0bWNT0fia4eKo%2FB4YhvP5edSokwv2k7RmiTRTG21UB09dAswSqZ5CL1qIZo2z6YhSxb96Y1ZyofLZohd3wcso%2B4wZDMBKG%2BEWEReAdEVNT9ki7Idn4g7CQfF7PXJ8ZhF%2FfM2LGgnBxuXLF5ukUnvYlxttou5merVnqlZAoerhieeDkta7QkZBWqoLfpdpzBZ6I3SVWbTv35clbIGyK%2FR%2F8n1H4TQinbwncTJd5dYR7U1oIcUYOpRe0W7uKSHZsxRQio9TUrm54UaVpMZoR%2Fpxk4oLFQ6Q1mV5z9Vs2%2FqszV2J5gxynyDDcd%2BUghjgi5XZzJRE667l8aFZO%2BDT5WkWRGC25MkS0Jgcddg%2BdaD5QVpOEZjuT4zYydnAFZjwYhkR9SGr4CCUV%2BumJ%2B3cu3bV6gvtYPDdn1NgMVqFeYyv60FK%2FzuaJuveFmyz7QtLlc%2BcFDC9v8%2FMBjqkAcFHByjh7wy9i9c%2BVzWok95SjUfh4ejDNkVFB7t5v2QEuxdyhMm9gp4KDiepxXc7jYeAIf46Xwyb4CCiIlXIk4%2B4%2FYDleTU7yMGmVFTdb514APlJe4Zp0cwJslT8FKeRqyrsjk2S9wN%2FJA3c7EphfyBYhJi78W%2FkZlMCsQ6gFZS2TvYrwO0oUP7h2RKAu%2FKcZfM9fRwJ9MhrO2CuHqgZOMh6Rwt7&X-Amz-Signature=096bc84bf406a1207ea53b9f6ee91e5edaeac7d377ad01b5837d719a3f385910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VMDRT2ZK%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDJehuc%2B%2BVePYjuaNLlEYCVY92UkAEXSpgn3f9FVYCMwQIhAN33dIiKULX%2FSQxKRnzS0lgJaVpF88AKaDdsBoevAEswKv8DCEQQABoMNjM3NDIzMTgzODA1IgygKxpcQjgVmcJ0coQq3AOMFF0UTF09DV5BcBqmUEn9td6W2a5loWbSdhJ%2Fs6sbHU54gao6Vr152GgpVMXJui0b%2Bw9l3qL14NOGDY2tlVG4aO5RhMt%2BJj1PNxtxfn6AJrAi1oa2WMf6EMTXOBl1LgCf5pZeUo5sH8MWyz6Tzj1V7jVRKg7z011mAs%2Bd0cZm2mw0SpNc4fY5Ihz0bWNT0fia4eKo%2FB4YhvP5edSokwv2k7RmiTRTG21UB09dAswSqZ5CL1qIZo2z6YhSxb96Y1ZyofLZohd3wcso%2B4wZDMBKG%2BEWEReAdEVNT9ki7Idn4g7CQfF7PXJ8ZhF%2FfM2LGgnBxuXLF5ukUnvYlxttou5merVnqlZAoerhieeDkta7QkZBWqoLfpdpzBZ6I3SVWbTv35clbIGyK%2FR%2F8n1H4TQinbwncTJd5dYR7U1oIcUYOpRe0W7uKSHZsxRQio9TUrm54UaVpMZoR%2Fpxk4oLFQ6Q1mV5z9Vs2%2FqszV2J5gxynyDDcd%2BUghjgi5XZzJRE667l8aFZO%2BDT5WkWRGC25MkS0Jgcddg%2BdaD5QVpOEZjuT4zYydnAFZjwYhkR9SGr4CCUV%2BumJ%2B3cu3bV6gvtYPDdn1NgMVqFeYyv60FK%2FzuaJuveFmyz7QtLlc%2BcFDC9v8%2FMBjqkAcFHByjh7wy9i9c%2BVzWok95SjUfh4ejDNkVFB7t5v2QEuxdyhMm9gp4KDiepxXc7jYeAIf46Xwyb4CCiIlXIk4%2B4%2FYDleTU7yMGmVFTdb514APlJe4Zp0cwJslT8FKeRqyrsjk2S9wN%2FJA3c7EphfyBYhJi78W%2FkZlMCsQ6gFZS2TvYrwO0oUP7h2RKAu%2FKcZfM9fRwJ9MhrO2CuHqgZOMh6Rwt7&X-Amz-Signature=f06966e72f857965bba3cf953a4f6be55f0b157860843a64866b67b69912f37b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



