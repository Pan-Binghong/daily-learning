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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHR3IETN%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCqXDAO9fr%2Fhf9uFpbt3TFNxW3kmkV1YHD5vew5eyRe3QIhAJ7GErIX0XrsCWJjNI2JdMgJ7KP7lJjXAw%2FpnKw5YdHsKv8DCEMQABoMNjM3NDIzMTgzODA1IgxzLPRspKc5nylZX44q3AMMzRZE13OtTIq0Tg0A73g8rqH2iNTR0blo1aIOmrAuv3mvmnqUMnnHBh0MnAaTSjnzha9%2FDNrcKKirxp4kAJ%2BdhR%2FXkyN4Li2uW3OV5JlvpYFYMXQqygxWq6yMWMkb28AkepFCB6Sx2ol%2FSQELHP37boIlv%2Fjtn2VVWBwoAV2MOyjIEWZm9JSuWXKzPbjByjBk%2B4f4Ri6KfqLFi4pt00TljFCKKzu8NpkrsUshjCO7vSpvF%2B6LgKTbadOs%2BTKwP50QLNU55aIsH%2BE4czBvoFj1Yt2mx%2FRD0GY8hc59CAFDkz5BrQO4DyM2u7ez9yHQ8HiXJqLHZLuDuu0V05mWa33Z0tiPb72oCoDCMXzyp82aIzgX0vg%2FbyC67OxnD0U%2FwgS9YWggBl7OlmiU4A9dxL%2BLl%2B25oVGtNHDrYEZCbO0Q7ES%2By%2FNoEF8VHJb1erBk%2FHVHyjT1cCXkUhcuLmzu0G%2FWpgfJwhqdItORM%2FQqnBczn2huyXxD7CCChRh0aP0yq1Qxj648e2qEilYrJC3%2BOLfQcz1cAuaZagIL9bZY%2Bgrr0oFMwQbYzgIMXkBII%2FuUClVJN7YMYbMcmOTrO4dZPO0kq0O9b68hGBQIWTnISgAQSSMy9Leea5XU9nYAcDCA8tTIBjqkAauc3U%2FlkYddTWo9nY6cMIXsDfStYV9sKyEIpJtHbcX0EcknW6cm1y2bJ3I%2FBTXQIagl6%2Fk48C%2BBDgbgO%2BY6irUQUjdn%2Bjnx4stZTjR%2FrcHsJ0oZRx5i%2FarzailuIRNmhsJWH3XISarPFAjrBnLPhUZU8XQPUQ6fbBjWNBXgO9D6XihEp2FW22mLStjeF0NJal1rJ1k5lnihn0rTW%2FtSWFv7EiZZ&X-Amz-Signature=30c08fa81f7787c8fd18810a0d1ab00bc66ba0b1f4a84e313bf5c7797fd901fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHR3IETN%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQCqXDAO9fr%2Fhf9uFpbt3TFNxW3kmkV1YHD5vew5eyRe3QIhAJ7GErIX0XrsCWJjNI2JdMgJ7KP7lJjXAw%2FpnKw5YdHsKv8DCEMQABoMNjM3NDIzMTgzODA1IgxzLPRspKc5nylZX44q3AMMzRZE13OtTIq0Tg0A73g8rqH2iNTR0blo1aIOmrAuv3mvmnqUMnnHBh0MnAaTSjnzha9%2FDNrcKKirxp4kAJ%2BdhR%2FXkyN4Li2uW3OV5JlvpYFYMXQqygxWq6yMWMkb28AkepFCB6Sx2ol%2FSQELHP37boIlv%2Fjtn2VVWBwoAV2MOyjIEWZm9JSuWXKzPbjByjBk%2B4f4Ri6KfqLFi4pt00TljFCKKzu8NpkrsUshjCO7vSpvF%2B6LgKTbadOs%2BTKwP50QLNU55aIsH%2BE4czBvoFj1Yt2mx%2FRD0GY8hc59CAFDkz5BrQO4DyM2u7ez9yHQ8HiXJqLHZLuDuu0V05mWa33Z0tiPb72oCoDCMXzyp82aIzgX0vg%2FbyC67OxnD0U%2FwgS9YWggBl7OlmiU4A9dxL%2BLl%2B25oVGtNHDrYEZCbO0Q7ES%2By%2FNoEF8VHJb1erBk%2FHVHyjT1cCXkUhcuLmzu0G%2FWpgfJwhqdItORM%2FQqnBczn2huyXxD7CCChRh0aP0yq1Qxj648e2qEilYrJC3%2BOLfQcz1cAuaZagIL9bZY%2Bgrr0oFMwQbYzgIMXkBII%2FuUClVJN7YMYbMcmOTrO4dZPO0kq0O9b68hGBQIWTnISgAQSSMy9Leea5XU9nYAcDCA8tTIBjqkAauc3U%2FlkYddTWo9nY6cMIXsDfStYV9sKyEIpJtHbcX0EcknW6cm1y2bJ3I%2FBTXQIagl6%2Fk48C%2BBDgbgO%2BY6irUQUjdn%2Bjnx4stZTjR%2FrcHsJ0oZRx5i%2FarzailuIRNmhsJWH3XISarPFAjrBnLPhUZU8XQPUQ6fbBjWNBXgO9D6XihEp2FW22mLStjeF0NJal1rJ1k5lnihn0rTW%2FtSWFv7EiZZ&X-Amz-Signature=ea7898aebe70dfba8caf8c9469c0496a60198662ade1de38a71530c324c73048&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



