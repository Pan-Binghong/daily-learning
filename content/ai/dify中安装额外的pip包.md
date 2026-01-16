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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2XMJLDH%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDzVrFK00EObkFylXdn5vC0QLVpXIeBL2ZHszyck2Ij8AIhAImBgU1eb8ASWSXkV7wcDTuUyN1n%2Br9lXHUiiMrVRWQBKv8DCEMQABoMNjM3NDIzMTgzODA1IgzhrGh6Gu1xO8bq6koq3ANxdI1ALzKo5F9Xm6uQ63g4QvewY5z%2BpkKGxXKyB58UUMUb3rHRy5iwJj3pJ69g15VxOov1M%2BxMoXI5xwXc%2FnTtX4yA1jGHb1VCurua63WsyU%2FtW3aKHUFsjceqaTT5YShfHXz5OPKW9jx1mbpmbIxS4xGUr8Y6v6jY4qw7wCLK3ay1b565LqY2YpBDS%2BXwenRWmXms0H7yslOYC1VFEMbmsHRfhh0brN771DUw9dbArr7q0fj6m8Zbd%2BLyVdJVJVgDwBajBN3VJismSvPAxYalvHapaGKRAvBz8x1OvGCrN32wyE7ueFfUSUVBx8KuJlsHYnJmeJpLRI4xq3IZJuMUu6GSsGnAlN%2FIgtgVzIGtmH%2FmbwkjD1spu6j0igwDTfk2OfDS8FTa92ngZo1Ovvhf7DNLwM11WfKod52cSl5XSFkkvPmALybOADvP%2B%2FfHCGeFUTgByrVpqBNvvX4aU3gAXtPan3pl2BkshGjm%2Ba9PkkLiOtgZsfmkSeEQcwt%2BEVZGkXMN0TkCRF4pQzRwEOhJOCrfUGYnDMTIVGnLm%2FPvIkzwEN9ugB%2FID0w5OBD2XEYyGf%2ByfBFcJjWRXDuskTecu3Iugd7N6SRKCzZFWIEBuQ8JqrJH%2FW%2FRG9HScTCdv6bLBjqkAQkmpAHDcBmqT%2BJ6bmXaN9sQMtjhHO6sZ2o6FYlUC0PNfM9jInCmMUwlie39vQMCL0FmMRm2ZxwNe6dYUIo3f%2B1pigbY4rSLVk5EC2VJX%2Bv6xqx%2BN3p%2BCQXU2ErN5lRnY%2F%2Bae2N61qtwf%2FiybLN9G3kghRk4mHlj6iEATg4gQiPNPp5FQ%2B6sWoI5vYWdzOQMs1SdpR8Myic8t89N68RGyEdvrCuj&X-Amz-Signature=2af483ccdc23a976ddbdde7ffb777da3283d383d6c9007645624f2c80c28ec4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

