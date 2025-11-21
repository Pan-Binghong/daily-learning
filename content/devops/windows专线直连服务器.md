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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOBN4O6G%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIHVMlbbqFGZsjezYQmcxVGVlRejA%2FCtkUD%2BYMrat1kJbAiEA6P%2F%2B5BtAhxF1XXdEOToHf2FVI%2B3isMfgYkPiCJqkFgMq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDNySb6167VwuSXQqbircA%2FFV%2Bw3vz1Pj4CKvV9FPcNW5npmDB0ifmt53faTC5k2EkTD%2Foj08GUzMJkaZZwMEP1kubsIi2uH5k5QLBaXHvoGz9ODzkIn3mAMEcq1Y%2FbnqTOQ6aQdyX62b6l%2FP82PBa5pMcke534zPK8%2B4qwCrTZ7943FxYkGGWUuME6vvZEuH2zC3Ijm46guZqpj7ME0bPcZxThaRcL7IYofrP85Rca3sEHvUJ4J2eSfqed4jeXAV9zzg%2BJO3q91jpmdaQkL62kRvxXXzq5zrRkQ1syYuBnZE9U%2BCR0CpSkvQ8p3HmLZtOTYwb4HwahDuJ%2Bfu3VmMk1UqBy%2Bv0HoyJrE3bYiB5AViZ0I8CnFWesEEWvSAbbcWDVkc6YW0HdQQj%2FJ%2F%2Ba725fzv0FegYJ38GePUHsCDVLt1UqWb9reBIXxb6gL6CwHuORciCqahd0nkRH%2BmvjfGLMb28mtaKulyUG9Q0Vw6pKu2ez5tRMRBaUtkK5Yl%2FWkTF6aX5yxxuJ7geVaqVNZyxKZTHgYudNC5LIIuMcvncV%2BBifu1eJbXblKJFOkBoXhh9vhdLTPMunaPd1OZ3FqnK9XLjlJW2njoZ8X25eCXaVyht1%2FVBJ0IHI61lZXtMYB0C5U4W4cA7UPxsPAaMMee%2F8gGOqUBHidBK7YSi38Jgjz6axU8XC4a1e%2B8t79sBt8ON62z%2Bbd9GS%2BIULV02Kdo5CdVqgZZxTGTMxwvEKlfq4nZZn9in5b7bZZFgfjQOQvdr7KT7jG24nAAFJ78q6ZfKLUq3lgIZ25dz7mMk1fo1RgdGTSleL2TvtskaXTjE9Y%2FbyVBNRtPsEwmJ%2FFDwt4sVS6tvUevKDAIZmq2KGRqUlNc%2BO2yKv8ZHaXI&X-Amz-Signature=0e06023c76d2f95dab26e128b9427d9a98b13f78d966f4db4471de8b9d245fae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

