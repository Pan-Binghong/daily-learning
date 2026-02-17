---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH6KZ4IR%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCIEnqXrbQzFZu5ImSC0Zia%2BmNpNtAOP3upu%2FzaRE4CE9cAiBxyUvmCGvMVAfXiP6TFhHvBl3XwmgrYf2KDqqojzmyrSr%2FAwhFEAAaDDYzNzQyMzE4MzgwNSIM%2FyjzbNpdTRvVf%2BLJKtwDPrWBasjHyTPPLpTkzI%2FX0eswc7uT0rmy5ezAK7cnQl2UaUnV21xvbhEFpZZr9Pj30BqeOZ9F5dgL7hd2%2B%2B67WOE8ijNW3q6%2FPUqnh5%2BA8Y1sbdGlHhMJkM%2Fsk%2BzhnauWAXgj5nFfrDO4n1S16IDRYvlWpKLKKxq22cUJLaegoorGJSR1y5C5KislMOcRwYFTaEKq2yiWilo96%2BOgN6CTBILc5YOCQ4l3QfpuJ2TRxBFEjWJ7SccUkeTr%2F%2F80pZAfFZNpSmqpMQcS1qXqmOoL6aVxl%2FUn3H0DO2mTN0%2FDCaVOFbsi8wL1AzImz5B2hvOlhkHakvCfi%2FImAg5HcRTCbu2KoS%2FHKD14cwfG42qh1yaVEg%2BOCePOncrOSjajulF0UkEmshsUFolZ2XyZgGd9SF4n2VW6tKgMHa75%2BHMiQMi3DovUaYrXb1UXhMXQur7Qts4%2FBHRMjbl1GRvL%2F3ZXi%2B%2B%2BX2ckIrbS9QQSUNQ4H1v0RQ5ONd72H9zVx4A%2Bfb7qgoDjeH9vubgNB8RMAqVQyWoZurqTTaldy8vWV3NIG8uFVzuxSq2xMSOXVAzuCMgZoJYmiA0TZvA9FU0%2B%2Bn1DeU63uwrVua8YouOX397GZMPHGEkHZWAfjTbMyxow37%2FPzAY6pgGLPhjP5FWuusBnnX6tiS73og7Z82KcmaG%2Fj6ey6WPJ6u2pacQyk4YXJ80SGXPdeESM8EIrFLPHgd5dl29o9oKYf5atatXyOj%2BkcgI7HxfAt5o7MARJs42H4E9dJqV0CEUuy8t0hNxSsE4UEz1gww62YzN%2BBNlntEkdwgT%2BhS5YFwYkcfzJt7IKJUxUV9oJaZEAiEXuc%2FdaKfTe6shS1RipwPM1SObC&X-Amz-Signature=962b993ad7ea2d2c96c2b1bde5940bd9d8804f7e6a58f9864a2bd3763b117fef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

