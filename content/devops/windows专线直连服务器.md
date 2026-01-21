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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PK4IR7Z%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1TRChXklaV3XDJQ3z56K0yOtGK0WFphmg9Hcgg0F9fwIgO20OpZj8MG81WJcsHPwvyYGYclqFRr2ThROjHbmizoAqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNS9GL%2Bh5rOpLyPbrCrcA7%2FLnXiBy1dkseGjUgN03OPEGcQW2lVES7tSFpFpiJ1DQJURF0qhmUhlKjAbI5zx88nh9CcQr5zY09kN%2FzvPiQ0wbns68jfkx74%2B0CssDg6IujqPKXzmXE61wt1cQB4JOGCHYioe9EXqDtrAFyGzn9fkFiTSy3uDvbHNMnJ96LEMxbKL%2B2SvlTIYQ5nvPLB1WtOvFXxMn5FMHi7CR4BV5BKd%2FxYed0EyESm3nTD8RmlT9xb9YpQo6Z7Ek6uosTkao2L09pY6xdizIqf3%2F0eCly7ybZ69sS357WXx%2B0csm2brEsJowTp%2F%2FDS6OTlv4t20%2FyFMaXZu3pcklaZRE9k%2BicabT8VR3t0sdXz%2B68%2BPqHayQUwC0pP2h4RuG1t6nSOs2qgzfCoe3%2BAwpSISaC6AaPHMnJHJWwDJsH7x60Kmu7YQaIBuzUIymIHgYkp8opujDnglw3HPzeYOOHBflynUzejwzeYgTq8YUpw1jUni%2BWsTd6Yw4SJiwDn9orpwVwMv9syh0YHdv3ONh49aC5mNv%2F1Pr0rgh9kpQ1ShuOAnPAp4ATP%2BOymzuCTF19BwqLB8aDFzePLM6kvVZisP%2F5Lcejp%2B91KI%2FoQZRkuI%2Fv4Ww%2BPRD9Ib1wAEcfBqaQVOMIPYwMsGOqUB1VvUk8PcyzHBh3IINjJe1r2BngFBl0Z2Gfox7v5M8ZaR2nzOJvz5yG0ZmoK%2BxhCIjxiNfpUHq0j8QoCvG%2BrLJQ3kySmrxi2YGabAMxIqdf%2FRd69rQlaqKm5KozyCxhuNHKs85FYSdUvbnG16bCm6bog8x7%2B7T6DwhtU9N9wWQKCRp9kHX2I7T9LiDYGWUbn3jJh2BkI%2BPXLVogUw9F5r9kgBf4kT&X-Amz-Signature=037aef8d96a3b88dfbab97accaf6feec4f8d58b19d77be199557bb63e51962ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

