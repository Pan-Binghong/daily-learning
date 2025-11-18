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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z6JR7PLN%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFBQYLLR235ebYm50ge3jsEfUJgEENZgq%2B3VEE4LUOozAiEAuQQk7pNAUOBaON0ncieGRcstI8OEb86vQqrqojFWBWUqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHDksAC6ArPhZ30cACrcA2geOasEO9efl8ENzeFYvKB5dzV9rQh99w2ryxxbHWBzTU8ZhbszkRLjsASlVPGeLypsCqJKpOSO3LeFA9lBcEfa6eb%2BFzgiqINASLtqAO4FgDj3ZAfz0yTPyGLGzUtyPvWnSO1wuRC3antXNoMH0mpuDMozrdG9oQAjadxIzOSRJr67XEzd3LSlIqOi58YXdT9KqO%2FV9w4Sk5t6TIJRla368kjYjCOjuRm51ooAKbYQWG%2Fv%2FM7AxnjGS1bSJeTPDDUHGHfzL9wRokENO3BhDPiqj%2BKs6CK0U%2B0jAfRGhDetVMINrK3JTxLsmBBOSvblHZds7UvLxZIA2wn9I%2FNETi2RF5CcztiPsxOJN1VVsO2D%2Bb8zZrf1kqdagVW4OLtvin7yr6LPPTtdI29nfNyNyBeBQaznI7I7P%2Bb9msGxPmhR25Nv2CGbPyiBcurt%2FCh0zY8kmwaC6TP8OobFfV9Na3geXQJRh8waw3l60ACL%2B1dPFw81ZWt9YknZiljQjO5D8ZdEcjZjiq9vmYZeN6pHkjfe2TNFO59jaQYSsiEe39vBRymve1sRnEOn8enRn28jVMN2IaS5kUKH6sTaRrenMaZHMXq7ce%2F%2Fi%2Frc%2BY0sY%2Fk1jplqv2Ga5tp%2BvQ5RMPWX78gGOqUBoNBPr0Yl%2BwdYOoxczCbc%2Fl5rptIqEvshIrD4GGbal0Reb5w89jU81JdtyljQhw0jOf1XXVEj2IvkB3Q0qFW0Tz2sKkK1A3JE79NRAgKukTi5ks6IwVHyRawuoD6xWHSxhX0B6B0zFkYuxLMywl5SnZA43zAtdu8U97AhwWmacL85qaRbFSVS%2F1s2ib2loylM5cA5BStreZGSQOF5IiA8qZfPRO4t&X-Amz-Signature=8e12fe914a14dc80b3e5dcc51233170f50762731c067f0653df3999c30b07215&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

