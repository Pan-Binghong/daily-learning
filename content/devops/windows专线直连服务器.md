---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NIZI5HP%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIDThAMOtRKzZBvTY%2FXTzGxKiVTjpvF79z2XgIq8wskPhAiBVMsMaRcGL09v%2FyO%2FBRvyT%2BQqv1JH4W2%2BAH3bCfKdj%2Fir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMGQOgQ5sZbiyPXth3KtwD9yDBa8en5gQp7vK9ypS%2FIDFC0XHBDKIlDxHwpsXHb74CVb82dvOLXSlzSNVAZ89X%2BPSJrETJkP3izxItC55CUhrXjUcAKCgamayI%2BNrV6LAT6mpD3AXUyUlVE4iw3NyyIHyr%2FVjrqsFEzF7XFctePo9rv9zFMvrt%2B8HI0e%2Fd9xaS%2FHEf3tqSXPyNBGBm7oThF0ZYz2u2Nt94uKGxN3yNwWkjyISlPU4PgfMNzVL0mLqRVlJl0DNWOeLuWJgBACfMP78Ri5KS5tvrN3DhTM6CToycMKdignTF2097pBhrsJoA9CH6ltyiuOK7S75IVYECbnGis5CRQQ7zzACHZUaJw%2BcT77RYOu%2FAecIGGr0KxtiGKIRclJ5EYZ64g7%2BrhGeq3GiYS09KoHCxyn%2B8ar5GGR1parZ8VqWucebThJLlqIHxNO7uxxGAdt%2Br63rqSfEymW7Q6QSEFWtaq2XsvBDxTIX1rfNlxvWukbhhCgOibnAcD4FjUfx117dfXMmasKUqHAXI0TkIfBN285tg2d%2B8T2ug0RbblT2TYl2BnMZh6e5vySxF8%2BfPfZEUBYzOpgAxAQVpunKg3aRoeP5gBIrS4DnSeLNubyTFkNibVLgoXWp8K%2FxNKAvTX%2F%2BjjI0wzJa%2ByQY6pgHA%2BSgoCqJZ3sVS9c3QRIFs6ZPZ7HLb4m9URYkhOzrgTU%2BYQcIzbpMGREoV2a0IhhpReCRO8Zpb0R7nXhKzLvFqh7JAzlQ0PL1n1TS02pnygiE6kdGKCpS3IXVQZMnBh%2F4zGyf0qANCkYgsiiRSpvxVoOQrH2O8r%2F%2Bc%2FXoNKuJGDgGHiRLqeR7pPshctJsvCfwsNZWPB%2BPdc1eqX4GyKZkSqtyqlVHx&X-Amz-Signature=83249fdd53c9d454241d09b8f1c62e833754f42bca4d3fc17bbb8436d9272515&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

