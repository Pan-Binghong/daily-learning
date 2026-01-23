---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D4MM2WB%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDd9Y3XCdBcfVDv4CDoOK2UcOvJ7bhJviApZGk%2BkGDuEgIhAK%2Fhraj2pG3IuqcgJwCIZCFagGmuTzZvQGMHv6ct1F1kKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igws9qF%2FTBAZmICkJsUq3ANayQBsArwf3LOhuPl6lkEK%2FVhl%2BTGik2KrI3zznQmg5k782YwIym3tclyXYm7jxXgD8TZXlX5iiCjmj6jSUN2I%2FV8ZFLW2P2OfECmi3Rj4HcN5XLvqX1702BfU0hgSeKatw4047JxUo66j2hdleGEMwSnkJkim8wLFMiUWu%2FFxlgXSufuLXUXvL7JQrLJDjJoL%2Bqg8aHNiUR%2F8PfAU61nMhJwlAsIDVGVGmgiWkYieB2%2BqVorlCyquhNAgppbgl5KzlruY2b8xozcX7obyuskCqMYHbyD%2Bg%2BV0%2BfaTZdmygkZRLdRPsk27HjEQkThyXH2qMtO4B6uy0TfgcmCrmeuhOsNPwiMrPf9PZQLOGCpiX98RjYKAamr3FTnyWFEYvUu%2FGcBV0MrMhdActtOkXKb8kKq1jLtjZF4rp02B4Wjgp5Ep8CBT6o0Jxf%2B1veoKezC4hbTYr0sQyDJVVJx87%2FhIExoL7zGx7lya7xD64nRAxJMkBIVrpee1QjHaokjuxIP1g6WD9h77oZHG6jDIMKpU1LBARJ4H4lfKB7BTGj6AEwAZpazvNvM0HWEEifh6qrDmQ7Hol8p0n1%2FBCFBNXkhZBRGI%2FRCZj3oHXiQ4jUKgk7Lw7Ecd5dLWsKbPDzCDr8vLBjqkAZXcYU%2BdcXSKmSAZsTU2rEFYQzth4tEFm%2FxRr%2F%2FpR39O0jMxRpEp8kIttGC0VS4wY3X3JiJr%2FN%2FwY6PIjGjH7VL4d06G3IZLO6ZlNi%2FfaHK6xqfkGd8XY54qRlb%2BGIeru2auw9Mnx1F4dHvQ8HJi%2FlFEC0grgWKM8o0FLJJuyhXNK6tOBVnCKJMCSSINWvkn8ceX4JaSds8bQ3i7jI79AsQgGMYo&X-Amz-Signature=e71454bc0ceee655c050d3a9ad85013e112bfa250c07fe47f6f4bd274ab6c4a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D4MM2WB%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDd9Y3XCdBcfVDv4CDoOK2UcOvJ7bhJviApZGk%2BkGDuEgIhAK%2Fhraj2pG3IuqcgJwCIZCFagGmuTzZvQGMHv6ct1F1kKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igws9qF%2FTBAZmICkJsUq3ANayQBsArwf3LOhuPl6lkEK%2FVhl%2BTGik2KrI3zznQmg5k782YwIym3tclyXYm7jxXgD8TZXlX5iiCjmj6jSUN2I%2FV8ZFLW2P2OfECmi3Rj4HcN5XLvqX1702BfU0hgSeKatw4047JxUo66j2hdleGEMwSnkJkim8wLFMiUWu%2FFxlgXSufuLXUXvL7JQrLJDjJoL%2Bqg8aHNiUR%2F8PfAU61nMhJwlAsIDVGVGmgiWkYieB2%2BqVorlCyquhNAgppbgl5KzlruY2b8xozcX7obyuskCqMYHbyD%2Bg%2BV0%2BfaTZdmygkZRLdRPsk27HjEQkThyXH2qMtO4B6uy0TfgcmCrmeuhOsNPwiMrPf9PZQLOGCpiX98RjYKAamr3FTnyWFEYvUu%2FGcBV0MrMhdActtOkXKb8kKq1jLtjZF4rp02B4Wjgp5Ep8CBT6o0Jxf%2B1veoKezC4hbTYr0sQyDJVVJx87%2FhIExoL7zGx7lya7xD64nRAxJMkBIVrpee1QjHaokjuxIP1g6WD9h77oZHG6jDIMKpU1LBARJ4H4lfKB7BTGj6AEwAZpazvNvM0HWEEifh6qrDmQ7Hol8p0n1%2FBCFBNXkhZBRGI%2FRCZj3oHXiQ4jUKgk7Lw7Ecd5dLWsKbPDzCDr8vLBjqkAZXcYU%2BdcXSKmSAZsTU2rEFYQzth4tEFm%2FxRr%2F%2FpR39O0jMxRpEp8kIttGC0VS4wY3X3JiJr%2FN%2FwY6PIjGjH7VL4d06G3IZLO6ZlNi%2FfaHK6xqfkGd8XY54qRlb%2BGIeru2auw9Mnx1F4dHvQ8HJi%2FlFEC0grgWKM8o0FLJJuyhXNK6tOBVnCKJMCSSINWvkn8ceX4JaSds8bQ3i7jI79AsQgGMYo&X-Amz-Signature=8a67c944e2169a4bacc3addcc55df4b2c8ca085d9822a84e0ed5d1a8cc1ed859&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









