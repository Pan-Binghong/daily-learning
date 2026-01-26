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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKJUHBRB%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIQDRoMYp3hH%2Bne%2BjEzCKU872KHJQplzd9fJc6sZE9zDcyQIgTSyrSxdz1RRHMifxdAA%2FQ9sayGSPdJyyKkMDY2S10skq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDAaa0W2x%2BoxobKC%2BvyrcA5HyR0Umf6ceKvyzEQfp7yxExX93Z2WvPzPMpCTkvOZGRtDCXh4rSnLOI0M1AfGvvsmkJyTcuESnueBkmgiPGHOHs63rtoYBSsUTk511RFdYrrTbHp%2FLNTsO7I1aPQmYuQfLh90jfw3jUdVZaauYrbzq3H%2Bvqxx8K2E58YuXZKwPk8vJr12pOJw5zMtcTyXFzY9K0mH1ogYrmMOYptDSoBZWWvdAy%2FOU5giBlyntlZRe2y%2BuPVK1oQbVyvSqIRqVZSK8m0pqq4eaW%2BRhIu2bV99TGqRxz%2FOk6MEzMCWBr7OxHhsnT5HjTTB4%2F3V1EC7fYQeHSTfX4qujwI9I5oeaznF0rdFGyQuwdoTq2rjTGIH3a3aQk%2FLYDvK6aUtUVu1nONulrlWqtqwy3OSbjo2jeYbpu0W03QcXwPYp%2FTTQmJHIW6C2OsjtE34uXHXy4Y3Zs%2B3zfRanh%2Blu%2FjCctLUp28w5OV9Iqhuv%2BJ%2ByY%2FkLmYinXy6j8HOlU%2FmaUtDUL5s8kPdwu%2BZWVFu%2FWGR1BHoomw3tpUhtlKGDdoFQgsF8XAAiVI1zrN1VGMqoeT%2FJ7bpvJZT9rSf%2FIvo5UUStmDoJG97q688hBAfx8JAGuqr6gGGP3BBEYDGlathYcZIUMLux2ssGOqUBLk3vdslAgsonOYQVRxR3UdvH9pW6pOmmEGHgpIbLIOD%2BhjL1zOz3%2FTwG8NS3p9hoLrGKJotsqjQELMhWBILKinrG3yIa2z57M2bThBcu4mh3Bts%2FH%2B5wQ6JTcSmOIdvcnDePSZCvnio4i1ALuzJLA7xxkc4NMdTsRwPal%2FOlZC5%2FGVsXw0pdQF7t0GsmCK0eXJeVCP6LydBv9HgnkvgbJsN6MIQ8&X-Amz-Signature=358fee7aa4ed061b90b49e158fe017da6efc3b573a6fe9c4e9f71dba32ebe598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

