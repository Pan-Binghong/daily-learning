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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGIMGIA6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHB4ZqN9c4PUB8kzkjxDtkUaTunOghydlW%2BjZ0bZdKVjAiBCNvLnSl0aTh96ZnI5bE6RRU96Xxp2gtUFBlnAEx5VoCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMUnIZ0QGxuRfVPBZyKtwDLJGryDZSiwB%2BbFCmHivWC3t2imVfQ8LTFClw9%2FO32uVE16iZUDOC9evfDTn0SUOn0QawFZXyNkSGbtfUo6MxxuYmNIFiH8621iA3J4Dxxs3PSAaJ%2FQMv2rKA6qXRHCaARiuC895NWNjxiFfXX4rHcn647ecwh9mpLapPkUmv9bKVydjqgFL8gYnQixD6t7O%2F%2Bh5neVcHmbFjxotgNYwS6%2B3jY0bTjNkfLPyZov46h08fAGj%2FYgFlwkjGYjoJB7zhGBmp9kkxsY%2BqMNDN2PJ23sCZBNuo4B%2BfDyMr2QEVZ7MS3svoQ66VI9GZQfzAuWcAhT0uwoBtr2XX7mHdDxPTABcds%2FLktv%2BVtDoXFXN0gcJEr6YS%2BXHzq9LYlpBBuRsZhvAoLMcik7SkhZBx%2BXQBOuZzmyMo%2B%2BPZHI1pPG41eEb7VOFEN6Va1vKmHuwiM4RKBLHmoMlD8vDAdd5qY%2FWR1ECyqhurx%2BvE0lxZpjthryvv%2FtQuFtuvBtHBk5Wl%2FFb%2FqN0%2FfzP97XwFgv8FPBfK0CQ%2BYNTp2MpCMS6MH9VptRrlc5vDbXx84KhoUUmIS8MjdZv6ndqQEhZoEbl3JjY8qpCyrXsxXgAFHlDpWs%2BQ1RfuzcvbPQY2yKY3euMw%2B%2FLZzAY6pgEM332b9ZrOuF5CQ5r%2F%2FREKKU6UTjeMxErCUDJHbWtR5tkXErrM0Y1CMgt%2Bv%2BswojZYNQ8jeJwCU5Gf2fGnOrbq1%2BVzaIjM4CrH0U0P%2FjjaBbBotpQsIZyHbFeAP5YDxVqUrk6S03bhyIloqY0LVOJXiBN%2BOQSKyTCqkjVGd1s3T%2FqH6qAL8hxzH%2Bm8ujBjFOVVuGrKxObG7P8Er%2Fvxc%2FYVeDpEwRN3&X-Amz-Signature=6f396e950124fd2f12182fcdfa4fb9ada3851488f7885fcd434cc2344235db68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGIMGIA6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHB4ZqN9c4PUB8kzkjxDtkUaTunOghydlW%2BjZ0bZdKVjAiBCNvLnSl0aTh96ZnI5bE6RRU96Xxp2gtUFBlnAEx5VoCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMUnIZ0QGxuRfVPBZyKtwDLJGryDZSiwB%2BbFCmHivWC3t2imVfQ8LTFClw9%2FO32uVE16iZUDOC9evfDTn0SUOn0QawFZXyNkSGbtfUo6MxxuYmNIFiH8621iA3J4Dxxs3PSAaJ%2FQMv2rKA6qXRHCaARiuC895NWNjxiFfXX4rHcn647ecwh9mpLapPkUmv9bKVydjqgFL8gYnQixD6t7O%2F%2Bh5neVcHmbFjxotgNYwS6%2B3jY0bTjNkfLPyZov46h08fAGj%2FYgFlwkjGYjoJB7zhGBmp9kkxsY%2BqMNDN2PJ23sCZBNuo4B%2BfDyMr2QEVZ7MS3svoQ66VI9GZQfzAuWcAhT0uwoBtr2XX7mHdDxPTABcds%2FLktv%2BVtDoXFXN0gcJEr6YS%2BXHzq9LYlpBBuRsZhvAoLMcik7SkhZBx%2BXQBOuZzmyMo%2B%2BPZHI1pPG41eEb7VOFEN6Va1vKmHuwiM4RKBLHmoMlD8vDAdd5qY%2FWR1ECyqhurx%2BvE0lxZpjthryvv%2FtQuFtuvBtHBk5Wl%2FFb%2FqN0%2FfzP97XwFgv8FPBfK0CQ%2BYNTp2MpCMS6MH9VptRrlc5vDbXx84KhoUUmIS8MjdZv6ndqQEhZoEbl3JjY8qpCyrXsxXgAFHlDpWs%2BQ1RfuzcvbPQY2yKY3euMw%2B%2FLZzAY6pgEM332b9ZrOuF5CQ5r%2F%2FREKKU6UTjeMxErCUDJHbWtR5tkXErrM0Y1CMgt%2Bv%2BswojZYNQ8jeJwCU5Gf2fGnOrbq1%2BVzaIjM4CrH0U0P%2FjjaBbBotpQsIZyHbFeAP5YDxVqUrk6S03bhyIloqY0LVOJXiBN%2BOQSKyTCqkjVGd1s3T%2FqH6qAL8hxzH%2Bm8ujBjFOVVuGrKxObG7P8Er%2Fvxc%2FYVeDpEwRN3&X-Amz-Signature=850799dafed0d8784d30c157a4257107e743159fed2903461f77777f81853657&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



