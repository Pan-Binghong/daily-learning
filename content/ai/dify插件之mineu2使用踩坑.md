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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O4GTW3V%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQCjbULtaB8vNUr%2F44O%2BPOuuzSTGa7uXqeZAA9Nvtix51AIhALHd67ntccBjGOymrMusjAT1P5ksjcXLZY8OTGAhe5RbKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXQFjDpUvi2h7P4s4q3ANoOO3t7KXz7LMicnzRk9%2FHHzhM0L%2FLlmEiiDn%2BuK0hbmTND5vkC0%2BWOLdDAW%2BfGpWEgPz8T8bZ2JIclXBukcTkZVGP2V7nHKVSyw%2BHmW4UATIFQOnXH1rdknPBWxNjq00Z2jsS0Fj3Xd6NGFY0PVoh5sMmLY2gNlCSsz8z2%2B89toyKckwrFnIvkajQYng2K6Dd7c8U8WUThnaxSMHyZ4JO%2B1YjZgI5KCfLA13t2dbZ3ayHl%2FTLfdV74l%2B7yLVVSWNgiltTPU%2B%2Fa4VzwSElH83mG8Oj63WxBSDQdlAFT4fV0CdGlpkZJ7yd3X0doaJjLlhUIgrKhUQ8Gz6d7Tj%2BV4BJajIAyq%2FLYoG80kFa2hx6%2FPHRAivHq5qfvHydqFgnRF0pHPnA8b9ls8%2FyCe53gChZQZE5PoQcEbDIWhDHY1DEIrZWiEyINA6C9OzqylxZ%2FW1wtwkYyxaYYUREre2qZ92xa%2Fd7iX8CT8fmpPRzce1jemZbPcOauVKs3kIKEVQYiE%2BUQ%2FLEXduTbSW2b6k5bYRXtQHI4PsEHwxzr8iZGv%2BgzIHjaBu842ZcdSlL3s9QerB0uHfiLolUaDScUb3Q3Aw015%2B1ntmZLPIWkgGdRzEqjbSGr6cRSrnU9mhcKTD0tfTMBjqkAbb2hDcKxXT3%2BdMWeBkFUn7o2%2BXsLM1amvhhIPy1addp7AnmXPquFr66sTkfK%2BCKJfaAqwR9TBkJoYHginH5osEKOFV9W983k3E2XWspNChjag5JoZE%2BPFn15ud0hgrotn2FoNCVh7vKEiyI6gOcJzAirEQ%2BuOAIgF3b4kjVAR01scnNWMGcOIYvLHihAFtDHKfiX3xWvpJ%2FMU1N9IbacBcxRKb2&X-Amz-Signature=968cd7925d4206a8f66a7f5030574014856893e84b9c93a08b3b169ded948947&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O4GTW3V%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJIMEYCIQCjbULtaB8vNUr%2F44O%2BPOuuzSTGa7uXqeZAA9Nvtix51AIhALHd67ntccBjGOymrMusjAT1P5ksjcXLZY8OTGAhe5RbKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXQFjDpUvi2h7P4s4q3ANoOO3t7KXz7LMicnzRk9%2FHHzhM0L%2FLlmEiiDn%2BuK0hbmTND5vkC0%2BWOLdDAW%2BfGpWEgPz8T8bZ2JIclXBukcTkZVGP2V7nHKVSyw%2BHmW4UATIFQOnXH1rdknPBWxNjq00Z2jsS0Fj3Xd6NGFY0PVoh5sMmLY2gNlCSsz8z2%2B89toyKckwrFnIvkajQYng2K6Dd7c8U8WUThnaxSMHyZ4JO%2B1YjZgI5KCfLA13t2dbZ3ayHl%2FTLfdV74l%2B7yLVVSWNgiltTPU%2B%2Fa4VzwSElH83mG8Oj63WxBSDQdlAFT4fV0CdGlpkZJ7yd3X0doaJjLlhUIgrKhUQ8Gz6d7Tj%2BV4BJajIAyq%2FLYoG80kFa2hx6%2FPHRAivHq5qfvHydqFgnRF0pHPnA8b9ls8%2FyCe53gChZQZE5PoQcEbDIWhDHY1DEIrZWiEyINA6C9OzqylxZ%2FW1wtwkYyxaYYUREre2qZ92xa%2Fd7iX8CT8fmpPRzce1jemZbPcOauVKs3kIKEVQYiE%2BUQ%2FLEXduTbSW2b6k5bYRXtQHI4PsEHwxzr8iZGv%2BgzIHjaBu842ZcdSlL3s9QerB0uHfiLolUaDScUb3Q3Aw015%2B1ntmZLPIWkgGdRzEqjbSGr6cRSrnU9mhcKTD0tfTMBjqkAbb2hDcKxXT3%2BdMWeBkFUn7o2%2BXsLM1amvhhIPy1addp7AnmXPquFr66sTkfK%2BCKJfaAqwR9TBkJoYHginH5osEKOFV9W983k3E2XWspNChjag5JoZE%2BPFn15ud0hgrotn2FoNCVh7vKEiyI6gOcJzAirEQ%2BuOAIgF3b4kjVAR01scnNWMGcOIYvLHihAFtDHKfiX3xWvpJ%2FMU1N9IbacBcxRKb2&X-Amz-Signature=ce67b492e3bfdb7cae9e652625a3f4ee0a4e2b999a768cd894acc8d737f5a714&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



