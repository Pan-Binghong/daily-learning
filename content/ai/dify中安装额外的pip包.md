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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2USCXSD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDM4wj3IwheDpjvFGOkFTf1Wl8LxE82xLUF2RccFHbxtgIgGmZhBX%2F61ZWKo0EHdMwtlwP6Zvrb3W%2Fo9mI6orgH5tIq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGZmDaTD3fir%2FEw4eyrcA0%2BRT9JWQZQSdG4w0B9J8%2B5UArqgJedPVtT73T1QznjlynjinxvP2FQBqoUcyG7cz%2Fv1UrHTJhAmLzlDZmpVUwc0Fk4xGyMuVGevRwMe%2BZrcS%2FcRLMCpZekQT4uZclaaKauxEo8uPqvE%2FlEEAQq9TyO3MFB3rc%2BvYACpizCbQYywi6K%2B7M1%2BrFQw0X9mwV%2BbgzRLjmXqNln61R76VaH53rioA44ClA4pOR8mpsAF3rBckVdtiSV66ftfTHPhJG%2Byq1tbStwu57XnTKI8KTv02sH%2F5MUawjdeylHojqKZO7Lh576VAY2nnJHzNRB7o28%2FY%2FzcqCOa1PUW1BlUbDElo2DRq13dhv6M28In47FCN5hyqIGL1t0cwkX4Ke89kJYj92EJpGASCa9N%2Fso4l1skCtp4lrQ3P3wUvc%2FMoAtxWUhKlJAzHcLx1lLbTq4xKnjvjCa9tqbniFCwjoPL%2BL%2FDewH2fDlWG7I3nNhPgGXZaidQS5CDCOfmec6nBx5hEPOFWat1pQC49Cc6UsjQu8hkzgyMH7pGU7NNr1HBNg4F2gHXMkNMePPsRtSE5NQvMHUF7Phu4OGxbGW5QSGOmQz%2B6mNVVzJnSuhngfSi2cxgwRHOc5ysEpxiFjm5tsnrMJry2cwGOqUBUdtG4mB6GvW%2FHo35egkVdVSmAcUWOJjox8Q2%2Bfb%2FMSLjBUFlEJO8k1mL%2FyHZMtZBClJXx%2Bihuz2lDJf5Vm%2BKp73z9J8qX7orEXr%2FL%2FRfBhegf5hc6OpSrbGoiNoQ4Efa1XnetnTJa1IDlcUleoUgiAJeBEu1fPrx7ZN7PRinVWs72dyWyUZaJwLFRuMdOPKkGAU7RuOvlYu4VGYqKm5ItIG9Fe2k&X-Amz-Signature=df8770efe283065c9550957423044c570155cc829981ff895101fc27ce7f77c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

