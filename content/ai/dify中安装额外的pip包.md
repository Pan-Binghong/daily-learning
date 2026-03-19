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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T65ZJSK7%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCICNVIHW4XRtFpQ1EwtJUeCxP4qnxddVtYvuoRRJnnYdWAiEAwj%2BCK38P7j2ePtLKx%2FKzfUwfrdZnBQFm3jl8RCGsCwQq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDHanvZKXv1jgO4pezSrcAwh9vIB5uj17AwHNUso73Yx4lejXzyhpWDaY%2B6YtnEzE003MNrLNbKQZ7MtGzgu4pf9%2B9D6awRwYdWCNoW6G3In41%2BByq3AOSeniZAINf1FeCwHZHe1CzJz7itZK1LhJwd%2FhhnxFjFeAsxtBIS0qK6PfchiF1Ak2H2mfVQ%2Fu3lxFK1%2BkfLo5Ns91H3n5sI5HGollrlhbXaFRzZOJq6XQPT3zJlu1mXDWc4MJPMWvOIoAx%2BolUciOWoPhSFp1%2FfHfNJwKvxLKwBEc1fsUTNYfhRXMEy2sMvVF6nhOjbk17WOV2rXjB0ePkYCjQ92t8ibAn33iw6W%2F1AVEqCyMaosxhXMm%2F4flTtYKRMtFkxtX%2FOdP4fvQ94m4EmgbfRIwW9XVpnmSktEGmKqP9%2FtdKYWwqk%2BTKgFkhcRXrgTkp%2FI3Q9KQRoSKdx0cd6ieVUYJpEzfs6YPEdWKE%2BgP7TDYQ326X4ZCXHKLrUv8SWVtO7lNoxA0HIFqxuRpG%2BVDuf8OkWiqAOwo5R96rM3lNwdB%2FThBJw2gE4F88hJWhum0fUS7RfLwRXmk5g77Keo%2FqGAZWeCIRbl5fIYLLQJLja6EH6StQViDTGu3plNfCjLZGjNTDGeNEBHm%2Bx8PgcALvz%2FsMOLG7c0GOqUBaIGOQHuMF1f%2Fj0sywzUEP72nQoA%2F%2B9F1BXKxffVJhRDGsSt9Wp%2FS7ZhubVWE5hgtpyD2kCjkaHd7hzEQnZXVM5U5nS%2FMl2Q%2BbcO%2BPt3qzfDXMkZW3EUhBjXpsGcjWfAqEabxIvO9zYyqWLfZ37WuretCavmfCR5EGLRl9ddxE1atiLF9%2F8QY%2FmoTiYC6rG3QTQdvSfTJ6GGnmx4EtTmJYxn0OtCb&X-Amz-Signature=06e1c1dde1aea203f8b42b8143546bba5b3b8d637c1cc0aaf762957ab88fff01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

