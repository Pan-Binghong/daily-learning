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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGM6YAYM%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH3zpEnMmEF2LdGf4MIOClRPa4VtWNqRrI6DHIhshU0wAiEA1GBNfTT%2Bpz1%2BAsf%2F24OR6v%2FcSRwDzQrd9t9HX%2F7EiCAqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKsUHi2fziw540kJVircA007dqzt7Gs%2F71dDZbNfWiU9p2RPWLv8jkZCPuRcNja1Z9plLymRxiXTrRlS0EIqri48dzOilIsY4RSkVWDz1Ny3TUxUmoRgl%2FTg3CRvHezmnY9rhgmmPnpRTQ%2BNKruWTGQi%2BJ77mRXEIZNJ6SYG5XnpMJ1rRsQkx4Ni4nQrhKThoTQ%2FBKjFBz9%2BqnsH%2FSnc111D8OsTKlILebV3Kv5Vj4O18npzycRNBGSMarED%2BJlkJqAJcTnLx30Duv97CWtJT2YUuRakD%2BJuuYKfX7oE44Fw7d5CWJZD31hnNOw2QySNkXITHcfUtoqfPpo5hVfpfD6sC1WY2IFPbjMTPxoderHmW5%2BTeORPHEfq%2FxPTjnUh%2Fj6mc76jS3JODaaY%2FSk%2F%2FuBOwUrO8hBkoXZVhuB9x37Jx%2B%2BHqU6wBAbdkxXLTezZVNc4ta7%2Ftws9k1d3FaBDehmoVS7CULMJi%2F3ah6ZXARKZr36oq0DH4dE021Bu4RXCU9v1213N2IjpIDk%2B0KWKcIHH0lFquKnaHAbHkBij0zY%2BbPlPBWaTeosT7BsfbAo2MsRXtRHFdYdAQwWc6PQoFvge%2FSihO1XT%2FpWHMlCbXNEYyURR4WACUTkHzuj%2BPS%2BRY7Bp9%2FcCKHKWul%2BRMJiR2M0GOqUBUuPvz1IJC9%2BmiV99hztR%2BcyuhEDSQXS6%2By4pYVxAUoRzOQWgsZtoohug%2BjBLM9QBEyjKDq16DOgR%2BXBsPx7VW7iX7wgcouv7CKWPzW3fjUG%2BQK0SxMs1SWB8AexZ5HlUReFWVXDLcmXQX36jsJ9bM0jQw%2Bgph0MXvpeRrCpYd21pjQqTx%2F0kRM5xBmKaI0DFOsdL5Jez1zQYyZMFNLzXhQAyYdBq&X-Amz-Signature=bfaf6d3a52432102a1e7eadd89621f661ef222abee5f78db623ab42facad9750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

