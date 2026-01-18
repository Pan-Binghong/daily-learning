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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZSZ3UOE%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFUGC5MrL%2BTTiHpLL7PmIYy0kcb1PNKQCU9PzEUab6FCAiBb4y374bxQpcyb3%2FwvKd4gV89Kis%2FulZVX1jJKI2H3fyr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMbTlTwR6X%2FKFi5YxbKtwDF4x1CnhXtdNR9cOlqnnrEIK0HFAa49zUDEwxf1Kp34AWscr9AIYN71gZU0%2BUPC8hT9ur7ZUpgVCZJ%2BOBmI0Xp%2FB6sahmISLh%2BxWEzn%2F0D6ya9HlhnHqhhSlJ3ZyvoJRpn3gk4VRXy5BPnB9pzk1l%2BbKw2DEEfJzAfTBmlPf%2FGyDYH4bNt0IgQtK6K%2BAA%2Fr5P7kTdHyVFFkTW0Qhjw0Pmwcj1UOSX%2BPlTAHUX2YhicjtNHmU9n6G2MiHSHBZWXKoJmQIMvH747opxqIbiVlxATygat2ZqXXDcUJGlk505zYnvBlLuIAdSnAqstTmjbhIwrqQf64ueId40Xn9dVvJiTWGvTWhn5w%2FTgsVc11MdDXen%2B%2BzWSw3%2FNVBypdy89FNV3VMa7HVCmpLG0Og1q5K4c0soQgVdQqb9C%2FgVco8l29K7AROeQDtejFuxlkcUpopbI5gxUgW0%2FUXvlAsGU0e%2FFL1Q3DzeHJhZ45SYcXAHp39bYryBJTF9kjsDaQOJGgu%2B2XOfSUFX9hJ6NezfXwj%2FFtlz9WgIWx%2Ft05ePHgv78iZmBoWg%2BlXnr%2Bk13%2B0fK%2BTKOLmzKsXj3Txsvd6y8KlaHHvkZEZX00BxymtjSlVMrzN6HBc0g8xRbpQ5LkwwuYGxywY6pgHXmh9GyNb7SI7wOw6q%2FUL6Ekjyt%2BBNvUstmU9Sr%2FF0x7bf9u3WGHSdTQ%2FNRurpkwDdG0DfP9t733l6nrxov1dgEhpOEArqRFdLKvS07CGXIPwf7bTSOHWrQgRShPOxNI6lz895dTz5krzIXTvvG3qBwu0tzDu4d2nmirPqaE%2BgJnmnr8LfXXYAH3F1MYM2aCUmCyG42rO3i22l9J3ayGX7i0RsjG0r&X-Amz-Signature=393d0932272bd4658396777079d6874269db270b5015a83033069bed8c2a8292&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

