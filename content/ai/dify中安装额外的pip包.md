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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6T2WD5D%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAjJvQq4gP7vf6DA9x9W2O39JLEvclioFZhTIjwiXHDNAiBe7yoF%2B9%2F1Thwu2BBAk32Yhp%2F4zGvYpLDtBFv6k%2Ft81yqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxv98LAQg0t9Xe150KtwDX%2B8vIZsfGP8gtR2LsS5V%2B8nOTkiGW9DkcWliR19YpJ81XE4InHqEOtAtdKIX54ZZm8f8IDdjx9c4cf8q31InmHpC1OVNsyyAa9DOIUYthxbZkS5Vdb3UNmbwmyQ%2BslYST8P5upXJrMAEdn70xF%2FQ0Wthu1ogbL9WD9ZQ3llRG0e8LsXFKin%2Fh50TxdEhf1Q959j%2F56FIZt377w%2BDCf%2Bb0QSFAOHYumVw1hxoSvE%2BlVesCtsqp%2FhwnYj6LjmIgrhnVYyFZfkTDuvunFvBEfW3xdUFZJDstYfRerpWWJgyWs6FrQbJ03nsDoHvcRvgBUypqFxE2CsbVclmgwubqcyTefWyOdkZ7oGZ3ZZswXdJpcs2K9ybs6zy984Fg9x%2BUFqjqGCEDHb6uJL96mjL%2FC0AgLpTuY4HVvFFNqOTgxV74z31MgS7%2FEzKCYrUiJnKfbl9gGMIlkqv%2Fc1dVkbaSAMUAdqKIlJSWTf%2FCmQ8EVsT0UWw2jkqp6CXYyZ3oDm08jtw4nUTdcioFWvmTFzxc7HCpEF4gnuxoLz%2BqwBvww%2FFBWuLv9C%2BKbKG0NJP92agxedXgVqbGiukhT%2BHaSm%2FoHSWL8%2FMvEu7LcW1F7FGTQyNZw11%2FFQk%2Fwdpdr7BqhEw%2FviGywY6pgGGiijTDc0VIAlHGw4YMrSaqmeU95%2BI4jUL3p0yI181OV7PrtQm2YfakEXI9LxK2QpBjvdHTXyGYLkszDs9zoQ8nyheQrvMO7Krh57HhvrTWBL%2F6cB4l5Nv7Yyl%2FwncOzpcN%2F5gIpt4YuP2Nf%2FLSbX0mYe7zzGsA2BX2Yws%2F3mzhNVOXMjO%2B419mzLUM4wT9JkeNIeubpAj%2B1zYojDSTxo5Esa1YB66&X-Amz-Signature=512a217e2ea476c8b63b3495220cac48c2a1dfa5bd973a1cb73d0b10df8c9b2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

