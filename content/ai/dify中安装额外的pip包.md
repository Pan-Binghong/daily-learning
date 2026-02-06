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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UB2OSZP2%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIDqLUP%2FHCtsdXhiRunzTr3PyehHJOOx3Ut0Qi2VbQq06AiBeJ3f63uNvGNYhYPV7kdpMmmdQ2expoS%2FA7qVaX6%2BwmSr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMHBS8hq99M7OHgSinKtwDJM6DPZq7yzmGHjo2jTSppd0zHd8voX%2FxwrGkEU7yww3b9OuJ%2F4AGLmrh1h3R6a1Z3RpTEu8UiWaQF0LUxcAntsSu%2FSy91HzNW8JD%2BTqY5oJEnLdPPfRh2I3Oq1UHf0krNqjsUjl2S4h3jjt2GS9ByJUfU5HO7DwOpQoxdQWS%2BhByw3q2OnhjBhrnGeUIqjQefxwW83alk6hIQ3%2BAlzvXTCPjp9zrCG98dHyKJhthCTlPNCwSZkiOVvV65%2BtvyV39BklaTpOv5CpjKOzC2WBDzgtedaO9PLdBQQIblG8BKWFC4iV3KZ63GhyRqgZU96uj4oWwE2OMk%2FYyrBCGMra5X99xg%2F7CtMf6CWGjAPZERCPJPplE%2BYic2T2gulBz99jcOgNXGm%2BDoRDyvvbAQkq7OPdCZj4u0t9pbwR%2BLLc4EYbkwcdtfEBuZfPWp0X2mbE7YEyNhuVuvjdyFffshDiMdwOXozFWBnivYXFUZjkgg2Ki6TUhyQS9%2Bd0NQx%2BpaIYwPPv%2FVZdsadLLzsaIccFS%2BiRG93TQWUYxgSW%2BhLtRNxyfixDkMhaiEgG124NLrG0r2LE9YFF%2BUlMPpyd9E9rt9lL6ySpwHi6VomMdTlsXFI%2BVmH7pF3BqQ66SYIYwkLmVzAY6pgEX7eBjVAWHrM7iHypugr9h07b9buyH4846y%2BAkVF%2FmrwpbbwYQ9OGGJkjxvW%2BSkydddkcQz%2BPbL%2FwSZpjCTtPEPpPue52F2HMBkCwPSAf%2FtnQEMbbSa%2FrmjUdQr5pc%2BbbP8%2BNQ%2BklM7VatoFkczauVOopBzdh0uI7YHCdIILMZUund2CI4%2F5%2Bd8ut1Q2IKLwDhIojaqgT1QeqWNjX4dowKjyXQCSzt&X-Amz-Signature=183eeb46a8e517c3c7a38eaf0eca5265110b0c73529525c3ef989ba543d0f977&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

