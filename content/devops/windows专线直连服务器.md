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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCZN3T47%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuqsV%2FLB2F9qgRUQeMUrDXvHMxjgKE6Y%2BdFJJsyYPQwAiEA2oOtW2V7vXCU0QKwa0qL%2FK7bhN1JW%2FMCUh4a3rs4z0oq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDBiWTmEAFFS2qoUqPSrcA4%2B304eyyq1ItgRktyacShflMZM1rH3YnomgZI6Q3r7KEOWxFxGCVL2PAvWvD2KRhmXyKyt8jFJJycP0iLHAW3NpTNxZXQRbdMnlccwkM4LJGOWFmh4MHGOLlIUQyy6JRa8sRBtD2FG%2F1dma9F1sLIL1%2F6YrmOtQCGfssdipKN%2FUrPXfkfofVGaS7CgXiYEWQtmYyJ5g7l7dftaA1XhS6eqpTwv9P7w3BiYqfqijkHh724j8ogV8qAGdApl9upb7xKALuW3HB8wBdDgbIfr5lTxT%2FPxAw8U9i14LyrNYNjPDsJKPopq2qQ6N8BuU8f%2FlfhN6YZvOG8xbJBlM6sCRcomyJUGsERoIObezF7HulK25yfRqimyZvonfHeoF7R6klyfz9OLIeVh6HaYc3Qw02dSdKyz1%2F5n%2Frh5J3s4A1Xi9xH%2BSjpfEuTHyMzllA%2F4hUA0lO9UeMsYKYm5Utmm9m9tuNTwNT6eUuo9MGVbF7zli%2BBrU%2FECIJhIhSPArMtvg4xCvo6zq%2F0Yzgve258gfNjIluYjNL47waaVqfvoJSr2IIytI2L13u1NQ0nfFnlkzseVJn5uTWAlciCttsowvCgI5ykM21%2Bd3%2Fww1JHvuMGRHeT03AFFGH7ueqsn5MPKLoMwGOqUBVvGchzx7JbeCTpQzyrSMP5a8c2fnaKBvSJRadb5aumclLK3Efs9BXiHw3ZonlFKJ7W9DyqSrGAVfYsCMGfktTZplkHNvRmmuO2cb%2Fl13Eii2zol6fhqrvTUM%2BRBr4OzE3IyaksAAPmyQ76iyo4ZLuz53qEfH6dNngZPNirp%2Fja8YzYLq9Qndt8ECLTGRRocZcVsTaEQWEPLNnLPfTom70AfEVcn3&X-Amz-Signature=26996bfed6610dec16a307f3d5b35b8ef91ad7d1d98e89d195a343aefcc946b4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

