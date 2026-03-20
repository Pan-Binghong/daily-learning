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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGMNHK4%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDQlukzENTcJBFNtZ8jxwUXWnGMmUU9AxSVKGSclNCfqAIgSKTSkT6AKD0DOEIOKh48zlDHfNf84XipwW%2B8wUk%2BDP8q%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDApGY6Ved1ZcxbA%2F9SrcAxYdIy5gK0w0YxKfpE52evgH8zKTmS3zFPi7U7qHKq%2B7qkLC%2B40er2dKNrYX0EIyrhco%2F6fRKi4x1t3NhWBmZQUTK8q9EYGsw5ocOn%2B%2F2UZmh%2FUIfIFS5wQ3hZKVNdgNllO31ZfB5r23NjWOcJnxx5bxHtfS%2Br3vIS2ghN6WrSGG%2B7%2FwqdHe8vrMU95iLxNXxpHFdfeOqPvF%2FgBQCZjO1LNWOy4AJQKPTCdZK5Sw7Ayvj0%2FQ5GE2638mOc%2Fx1sdAQN9qSzX3re5O2Aj6j%2F5mU3rDI0%2FFkUOVoCaKuBlt1IrlMm1CgflN00l9wkA%2FpuGxPmNl%2FBfhgi0Ueijo0YUg6AkLQim6n4alT8A9rBKAzmFGGVii4Z%2FbQsKj%2B11WkXYUbi3Ukizhn7Qc2KN%2F7JHgZ83pzXUDDHAGXN6TkQzsBVptvec1nrLzZI1Ci3BQl7j8sq4lqDtw2vhRa8HyVaWXNy6m3hAMvzHOpWBho%2BGfvg8MKc4ouGve7WscmYlEDPFRwbua9iNc%2BuTJOVntJCJs6%2B73fVHhULXJPVac8AjGUYBWv2FUp2%2FcYR3gU%2FjZ6B%2BS4SYC6%2FXrvdroy4GWkjel2iXDF1%2Bu1VqHaYr0Jl73PG2SHSjreo%2FhXph5qVXEMPm38s0GOqUBBxmt8xCqUq%2F%2BdkdJHmpTdlsSd1Tg6xNj%2F98h1uBiugQjdgYuLqB3%2F%2F79gzoBEGsZcppk9STsQMjWXuO2cKpItos%2F0%2B5ySDWMmb0pyLCg9OSdmbAN4w2ynPeWqjBwN85MbgwwO3egI41KS9OjzTcBzIGWVPnQfPVHS4MuUhxpVvjfwwNxuhLC6VH%2F%2FsnrGCJboIR4GxqsZ3dwk3NvbySdTo6gpsC1&X-Amz-Signature=987245e3edb7d850e5017d18c8f29a4d0bd43d414dfc0c26a0a14b5c52c3a4be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

