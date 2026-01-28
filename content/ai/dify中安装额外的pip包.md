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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7XAZBMC%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHcjtB82hIdJTrj8%2B%2FDiewzlSxd1LKeF8Xp1C%2BHJLubWAiEAgY7hQZ9qT2xtjoVaVgpaq0ok43cwxzJ90OXDtTslOxUq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDAW4BJR1XizBVDt%2FJCrcA%2F3iLAXd7elgC7XOeygwgSnduVjIigBTGIXnw9xzCcaUrYStcX9hbm8bIPfOQ74zPjNwPQY8bpE%2B0SNiBMdK7aWVCLYggiqgKlN5wg6ONzBstttA%2BKCnmvhD6gXVpAxJntYi51ZzTPQsFORWTRbQxee2GRQt8l09dnJSgqGkyj6VkUKLvhfPEUGoxOD%2F6C4knAW1bj6Qrp0VqHESNjkTrtaajBwGISPthwTXXZ57iEFIlmuSwIzUnnDMA1J7GXQs2tt5xT1Hpn2OdYnhlkZUWR7y9yrKFeP0ZcyOvi5ZwHty7F%2FzFdtazj%2F86Zoq2jQF%2FAgxO%2BREzg5tH%2FGE%2BrhA4vJY%2Bh2HQOrKVNpBf5QAFRCjYyl8LbA%2FJ0PC0WnNkLivXDM%2B2PHTu5vXCz6ddgBv1XAAbVaGTpjzXHIkBaHDXhOP%2FNJDvPTpQrayqNPoTPy%2Fd%2FlRa66mnfOpqZD9rwUzMfOWZ3TuP5LbHWuwPALRcV0Ttw8D0rTm5BCjpTZZram%2B1%2BnTxlotFhJMplW2VhhtSJsNogqE7O8kRc1sKMfZ5VYt%2FofuLBWk1S%2B9pHFSY5Y6KhLnJd9086yA9lTs9BqUYXw0pCFmc5gIDvj%2B%2B%2BfKz0UTh%2Fldmz2mZoQhm%2BwWMJuW5csGOqUB%2Fo0Re6x3SNaZYaXIIgvO1RcQ%2Fx0PO3jEFkfzHTTz5wLgRGaO8aMp%2FagCnko6uLDwPLXa9V7xO6zNcCmLCJVJxh7ec6Wlqf4PvStSVx5AU9xJTz41geqUHLca%2Bd2H4J0WCidHaZO%2BAbqx5vlTx3x19q3IqG2hHlbYczRDyJjbsSBjlhBBkbf5HRLoW4%2Bh13ff7L3Btx%2FYo2BhxMpDIhAnxeibld4T&X-Amz-Signature=f707c06ee1610048fdd67bebd2e0d6b2ffb629b520be2936903e2d5c946322c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

