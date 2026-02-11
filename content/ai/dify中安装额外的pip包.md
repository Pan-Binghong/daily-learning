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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHSD32PC%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDn2s1c9pjpa34CEVdx7Jydpe83dfzy32wDKd2CJ2zT1gIgME%2FjNaTiH0DGf%2B22BeP5GYWhHRJIjIwn%2F%2FEoYUM%2BJb4qiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPJPpr6GzAOovEldfircA5yN7uNqqnCtZKy1W8Z5AccpDCiDwyJar5dbcTTFapoO2faoqKFvidpwHeiXY7sl%2FgB00FzzUmElK9j3Y8bVlOiASWxS1BWCoInsL9Nvk3Ov%2FQnJnGrLd%2BPM7I6zQ5EkyS43E0PRI70DhVrmlKl2t3JdIIZ5DwvyGw7VMsZJippBWIfDf%2F9phJ43rmGQ0Bdif8u95qJ%2FDoI2vaj%2BSJI5cFBsrYvIjIAYPsujtDDaJe11VvfGSzspwLFZOhMicvyrPCZDx1dndW9bQLK8rHcjDnx0CrzHI9U7Q%2F%2Fw1Pp9DeUrHnJjCnXOwt0WpkX33F6epS2aExLXWzvGnBaO0aJRVY2YZvjGK7GEY9UlE8FZQ5Lr8hAKT8HvKfV%2Fl20PpMgvqE9%2FZnmBwe%2F8G8XjLz6uzDHShWFZ37SVyzoSOpLXduIEaKKSfBjWt00kSxYWOYyzUqBzVEVGnlchD8izaOOGRGKhu%2BOvBwHsfcIgm1Fpnh59uwqMxV04XT%2B1OI6zPgsDri6btqLfiEqHT8wxwrJyV1YYYAiL9Y9R1pPelaNk7LRPy2AuFsSxlRIelhBsEjgvBhlNiZlpUyHwWEdzznfm6ZUbJbqSkKLRN0miN1ypWFyQsz23xvtkOWWbEqWNMM7Lr8wGOqUB9JLuJNjg3Y524He9xp%2BN9Y39VERltNhPPoLxG%2F2JPcmflWp%2B7B9%2BMBwxG2sya0FakhTEFf7ggULIzmEshDnsYQBBPaiYXnueMoKjgr%2FlwqzH7XKR5CuBnO1sS7Cc6tneN%2Fb2eqIE7iCC60FgaH2thxSqFE8JGKULFWox30p05tM54ACcigB12UPzxXm1dIbxv3FXszn7sZBKJvyDcIWPFy%2Fzk6Az&X-Amz-Signature=55866f780735b46eb3717630a11f72ba6bb9b2d8cebc6d7074271233e9a826b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

