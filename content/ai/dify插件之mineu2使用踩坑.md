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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUXYLLEU%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIEIodEWXWc2T7Ec7QAuXMBKQy%2BeoGqi2Z2QAtgrvLAdwAiEA1cjdxAJL0S7%2BBRf%2FG6FaujA1u0FvWQ%2BOoagwIWSPtM8q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDOqc7Mqq6kEbWk5zBCrcA5AdpyCcHJg%2Bv2dX1kKYiEmaP6hY5d7LOrpYaF53b8fKxYH4cx%2FxOF19I2JaUbLH2lQ2M87XbWgHJBMNYyzG30czemcR0hNPNA3O1E1d%2Buy4pvctg%2F31C%2BTM1IWYzQ4LZzLlDcKY1kakheZ%2F%2B%2F3cYqup9v%2FyWOYg2oPybWO3MyGcTy05injMqCxHHjTzxQDv3XqeeqUTjjdnXQKyoKUto58pf6WUEX4eVFandckt8JRGM%2FE44z8n%2BqhtrrnLzq86BI4WIXLJiRTiWVPK2TYr0SF%2FyHWEYvhKWVlIX2itbZ0sg2osnVQFo2%2FCb5mWQhvOgvFG3tvewRpX18Hl0Y%2Fbiedy1KuQdyicPRIUZNgcc6NrCPAIFjFJvZz78BG009n%2F%2F7YCtTSnEpqv7klQEHUvkoLIxe1Ry2HNa2HVBJ%2FDIcJ1W3IZ9y8A%2FUC6uiH5ZbOsdQZfmT50fsmmgcmA0SIwAGln%2FMZWv1tOAIPpQV1BUIVVs6vuqmaPANzJXxD%2FTZp5o%2FlTTBZPjbaWW6VcfzBxLXdAJXP6m5KVLSYHWoa98jfA1052Qmcf7Ip2wYgQCE1OyFsiy9QKvVN2jbRou47N%2FynZ%2FQqmIxduj5GQIe7ao0gPhJ3C7cYxSMMdhbnLMN6UvskGOqUB%2Fh3DuVAf0RSCbU0MeCIY1I0juTR%2FuzLgSNC%2FGNXtLEwKxmBwgnvxMcDCqZ%2F45VkFFFoRxsqu5o4XPL2ExT6S0VthGtJwh4Sjhk7fsi2vTstjkjABwllnNwuwq9R8VxTZ4z8r%2F18pYOs4HsRP5GNZLBgjKRx%2FMe8BGERitLyETil42n85MMJhyzUafEieiBBQIHvjstkvikR5fCcKJPYPZW0YTbIV&X-Amz-Signature=0efa59fa2c2d483b83850b0af92f7a8dd31772130f5f59a5f01a50402861a6b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUXYLLEU%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIEIodEWXWc2T7Ec7QAuXMBKQy%2BeoGqi2Z2QAtgrvLAdwAiEA1cjdxAJL0S7%2BBRf%2FG6FaujA1u0FvWQ%2BOoagwIWSPtM8q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDOqc7Mqq6kEbWk5zBCrcA5AdpyCcHJg%2Bv2dX1kKYiEmaP6hY5d7LOrpYaF53b8fKxYH4cx%2FxOF19I2JaUbLH2lQ2M87XbWgHJBMNYyzG30czemcR0hNPNA3O1E1d%2Buy4pvctg%2F31C%2BTM1IWYzQ4LZzLlDcKY1kakheZ%2F%2B%2F3cYqup9v%2FyWOYg2oPybWO3MyGcTy05injMqCxHHjTzxQDv3XqeeqUTjjdnXQKyoKUto58pf6WUEX4eVFandckt8JRGM%2FE44z8n%2BqhtrrnLzq86BI4WIXLJiRTiWVPK2TYr0SF%2FyHWEYvhKWVlIX2itbZ0sg2osnVQFo2%2FCb5mWQhvOgvFG3tvewRpX18Hl0Y%2Fbiedy1KuQdyicPRIUZNgcc6NrCPAIFjFJvZz78BG009n%2F%2F7YCtTSnEpqv7klQEHUvkoLIxe1Ry2HNa2HVBJ%2FDIcJ1W3IZ9y8A%2FUC6uiH5ZbOsdQZfmT50fsmmgcmA0SIwAGln%2FMZWv1tOAIPpQV1BUIVVs6vuqmaPANzJXxD%2FTZp5o%2FlTTBZPjbaWW6VcfzBxLXdAJXP6m5KVLSYHWoa98jfA1052Qmcf7Ip2wYgQCE1OyFsiy9QKvVN2jbRou47N%2FynZ%2FQqmIxduj5GQIe7ao0gPhJ3C7cYxSMMdhbnLMN6UvskGOqUB%2Fh3DuVAf0RSCbU0MeCIY1I0juTR%2FuzLgSNC%2FGNXtLEwKxmBwgnvxMcDCqZ%2F45VkFFFoRxsqu5o4XPL2ExT6S0VthGtJwh4Sjhk7fsi2vTstjkjABwllnNwuwq9R8VxTZ4z8r%2F18pYOs4HsRP5GNZLBgjKRx%2FMe8BGERitLyETil42n85MMJhyzUafEieiBBQIHvjstkvikR5fCcKJPYPZW0YTbIV&X-Amz-Signature=86eec9cd0ae88b0e6a61dadf4afccc1e9a1eb481f41eaaaadc5772205454a0b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



