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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJ7LP72M%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDa2ifzxPkqQ67EA6bZyxqeTK3rqzrabvQ88oAA%2FxLcAwIhAOWbQdG9E%2BIifvd%2BqFBlwBD8YiSh3BbsErbf6bl9B%2BDIKv8DCHwQABoMNjM3NDIzMTgzODA1Igygh7HB0n5MZt%2BIQiQq3AOU%2F2YMxIGRkJSL5nWbHDxInkTY9fF4vIC2304mBvGvX7IVbtaSVqzS3F6E14fDopaVxeBv3J%2BbK%2BQXQQMPdsLrgqd8Lk1KYb75PTFcXjNPhSvBb34IaRn7bbWyRC2BSqrjJcAXTbaUK7Qm8kHZMVubufJ6lX2DzKdZ0ajMVkL5Wka14VIQcPjqyahi5XOViOQwabXFyTBB05daRZcgi6wJSKvMFvM%2F5fPUrIylgD1k7e7opk0ecv5buiVvjaybyx3kWhd11j5bMkJxGPeso5jiDyv7I5pOfwerfoj%2BjwlzsHIWAyF6CPXsSnFewumtXEAnFizm%2FgjbbqAfRoZJEjdO%2F7tZVSXvpIq0ldUUtETdn0TesVBklSSDH6eCLE%2FoFWhq01ygx1eabnmYDSqoQCgO2LURMLB4%2B0L3qbGAEMJcRUJLEbNUIns%2Bm9vRDtojlg1wvMw3DaDYEupiEOetsfFDjp%2B8xcBliHruVc9fRiR%2BkHPi1HwDs31CR5Eh3rsCipvF1ovvOThtcCgGWA7D3SLVDILN2v3WhpPyqn8%2FwPCoCp8A2v0lt97Wj1gBjPoNy8Qrp1EJpAFnrgvTNRpRHZ9LrEnZZ3ZX7k6Ykpym2fkD4GTqmjRIPLUuyHNn1jD2ouvLBjqkAaQGXRxIZn6nbI8m%2BmaBfu6%2F2qmsxAHHlllXFx0T%2B%2BOkRQfOQIIvJgIgvw3A3NI%2BqPcgP22d02geRFttZXy%2BEm4BFhaob8N%2BxNg2jxIaufVVQuLTzK3VKTkJbWFLEItIbpRRoZrUwCY3IM9krqoq5kKM2dcO0SckJFmXyyoqyJT%2FdE3XMjZ36lhMX4T50wxGvHYm4agCAtVTbq4LjIRCg76gRkte&X-Amz-Signature=c98d7b91337d965f7d5a862c182010d9cc7db204042007bdd43cf43e3b4d8ea8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

