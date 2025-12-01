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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVHIC23K%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIFHUze1%2FvdUAFje%2BwaudbW0C9a%2BabSyDxg53wFfjHz8NAiEA1JPRDx0f6fxbgnFJumJqhsCfnxAxpRsGlWQVfEdtM3oqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM5aBx0t1PCJ1P33uCrcA3%2BkkGtWQy2iePRQ10wtJzp08YEvxaJ7iRXF%2B3HTnkaffTwuRavIElcDB7QqQkvDCZOz6syuc8%2FFjkHTwGsLajZgxjymb6MJ5iOP3m54Dfld%2BggOEHf4i06t0ewo4biAC8fD6G1VI6YRP8PEPpxiBFya0HSY0%2FRXDWAPO1zzxZr%2BVekMsLlQZLqfB6FsN2zmqtUtkGMojwKTAfQLLyEZXXhRRse7sP7rLM%2Ft3VbBkqgTvXXRZNbm41p3UiOro0CGx2VrPLWcwfgE8kZqQuP1x7XEBDs%2F580C9wKwMKkJZY0cq8vNPzwH5s7eWu5L8RthcT6zG3AYYwD4grQCqQZMzodaeKiFjkJl8ss9P4leAFRsHp1SEhsBipo2rd39%2BsUhIM%2Fu4pShJ6xKFBPndN4tSUGX2fLzY71IJT7N1MciZt2YWirudPdrcGK0d751Qk8FfLu1H1Q10luBdz3M65Glpf9tDyCQ5osjT7Dz19qmZN0e6BCBpQ20VRBIWxXZFmsUQDmBnDiu%2FUbtjgAMOHWjyTIeQbSf0V%2BIXWSXQWLz8SQDbXbkEZrGRjYiX4HkqpqJgNHGPG9GCzNU9QqrIPu%2BRlxI1TZFVrr7PzUFzJP33%2FUtnmgryQfyjTkGgYPVMNCBs8kGOqUBAqXUVpym143Mny0xYAInF%2B87hnZrF%2FllH7BWL7WYRTVf7mN8Y3i0F38cK8y6QmKV2sM0Q%2FrP9IN7zHTGsCmnq79dpalOxfFh%2B2ddMeQe31ti1wxM5OaW%2F8H94pgxHDO3c3n68MTbTN8rByZhUz4itJuhrHFzo7Rj2wP4jtorH2cpYqI2%2BBj%2FzDUvsPIbqcmQokjnrRXywV6B53PofzEuNlm8IXyB&X-Amz-Signature=bf07a28bfeb30995470a760b92b0e49e27c81c1f718e301f8d964d4f61c092e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

