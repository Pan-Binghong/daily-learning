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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S53AMTXV%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUrtj41f%2Fc5fGbDNjUE14N2n2zuVgoO8RKdP%2B0hopiuQIhAPoe0gso7QqKgzVWbWS8e9JnVsS8jr9sgaUqsIgeGvpAKv8DCHsQABoMNjM3NDIzMTgzODA1Igw9LOF1tDzvri%2FnY2sq3AMi6ONy4Ya%2FzZs%2BnZe2rL7b9PKIW3hpa%2BLLaG%2FMOgoYjjnuCnSyPaHzrXTkYrNa42%2B84PIEVe6g9x%2BhYpjXK305hc1WjWUB39Tr90gncw2J%2BO48F1HxS5KArDEYrycs4i%2BHzrVf5L9LvCvSNo9nvRmyCf4CYOOgNo4uG9lqxIN91%2FOygfI6WXL4cd52lWdDH2%2BA9rIh2f2S%2BCao4499jD8GHr%2B3Ex5lUPHPZyvRwtlve%2BolJJUykeqvshvwg6niUQ3kgNJG7Z8WOZZoITYGT7ob8%2F3UUoAvq%2FFzarXHaCB9qFFUJwXrrHj12DyhQQKOCKDM7kkdbQ7RnP7zQxwxBIyKk1UdPUaLsFaWuIe24x6mo%2Bfsi2cyeVgzbnLYVI19WoAx4hin4lAN2M0QYUxj8wpBzAEJafzv1YSF31%2FP9fGZoSKvtW0XQixK84KopNIWtfJLZaaZm2juHMyLx6cfCkI96HFdzKvQWMrxveSYJA7G2S9tHnGP%2Fz8utkRrEVG0M8iItUutZHYsCESxpRO9Xiv%2FpHFH78TbO9nZtERjA83GoP1PLldg1YPDnimJE%2Bem3i7ztBhv88D%2F3i4VAWFeibMs8O%2FgPaRDVfiziVSiyN1j4CwLymKoO7vob3xypzDRsJnJBjqkAbL1E93MjuvCKZ8TK5Jz68%2Bf5IlZiD4j7kf8eDASADUkri0QcADWUw0QRCCsiPRd59LP%2FzsHf2ZA%2BcZtc5gkHKygxmmu9jw3RNpqMqCNMcVXMhHyOPTI0je6pkZ08XWN3fUJwVUsy23TYN8Clv3rNeGBgUlcdU7B3M6h0cRU8TWX%2FMD%2FHYrXjVhwjxp%2BBxDaFMV8FmYymE6y%2BTJM7GwIWNXNAXj8&X-Amz-Signature=dae25b6671ccf20d647d6e7d691a9f3dec9209864408d5bc5003999e2e6920cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

