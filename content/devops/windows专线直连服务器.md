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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WY7G77O%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T034153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDO2yU37%2BuynNxPK8zLYgCl%2BWWCInjKEHi0p%2BjxaWpFfAiEA0qnz49OT6X9y9l5dFqncjYd7BmKwAib15Uozu2CzCpsqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDwBzUs3VblbUEysWyrcA5qGltQzYDJylXuLTCM0sytLtE1gWTSr8jXhUVke1pIpo9vRE2Jgn18EVsyS2n0XW8z4P8HmvUrXhOZ3tVroMh72f2lqsinT%2F539oQzVD5gMBnZdb4HpA3GOo69T8kIYY2R9wUdwuWG9AkIsn0SB8b3Fx7F8UinXveXTP11ksTUg43Zoa%2FUYzcomHugnB22N2KML5xwOuQnJORQx1lxZ%2F7OEWazQs331UE4fDkWExWAEBfLE0muubyFQ5BfYoh1ByIARRRtDRNp4ySZmPpbT8lKLQi8gRIuq2w4nm4nr9r3P4ttiaFdqfDQSFExPCAY2J%2Br%2FnbVOZdb4%2BKlDJ5b1IalSwy1yG%2BqRQUarSQp55SaiZ8VXeVyuSaJ0l97M9rZJWOuJeUMzqUAZ1L6dczjRi6%2BR3bh2Bdmpi4E9NzWZAebT3GinWbja1RDJr0g6%2FQPsygEt44ESOjoRFeHfugH9RSd9XBBtd7bMZP1fZbqTax9BD91Pp89ujIyccYQYc2Mw%2FmpQsY08F5lizNkAl6I83UwJL%2BkcHYa5zEIyMJQeoyHOjZr5Tw2i8aRqR%2F1umlDwsqCh9SaK4CfhoNHeYxaDPp3WAnWXp3lVyJ9jBWO9Zjl8f5Fxrsn1yzlJrM7IMPKljc4GOqUBzBGoFVOC2c5vSj6ki9EWwDpVLytOnnL5TVkJPvftCIBLJk5QOJ9sR7xQ1AIdun0Pcy80yfEhqSytZxn%2FW1%2F8At2uuewSJ9hmaBohvdge%2F7saGm2dIuQVe6L1WbA59LlHsTrYEE1U4ASnZxzf2R0lvPY%2BuYb5%2FGkRyyuaLOQUSJ64Kmy%2B2DtOn%2F0NA9jSZwG2%2FvMz3JUZQiSSeMwyKYQDbJv6Vepa&X-Amz-Signature=205ade3336dbcb2447b1b83fc4798416890f705fb58827305477c782b2617b4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

