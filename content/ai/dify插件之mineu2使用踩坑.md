---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
标签:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ65LGXH%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkC%2FXqn028qq6N3ETc6aqq%2FV54XnDd64jKxeC71xqdgAiBXvsl%2FO9WK8fef9%2B%2Bk%2BoJo2qZakb%2BYG%2Byl0a4DCRaeHyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWuuwCgVlX68lQjHKtwDjSuRQQSR8xeTxZ6PreltUXGZT6MeO83OQCsKb1d0C1cJbDnEhffyU6cga%2Bgk6XU8eJviibNGd1OUT%2BgXjyg%2FVrM1nzToO57DW7ZWGvV%2B7nJfq7DjMJXNfj2LoQjsuLAUDEmmcg8YsDE5FnbPHcNjZNb2E0p0EJDoGIoUAebCRUtsNSM2GmchqbDKTzyRnkhN%2Bdzi%2F6Kee0AFLe5p%2FyTzKo7Vyr2QmrUVfNIC8Fb37ZfD8d2qYY1AsgAy1KQ8tVgWsvgB1pkwjmrsriIZxU9NPVG7kywj0eC4ywGlQMUC%2Bn%2BzPnDv0%2FLrEwBDpA1zDiBVkANuse%2FdPadWhz0qS1cm0k809Vmup4ttUgnyRSlPUzt2O8GOmvSb%2F95yWGt82AA8KYy7oYf%2F1u7vmr163dqX9RkSVg2K85Ak4RgXoAUZWd6ftmoU2hcVu4rtYpCUum3NMaeBodwt5ABELiQ3dgVLIL6jSn6hNoH1XIRT4RiyEbkDxf6lP1aEF9M3iCwecgQxsMY4uQWMZO8mW6jV1r98p8XK2GTbMvxmfO2Lj9pRj4C06Ingns7oocCFy2pEPj0ewq3yO%2BXfulp8cCxsYU%2BJLr9hSA56oyLrzBzIuXpavvgDRMWSPv%2FWzhRQytMwu6KsyAY6pgFdTgG0IpwMqrFJj699qYefq8rvOzMqtyMySP3%2FFaDTTe0rtNB1xQ%2B%2BjlAK9TRM93KkRINdhEPkOB%2FCiIbUbrVY0bnolsUTAmTSD8iOpaekPM942BD7GQ2jRQBvsDVGF3oGQPqL0icDcKy3kdAkC0ueg%2FJLsY2QMnBprFg72oIFKSsU2Wcx3Wkbdh4QJaow33YY8oBcAjOPKJFlmTDZp4Gh43FuJu5b&X-Amz-Signature=3955447c4ff569f4ab5f5ba165e637282466eb51070b98557f5bc1753bbfd6c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ65LGXH%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkC%2FXqn028qq6N3ETc6aqq%2FV54XnDd64jKxeC71xqdgAiBXvsl%2FO9WK8fef9%2B%2Bk%2BoJo2qZakb%2BYG%2Byl0a4DCRaeHyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWuuwCgVlX68lQjHKtwDjSuRQQSR8xeTxZ6PreltUXGZT6MeO83OQCsKb1d0C1cJbDnEhffyU6cga%2Bgk6XU8eJviibNGd1OUT%2BgXjyg%2FVrM1nzToO57DW7ZWGvV%2B7nJfq7DjMJXNfj2LoQjsuLAUDEmmcg8YsDE5FnbPHcNjZNb2E0p0EJDoGIoUAebCRUtsNSM2GmchqbDKTzyRnkhN%2Bdzi%2F6Kee0AFLe5p%2FyTzKo7Vyr2QmrUVfNIC8Fb37ZfD8d2qYY1AsgAy1KQ8tVgWsvgB1pkwjmrsriIZxU9NPVG7kywj0eC4ywGlQMUC%2Bn%2BzPnDv0%2FLrEwBDpA1zDiBVkANuse%2FdPadWhz0qS1cm0k809Vmup4ttUgnyRSlPUzt2O8GOmvSb%2F95yWGt82AA8KYy7oYf%2F1u7vmr163dqX9RkSVg2K85Ak4RgXoAUZWd6ftmoU2hcVu4rtYpCUum3NMaeBodwt5ABELiQ3dgVLIL6jSn6hNoH1XIRT4RiyEbkDxf6lP1aEF9M3iCwecgQxsMY4uQWMZO8mW6jV1r98p8XK2GTbMvxmfO2Lj9pRj4C06Ingns7oocCFy2pEPj0ewq3yO%2BXfulp8cCxsYU%2BJLr9hSA56oyLrzBzIuXpavvgDRMWSPv%2FWzhRQytMwu6KsyAY6pgFdTgG0IpwMqrFJj699qYefq8rvOzMqtyMySP3%2FFaDTTe0rtNB1xQ%2B%2BjlAK9TRM93KkRINdhEPkOB%2FCiIbUbrVY0bnolsUTAmTSD8iOpaekPM942BD7GQ2jRQBvsDVGF3oGQPqL0icDcKy3kdAkC0ueg%2FJLsY2QMnBprFg72oIFKSsU2Wcx3Wkbdh4QJaow33YY8oBcAjOPKJFlmTDZp4Gh43FuJu5b&X-Amz-Signature=2802003dcb6d92165c4841524c30bf10ed72f87f7270cf1cc9985b725e72d8af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



