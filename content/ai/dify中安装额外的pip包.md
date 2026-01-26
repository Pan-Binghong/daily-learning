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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E6IBLXP%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJIMEYCIQCxciTkOU6Fr6JZCDThiDKoVHNgIgviIiFsw9x%2BT7zJVAIhAN4PqTxLaHHUDQ0IFjHcZ4bjt5GRZm%2BbwJ7sWhrH0ehWKv8DCDEQABoMNjM3NDIzMTgzODA1Igxu5dVHG%2BbdhItXREAq3AOgk3XskT83C3AF%2Bsn2EM6BzDdNltN0GZyghj%2BIUmsFlHo9FiKzjKoU%2FLkJeIMh3IzDfWJJ4odVVKDNmMHIUv%2BKfLgAkloiahKz4zKlwXtFDusQP38JcEfKkCUrqdfq5fyYetcamFLnsiKWakkHVt1Li8PqTZmzTHqpSIrI1H0BkNsZ1k1nY%2BPyK9j0tE2FUZ3k%2BsWyKi1d5kB8rRmWLCUX7CsunB49%2FePrW%2F%2B8OxfSGSq8Agf%2BqdADVrVG%2F2WhmtWaZXjxsEuAS0b%2B7aS%2BFZP%2BZJyzat%2F%2BvPPMW1CaKA1%2BoxZDKCbkt6JS3G8dpFVhcTe%2BA%2BqjtVZZKUVInuli9v5ML%2BHkiIQDu6JLoAUYsb0uP8BB1ZkljLK5JT6kEh%2Bknto74L%2B4vJlhEszLNbctpagrfqbr1zA%2B7PFlcB7vf6r5WspvJChpqxdzM91sfL8aFcv4FSdV%2BqNst7jpTYndsfcthmx1irH7UH26%2ByUeOCmUchd1H%2FrYrf64nOcn23r5wz%2BznytR73QqrraxXHlnrdARMw%2F1pO%2Fs6U%2F6w3NLIJp8CKd11523XyU8MkS21uvswsD%2FMVFYBmwN1Q8uHmmA7HiCF1pskWTO6gU%2FYgjMc2QHpFpbXDlrLmgiwGVwgTD139rLBjqkAYPlyuTvNMkxgAuxPVtT4w3nCZzbsZQwvI4ChuXXHOvdsVVQbKEhOIdQ6ONKufF8NKdD6vOMNLqApnwaA6lknaZkxCb7HDpgx5AylG%2F6HNVuW7aPG3QMo69zLkiFj5W0KuDScvBWS0uxvNkKrtQKZ%2FQa36Oe%2FEsB%2F9xwbAc5oZ1mgd8nIW3qkSSIzwTG6lCqODmfw3wio9MNZ%2FYZGUjLZE7v1hdT&X-Amz-Signature=90f594c5824b838193b506cce297dbd5ec9c4106e8455de039e4ff164c34829e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

