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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STIFXAM6%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC3sKI1xhDwyc5rxnsNzGkwnz3a81slJIDePxfrWpUMjgIhAJtJtMC4xdmz94vYZ3XwVmeg58I3WB8qvdXTmeTTbDnXKv8DCCsQABoMNjM3NDIzMTgzODA1Igxk8VQQDQg8PWdtlugq3AMKZR%2FjbV3svyfhXzQ%2B3pkdKT9RfF5ZWO5d%2B5S54WpenurbUPqt7bKAZsvuMFMC9yy9vDbVCkPsLY7P7FPUNrVVsikl%2FXQJ%2BWFArTVbM0MIwpSs15hWZs1OWQvoFHri1et3Aagao3r%2BYnmE3HTabN73%2ByraApEWKNTWwv27IFl4C8R3NktyOeE%2ByCeY9ZVxYGKMtkhMb1XsOrwRlRVbA0hx4VRPJeWIMV3echz9pBM3%2BhbYnCoGwnr%2B3KGL8hbuB6Q6KfetyPpW9j10j6ZO%2FmQkKhB7sw7Hve3w55vdOu8Bj5U0Ds7EnvZyWh3mOGjIk%2FGhOCeBZKhk8js%2F8%2B8yQmh0edKRx4VBX1pppUVY0MCsrIN%2B2rviM%2Be%2FBBlDjzrNa5dv9hPAk4LdooKd1pEWAcTYKG5kDr50mDt2ETlq5qdVynWXNFC%2Fh7Z9X1XU4WSR4FObYqjaqZwJ6xNvcp3jUYQNrYb9KsLm%2BqKZyjw%2FrEgw9H1jnbhpWKNXPTuhLX83XVW7555zs8Z%2BO%2FqzKX1baEzwQ1dNenoAnH9GBq2KpOeVVGMqxXs3kebEPE359sbPq%2B8yBACfVwk8E06pt8OTxawhtHb5Dx5YQXLe07sZ%2Bvs7K2zI23%2FK2TYqFQn7nDDNsPjJBjqkAb%2Fkwb%2BqdbCIV%2BuyQTvk1y%2F%2FGrZHBISs1B0f9WEMLtsN%2BcE41jmn7BNVP7zzuJ03FhTaVkLcgcRrpbC8liyi8gP%2BL7cizw7aWUfLFGt%2Bk7MbklayTZKJRPfY%2BHnmAeqYnJD%2F%2BWoWPAdSR9IQc2pei5yTd3CL%2FPeNjvgOo1bqkZ5CWFGqIknr9VJlqE6maPBc4tW7D8hOYMbGa6VJFm3fVFAvuhF%2F&X-Amz-Signature=beb8c78151c4f41f2d9b41e249df0f0c715a71fa54b5bb55c5a5264f854ee33d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

