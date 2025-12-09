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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y33CUX7H%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T025005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZ%2Bt%2BAuQpybIEnBlcvHihbjxpnn6l%2BJFVU8Vig7tstqAIhAKab0RaEUF9fibosSE7VirNaZmtNu1DgfUTzR7UI%2FxN8KogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaRGLlK4NtPOd7Gi8q3ANGB3v3mqSsrpx4DyoY5zYkRFv%2BJm6QgkCIp0WIIgx8WI2m18URZqr4RMx9xh%2BmC31Dgt9xsarUfVOd4znZcb6EbRK0tCsojivWAvi9n6UdZwJjAWYddPjkQYnsSmhUn2alURE6kRESHSowWRtSZki3KUBSo26E5lDtX5XoaBe3Ad76R545Uc%2BglrOSLcWa8VM983%2FlEiTDYMh8R0ro5UQocqeF7rQFqXLQW12lYhWYqciI9sqe7Qt%2F5bN8higdBqIGWVUuF5jh5F75qVnkjGuJ1EPcqQw%2BYIUFB1ju0Uzz2Wumvy1XsLeGaoiC7wYmvOgeUPKmgJD421A1duBDjZQ0rRKLRjQQl79tjdNx5AMmEH3x8h%2BfYZ3KxFtPKf6onxSVsdx7vMohgcqzNRTT2SI7fY05DZVFjmT%2FH8hO9LZKUJy4JlN24qrnlTs777MQL1dwsGaw8Ox1H%2BRvMMoi5A6YNi2ihNEKKalHJz5DmPsHiC%2FfjChxncleIjWSZLX3%2BNnlKCikK0zfZyXmXbMMg9nENWbgXvLIfoaixhsEItnorRVLu4cQKcc%2FVSdQ%2FP8OchL6e%2FhR4K%2F55jQsmALyf2e%2BFygJTaT58ekADEV6gh4w3%2BpdLpH7oVKcSQcWFjC6jd7JBjqkAYc%2B5%2Fw8Lbo9fW4bP3zCZjpXIMSteSRkCi9vLz5JwId9IdwnM1iuh8BHVdPony1bbd07qx%2FFs8oBabNw0oqFP%2BrVKn7PNCP%2FlXnl3Zl5OiWWI0ubZI20YyAEGJx9%2B4TXGLxEjXJ8alT928OfMAp%2F1Ac%2BV2Cy3QiYP%2BoqwagZhLoh%2BOkpg7HYTXVxP8c4C16jNutpA6zvzlq0t%2Bw%2BPg0BIl7W88VH&X-Amz-Signature=e345251d25bd8cacaf027570693b5eabca9cb65964edeea1592e7f9c447dda68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

