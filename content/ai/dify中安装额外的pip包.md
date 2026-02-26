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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZCP2WBZ%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIErFJSImPmQqq4tOeJrpQ9FpeMPf3LCZo8O8QYQRm8ZQAiEAxw3Yd4eE1%2FvzURRI1UkEMZBpwkGK1daJYvnccVQj734q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDF%2BxENYVon7kU0enVyrcAxTXfxs69%2F5BPVv0R%2F5bHUngI%2BGthIqTp%2FTPyCJBKrYpCs9mnvoagZTsh1mzjIMLH6kLl9P8N2soTOzRoFZkYaZThNrt8VeBOP%2BqTYEA3A6bugA5CmpeLx07EvuUdE2FXL9arVU9kMGb22IMwpRzsbLaWKlAEFYKUZ85HuGHp82X3THcXD6etGazZ0Wua7AjK0U0UOaleI9Vi0ZeEGR2jZvkdRJr6d8sXsmqevid%2BZVjlZB%2B4ZXRQ%2FpaWmNmyScDdj%2Fslr4p9VlSW5tn6hzhZ%2B9MXxt%2FBZnv4JitfepU6Px2EWMNZ4wi30NFh2cJ%2B6CqTSt0DBR%2BRsrE35mFD0%2BcymIW0Al5H3TflA5peX%2BaXdt%2F5elHoZkdDNUnUkyN11%2F%2BY1dtmxoUu0K%2Fvf90PJXQSQZqdEhCyutsyz5hLIK7ZoLJo0UVWPZyAr%2Fbw4mPlfRd2Kg1zGYUa0QB%2BVDCdiawl5ITfai6qSNVdjzB5PTcoYOBYyDbr24ewgc7A4LVJtAgk2CvbQ0bunRB0wzNvRp2DUq78Yq%2FMInWHW6yhZSG3ARsJ8uypxJK6L2xxAZYFCQ%2BRBSB2LJU4fqIL53qUXt%2FVvutT10O7c7ZbrN9SHD0lgHtpNJKUREB%2F4XYW99XMJn2%2FswGOqUB%2FQtcR51OdprDTwRwGu2YWgxsTiPsXabVjrh%2BONm443KSZRf%2FhGhgvIWyzvP6v3H1xR7P300pHK%2FX6VMBEHvTXVP%2BRiIR8rdg85OC1Gg%2FCxbMlEOO4UHNCQuT5NW1AADDM98Q2eEJ2jU87t2%2BuGaSopOmOTiZd%2FzhAUSscVdXNk%2FR9ojxC1iDtcJn36yQIA7Xerqedp%2BHFr%2BwCi5BB9ad8cLJiwLd&X-Amz-Signature=cc01f612998f3529ffad584799989ded095d6eaae2776049e006d12930a7790b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

