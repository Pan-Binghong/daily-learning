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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LNVF6AZ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICP%2BjgJb7TyYKw2JZcpEXPcKCoGDBys3sz%2BVj5V8mD5bAiEAvjTJLxyuJATrclIJVzKmuc992E2uoei5TCQ%2F4BwSPIQq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDFy2LXzwH6jefZM07ircA82QTb8aNQTlIjjQmUaFoTwjQg6v1GelhvsixISZaz9hWVeF1Le2VbtPhooonaw3u9TWj880FcBldB1Iw6X5%2Fon%2FG8LlL5SaqlsmAwpLev%2FIovJ4893aeCupHUFskw%2FEpLDYhe6Mnvyox0uHAahg%2B9lQMq0tBUqMIXscefWeyoJvH5Jcg3G0va19bZYn98zX1iUq1iAdcAkgXzLcVIWaYV0KvXgMcGVY3J38lemhh70zDGNaBnDuy5goIix7x0%2B8%2BwZ6wuCeTTAiOYS6BmTylYh2Ca04STn7hsasTI6vH3GPXktZ%2B%2B5Ni0dIWQCR7gh0jNJO%2Bue39j7sSW1wLGC4VwuKiwnDGgHtODbkyXeFmEbos3SWMiRvihdMhBByO3HcV5%2FdJIaGLwgTrAZgeFtqMfEkSiigjwgJEFhhMsIrurtZqV6MNKfKhXauHDPblThnlljdDfXh0fFMVNuFCttg%2FIB9DwO4wkcQdur3QtrRrNUOaScLtwLHAyhE7EiYc9gLh5Ta9%2BIQZNSnOzYGrVpgjbjUktj1udPIi6y9qvbjJbHIxKkjYVgAeWv43qF1FJFaEdi%2BbfkhxBOPqRKyvGXlO%2FFI0i6ooTiY1EdXYvuR9M71znwR60x1cRnQ3T9sMMui68sGOqUB8d%2BIKsSGY05u1XVxBZeDnTWtkkHC5xMoxT1TqJIMtjfB0dsJdyMcmXXl9yIMJsIMjU%2FKsC8VH9qIAaOJ93OT2YBV%2Bra8%2BrGRi4Iifhg3CpDYLNbYQQf%2BO3RgcY9y%2BO961rKOm2KmzcNVg5%2FOO73FrQJVU7uIHwvE7Owsf%2Bv2naw8YLMk3G1IX7iwftt6Y7tUCx36k54OoAuHW8b7ta24KVozPUkz&X-Amz-Signature=65013b516c8ea42ab67a1497c0a788a319532b6a611ba2ce0ccdbabf6d4909bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

