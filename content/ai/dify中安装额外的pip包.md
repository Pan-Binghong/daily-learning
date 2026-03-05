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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBLBYK7L%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICXRgqhRPSM5UfVpqd9aphxHSkig6O9jR%2FKy8yPkTntdAiEA5WBUq0IYHjROxnLDlBe2t10z9YgyIVg081Pq3lWHbGkqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIGrB38tfCL5IBC0vCrcA2riof8xCEb08yV5pNlKEiBH7mRzSezxXYS1ZX7hkau0uKNeWvK2Ijfuu4iUVwhARuX4cVOzmXS0zZpO2O%2FpKz6rvieDgEAljbVWsiqn%2Fv23KmOdzRVov2sMXWhoO%2B7TGqzSGNPn4r7GOuMAMhQAB0oJ%2FJPzCdIyBSrAC6FVOUjTIO94ygIlaobUGia2wsg5n0pacu%2BqqiDNbQT1DhEkvF5HBKxHC4PLR5ujKTKmy69khK69FCRJbITBGJI5OQrAHNGM7U3Cz7L%2B96fhPKgUjQNnHYaeUCTvxQFFFrm8oxRsiNnCzSCmL0rcL44N31lzBM2SgrW7qsyeS9PMMt8DhbtZYFxazG7SwI1Yf3Tw1JqOW92PTpDq7DWH01e7dXT2fHieFvdeX3Xv8YLWtncbVOc3yCLJm4FkchTCSLsz2Q2aBNEPnQ1qW8x4fbDblLKQFBw%2FzhcelC3JOcrmV9YJyJcsTcaD362i7cp2jLhsedRfWfXEy%2F%2FoULSAh2MohwzGSkkYMjzWjPmQk0ojzMiy7%2F%2B9cqK6B86BKQJeSgoeWcNQOsGCn76DMnp%2FKu8Vk6FALt3hiJNrHfCz52C86ylX%2F0BQb3ImeJt50y%2BfTTWOHK1fgz%2Fxn3p5yNK3zrgJMITgo80GOqUBijYPmRnd6FrlEgQv8EcnZSyXaDpsrXVo0wlH7gQ%2F9Y2xgaFK621cxsDs0IzcqgVJ5yUGaFcXSIwq88Ei7%2FbuAWm5GpBzlDIZKyg62NDhur3x1lfdq1YbT%2B5haF16Tg2zFRGdtHoEILDygJWrnMnIcFbTjK3VXb5w8u%2FGw0DtsohGgYHwae4vmICdOliJtwFa9f4Zrn2ZxQesZRwT%2B922O6WFC%2B%2F6&X-Amz-Signature=827465875b6a79191a39d34f2477f30ed2da22e6653e216a454b421e38726d4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

