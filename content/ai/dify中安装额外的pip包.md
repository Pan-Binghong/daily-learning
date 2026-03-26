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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I3GKX5P%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQReVD%2BjPubzPDaR1CVzMGK53da7wkhq8HneLVEGr4pQIgWNeJ9dK%2BiVFmI7z3GvUUBegFuEdEs9tAGVJ0ErWOlq0qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIPUQuCz5VDLHn%2F87ircA0xgKcdlOeHeNMiOgSRN2W1U2OKp3%2FQsWYo1uEMTWF2KZwolgCwgWYdaarguz9u8ps%2Fb5a9NZWlcazeEAfXVZbgscogoSEnE32NUFLWrPlUo9qOQBGtJDZ58hV9SczIOqyskj3fBwYXuTuLxdt%2BLN9w93eKpyJEPT6dbfIu1lGN9eTsbDiuFMGj7IlW9q1XVuHI%2FajYNgOoI9ZquEaP5kRiCHW%2BaIZWfheZsOHLVZYd2mi4gbgz0tSUcjICH94rFyubUsnxgQXzCDB3wO%2B1lFBE7VmR4IlHr2ikRzvj1CUpvKMv31tOhOBjNQ43gPLrQEHVezT9xLwMWFenVXOHzkLcXSyeiJ1GzYbzYFzDUynBHE4d65U7KCowPCg8iCgqp9U86D95v1B4RiiFbqjTetQ5LU5ZYt%2BvspVAxfq9fbVfJ%2FuUOdntl90aUWGtuN%2BjaYGDl0QSspb6vMhJSVUVAGFMiL9vv94lYyLRnW0P%2BXI55imFCdtIvlTIrbzkwFS6G5bRaEglazHMXsrWSKnNfVW6Ksr9EZXVWFf2ehUynpG3SnYfTW4VmL6ju%2FUjdBVMwdlUg%2FU%2FLJIwNyNpydGf9rOysxupBM4XQuP%2FpveuP4Vy1zowDMt37mmI%2F53uWMKzJks4GOqUBkxhfLeYrXKR%2FBH5ErLhtYgyZc72up6NNA6rwgq3V85whqR%2BvzHBTK7DsoEp6%2BJgZ7PtxNlmxNnYgVF4e2qZsClKHh9meRcv5k1L%2BQnnymYWyYNPPv2os3wSulyniax9eBN9MJrlZdZZN6x6Hlm6KL4mLcdNCXMQe5F%2FnPTKifwJ5I4pwy8HqemEaEZqv7AUZU%2F9H%2BY2Z81huq466sRBvbVPZNdid&X-Amz-Signature=882792a17f30a9ccc69eb60b5785d67874cea96f419e75ef74df9762dee087fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

