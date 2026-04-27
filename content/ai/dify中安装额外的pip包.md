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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTNCUGLX%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmeOS2y0Vw47rTFA12JlzvKiYGkmsWGHGo69%2FfYC4JugIgWso88IOO57geDvjiGfjGn9dl7Oj5ovum09450qBA8XQqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFPsSFP2bPFblI8rbircAyJDBB6plCu4JRVtCrbYabh9Dbolxmjabnu8VwxHTvxNd07SsNG%2FWBqjP44eqbwaGcptqrky5Wbq%2BOuATu0nDK3Xsru1t%2Bhm5OR0KkIs81uin%2FMjn7mfyezvd3nTdgjkPsubCgmpB3P3vLRrwT2hPIX%2Bvbp93tFh9lRGqlSeNYcNDOu4kr9MFZpULduurvN2rDPdwY7wAKCgYN%2BQWW9j%2FKrKq7peze5hU81CIUVIOL5k6SWmvdVoJGuITWFqsWI9Ht3NCPDT3K%2F4iDcWSuzSYvI7YHBFh8%2FnRi5lTNtekvLFFYwCaGrkKzCq8VjxIpfVCS0Mlr6kv7SwaGgWUFe6t%2BHsifbpBJs%2FUeAj%2FewpGFI57N2B1q7S3ui03LB3Ru76QjDrirUYpHIIxMusG6uaVw3EDIindZCEF4jKZ%2B6L209ywR6w01v5KyfaFk%2FHWN2DRxDObqHYJwpOlCUgK5bbFhSmzlGDirp5J1KFpwOdM%2FQQZzrfJXaupbeiEjBPcKu2OSvA8o8QR518hUuHi91cqg04C5%2FfH8jvjboZ6k16SfoQ0%2Fi3L1P%2B4PYj6p8gXaNYT3y1aime2uhzVurAfcbPPKbHxOgZKV%2B9c53tzJsuvxLohx8dYLSe4eGxYXnWMIG1u88GOqUB2ZyaaLPkZKc1C6PDQ%2FW9OWS6I3wOyqOOFCLExiDeeSvPcJhuMYzJYEOVePWvcXHp4JHy9uCsA7X2xYloA5oowD8s6dtz%2B2eFdUi9jYksxSnrUcx2lRgYHIJ%2BnWLvEYXE7lvM77nDAJddHElY4v%2Be7NnPG3I8UP52apXjMQs1%2BI8tZvWAxWJQUHkSv9uq4Y7YBUC51zxsrwt590%2BS%2BBlu9lG%2B2z9x&X-Amz-Signature=8b3e7bb6b68268d0a3a40f84de9bc5c9a4c64423da6a7ae6cce95a738b9f7249&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

