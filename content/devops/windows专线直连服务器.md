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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBCJLL4F%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEwAzXoIIIM7uJhEeuRUUa567QWFtDVAL4dXhRMxGzdAiEA3NB1NQDqveqz8O8C75wLqFGBOYKqB%2FaU1CduM9lpnDkqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNF8mbcpy78UrrOPZyrcA%2FaAZdsG6aSEXPFjQ9UzFVGDxK7NToGU%2F%2BeYu9n54e3bTvqbZCtbjbd5f80oYdga7Gsh6m6Tgy33FlMNq6l3OQ1GTVjvNt%2B4UYgV%2B5pa026DCv%2B7LlnuIAc806TvFPV64o2t9MetN6460h8Wgzl4yXYIiUF%2FKgik6glA%2FDfth%2BT8E%2FvSMniFCC4AxswrCqw1UaR6P%2BEAoDAnwVnRlhFoj0RXGhl2jgw8WIfqljcNdqm2YNCejt0Psst58sXoF0J9KG%2BNCjOz5s%2FebTPliRkNxgNx2l085ZYl%2BGtlLdip6c4%2FVmqXL7RXkrj33Q0%2FetLs2uYSIuPBI7GRcY5eSWcccNG6vE%2BsTWRn64nmzvz13hjIo58n7vKrE5Lyn0Nw%2FQO9S46WSByksdnN3cirsnTNcsVFcsrDWCRyKHAbOMcYrZeN%2F%2Fl05pDQuZldAtjPPKxVdT49NuvC8io4tF0RabBh%2Bdos9E91IUe5clZOQMdnxaLozvDp0D1iZnfyeWtRZE59qjbe184%2Bq48TpoqvG7MGJsEmF7NiUZK7IyDwPFw6onduYoiL7xdfZrvDcXJBTbWfviH2uaKGY78FrnoRpV9onkV7UsiRvd4kqVf5VSW3fk4hxo7Po3waEZOvhjbSMM3wr8gGOqUBD2epTtIbm5%2BodGMwaN1DMNj0%2F8wZFmRLZNYLwdb9FWrWo43VW4%2FhX8hZ0PKDH7jMvlFcQ48I6VPfQWra5%2Fbz2PL7T9ay9DH8jWE2l0puIkdeYt37muK6AmhfQlP3DG2YfcJn8ysOUlhFJIGQ7HaoOctwA3csGtZETHNsgjC4kyo%2FgCAwSYjTB%2B5k3UEiNlwCdjgelIb80CKFB%2BQYZzEpzGRgXU1p&X-Amz-Signature=248fbb3281b1b50a923f1507589f5efc4ae6b8775b273c8aa06c4a1ae7903f19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

