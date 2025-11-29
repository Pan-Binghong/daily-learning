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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZQW2FT3%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAj3MLKfad7NHMyS9M%2F953RdIX1x%2FeQPOcFlzu5pKAthAiAHe5RX4oG8PJ%2BG6y05RYC3KSmkRytg%2FF4ZjvvhJ0vngyqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQI0kB5Q%2FVg4q7bQ0KtwDX8Xm7LOfCkV3H8N4nm783pLcZKPXdrO9neAy1pOIxr5MWxco65towb04%2FkJD1lHhujNZZnhwGAi7AtVteoBgOolSxvTPi%2FUXHmFmI9m4HGuRayym729kR65IbNaY0WulUiZTEdYIwSW%2B81m%2BM%2BKnoiakApMlT%2BcAYDAY8VkkSXt6GUyqyGU6y3v70AZIGOqn73siNlQsW63hNZK71FyZwrm6DmTT10oEIojLD%2BeTOeYzXzHTnkusV8JjokHzEbrhHEOOZMx4fVZptZC%2Bc3aj6oceUXwPuVJpXN9PTs95Xv%2FAIYL1jsf%2Bf0mUiN9L63%2BiQz7BqcEcdheeXPFGsojZHodSQRaYiKN5SYjmIVNfF3ZD4t6SXTW3rL7wCfkBuvDG0QVm%2B0PloPYILTvSUtcVFTsxTqoPo%2FHeVrZeZEi2MmfatLhw6sCkRhvxsRZ5NkKyPF36nNs71wE4BY9ONac3WCRXJLcjrXHNBcvI6SC%2BIxoa%2BjRliB3TOGVNPUDCI4pD2abaOHroqS0xY%2BVnGqbaygUHKtCMbBq%2F%2Fxbpr00lWr2JPThwE0TLxd1hP2Fc8EitaKxvuVLgTGANf2Zgh7xezt0jU1H%2BJzfPPjaesZqb3jSwiKAsKS0VsKZlB7AwqZWpyQY6pgH%2BHj06ciD6kiIMRehkY9H0BK5k7GJjh%2BVv%2FVP3XFyPwd9eHnUTRLED7nuYE%2FhDAbudo8dHRDYx1r9MVCn9KeaIVGZVWNp9U1yAwPMD2U%2BKWzIGpHy30dU%2FnGjauh3X4JbgLTpEm9qFRk%2Fog8va9tdwauMAbEtND4U8u2MY4XBgNRvOXOBd4GvQHosqpl7dEtjKFQ7yqvHjAMT20NqB6dRSG%2F%2FBEh1P&X-Amz-Signature=28dec6e911403de867b43e1e83a9ae7b3ea2166aa355747238c78195b02897b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

