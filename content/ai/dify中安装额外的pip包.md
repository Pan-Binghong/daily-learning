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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3S3UFZE%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH61sT%2FS%2BbBvOp8SX6V8m4SRb3Dm%2F1UdOCSG4XS6I9JmAiEAvUE5WFkTVAVcOCcKJqboamzC7LIUdonzrQGrKwpkJMQq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDGx4R5c%2B2VOJovCPpSrcAyCIMdw0whGLpXZnYZBlVb%2FyHCTKI4hwgoWB%2FX1CKJE3DfiILnzvf6LSOcgHHKJo%2BlEelpBsRNL9%2FsRLsoeU4nOZAaXwdJzw16cmtDvbTN9DBfdZE7XBkYwvXbj9jL%2Fuu8W%2FMmJkNi3GlyY8cCWfB6lNzMqBidMzeEWcwuvZ%2BzV27MlWTazTKBhXeoPTRqujhnED97TPtC1ncfohliVMTIET8c0TtFZg9GO8vE2cqGW429i5tbEK4A8gcjs3lufLkdpUNIadtT6F5ugqUuAqHDfsSaQMHmQ8%2BvkJhXYm%2BeDiRk74vlx%2BX%2FAIVgceNcqvfjXfJeOi3c3qfE%2BXILVSuJqnnZdV2w1OIwt2K7d9hypESXsU8b%2F%2FcqA85liqqaP0oKKD0lDzuBx3gJu3KYRoWvBHnu2yYlNx7xxBtQrtASETt%2FOzK06cUNOCP0KEg1Z3bl1EPAwzOZlsN9q1Gzl4uuSKrFcsF3T0RbchCX9KgGQQFj0t6EIqhE4Lgd1KORQg6K6rD1e8GLznYR8PQOavZyh6wVK6EMepI4wbmw4xNrDtse6XGKIR2LFir7ShTMGIay6HPCDRgYt7kROsh44Y%2B%2BTsSr%2B1bkD3THT8MSUEPg9IDrtK6q%2BUxirEwcoOMOThwcoGOqUB2a%2FKUJbWBN8OrSPoRFYsijOkzlXUtx44jWuU6EskP8v%2BRmhDHHg7%2FcmFtq10SWYF2ndBVIFkQnRgr7aw5ppyrYDpsoB9%2FQtpLBneFTOkiBMcmaCn2r2f1PpW5PtNpTdsQmPf%2FJ1mYYhNV3UydCzNtx3OwNoUw%2FQsfvaE2RWIQHzd07qjZkzSr1R0LLLeex8NVw%2B8ID16Y4U%2Bddlx0SaLyjHY9dMG&X-Amz-Signature=c8993cee4ae1dc3c78f6d6b6b3a62e36e4c36e52ad8f05b6acf4dc411bc46a16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

