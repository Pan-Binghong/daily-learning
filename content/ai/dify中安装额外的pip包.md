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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZE4LIJW%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBypmGGWMc1O17nQeNHIxwK99ukZ7ViIGnqLhM%2Fdc4mgAiANFawGzN%2F3sHHyIkg5RsHcGnQSUzIqLn8UuJ2D%2B%2BnXYSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMpF5sL0ymywx33%2B0XKtwDH4fYskMHEjmFT9p5gW%2BaiFZmKpiYfohFX5oj6Q6MD14ospF2bYZ3nezKkpMb6rRxgC4rTrX7hqISn2kGJXOqKHpImS7AOzfIS6PmfV1dnn1G%2BROMFLcEooEYgXBdfJFuZABzBrz5s2Aer5SO1Zf8T43g42x8%2Fw%2BSLbCNiBIFF%2FRlHQMmR8k%2Bnd0PaXtaFUcjiRFwhNrzg4ZwlljvFIaTWZxPnFb0UD0bsBSs2wOauDCMgg0f428otO35F%2BWcr4tRzkfnqddK0bp7XgnHoOWZetS2BJyljJCnviwnIxUNapKZOhIyARV%2BeW%2F98%2BOeQrbC2BMkeud5KodflT9rsgBiGO8E4KeEpWqSMhFjgRSliVltsdwGJU1a%2FfAFpM8fWmY84nRQstRAH1D4loTFw3bVl09DxzD5YMaxXQpKpMUn2DgxDBuXtrH0DjlDZDM1eqU2F%2BbE7XV1wDsZiFHN4QG20NteeFDAdfs1HWTA19834AP2wvQSEjvIdLf1Ojay0SEjx6ZzDCxGjbcpq6%2BIWonNTD2Jze16lTcXjL7o2C%2Bl%2FE529%2Bb7%2BFCR4Q3jWSMR8EroiVeWmlwa6ssBICQYlABKI8ETC4qqOs%2BXUxQgtsgWD8SsXPYkCxVZ%2BvLqTBAw26WrzwY6pgHRZFWkw7sISPGdDGMKuPkaMvC5czdpjAZsp0U4aFaMVFZR828K5LYlZzJbGCK7GQtCB%2BYqFULY2%2B3S1xulz7Qzf3d3hJQQmXF4k2VHELqOEXXr%2FFKHnkxaQvWpNV33ptRG4m6USMDCTgQita91HiG3kPmr%2BfadfeLCQsXqfKSEb5opHaPw9wD4xI3VGtZKYoZYwM%2BtOXspayi8alUtlInnLYi7Hvfv&X-Amz-Signature=bab08b32eb4217ffafc67ea7d6f468c27eaa3c03be0a1330486b59d78fac2b00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

