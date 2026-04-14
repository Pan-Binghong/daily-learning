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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BULEJDC%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEzDx60KGo2Fun1VwLaPBa%2BzBTvx4PkVf8S9JTbz2rxvAiEAqr6fimh%2B8hXRZqywlTow6g8MFVaW90vXmjESAJutcIUqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNds423%2BWeQooYkldSrcA%2F3xSaudIASEZMzqbvSOwRbFUT8DTRsAXoHg9yPQ6O7yIYgErhV10LKxnMLZVOlppWN1KdsWmBB4DQpKy6EB9Zg%2BwiGHZTTtV3Beea0z0lZd6QLcEWdLGYEgqXP5XQSHJr9w5nXagbI3EjpvLb6JDNhOB930FVc8%2Fhiwxp673jgNW1BazuRz6T1fjaK94Y2QRtNNYlpczgVd5iTv2biqjRZvqMZXcfKDwHzNGCzPqTooO6bfJYm06za5xii%2BRLD2wDLWKvaASHr9YDJ3hhwj6wTuNYQ7%2FGs%2Fu4tmj4i29qjcPgwpsuTOsHaHCMImZpA31c7%2FRd0cbyUme9UunMKG1O2E3daLbsBNkEzKYIO3R9HyzmaFjh3UCifhrqiKHIWNL0wggUNap9ZUBDnwe%2Fn9%2B437DYJkCcLQ6OOcoTshssWniSGZVSXB2SqgG2ECggpFqcY8GRx8itDXf3ENjs6O6pBGyy7rwZBQtqd2Vpfi%2FFHFwdLn4JnDUEoUceqYRkBz8YAU3zaWPC%2BLvXpxfsk%2Bpk1UjARohtjLZsLND142k6%2B7hMHaI0N%2F%2BjXLHRCMjDvwJuMt0sC1qfonZak6G3%2FA%2BqeH1uyv6%2B%2B%2BGkcTwcs808fhZ10cpM9i9QFOXYqkMJLf9s4GOqUB56da9cgy9pLayr124Ew9aAR%2B0NuQrbY%2FSH5bSUAvfrsg4t0fZHoVwC33pADmh4V19fXc%2FzAP8u9J6iEErxd0gSTUxgVw5707zPK3xty0ITCWm9sFqiEHSSbF%2Bxl%2Bq1BHjBJmGP8Hg2XLAZhELplk4q4HxMYo6SmtrQmweWgd3GRMMtx5xrkwfBs8gJNWbfAQSoAsqnc9inXApSILOWh6k8%2B97I%2Fv&X-Amz-Signature=99dce9ed892770b9a8d75e5995ce8851f3971f7961d2a866d8b2cfa62aceeebe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

