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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UFJTWJJ%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCabXxzCYnNFMF2R2stHe3C96vnQO1m9QtJHQUrEmyjLgIgH%2BAx%2FXlvJv3fhwKCL8aQskpSWJ62r09rnZCDWUIPnmUqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDy3XonlmYmGta7OcCrcA2Wrz8sq2XUL%2Bp9EPxriRy03ZhPVZcGWaQueHkhFvqgsbtmLT4rF%2FaMfsmP2J6SmsaYtnScsXlXuVDn%2B3kBi1WcY4iFnrp%2FudgU8OxGTtXP5m9lzMsK4BTUBL8nUWTjE7yp%2BHNVRZgx%2FboRYpPN%2BltaCdPQuTeCicr6QO%2BkLzOX8nex4UlLZvytRr3kuSqPNPfLfJlNICW8VFON22lyfHwPokgxrTSaijjwhyvgtSpXlxa8Hr%2FOgCbdLco2icLxeRbSZu%2B3RBMuCccJbkFP3i2oR9ZiPoSgJI%2Bv2okcmmaq%2B57rzVb3KwUwpnySYU3QEbYZoU5ms88%2BRbhgVSdObXFpmYNuYcK3xvhCJiF0PiKgER0O%2Bzzp5rcfz%2FT3DlxmgXq0PevlqXN%2BjxpIEK2T%2B5gJBMR2T42VAOQJtVDtNLkXJV2R55svppwWe6D4XfZHUxliQmSzPn9D%2Fapd8c0yDWOMRBq0Yan4OtJOtOKlbteyZfpkeh4oaQxatLVWSqUKCdIAVho0CQOAqhmfJ55oDHYXyhq1M%2F3ldtqyC%2BJ8w1AgFkQKTVQb7qJWaTYWnUxBL6mci054Tx9R1eJUGKkdAMzSlDqNV0w1yO5g1wWFIi89epI4faNctxIQ2VhpuMIjh5MgGOqUBjNL%2FCZFhED3%2B1odvbGB841J%2FMQ1%2FgK7rhqRL8mQjQ9EY%2BCB2l8yHKxc7KZQB2YiTyYQm2JzIC%2BVHULmAyZQgxgGL7MY8LKplOLdHEnlnsFu%2BVdi7yncJ4PpUZHDaBmtLnhj9puapNTgUzu5FC0fCk2Ju9YfQg9KS2WLWcVu3RR4d7HIyRUeSlIcZxD5Ah2DrnaWIGXb4VtEspCwcqqAlyhvU7dtS&X-Amz-Signature=692f5240356178dff4289e6a8027b7fe954c4be0a81c38db31c5d8f42281bc29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UFJTWJJ%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCabXxzCYnNFMF2R2stHe3C96vnQO1m9QtJHQUrEmyjLgIgH%2BAx%2FXlvJv3fhwKCL8aQskpSWJ62r09rnZCDWUIPnmUqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDy3XonlmYmGta7OcCrcA2Wrz8sq2XUL%2Bp9EPxriRy03ZhPVZcGWaQueHkhFvqgsbtmLT4rF%2FaMfsmP2J6SmsaYtnScsXlXuVDn%2B3kBi1WcY4iFnrp%2FudgU8OxGTtXP5m9lzMsK4BTUBL8nUWTjE7yp%2BHNVRZgx%2FboRYpPN%2BltaCdPQuTeCicr6QO%2BkLzOX8nex4UlLZvytRr3kuSqPNPfLfJlNICW8VFON22lyfHwPokgxrTSaijjwhyvgtSpXlxa8Hr%2FOgCbdLco2icLxeRbSZu%2B3RBMuCccJbkFP3i2oR9ZiPoSgJI%2Bv2okcmmaq%2B57rzVb3KwUwpnySYU3QEbYZoU5ms88%2BRbhgVSdObXFpmYNuYcK3xvhCJiF0PiKgER0O%2Bzzp5rcfz%2FT3DlxmgXq0PevlqXN%2BjxpIEK2T%2B5gJBMR2T42VAOQJtVDtNLkXJV2R55svppwWe6D4XfZHUxliQmSzPn9D%2Fapd8c0yDWOMRBq0Yan4OtJOtOKlbteyZfpkeh4oaQxatLVWSqUKCdIAVho0CQOAqhmfJ55oDHYXyhq1M%2F3ldtqyC%2BJ8w1AgFkQKTVQb7qJWaTYWnUxBL6mci054Tx9R1eJUGKkdAMzSlDqNV0w1yO5g1wWFIi89epI4faNctxIQ2VhpuMIjh5MgGOqUBjNL%2FCZFhED3%2B1odvbGB841J%2FMQ1%2FgK7rhqRL8mQjQ9EY%2BCB2l8yHKxc7KZQB2YiTyYQm2JzIC%2BVHULmAyZQgxgGL7MY8LKplOLdHEnlnsFu%2BVdi7yncJ4PpUZHDaBmtLnhj9puapNTgUzu5FC0fCk2Ju9YfQg9KS2WLWcVu3RR4d7HIyRUeSlIcZxD5Ah2DrnaWIGXb4VtEspCwcqqAlyhvU7dtS&X-Amz-Signature=7911445900ae79666b47dd513d993d6735d1dbca631c117003f1ec2481da3711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



