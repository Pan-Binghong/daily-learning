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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QKZXYSS%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIAKsrTA8LqDkje0UauC%2BmbYTTioR2EucRL8cmg%2FbO1q0AiBjUjb%2B9IS%2BQdcjtPDibWYV0GaSRZ%2BxLBBGbuOrzcmtcSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8EYg8ouPCSKIVU%2F9KtwDJJJLKGmGsdcoGJ%2FVPGu%2BIkFymreHYnp%2Bottu%2B8GBJz0XFwDTeZLmTDBBH3%2FLbrtuSlvSpSNXLcmr%2F%2Bl5dG3mr8SL3yDswJzGQGrgdGwdtNrgW5dnpnO%2BZAjVx7ewg7xBtkPCCr1KXlMu3fc8Y5jeGgd3ifHg5%2FjnMjGMwkhcCCQjH3354xHQit7OIorqvHGjWm%2Ftz4bMQFzIJkMs08GMdLYE6WBVUHdz%2BXxBpiIVUktULgQ1JJAOgedJqG0K9DqdlssvFnLulX9tyG4IMDz9BNVOyiePB2Us5m8DRYUHOEz0RJDWkO4cpw4IzMaEIDhbX0Qevsa%2F3neNfyqheTlgjhZcGVxtwSh5%2B5odOWGHB2PIdFdHJJoWFJByFQc3PIBM7yNDt6VFe8E4Hn5NTgw4KVxr59T8FxRa75l3Z3j%2Fqn3dCBcdR%2BBZ3Qb3iS%2Fmc5ry5VbSI6WQwTsqA4hstNy4juggtHuZ%2FDbD59B5h1WJ4ka4F3yuT5s%2B%2BNgvjppqx2Cu7%2BVGC6paIUhOVoiiTJcAMmnWQiU8DjGcD%2FybMCd8G4y6F4tW1QUjUkY%2BfLDVOp2rAiSbOJtUMDMxWZe9dfvPqsb1zUETjIyMg1nFYdr%2FfX%2Boc3vyLOnaRdW2P8Mw%2Fbe%2FyAY6pgFekW6gW7%2BISgPenRUXcEDDAPVML%2FHx2NVtIjTLsy3g6b2a42Hy5LLGIUiJjUr7KNczOplF0pbctrmYhOxj%2FOeLjZpTZqrBS4feURaKpx0kA3l93MiObRnuYh%2FfdwtoCllwBr4J%2BLTM2WKmyapd0r4pBjjZfoNY%2BCYlPNptrkRONbZUhIpeP4zjv%2BwLevlv54AO7ZfgvXVbs6UD%2Bkd9COJpgTcCQ%2FdV&X-Amz-Signature=9db30a79ef5aa81627d86b1d0ca3b1a6219e695ac710fda0e54a67549f17decd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

