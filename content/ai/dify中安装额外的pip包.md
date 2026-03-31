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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RR6SSJRM%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGfmOVBd0oiCbX5NhpIaANcSRZzFUaCk8okgsedWODxEAiAouYytA6Ecy9RJXQoMG79PkqGvYHxJz8y1KWOx0g1v2yr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMqysgYlWOBZvFOSF%2FKtwDxbaIBUdfSOofIESXgvrFMvUkf9vTFj8BSOrmyX6UsRWDoWiendP3QgrlIKTQXHMfqh%2Fg1bSi0zoHBqej3V09Isl7QBfva2km9ZRD63b%2BXXVc%2BfyaonShM1w8Rw%2BAx9MsT1gSXgiH0rNCJAvBZeObqj3tMS8AvN6JRrON2pjVq%2Bhsh0Ka86bkwXzX%2BUpQ%2BvGzzFZ5IEOKrAtuBr3kOv%2FLgJ43jf%2BLlAzbmpJmkhhye0ozCbRq7OQXBKtspP5JPLOOjNpyGrzCYCPJrJxCMoaaT9JyedqSPgHKpJ7vQuoCtmiUbrKAB8QGG%2FBm5rSRSDGJegBqy2i8d%2Fc2j12IM9RQnHLO4wBdH5engaUVhd4OoQ33DBKaKjXR8w9dceIREV2Fad6Z8RzLkml43K3xL14tLZ09rzWO1w97UCebl87T3keY%2Fm9suFlgCyf4tg5WOzCrvurJ2QJzwoToH0ujKGQUg6TsQSs6CZBUu5QCh28fqxyQMrRJkJcOKLCFJP4Jf68C2agunxOx1vE%2BUS2X2Xc9dH8fyDHsuhWMmd8HvnTdAhbYYwg%2FjybYmploUtM8lRDOJ5YR%2FVCocJSWnoDXKU9lGWjr%2FWB8VaYTghcwIXJ3ei6BcAqezKGUyim1o70wwPGszgY6pgE2TuRG85pR0y%2Be5ZuaibSnnTi43iedMrfUgDYsvZwVTcRM5%2FTPrM7yvnI%2FL%2Bj8rnyZOmtuMSH4qWt41bTBG2wRepeTYDN%2FkW8IhfDZrdGs7sqqlbXZOViee18yYQzL3ZF0PkafmrR8p%2BHZ3y8r%2BXyaTzgNSx3t23y%2BV74ycJOiMzYEbAnmHiA1rrLjzz2OsxrStC3NdZcNp9BkdYSHOXvdvTF56vq3&X-Amz-Signature=bfa431e20a229839c6910d0d847db83ef8abbad612021b959f1d3d9f030f28b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

