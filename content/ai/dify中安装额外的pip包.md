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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SCQHUZX%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIBU%2BxRjBoaLkamPde5RGdU%2B%2FcsaTJJk19Jz7uxdh7juqAiAIP4KJP%2B6f6QVhUzuAgVeUnf3WBneGvnGnMt%2FmYumEYiqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMILwdKAT18%2FKcLQFxKtwDArHuuzM3cj80Dry8I26sizeg1fKqRblX73BtVSMN3JTNUuax%2BhlSF2YY6%2FGDkQKBAyxnsl78SZrdcN1BTX%2FurSqDRuEMKni0oeLBYlqET6TN3f7KrZ8XF3hatNC5QqKKh3lOoPWmY4%2FiUvkI2erRR12wqY7L%2B%2FScc6taHhL8%2Fe1TSn61sDBZ32YruwLODK2RKeV%2FCbUmZDiKy%2FK0OXkzqGj8B390%2FGlUvMsQmPQiiEoZs9X%2FJmd%2FoowNE5dxf2Rddrb0wX2wU9BbL0WnjjyAjhLa8JED%2BaEecQMAsoKuxKakFS7nEPViZ%2B8C0YQmeB9Smxn2dCOgN9PbmGEeuqHRtgwRaaUO7MBXJO0iMKGCx%2Bcgt2YG%2BpOJlHAjuvtLHoLY%2BeatWOjXSeQct7HSNEarvlk%2FdzgE1Gc10D9Iaav%2FXNPDh40al5evPpg9CmkQw%2BTXOso3iOMB1ZigUuEzyKXJNFi%2FSuP2GxVpRnpIfnvNE0r4eSKaj84fPLToiDFhR7WD2s02AoRHy%2FzI8W9UrufHs6FPbK3F%2B323K5U%2F6ZzJH8HhlWzmOlAt2mlYwO5A8IKJl8P8GwEHzyU3xYyMlWRp9I5bv8fQuTcEjXgafxI3Gp5eqPK0WCkD%2B7jKtoYwitXtyQY6pgHVlIGhskBzHiopgEnnjHXzH%2BRlqFa80ctBy91vrXDKIjzS2Wx5G%2BdLCY2VzZC%2BxbL8jgYdVcZJ9T5jz8M81%2FgTZcUYypPxPToP7UqGfVBLw%2F4VztuRlKbwmKkKrqWIFECUmRQMDag%2FlvRPzGE5MPcXZu%2BiQfqjvJlOcMymdlQxy3V6ZTD6Dveu3Upr3zsnSNEO1uwQ0JNpKYeTkv0JgXpaIeTPmESi&X-Amz-Signature=9d3be35732d77f3f834650070a92422a9b3e8e2634a754ea6232eb85c93f2e03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

