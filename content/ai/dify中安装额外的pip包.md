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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR3FSMXZ%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDQE1tZAH6A%2BP0%2BTJNivUFpRnO%2B%2BKyQNN%2BqsvX3xZoQuAiEAlZdJ8DZXgJjQAnc9wQfFEruA3YDAZ%2BGrJTiGV7p%2FL2wqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERKQotEjzvMZnImeCrcA0jMHFdnWfHWYLklOqoIsNn1EQ7xG8pRhR61NRy%2F9aI5xQHjlbIw2xR%2Fqz6zc%2BzJS0YVbXUOup9dMpMTMfkExI4iUXvOCGuHDJIc9pKFMN7Z%2BHn6zp2uQCKM7AGWfvDWD1uYnDvQ7qC%2FTrNnKoa0szGitK0ikdJfZhriw%2Fucfd4O3gWyQQXXJ2Ck0H11uL2OhvokHt%2BiXe9%2FDEcv7Wx8oElKEYN1o7IAk%2BmkAPl07tLoJ6s64ZNtwcQWwkV%2BroHEhSaKWfPgU%2FShEA%2FJvHj67q%2FiCBZdJbJOpAnRIPGHunvwwtlByvBuFQ4ppqSW8Rl9C%2Bdhvqg6r%2BzlGHirZqWPVhy0u0mfaNB%2FsMyxUs78FPfsQ8tvoN7gRArHEtCFJRth8u%2BD8TO31aeoXWasNYow51hoF7OzPHz58l8uI1UrEY9RIDKI1bycZs%2FmYpdMt0j%2FalRSA0Jy22Lq10vOrTcxubjdB%2FJTMcCIeZY510rNYVio8xNjhi989eIYmk1astwEyqXIWJkwyPGnez7qb03JPgdg67DGsGnxDHlz9KMtEgy83G5RUwWq%2Bf0vZcAip4t2rdMgkvjv43yf5FRWmb3QTLRAPrt7XOwY3Wd7S0%2BoDJkZHj5IGBvUme4gsTtzMKHM9csGOqUBfmgRiYoDmTfkDpW0H6LBef3Cl6FuS%2FuB7g8NeaoIAP5qJlpDVR9V35pj1EO%2Bky3gvWqI0K2iOIyUvHItDYvsqKeyXBiuDYUDWlenZEALHPJufsb3JBa%2BQ1UcSlDhEcs3oUU6VeQzpNm6hEOEqn%2Fea%2FnR27W3ml9zRvLwjMpu7rIWaWNcHI1x8R8J9fNJSaOmX48TsXObC%2F68FBzsZLEkeHHJjMjM&X-Amz-Signature=f1721ff390e2c858cac3283ad57ebb5213b3a2d790e53c163e120b84a520c836&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

