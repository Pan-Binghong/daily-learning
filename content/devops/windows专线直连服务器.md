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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5OLBZYW%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIE8LjpC8YhmI2icgqj%2FtsA7tFH51H2eKJsG2EWI7SuryAiEAlu89g1UT5bXjCYeob7ikM4KK4qvk0HazSfi5CQQ8Iy8q%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDCuwz3Iy5WASqmJVuyrcAxccHDsijfysf1y9VERAQclSdp9oFczShwLS31pG9gXK1ouSMzIJOr8NdgiNfdMq0Kq5SWDdi3Vbr2sqr2xwN3FN5yqkKLBis%2B1nqFULCG4XETYIf8da1aOBiKZwzSmj22AK2M3JIGvxWKcID6lkIKG%2Fc%2FVClJ3OmPbd9FuMeJlwpBuFQl8DyeTyJeepWiayhd8JHXDYzzffTotYHOwAs24UoXhZyUl8TAiNVBHkz9sTrwNPx2ZIqJnYiC4OXgc2SmtXWQGM1glq%2BAUVzDBhvZWOTjKAPZwplPD%2FMLt9m9baEsEBl7%2FGHhmezIrJX2jn%2BNgInXt0r8qndubdFwlpkOmIQ0Zef86lcz8sfAJfBdWmNx5q%2F67UTqvGIzrwL3iWCF0jugYm3GwQPksI3%2BvrFIPNdJd%2Bn9chVz9%2FsnrsyFvL4fHiwzQczIOTgE3I9LE%2FzcYgaOby2Sd6W%2FB3Wo5zOlvxFs2oX7Vx%2BOjVoJZtpxlFoyoK9%2FFFjmV9I5dnLttzlYTi8sRDmQIaJPwdUwJC1vOwkKu8Z7%2BuECM1Sn%2BPsNhr5ITR0lOco%2BVacHATTwrIaYLhpf9wbHYCwzwXRQCTL%2FmXomYYUDDKK9mrXmQgoE%2FXrQ6yEt3f4iPPxQTwMK%2FE4c4GOqUBdxMR%2FVGZfjBNRPuh%2B1h%2FauDSjlUbwjxk3XgRJ2s0pvWRsGrHYCV7UVPkbuEYEnqSqkLyXpGc2ad0HVC3LH7lhsKtS9YUDOmpJd3Rt%2BsoyBmGY48%2BdfFdITYGgvXTvZzyAbyUsgJTS9Vvlhq9lsa2WYIXcAuP9TOk8hrtLf3S9gL6xxPWSBBd7yDwa99k%2BctFEe%2FW0uYPErxksmNtN4yXtCy4hUN7&X-Amz-Signature=d7b49cab68859649e5ed3f8a6b591ca09e5227f32c502f89d0bd36e292ad58fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

