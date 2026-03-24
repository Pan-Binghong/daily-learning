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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2CSKUSH%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCToopkQf7a55%2BQIifDN7tAS%2BSFyIpTxRdhfOakTBsCvgIgSBxHS%2BAJIZp%2F%2BH%2Bm2He7Rkr3fMG9MiUUoFYKuUWaPzsqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKJbGynmcx%2FVqCVhoSrcA6YPSrJEdqYUiBObsuyrNikwQnOUUwJrsdicWSSoaw2Z8PYEFUHnoN63g6h2idb9nFkfD2EzYXxfyvVfqg9oaupIblyrGe3nrGPFJ5%2BfxqzYaIp%2BiKVZiYbMPTiM%2FA7FosZFEZRDIZ0f3K%2FKAuUOQt5YCH0oSzsSR6gqkLnVWcp4bgJ%2BTBzAoto8wQAdSMgLGU83PeLe9y3hZygz3na%2FVt2bQwbNSykrOC23eTiH57KihkTcDVwNd8NxzRN1JbNNwuEgedG5K1PqarX1gbbjokbGsPtWD5i12r6mrXGlUsb8FtdzLjkcaqS%2FYDlydjDSszGhUH3ZjKu138JYSrcEsu6gu5tsCaQyEtva65joGZbM7LlEgjoZrtmPvZvcBFyLTOUrSRZ24v6K5kGWfezhkS%2BfxVUczQrLSOCdDvZzOkxjU%2FxVzb9AhT5lSPtoh8WhcMytZZ44U2ScUB8JL7FAMhzW7%2Beu1FILwOWpYP0oHwu8Xa6uGGMnm7Rxe6Jo5cD1Sl%2FnxnTTD9RlnQoHenoFyox1gUlkM7swt7lfKN8o2IxIsDHvIrYXMku%2FoyKwZPnkIV8cvSpV7sDNCNFAAoYVpM%2Fyoo%2FN62CSaVvxuIbRpF4equQj35kg2UvEsagFMI%2F0h84GOqUBWYjWtdOcd1mbyKVevk5MLXBGwdQvf9HvFP93K4mQAoQ6qR5hiC3ZcE7X%2BIBNKqcKaETvNwR3fj9PMI8thTCMOlNiHnS8Tq%2FDBA6zyvIuzK6Yd4rSZ1OJRb5QitoYJzzfFgxl4A7wuv8LbCYwlsoYnQA5D2Vwj0TzNOSnmRercshLJ6v7ytUbtluhCcNEnm3TUXksuNLawyIiPK7cHV50kvg98XAP&X-Amz-Signature=168527706588ceae03b0966b54212031181e14ca1bf61021085c6b0f4e621be1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

