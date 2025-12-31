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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DGPLHFW%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBf8r%2FNv%2BhXWhiXI8H9SJcO3aX1lNG0sF2otxRaPgciHAiA0unCm1UtZVd02XDkMzi9T9YxeSRCGy4Ywvm4t98235yqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0THK9cppWja9axSdKtwDkDr0ktYPJSRiXBMTdxEV7JHlxKxpzMofH5hj2XyZrqgfTNEp0aGST%2FEtJOOrFtk0niyTuFooE9N7hbXXvFHFBRTABnYLnF8jTIA76wX23BDdvfHImuehSv4DjYHD6EZfwjp0Uvrimtpi1xKL8AQUFSl0ElDvBZ2iOwo2uB8LeP4vnayzxqfIVzp32%2BaJWOD67OB1eT5FSqfovFOex%2Bf0BjbW55XEhxxBDVoHlRXeLuqF16%2Fr0FAZVxH4IagR3O9GwJ14wyyGQjhbf9BDaoDNGUTEgQcsU9gr1dy3WJmreEgBEeyfTEuyHx0oVNPbmTkvOfAsOXQQaOI9aP%2FNFXpZTXMFWhznHj%2Be1w1Z0M%2FJzBkRlMIYK7rVdBHR7T7ZWEs%2FcOJiKFiXmT6RBi7zbWfpK531hpjfwyVpiTJCLPvIc7pRN%2BrnmkIS9xR%2BeeUsT2sVuB4iZERHADPMVdEvNYIir%2BWWYLHDDxRXXyaz2Lu4Je8zX3Sg67%2B4EsQ%2BhohKsSPz%2FhL7S2%2F8J4OI3CNbQelO4frOwXJyaLABb6o%2FqEDgfupppLhPKGxbvrOk%2F4w2QsV%2Bn3XlBilooEFR7G6WAyqx2fb7tBdPsyGv3L9NL8iYzPKhxqUdKGZln%2FJS4x0w2%2FvRygY6pgFnhogE759MzErzJEnDAWLl3euiHTsLXjWe5fkT9d%2BjIGau8c78NN0rEW8gVQJytnQ5N4OZo7%2Bq%2BuRKXSEniPZL0jPkn6ZFTlfbyjyM6CW4wIo4hj671Z4Rq%2FP%2F6RgkQ3jOzM%2B499BUIglSJN4wk5T24cdCmxQbR%2F7Y%2B2Hq4xkGXTA1KAbIzRCXjaaw5i19y8BkIIWHyMn%2BHvZfRJaVA4TKl%2B0qf1iO&X-Amz-Signature=b7d3b3f50a30440ed57133d9262129ba7b995e2c94f6904d4df24587b3c97749&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

