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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQKCRYYU%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICa2%2FLGBsemo2i84MUYvm3ihWr8JJnsjixveVkUBzr0QAiEAjS7AfSTOjYFl0ja37EgE4JHmCm9ShMgFIIvaalLItaYqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCf4Rz836jhiGKzEEircA%2BwMI2wUUHOmFVp52jKp6qAihJM7HD%2BeQVd33PZI9gHQgwpL3Op4azLUD%2BD0SVl7rp24y6BWwAf85juha51zvHO%2FeMOWMy85DHs%2FpcWy4oioKFoOqbXeBrCqDjeJCZSOhJtG%2Beo%2B365FXXJvRBxxH%2FzUpWl%2Bmi0z%2FUpPU5UTniLntMcviQapX15eqoD%2BaiTOtTVWf%2FRYN3syWkW2wRzqtLEVgYoamh7F4ugFx8WO3kXyCuuJ%2FQKQvUJ9T7CZ41enKmOWqdCO4fuCpsVx3oJd5C7ot4b7Vzh2cE3mDoGNj8nYGFJqd5agMawP1Mcybwu7YObLwyd7SjrS73lc1RoxbUuA5GMxW9qoJPDGVQ%2BC2usDyUmPL%2BWe%2Bl5MtcAsc1Ef3KxeLBSjFA71DZc8JpJ13915VWG5Zw2TbdOHYujBdMhK%2BegMpsU4PWCVal2iG9z5NvDm5WqIZ9tEUAK4tMzEnB7N1s8DEmpIxnmkIjQZij5m%2Fb9QTLkg1ffFJ9mV%2FfBNBEuTtAuxQJGNFVSYa4yuu%2B%2B%2FyGbAMuBnJ4W1mQqXHb0L18QOIdTBkvlKKQ5gxhjCDzROfJv%2F5Uy0xhli627LLqRSVnBDvEUpbdbBCubxxM8ZHkRGQRRATMw8lMMDMPaV%2FM4GOqUBQNDFzuL7GXSGHwTYx8RfPShUoMlZczNSMVyCFwXV14CvjuvLuVTzvm3geqR03SzQM6c5snT5495op2ZGZbeUSJmcLh70o8qk1lH3yyzE4r%2BMR5VxicAofWoBdxExWq%2Fu6vWpf1F3OJQ%2BsPK2rKdVRsbyO6wgLfymnxJ3C87ktU8JArnzoj8rbbQ8bWZe1qKVq5OhHpJwvLKVxm%2FHhymZtuk8KCHJ&X-Amz-Signature=ba2eddc6374c2e6d9c3fe3ef16114e499a3b47f058054db17f9bb8a0fdb6ec6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

