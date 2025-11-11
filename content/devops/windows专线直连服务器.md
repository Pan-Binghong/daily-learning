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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDXEMS3V%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIEfNMkYux7z1RV1zIrO807r45zHwKoxVSDq7XaUn2rUBAiA1ckUhWDOM9vjH5gHZ7HyI5xTNUHhbsnE30IPy4B9bkSr%2FAwgUEAAaDDYzNzQyMzE4MzgwNSIMksDSb5o6Wf2pn1f7KtwDa51QudjpRO9QtuJ%2FfdMQR2TZyXUjp5bvVKE%2FdLAktESWMeM979t8fna2YVqnbUE2cbxnqMWtKJrmQXJBqMtRLM63Q8WfYYbKJaKGTO1Ask0NCo3shvUae1ur2suN7pS6U2azL6LHp8uZ7%2F6YdRLG%2FHcqomUSlRpnCADNgsQUKS1S1uu32kUfROI9jCpf6xKD%2FH41I20SkgKnZRR7c9ZlLuOlEBr%2B3qLRI4fhEVJvN5RVsFyVQOOrJn1KONBfk%2Fa82CGKf%2BXqymgKiIfKehpd%2FqcAaM3nZvPUU4yNZU9HHgKOcL1vj3vyExauSxLgOBd8BOE7lFJR06FBXfZavF%2FHoRtWhlJF9oVJqWZPw0sNqYGssuaMiv7z2XJWwsV3il%2FLKT%2F4Dkqno6W6qDEscl28BaUX7EdRVCPKvaPPEx4Obq2y%2B9dgsOkH9t5V5VMpG710zMnYixGzhJr8%2FCPpjSLZVqU8%2F%2FkNR0TJG9%2FoAfrRX6aioUvEbgsTWrIwHBoQbWqyc5aELkaxcyBgsAEsHGG9OtMg43BMMstQ4VMT1af%2FFNKpOlu9y1lgjhUaSZTGdLrkYRNF9NXIC3iJa62ENDfzsx%2BDm2us%2FNuMCTJabcMSeD5u%2B%2BL9sPJpW5wEBZEw3r3KyAY6pgEFOVfIbdxLcMoR9b81yma9e%2FEZjBNmZVdeHxikCkE3M0g%2FHgFvrAPMi42EGdMOsqI5BnioCVIG%2BNUlXfwnU2qxWhn7tHcN31AWx0kmZWQJE%2BwgqLjaTDAga3mbWJwW1hmZToeiS7vaVXRpECXuOCAhCrkmmaE7hdRRh%2B22fDY%2FyI%2BxZ%2BjyGKT%2F%2BIQvRheLPSr%2FUV3%2FqTyFMsCgauFLndhD34Z%2Be9nX&X-Amz-Signature=c1c29052375f638a573d07e7783ee398451e2303093f0447ca88cd4c5cd560b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

