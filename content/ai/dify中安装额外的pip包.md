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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHNODU7H%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIHRrB%2FNln2J6WGlVg%2BjkpQz6yQByob6pA16peR08wDgGAiBXvYluRhvbW3XY7kHieQNhYFOQlhozi3YqQRwTxmdQaSr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIM76J78XCefpn7z3NKKtwD8DWG5b0bt3lJJiEU2dDXe25qZl5%2F%2BHzFPoGSKIF8JcGj%2FFEhfwcAD17LrUJlz7OTnawvwt%2B1kh2eFF8Z%2FnQAxTLVQtqidMFGmwijIJz0oU%2BTHH9Rb8xQIU%2FHU95uMIiTeu72wVtctAmbplDv68TP4ltSfMMPUvl9M15JfXARUT1HRHH7%2FdXqDuZOYWniDRaKAx2Tzya3pCQFTAIW5aFb6xAxMnRKgl7ALuUCkwiPgn6hUyWFvvwQb6qfsH8FflpLxQ23z3yCRxw7jFCnOyC6o%2FDeh3Gl%2Bi3Ok6rtLH30qHtjpaYFvXECLg%2BDnL0zkplBJfLo5iKfS1G3rSM4nv1D%2BC4o37ldXwHjWzjq3gnYMscvO7nTbIIVh7oiP66O0%2FwYV6p9rbykT1V1G5tWC2B3SjdJskIPQM8dB%2FkfXmwyD7%2FCnlBqg19Dg4w8qywakgPZFCM0xnM%2Bq9dlh8Ci%2BlxTbUFv0UJypCxFNTjDzQHWST%2BdRS4sejOjc2%2FTm35o0DaUwidYnOTFoWrkmnSbb3M6uTdN2RY0FuBYu7IJZSjqrIrRyUhCA5kZZSMk0QWesegRuH75cuPdIo6hbNAVSEE%2BS0TB19YqTr386SQKqivn4TZn1ZUfguDRR8YRnmAwhqGEyQY6pgEE5jfpCEAbBB%2FPufO4OcCY1NwLjgc%2FhVIOwhnJyMCWC5Vf%2FCBNUnhgjtpeU4Aatq3gpIj9EXSMhyHD7sP%2BHPRoKm%2BYqqcQE0vLrNZiBQgXjD8EwkexyfrG6zA762RiBhLDhsvyhwbLajWk94ZNJnQ0s7lmg3Goz54%2BSw9f92%2BbCbqz3itTPbvKWMnZ1UYanfcWGVgdhN%2BRmkEJRF8yA7rjbxM0K7zE&X-Amz-Signature=f00b408fc661765a69107312cd86a558b6f22a90d081f027fc8071dfe7f5e727&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

