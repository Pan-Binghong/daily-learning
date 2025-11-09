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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TM7NPRGS%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDgKxuBKoZIlyJ1IzUIEAcMKriXjA0UjWel%2BrR9pAuIFQIhALA3MZosR1fdwmP4en0JkH1y5Id%2BkvtAolYMMPRQrxXNKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEjVX2R62%2BYdPS7LQq3AMGSCfn1EFkHKzsliifN6pzR7CbSsPEabhW%2BHmvu1TFoTTAx9fiU2ePLJ6ZV7Hmei4Mqs8hK7aVTInV1ex%2FzFFmGHg9IQ7vfiri5w8dEuuvhYOV29PM3y7QZ8ATUxmC9k2TVZeue5MDT0uwsDb%2Bx3fHPOzhMv44v6KbVoHqXZju1sNOXMZTpljhNlM6PyOcIrNlb7VOfIUu0ebdjZn%2Bw04d%2BGrCQLbvCDJAbbSLTCziQSlYWVX366YTjUAt7eU%2BNICugNFj7f0sH2Kf%2FXiZsAJWhqpRJ4IfKy5Ow67C1d5Oa4MD%2BxQBcPm6D5yg%2FXxdZt1m9cULU3LCwx6l44fNQr58uoj%2BM8ef7ZzBWUfxYrtcA17FjseRrjZef4RUS%2BDCsyR1HNppZIO04bKpC%2F6o0iMRmkN1XtXBViZoMxpqKDtOX6IZHkSBivlRN5HzwAIdZAjeZOzU5d0oCtp5V%2FfJAZDDQGZHvYYwQfNC92HzaJNXsJ1HOHOrHvwA0v4lEEIbiQ1cGSiqv1loduN9rkRc5mF0NVuIvy99uwEhiSp5RshQ46KXtwSYS0gxp8yRYPseDCM1J3v5YLGqOmZ4R4swXRZ2g06mxs3Y6rD%2F0YzQK85lW9IzN5%2FWWNT%2B01MUnTDit7%2FIBjqkAcup4BCYjEsfiliZe%2BqmrF6AywFl%2FFDvNYV9T5csMGfmRZbv%2FHQ9t%2BUhUbbxKyMXSVDZZ%2BDr%2BOd1w0r1R29xBe2AFxFzMaLiKs6drDQRMmGWkU4LqZYhxw0PlsqE5KbqCF3V5a%2BCGh2Cr490gB0W5a%2FUryyWeIYeIiLb6GAE%2BMfKVnFwWX8EWtvwMgKcMYBVuvYVjiIs71JImFhPdqB4tRq%2BPicV&X-Amz-Signature=b0cdad81c2bcb2afd06d0033e4b6feec0af04168ddb51682d4a219d4325db49f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TM7NPRGS%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJIMEYCIQDgKxuBKoZIlyJ1IzUIEAcMKriXjA0UjWel%2BrR9pAuIFQIhALA3MZosR1fdwmP4en0JkH1y5Id%2BkvtAolYMMPRQrxXNKogECOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyEjVX2R62%2BYdPS7LQq3AMGSCfn1EFkHKzsliifN6pzR7CbSsPEabhW%2BHmvu1TFoTTAx9fiU2ePLJ6ZV7Hmei4Mqs8hK7aVTInV1ex%2FzFFmGHg9IQ7vfiri5w8dEuuvhYOV29PM3y7QZ8ATUxmC9k2TVZeue5MDT0uwsDb%2Bx3fHPOzhMv44v6KbVoHqXZju1sNOXMZTpljhNlM6PyOcIrNlb7VOfIUu0ebdjZn%2Bw04d%2BGrCQLbvCDJAbbSLTCziQSlYWVX366YTjUAt7eU%2BNICugNFj7f0sH2Kf%2FXiZsAJWhqpRJ4IfKy5Ow67C1d5Oa4MD%2BxQBcPm6D5yg%2FXxdZt1m9cULU3LCwx6l44fNQr58uoj%2BM8ef7ZzBWUfxYrtcA17FjseRrjZef4RUS%2BDCsyR1HNppZIO04bKpC%2F6o0iMRmkN1XtXBViZoMxpqKDtOX6IZHkSBivlRN5HzwAIdZAjeZOzU5d0oCtp5V%2FfJAZDDQGZHvYYwQfNC92HzaJNXsJ1HOHOrHvwA0v4lEEIbiQ1cGSiqv1loduN9rkRc5mF0NVuIvy99uwEhiSp5RshQ46KXtwSYS0gxp8yRYPseDCM1J3v5YLGqOmZ4R4swXRZ2g06mxs3Y6rD%2F0YzQK85lW9IzN5%2FWWNT%2B01MUnTDit7%2FIBjqkAcup4BCYjEsfiliZe%2BqmrF6AywFl%2FFDvNYV9T5csMGfmRZbv%2FHQ9t%2BUhUbbxKyMXSVDZZ%2BDr%2BOd1w0r1R29xBe2AFxFzMaLiKs6drDQRMmGWkU4LqZYhxw0PlsqE5KbqCF3V5a%2BCGh2Cr490gB0W5a%2FUryyWeIYeIiLb6GAE%2BMfKVnFwWX8EWtvwMgKcMYBVuvYVjiIs71JImFhPdqB4tRq%2BPicV&X-Amz-Signature=79516b3b66563f86016bd418be0bbb609e8e6c37d5ddfad6cd988b9c6e7d0ded&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



