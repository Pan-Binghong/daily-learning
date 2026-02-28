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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5XRL32G%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID6pNbOkRvfAyoh6nXkdfxtf9u8cvzA1uW4BNhs0Q2mmAiBJ1%2BzRD22vfT84imm%2BNpCx0a182h03GjQB9sZAewak5Cr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMQJE4fQbfp3MU2OYaKtwDg8XvKskF1b1QOVi%2Fb2tIu1hTrHxP2uMqQQtBPO5REZjZhmZnQyMrAUETlJ2M6Z6mNgU4BonRGbUUNnVX9X23tQKhMu%2F9sOrn9XaomcQ5HMsSSTnXYNd5Nvy3QFEMiozvGAgYVM843bsAH5JyOgEZ00RL67Ku0gjsynjELkTz%2FtjbrjNvWObeFBMLUYH3Z0FWRcaybx4fNPJ9kAKCjQk0eTxNEE%2BWV0yWlp7HBAwq5HayFNYXsgOuE27eMIbvjRPVAUYA%2FP%2FTCZqZiq8YZmQi4wlrdSA3ZgusSkoV7%2BLWg3m%2F5GZAGBuqU5gOw64bxpi7clnXGJw9ygr7lqacdQu5wuTRMgzp5cG5vYhkohy5qcOkvauibKqPfoXjahDXxylLnPxA8rXmep3sdLVAHgXIsU%2BuY6h0ak0VfEnlYVUOG98%2FsGjVmILTprlHknkQHT%2FCMKt60sgPzR2Xez868JzPJvnN0lSz9b5VnIjKmqpdZUwOSMdbeYEudeW4UBKC6UPkfjv3z685eM1rK8xmfLaTsqQw35zzge1D8D1aYuMF4Z2Lo%2BlquBz3KD9CNshwC8PPu19KgWNmTolyyO8Kh%2FNy%2FLPyeQivmpBAXP20hYwWpidvCnUXPzQ7W37goJEwgpaJzQY6pgGUluFREmlyaRinm8uvKj0EDelmaRQSjkxf8Hd6sdry10dHBlQa1rrDbS7JQgwYL2CjOoLQc14t4zUbNt7hndCNzR4WKWArhE22%2FAYQaJhg0dcDUA%2BOP10YM8owxu7QB3EN3sQQ5SF9HTjAPLjJ5Y6kbEmgHfNZhhNKPKPNdhtooGFYOm1OHAw5iYTp328tuOyIeMPpfaKTEzTqWKYGhriT94Utj6IA&X-Amz-Signature=30b20d3c5ab4283c201456eee1e957da5a635adf2ed3b30dfc7578c923f9d1d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

