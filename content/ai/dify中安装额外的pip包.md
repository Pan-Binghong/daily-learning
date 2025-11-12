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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CTBXUL7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQDQucSHtRsdcrgsLCfmDQLISwp3zMKCuTm%2Bgd98dynrOwIgDpqsRKiusg%2FqcCIEHqDkFdZy8pa%2F8rsrjkkFDdkqs2gq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDBVRh6W%2BajRtbhkRTCrcA1hEBsWupihOWMRydhtks61x7NTtF4LnhyDT0NKnZFsZiEr8eEJDoA5vBTYo44tIIRhHLcEVTyQ9JnLfnSPUrzETqvYCiUGABik1%2BATk%2F6MFwQnlGD5UskQPAKbJSUp5eK8xMH8LSjt6hvAwORA6EGTUDiJ0X637kz4NP%2BliV%2BScMF4kEQr7GvdDEkBMas9A5ME0jEb9i2BVNoJPIbDlAZSVTmC4kA6mz0npMZ8x33ftB0Ymps%2BV8%2BwcBqKxlA2vcqn9VgIM3KspE9HigmU2ajHDyiDL7zPcG%2Fq1AC8I8IGkzXu9L9959oYbPYtEOq4VIRZVW1Jthhs%2B8hyZuxhX5cXXLQapwN7bC4Y0hNrG2hH5IPYAmwXPvtWIaQz930Vm9VvvuWy5WoHoNEsXyKXRsVd%2Bc6mkcwDQiDmkBZjKVWRob%2FkjGcRhbQCidNqA%2BoiVRcmCkxKH5qAjPwTUiZ%2BB7%2Bn%2Fs%2BvB%2BD9owI3ZkX5%2Fzmt0OYg%2FVM0MXwyzjSBgHBNcqLjMOD7EGJ179Efnw2DWvDFniDt2dA4wSq%2FRFm%2Fau%2BQEyvim7Flr4w62S904GZCogWKaBC6RuvDj%2Ftl6b6IZUB7Efm%2FqOioIqT2RYb98RA12WNlsPomvcvbZi0ZkMOjjz8gGOqUBRwRCSwGrVO5SffpvqRDLWXCZO5mKaVPXptCUlv380zW4JSFRU37wNAGmGanWeN5Goy80OTR1z4YRPTZsvjbtnrHLETkZu1DZ4ABLFqZ4el3mxtj8kUdP954vehA%2FiRFaS%2B0CwrTv7%2FpNRWzNZzHH5F0GiNBNZDkoFNrlyPqAju9EbDoRy7kDPWvrFV%2FzQNYwYYAsyj2kGmPHECtguRlxvcQ%2FdDA1&X-Amz-Signature=d900628098e2a6bf2aeeaae25e3880b6fcb1125596b87352fc8b4513fefe2bce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

