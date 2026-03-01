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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WTTT4E5%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAxZFrlPSApp0DQjYslTiELXmTWQhxch0wVUPoTwLLO9AiBtg3%2F6xE8Ea3rB5XlI4iao8BQWGLbOTH1GkNefmJjW1Cr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMt2bPF8KC7OEhjETMKtwDj504RwMyKAfEMoiwzoyBrzVlK4K3hlcOcLPLS5KmcOZM1yXFTRqPRVVDe8ybilRtZQwCfbjLY9tSTn84XglzMVFwEbmB1dPU5%2Fu%2F2YH31W2bBbhVQNpKw3nvo8ojBYXZ59fiYYCLiLckbCC%2F6SFRml0FgM63sS0U9fYHd2phixpDn%2FeZKP4sIJV90dLE6ZjTif8urP0wTa2aVA7ddWKrG0G8A2bQ3f35R5IS2pLIkY%2B3CdY2qHzLv2DzrX5fUZXTj9az3ilaSa28L3ADM0w0vPl0UHUzrozAIiEwOaRI3rZgt3d%2BWgHzyPgKMMaQAznEZMU%2FA0wvgZkpRgbAAC%2B2YWP32wgc3lgJf%2BZl%2BV7Jid2VEzBDvK4iMLp%2FvNSYX4ymKUmuC2r1XAVR8bMnQdkuLi8sA68myQ%2BOzec5WZ2dreOwcrBGNHc41ewPQBOQ4hzYtlGBwY9RwGHG6uDRGRwBjTxgi7S%2BoXbywmOFa8DLfddy8RefRuiie0uuO9zrIZJIjD9BFtv6KMHfDHqfgNJJwlgpwjMK9mNn7xAxLlxNXsKiEfnLCtuXkghopcClrfMdC%2Bf%2FjWjWECYoNKglGz99p0%2F0bTEZgD4e1vy04cwzXPxVBZcUKWPKshP0%2FN8wo86OzQY6pgF2agXFjBVuG85kY7Zc%2Bqedqykrety033T0%2Fjvd9eAqijIT7BRj6nGnyRBD%2Fubs5QqwyZ2wjIpW66qgflD7KC4OOGhCNndp0ciVgiBLF9%2FE0sQgcummvxtWdtNFIhIJOTo0xppAjpqnd4GLe5TCrs42kyW4kYPDcCxcO8bZ6clkWBTQMoHNjUdwEpEkZWOhbKK6LoVu7%2FqNgHzOn7k74dxQ4ZVCdmy1&X-Amz-Signature=0645ef4d78e86d8b167d7287aa45b7d3d6b5269ac350a297ca839ff300f2ce97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WTTT4E5%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAxZFrlPSApp0DQjYslTiELXmTWQhxch0wVUPoTwLLO9AiBtg3%2F6xE8Ea3rB5XlI4iao8BQWGLbOTH1GkNefmJjW1Cr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMt2bPF8KC7OEhjETMKtwDj504RwMyKAfEMoiwzoyBrzVlK4K3hlcOcLPLS5KmcOZM1yXFTRqPRVVDe8ybilRtZQwCfbjLY9tSTn84XglzMVFwEbmB1dPU5%2Fu%2F2YH31W2bBbhVQNpKw3nvo8ojBYXZ59fiYYCLiLckbCC%2F6SFRml0FgM63sS0U9fYHd2phixpDn%2FeZKP4sIJV90dLE6ZjTif8urP0wTa2aVA7ddWKrG0G8A2bQ3f35R5IS2pLIkY%2B3CdY2qHzLv2DzrX5fUZXTj9az3ilaSa28L3ADM0w0vPl0UHUzrozAIiEwOaRI3rZgt3d%2BWgHzyPgKMMaQAznEZMU%2FA0wvgZkpRgbAAC%2B2YWP32wgc3lgJf%2BZl%2BV7Jid2VEzBDvK4iMLp%2FvNSYX4ymKUmuC2r1XAVR8bMnQdkuLi8sA68myQ%2BOzec5WZ2dreOwcrBGNHc41ewPQBOQ4hzYtlGBwY9RwGHG6uDRGRwBjTxgi7S%2BoXbywmOFa8DLfddy8RefRuiie0uuO9zrIZJIjD9BFtv6KMHfDHqfgNJJwlgpwjMK9mNn7xAxLlxNXsKiEfnLCtuXkghopcClrfMdC%2Bf%2FjWjWECYoNKglGz99p0%2F0bTEZgD4e1vy04cwzXPxVBZcUKWPKshP0%2FN8wo86OzQY6pgF2agXFjBVuG85kY7Zc%2Bqedqykrety033T0%2Fjvd9eAqijIT7BRj6nGnyRBD%2Fubs5QqwyZ2wjIpW66qgflD7KC4OOGhCNndp0ciVgiBLF9%2FE0sQgcummvxtWdtNFIhIJOTo0xppAjpqnd4GLe5TCrs42kyW4kYPDcCxcO8bZ6clkWBTQMoHNjUdwEpEkZWOhbKK6LoVu7%2FqNgHzOn7k74dxQ4ZVCdmy1&X-Amz-Signature=d393e3a56e9b3b94f5f903e423a6015fd0415fa03c8d0e0bd88611c8ab5cbddc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



