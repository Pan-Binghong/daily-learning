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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE5I7GY5%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEbx76wIYBcCnNP%2Ff4hPS0HaDmJBanKukp96KwLDw4p6AiEAh1LCAWSkkbGAeqoj4MCxDr1tv8eci9mkkSyr9acdPFwq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDKriY6mrN43%2FWL9i9SrcA2I0keP5JEb3DNdA3FGDpoawMQ4E7N4ATqS0vnNCuDSdDgZzNxt%2BGDngQd7SzYHNMj37vdfDRrDZOhBv9tQpQfWgVzN2T0BQM8EsqJr5WNGcK%2BDJnDTCIe9P8nomF6y3kLpfC9GqgKy46gz%2FJ%2BCsFg4y07m5osOZvdBONQSVJHRWMsQ2FO3YDUGufQVjmgbgpPvd9%2BGl4%2Fhu%2BpmRTrdNh0763Og8IomXxuNagos7AO4elRn10t0TbSpQDbG1%2BUE6QN8bogXoEnqOCbtjiHuv4LH%2FwrUlxqsMSkGiPN7lzbsD33R0WL5dHE%2FzGgfSBZddxNr%2FyjIrunoHbIr%2BpJb8r2M5G%2BjZDH9Gm8P6OnNO6kxXPA8BFttIxND0HeWZiQdn1tH%2BP%2FM28qXDnnNKQkhOiEwHzUK%2BFzUK%2F1vIq2Nwfy6OgeXNcsOXcg8MCV6ZPkFUsJgneuXTB%2BWZ5cYkJZ6hJB0dfXH185IqMQ%2BgtTxl92YYAAATVTTQOCDXeCRlK6RY1WKIWQQeIVnlonJ2LflweqWs1Ip2WexVn6XLyK7DIggGwHLDqryXmSKqRBxuufeDzptOSe2EdS3vdfwzABFtyhTc%2FNetwy5J0zIWwfCOmxDwq714aGArZOsKTsvuMOKs%2Fc0GOqUBtqLBJZUJW9%2BUEI0Vg%2FOBN6PNKBGFzVw0VmaReX1j%2Bal%2B47kKfuw6JAXWzFiuRJ21hyvJksY60cyoh9FWPYGGIpr18EgrCKb9%2F%2FqR6sW68UrQBQiKnLowZK9z1kfYOoInqrK%2FFhDDTj6x2TBRaYk8Q%2Frf8Ikco0S1XxGzCRD07uFRKTP8z96JRsc87kgxVdYrK1fmLDcK75xoJaMPdg5ikrYmsHxw&X-Amz-Signature=5e69ca1ea51da1c289029bd0b78db64e71ca116e994c39cc927d8b7f4f4c1afb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

