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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6LERCL3%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICUYdoq33%2F%2FJNJYByzAE83J9tNLlVaVrDq1y377ttJjbAiEAj1SVnSPAU43V9os4OUY5rkGR1Hr3ZTYUE6WAAK%2FDw4sqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN6cS4wOFQa84W6ZISrcA31sSoVy%2BObdx%2FbbbeSz98dohX%2BGD57ejyG%2BQME9UI%2F5qNsTkY1o8zQpu9g3p423%2F1ptL2jCXQK7CzMONcJEZ8H1hDKmumpRK3i9Z54mNuL74imUXzNKN282vVfzhgNuO0DfM6zweaaECgxit3Jd0rYhOBwy3FbphnRO3aeJFHMKsTRCyyJ0AGTIr16vb2eIPzBYCCL3cU8TlZh%2BRpjn%2FXhINGx5EDUh06Eoevx6jR9oXmxe1tQkZ2yRvNYwqIHeyN%2BpQL0w5sqwbsNWChCPN8EdYqN%2FvHAiQwRNjZ0DJlgmE7cVHF2znLm6Qez2mwq%2FyYHNlFrh22wOlS%2BXh8StDYhzD04dmRXKPVphG2vChO8WnaUzWfgX%2BdYcRafu37Ki2ikcZ2fwKV7o0gRzpjeaOK1IB%2B%2B0hyfrOM2jOFXkEW0qi4VgRFnkLQMATsECTdHDUTOLgeygQKa9FpkfJU6VGg67kKeYa0kXp1%2By2xtgtifnA9SGk8FvkXQl9udYE2EnHSay9x90qOCJA7UAbSKjHVXdFH4ugMPBOuQfRsA1%2BCZYAXMTF9h6J6LEbQ8nCamX4E7QgIkMpAK1Ac1ULM47Cl1vQKl7OzzviXKpdgqSTFKE1NJj8T6zvYCkc8IWMKXyr8gGOqUB%2BapmIh3REad8zTr006UirKiskGVmzbYRaXcF7FajySqXtODJMifEZKfYrmOoXsSeOZ2zi8r%2BRxbi%2FcPlQgU6%2BhK22XG8nb0jw1BzD48r21WaK2FvW7M7l%2BX4PCKM051D1LkYkZFLeGanHXP97CYTt90nCzaqgYy%2BBNR2cgpUQrQ6RyfUG8ezVjd1b8UV5N9YuoDxPyR%2FoScE7XHhGzxRZLoTFV0n&X-Amz-Signature=0a0e1e326f8e7d323f03ae56fe0ff8b42a7362623739c5e5b9ef71ff9831b85f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

