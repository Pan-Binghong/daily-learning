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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPRYUHXX%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIE6ghyOekI3eE3hw%2BT5DGd9AYUysV8A2HfdP2jAIbCMdAiB4st1cGeaiC0%2Fs8dscEABNOCoOUdx5hkdrSq%2FA%2Baoxjyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMA832IzpwqPZDZjjDKtwDEubkNWvhUxMZyIbDGI7Rnyuw%2FkYC5inMSRB3fr5x7IX5aTzDixtVHLdR3R4b6bThTE9EEJboR4fpTSupT3zeBI32rk7ySEgsVIIv2ZxNwxih%2BdvzodiI9cIzwAtXdFe%2FBqh7PktL2miQYvE7S51HBa1xMh0pxIc8TieaMadsT%2Be2MsLwHCP94R%2BugI1IQZVKg3KF1plxkHQe9Q69siM9ZK559HGkyzsDCgKEOHpkSUeRCFmmALggVCwGTKJ9ygjfhYp78mN%2F90Qb8iH4xac8aSZZ2pTf4Z2TEIXZLWTnsJRD4XDuQPhYoENdoAbWVk0fDl1inQ32HarPBW82j4cFpgt8qd3loqEpffbbBqgdfBJ3dbYR2rCce%2F%2BkTiLj2zyFJAT2V9PLproD%2BH52H6wRx6rSiDb2sES7Cr8fNBxAeN83%2B7MT12lalDJbp3yhE%2FtZ%2BcAv4HbTESDA6Y0mZVLdrXlkwqC7nT49KGoXW7Qt9VCgdSAa2Wpvtu2KLMGOAsm0juog8T%2BHdyY7AxHiQIpG6VCHz7flYoKMkZoZOrZWV6X2ivCUDitgfEwi3PlzK488o4dPXF6Nap4p0rs6iBaiS6BQV1HpXr1me55PVx6YsYnun3rS5wYceaj8sDUwrI%2F4zQY6pgG%2Fkk2Eyn3wYwvQzlkMNJleVyXn1AWCoInY%2B3tQNR8GGpEzyaoyBY5pmmHpkVSx%2Fe1NuF7JlA0V8zC0hcLyvhiz5EsVRmyZ9oz3Lh0s3WvZmGtYZrjGQ2R4TYZcvBvtkxh6f94xf9u0KUkyGS3y8yRDpD4xRynqS3U7bKI%2FHjoBezVYb%2F9fUD39jQv2emAxLb2QXT4wdKdPS0Ffdeq%2FLwyuL0MHsoz4&X-Amz-Signature=9dfadbd238336c68078036472ecc22e401880e29130b297ac38c03e842df7253&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

